# Platform Matrix

本页描述平台适配的常见状态和注意事项。

## Status Labels

- `implemented`：已有稳定 workflow
- `adapter-ready`：底层工具可接，但业务项目未封装
- `planned`：仅有规则和计划，未落地

## Recommended Matrix

| 平台 | 建议状态 | 登录态来源 | 备注 |
| --- | --- | --- | --- |
| 小红书 / Xiaohongshu | implemented | `.env` | 常见一次性研究入口 |
| 知乎 / Zhihu | implemented | `.env` | 常见一次性研究入口 |
| B站 / Bilibili | adapter-ready | `.env` or local session | 先确认 crawler adapter |
| 微信公众号 / WeChat OA | planned | manual or future adapter | 不应默认宣称已自动化 |

## Shared Rules

- 采集只用于本地一次性研究
- 不集成进业务运行时
- 不把 Cookie 写入代码库
- 原始数据进入业务项目自己的 `raw/`
- 清洗后结果进入业务项目自己的 `out/`

## Compliance Notes

带登录态采集通常违反平台服务条款，风险是封号；用于商业产品还有法律敞口（国内有多起爬虫相关不正当竞争判例）。缓解措施就是本仓库的硬规则：一次性、小批量、本地研究、脚本脱敏、不复制原文。

商业产品的安全链路：**爬取原文 → 摘要成 fact → 原创内容**。进入商业产品的永远是最后一环，raw 数据永不发布、永不入库到产品。

**能用官方渠道就不爬**。优先考虑的替代来源：

| 需求 | 更干净的来源 |
| --- | --- |
| 群体统计与分布校准 | 国家统计局、麦可思等行业报告 |
| 游戏玩家反馈 | Steam 官方评论 API、TapTap 开放接口 |
| 行业趋势 | 公开研究报告、上市公司财报 |
| 从业者经历 | 自己做访谈（可控、可授权、质量更高） |

## Retry Order

1. 检查 Cookie 是否过期
2. 检查本地登录态是否仍有效
3. 检查 Playwright / crawler 依赖
4. 降低关键词规模
5. 更换批次而不是持续硬刷
