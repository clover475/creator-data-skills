---
name: creator-data
description: 多平台内容研究与数据供给流水线：从小红书、知乎、B站等平台做一次性本地采集，清洗脱敏成结构化候选数据（path_facts），聚类分析并产出研究报告。当用户要做用户研究、选题验证、市场/竞品调研、为模拟游戏或其他产品收集真实来源素材、整理爬虫 raw 数据、给采集内容打标签、或要求出研究简报时使用。只要任务涉及"爬虫""采集""小红书/知乎/B站数据""来源整理""数据清洗""研究报告"，即使用户没有点名这个技能，也应先查阅对应环节的文档再动手。
---

# Creator Data Skills

一条通用的内容研究流水线：**采集 → 清洗脱敏 → 分析 → 报告**。方法与项目数据严格分离：本仓库只放方法和脚本，raw 数据和清洗结果永远留在业务项目里。

## 四种用途

| 用途 | 典型任务 | 产出去向 |
|---|---|---|
| 1. 选题验证 | 做「调酒师模拟」前，先爬"转行调酒"讨论量和痛点分布 | 研究简报，决定做不做 |
| 2. 产品来源供给 | 为模拟游戏采集真实经历素材 | path_facts 候选 → 交给 simulation-game-builder-skills |
| 3. 产品反馈研究 | 爬自己产品的玩家/用户讨论，校准设计假设 | 分析报告 → 回流设计 |
| 4. 市场/竞品研究 | 同类产品的评论聚类：用户夸什么骂什么 | 研究简报 → 设计清单 |

## 环节路由

| 你在做什么 | 去读 |
|---|---|
| 接手任何任务前 | [skills/agent-usage/README.md](skills/agent-usage/README.md) |
| 确认平台状态与合规边界 | [skills/shared/platform-matrix.md](skills/shared/platform-matrix.md) |
| 采集新批次 | [skills/multi-platform-collection/README.md](skills/multi-platform-collection/README.md) |
| raw → 结构化候选 | [skills/data-cleaning/README.md](skills/data-cleaning/README.md) |
| 提炼模式与标签 | [skills/content-analysis/README.md](skills/content-analysis/README.md) |
| 产出研究报告 | [skills/report-generation/README.md](skills/report-generation/README.md) |
| 字段结构与交接契约 | [skills/shared/field-schemas.md](skills/shared/field-schemas.md) |

## 硬规则（不因任务而变）

1. **脱敏必须用脚本，不靠模型自觉**：清洗输出一律过 `scripts/scrub.py`（白名单外字段全部删除 + 按 URL/内容去重）。模型手工删 PII 会漏，脚本不会。
2. **小批量先行**：每关键词 ≤20 条验证流程，再扩批次。
3. **一次性本地研究**：不做长期在线爬虫，不集成进任何产品运行时，Cookie 只存本地 `.env`。
4. **本仓库的职责终点是 facts**：输出到 `path_fact_candidates`（带 confidence）为止。把 facts 变成游戏事件/产品内容是消费方项目的事（见 field-schemas 的交接契约）。
5. **所有候选默认 `needs_human_review: true`**：爬来的是线索，不是事实。

## 与其他技能仓库的关系

- **[simulation-game-builder-skills](https://github.com/clover475/simulation-game-builder-skills)**（下游消费方）：本仓库产出的 path_facts 候选对接其 04-corpus-pipeline 的 `incoming/` 暂存区，经人工审查后进入游戏数据层。
- **[software-development-skills](https://github.com/clover475/software-development-skills)**（流程层）：采集批次作为一个 task 执行时，遵循其 task-scope-execute 的小步验收方式。
