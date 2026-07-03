#!/usr/bin/env python3
"""PII scrub + dedupe for cleaned collection outputs.

Whitelist strategy: only fields in ALLOWLIST survive. Everything else is
dropped, so a new PII field added by an upstream crawler can never leak
through by accident. A denylist alone cannot give this guarantee.

Usage:
    python3 scrub.py cleaned.json [more.json ...] -o out/
    python3 scrub.py cleaned.jsonl --extra-allow related_entry_years -o out/

Input: JSON array or JSONL of records. Output: <out>/<name>.scrubbed.json
plus a short report on stdout (kept/dropped fields, dedupe count).
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

# 与 skills/shared/field-schemas.md 的保留字段保持一致。
ALLOWLIST = {
    # source / fact 通用
    "id", "factId", "sourceId", "platform", "title", "summary",
    "source_url", "keywords", "path_tags", "fact_type", "stage",
    "confidence", "corroboration_count", "needs_human_review",
    "usable_for", "related_entry_years", "collected_at",
    # 嵌套结构里允许的容器字段
    "items",
}

# 双保险：这些字段即使被误加进 ALLOWLIST 也会报错退出。
FORBIDDEN = {
    "nickname", "avatar", "user_id", "comment_id", "comment_text",
    "homepage", "profile_url", "creator_url", "ip_location",
    "comment_user_id", "author", "author_id", "user_name",
}


def scrub_record(rec: dict, extra_allow: set) -> tuple[dict, set]:
    allow = (ALLOWLIST | extra_allow) - FORBIDDEN
    dropped = set(rec) - allow
    return {k: v for k, v in rec.items() if k in allow}, dropped


def content_key(rec: dict) -> str:
    url = (rec.get("source_url") or "").strip().rstrip("/")
    if url:
        return "url:" + url
    text = ((rec.get("title") or "") + "\n" + (rec.get("summary") or "")).strip().lower()
    return "sha1:" + hashlib.sha1(text.encode("utf-8")).hexdigest()


def load_records(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    data = json.loads(text)
    return data if isinstance(data, list) else [data]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--extra-allow", nargs="*", default=[],
                    help="本项目额外允许保留的字段名")
    args = ap.parse_args()

    bad = FORBIDDEN & set(args.extra_allow)
    if bad:
        print(f"错误：禁止将 PII 字段加入白名单: {sorted(bad)}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    extra = set(args.extra_allow)
    seen: set[str] = set()
    all_dropped: set[str] = set()
    total_in = total_out = dupes = 0

    for path in args.inputs:
        kept = []
        for rec in load_records(path):
            total_in += 1
            key = content_key(rec)
            if key in seen:
                dupes += 1
                continue
            seen.add(key)
            clean, dropped = scrub_record(rec, extra)
            all_dropped |= dropped
            kept.append(clean)
        total_out += len(kept)
        out_file = args.out / (path.stem + ".scrubbed.json")
        out_file.write_text(
            json.dumps(kept, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✓ {path} → {out_file} ({len(kept)} 条)")

    print(f"\n输入 {total_in} 条，输出 {total_out} 条，去重 {dupes} 条")
    if all_dropped:
        print(f"已删除的字段: {sorted(all_dropped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
