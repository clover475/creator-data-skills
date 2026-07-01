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

## Retry Order

1. 检查 Cookie 是否过期
2. 检查本地登录态是否仍有效
3. 检查 Playwright / crawler 依赖
4. 降低关键词规模
5. 更换批次而不是持续硬刷
