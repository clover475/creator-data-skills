# 数据清洗 Skill

## 适用场景

当 Agent 已拿到 raw 数据，需要转成可复用的结构化候选数据时使用。

目标是抽出路径机制，不是完整保留平台内容。

## 输入文件格式

- `raw/<platform>/<run_id>/manifest.json`
- `raw/<platform>/<run_id>/**/*.jsonl`
- 关键词文件

## 输出文件格式

建议输出到业务项目自己的 `out/<agent_name>/` 目录，例如：

- `personal_path_sources.json`
- `personal_event_candidates.json`
- `path_tags_suggestions.json`
- `notes.md`

结构见：

- [../shared/field-schemas.md](../shared/field-schemas.md)

## 执行步骤

1. 读取 raw manifest。
2. 提取标题、摘要、正文片段、链接、关键词。
3. 删除昵称、头像、主页链接、评论用户 ID 等 PII。
4. 标准化平台字段和时间字段。
5. 基于标题、摘要和关键词生成 `path_tags`。
6. 生成事件候选。
7. 全部结果标记 `needs_human_review: true`。

## 示例 Prompt

```text
请把最新一批 raw/xhs 数据清洗成 personal_path_sources 和 personal_event_candidates，只保留标题、摘要、链接、关键词、路径标签和事件候选。
```

```text
请检查 xhs 和 zhihu 两批结果是否有重复链接，并输出一个合并后的候选批次。
```

## 注意事项

- 情绪抱怨不能直接入主数据。
- 不长段复制原文。
- 不保留极端个例作为主样本。
- 事件文本应去平台腔和个人识别信息。

## 可复用脚本路径

本仓库不直接保存业务项目脚本。

建议业务项目将清洗逻辑放在：

- `scripts/<platform>_one_time_workflow.py`
- `scripts/clean_<topic>.py`
