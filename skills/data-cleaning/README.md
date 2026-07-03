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
- `path_fact_candidates.json`
- `path_tags_suggestions.json`
- `notes.md`

结构见：

- [../shared/field-schemas.md](../shared/field-schemas.md)

## 执行步骤

1. 读取 raw manifest。
2. 提取标题、摘要、正文片段、链接、关键词。
3. 标准化平台字段和时间字段。
4. 基于标题、摘要和关键词生成 `path_tags`。
5. 生成 **path_fact 候选**（不生成事件——事件由消费方项目从 facts 出发生成，见 [../shared/field-schemas.md](../shared/field-schemas.md) 第 3 节的交接契约），按规则给每条 fact 打 `confidence`。
6. **跑 `scripts/scrub.py`（本仓库根目录）做脱敏和去重**：白名单外字段全删 + URL/内容哈希去重。隐私是脚本保证的，不靠逐条手工检查。
7. 全部结果标记 `needs_human_review: true`。

## 示例 Prompt

```text
请把最新一批 raw/xhs 数据清洗成 personal_path_sources 和 path_fact_candidates，只保留标题、摘要、链接、关键词、路径标签和 fact 候选，最后用 scrub.py 脱敏去重。
```

```text
请检查 xhs 和 zhihu 两批结果是否有重复链接，并输出一个合并后的候选批次。
```

## 注意事项

- 情绪抱怨不能直接入主数据。
- 不长段复制原文。
- 不保留极端个例作为主样本。
- fact 摘要应去平台腔和个人识别信息。
- 本环节的职责终点是 facts；把 facts 变成游戏事件/产品内容是消费方项目的事。

## 可复用脚本路径

本仓库不直接保存业务项目脚本。

建议业务项目将清洗逻辑放在：

- `scripts/<platform>_one_time_workflow.py`
- `scripts/clean_<topic>.py`
