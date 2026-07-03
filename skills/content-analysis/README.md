# 内容分析 Skill

## 适用场景

当 Agent 需要从清洗后的候选数据中提炼模式、标签、趋势和代表案例时使用。

## 输入文件格式

优先使用结构化清洗结果：

- `personal_path_sources*.json`
- `path_fact_candidates*.json`
- `path_tags_suggestions.json`

## 输出文件格式

建议输出为 Markdown 或 JSON：

1. Markdown 分析摘要
2. JSON 聚类中间结果

示例：

```json
{
  "cluster_id": "cluster_001",
  "theme": "普通本科信息启动晚",
  "source_ids": ["source_001", "source_042"],
  "signals": ["late_information_awareness", "internship_late"],
  "insight": "信息环境弱和校园资源薄，导致职业准备普遍后移。",
  "needs_human_review": true
}
```

## 执行步骤

1. 先按年份、平台、标签切片。
2. 再按路径机制聚类。
3. 提炼“限制条件 -> 选择 -> 后果”。
4. 区分时代冲击与个体准备不足。
5. 只用脱敏摘要和链接做证据。
6. 输出结论时附样本数量或来源数量。

## 示例 Prompt

```text
请基于已清洗的 personal_path_sources，按高考年份和大学阶段总结常见路径机制，并输出 Markdown 摘要。
```

```text
请提炼“县城学生 + 信息差 + 实习启动晚”的代表模式，给出标签建议、典型事件和证据链接。
```

## 注意事项

- 不把高点赞误判为高代表性。
- 不把平台话术直接当结论。
- 评论只做聚合统计（数量、情绪比例、主题分布）；清洗规则禁止保留评论原文和评论者信息，所以任何需要引用评论原文的分析都做不了，也不应该做。
- 记住样本的系统性偏差：爱发帖的人不代表沉默的大多数，平台算法又筛过一遍。结论措辞用「发帖者中……」而不是「这个群体……」。

## 可复用脚本路径

本仓库只给方法，不捆绑项目脚本。
