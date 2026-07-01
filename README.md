# creator-data-skills

可复用的内容研究与数据工作流技能库。

这个仓库只放方法、结构、执行规范和 prompt 模板，不放具体项目的原始采集数据，也不放业务项目的正式数据文件。

## Purpose

服务对象：

- AI Agent
- 内容研究员
- 数据整理人员
- 项目主编排 Agent

目标：

- 复用多平台采集方法
- 统一清洗结构
- 统一分析框架
- 统一研究报告输出方式

## Repository Boundary

这个仓库负责：

- skills 文档
- 字段结构约定
- 平台差异说明
- Agent 执行说明

这个仓库不负责：

- 具体项目的 raw 数据
- 具体项目的 cleaned JSON 结果
- 游戏运行时数据
- 平台 Cookie 或个人隐私信息

## Layout

```text
creator-data-skills/
  README.md
  skills/
    README.md
    shared/
      field-schemas.md
      platform-matrix.md
    multi-platform-collection/
      README.md
    data-cleaning/
      README.md
    content-analysis/
      README.md
    report-generation/
      README.md
    agent-usage/
      README.md
```

## Consumer Project Pattern

建议业务项目按下面的方式消费本仓库：

- 本仓库只放方法
- 业务项目自己放：
  - `raw/<platform>/`
  - `out/<agent_name>/`
  - `docs/<project-specific-plan>.md`
  - `scripts/<project-specific-workflow>.py`

例如 `after-exam` 这样的项目，采集结果应该留在项目仓库里，而不是回流到 skills 仓库。

## Current Reference Consumer

当前这套技能文档最初来自 `after-exam` 项目的普通人路径研究流程，后续已经拆分到本仓库独立维护。

## Privacy Rule

- 不存 Cookie
- 不存昵称、头像、主页链接、评论用户 ID 等 PII
- 公开文档只保留脱敏示例

## Getting Started

先读：

1. [skills/README.md](./skills/README.md)
2. [skills/agent-usage/README.md](./skills/agent-usage/README.md)
3. [skills/shared/platform-matrix.md](./skills/shared/platform-matrix.md)
4. [skills/shared/field-schemas.md](./skills/shared/field-schemas.md)
