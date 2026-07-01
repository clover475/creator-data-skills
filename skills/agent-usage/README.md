# Agent 使用说明

这份文档规定 Agent 如何使用本仓库，而不是直接凭经验发挥。

## 适用场景

- 跑新的平台采集批次
- 清洗 raw 数据
- 生成标签和事件候选
- 输出研究报告
- 扩展新的平台 adapter

## 输入文件格式

Agent 接手任务时，至少先确认：

1. 业务项目中的关键词文件
2. 本地 `.env` 是否有 Cookie
3. 业务项目中是否已有采集 plan 和 workflow 脚本
4. 业务项目里是否已有历史输出可复用

## 输出文件格式

Agent 产出应写回业务项目，而不是写回 skills 仓库：

- `raw/<platform>/`
- `out/<agent_name>/`
- `docs/`
- `scripts/`

本仓库只增补方法文档。

## 执行步骤

1. 先判断任务属于采集、清洗、分析还是报告。
2. 先复用业务项目已有脚本。
3. 先跑小样本验证。
4. 先脱敏，再结构化。
5. 候选数据不直接写入正式业务数据目录。

## 推荐阅读顺序

1. [../shared/platform-matrix.md](../shared/platform-matrix.md)
2. [../shared/field-schemas.md](../shared/field-schemas.md)
3. [../multi-platform-collection/README.md](../multi-platform-collection/README.md)
4. [../data-cleaning/README.md](../data-cleaning/README.md)
5. [../content-analysis/README.md](../content-analysis/README.md)
6. [../report-generation/README.md](../report-generation/README.md)

## 示例 Prompt

```text
你是某业务项目的数据研究 Agent。请先阅读 creator-data-skills/skills/agent-usage 和 shared 文档，再决定本次任务属于采集、清洗、分析还是报告生成。不要把 Cookie 写入仓库，不要直接修改正式业务数据。
```

## 注意事项

- 不把隐私写进公开文档。
- 不虚报平台适配状态。
- 不把候选结果当最终事实。
