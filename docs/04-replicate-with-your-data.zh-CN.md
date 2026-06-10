# 04. 用你自己的数据复刻

## 最小替换路径

1. 把数据放入 `data/<dataset-name>/raw/`。
2. 复制 `examples/nhanes-undiagnosed-diabetes/` 为新的 example。
3. 修改分析脚本，让它读取你的数据并输出同类结果表。
4. 从 S0 开始填写新的 checkpoint。
5. 每完成一个阶段，更新 `workflow-run.json`。
6. 运行 validator，确认没有越级。

## 必须重新确认的内容

- 数据是否允许公开或再分发。
- 研究问题是否能由当前数据回答。
- 变量定义是否清晰。
- 统计方法是否适配数据结构。
- 论文结论是否只说数据能支持的话。

## 推荐产物

- `checkpoints/`：阶段记录。
- `results/`：分析输出。
- `submission_package/`：最终稿、表图、清单。
- `workflow-run.json`：状态机。
