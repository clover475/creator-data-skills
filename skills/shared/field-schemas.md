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
- `event_candidate_ids`
- `needs_human_review`

## 3. Personal Event Candidate

```json
{
  "eventId": "zhihu_event_0001",
  "sourceId": "zhihu_curated_0001",
  "stage": "junior_year",
  "event_type": "career",
  "title": "第一次意识到实习需要提前准备",
  "text": "你看到别人的求职复盘后，才发现实习和校招比自己想得更早开始。",
  "addTags": ["late_information_awareness"],
  "needs_human_review": true
}
```

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

清洗后输出不应保留：

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
