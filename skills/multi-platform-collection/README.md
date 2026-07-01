# 多平台数据采集 Skill

## 适用场景

当 Agent 需要从小红书、知乎、B站、微信公众号等平台收集研究材料时使用。

重点是“一次性、本地、离线研究”，不是长期在线爬虫。

## 输入文件格式

1. 本地 `.env`

```env
XHS_COOKIE=...
ZHIHU_COOKIE=...
```

2. 关键词文件

```text
2016 高考 2020 毕业 找工作
普通本科 大三才知道实习
2020 届 毕业 疫情 校招
```

## 输出文件格式

输出是业务项目里的 raw 数据目录，例如：

```text
raw/xhs/<run_id>/
raw/zhihu/<run_id>/
```

manifest 结构见：

- [../shared/field-schemas.md](../shared/field-schemas.md)

## 执行步骤

1. 确认平台和关键词批次。
2. 从 `.env` 读取 Cookie。
3. 先跑小样本，每词不超过 20 条。
4. 不默认抓评论。
5. 将 raw 数据保存到业务项目自己的 `raw/<platform>/`。
6. 采集完成后立即进入清洗流程。

## 示例 Prompt

```text
请为当前业务项目建立一次性小红书采集批次。Cookie 只从本地 .env 读取，原始数据输出到 raw/xhs/，不要改运行时数据。
```

```text
请先验证知乎工作流的登录态，再按年份导向关键词跑一个小批次，每个关键词最多 20 条，只保留 raw 数据和 manifest。
```

## 注意事项

- 不把采集逻辑集成进运行时。
- 不把 Cookie 写进代码或提交记录。
- 不把平台适配状态说得比实际更成熟。
- 公众号如果未实现 adapter，应明确标注为待实现。

## 可复用脚本路径

本仓库不直接保存业务项目脚本。

建议业务项目自行提供：

- `scripts/xhs_one_time_workflow.py`
- `scripts/zhihu_one_time_workflow.py`
- `docs/xhs-one-time-collection-plan.md`
- `docs/zhihu-one-time-collection-plan.md`
