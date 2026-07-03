# Field Schemas

本页定义通用字段结构，用于业务项目的本地一次性采集与清洗流程。

## 1. Raw Collection Manifest

业务项目可采用如下结构：

```json
{
  "runId": "zhihu-test-20260701-151200",
  "generatedAt": "2026-07-01T15:12:00+08:00",
  "tool": "MediaCrawler",
  "mode": "live",
  "platform": "zhihu",
  "perKeywordLimit": 20,
  "keywords": ["2016 高考 2020 毕业 找工作"],
  "items": [
    {
      "keyword": "2016 高考 2020 毕业 找工作",
      "rawFiles": ["keyword-01/zhihu/jsonl/search_contents_001.jsonl"],
      "rawDir": "keyword-01"
    }
  ]
}
```

## 2. Cleaned Personal Path Source

```json
{
  "id": "zhihu_curated_0001",
  "platform": "zhihu",
  "title": "普通本科学生大三才意识到实习竞争",
  "summary": "该材料反映部分普通本科学生因信息环境较弱，直到大三才意识到实习和校招需要提前准备。",
  "source_url": "https://www.zhihu.com/question/example",
  "keywords": ["普通本科 大三才知道实习"],
  "path_tags": ["late_information_awareness", "internship_late"],
  "event_candidate_ids": ["zhihu_event_0001"],
  "needs_human_review": true
}
```

保留字段：

- `id`
- `platform`
- `title`
- `summary`
- `source_url`
- `keywords`
- `path_tags`
- `fact_candidate_ids`
- `needs_human_review`

## 3. Path Fact Candidate（对下游的交接契约）

本仓库对消费方项目（如 simulation-game-builder-skills）的交接物是 **path_fact 候选**，不是事件。事件/内容生成属于消费方——它们的管线明确要求「来源 → facts（带 confidence）→ 内容」，跳过 fact 层直接产事件是双方都禁止的反模式。

```json
{
  "factId": "zhihu_fact_0001",
  "sourceId": "zhihu_curated_0001",
  "fact_type": "information_gap",
  "stage": "junior_year",
  "summary": "部分普通本科学生因信息环境较弱，直到大三才意识到实习和校招需要提前准备。",
  "path_tags": ["late_information_awareness"],
  "confidence": 3,
  "corroboration_count": 1,
  "needs_human_review": true
}
```

**confidence 规则（社交平台来源专用）：**

- 社交平台单帖的 confidence 上限为 **3**（个案自述，有幸存者偏差和表演性偏差）
- 只有当 `corroboration_count ≥ 2`（两个以上互相独立的来源描述同一机制）才可升到 4
- 5 只留给有数据支撑的报告类来源，爬取内容不应出现 5
- `fact_type` 枚举由消费方项目定义（见其 corpus-pipeline 文档），清洗时照抄该项目的枚举表

## 4. Path Tag Suggestion

```json
{
  "id": "late_information_awareness",
  "label_cn": "职业信息启动晚",
  "definition": "玩家在大学较晚阶段才意识到实习、校招、行业路径等职业信息的重要性。",
  "examples": ["大三才知道实习需要提前准备", "毕业前才意识到校招已经开始"],
  "usable_for": ["career_event", "ending_variant", "choice_modifier"]
}
```

## 5. Forbidden PII Fields

清洗后输出不应保留（**用 `scripts/scrub.py` 强制执行**——它按白名单删除一切未知字段并按 URL/内容去重。隐私是靠脚本保证的，不是靠模型自觉）：

- `nickname`
- `avatar`
- `user_id`
- `comment_id`
- `comment_text`
- `homepage`
- `profile_url`
- `creator_url`
- `ip_location`
- `comment_user_id`

## 6. Time Normalization

- 采集时间：ISO 8601
- 相关年份：整数或整数数组
- 阶段：固定枚举
