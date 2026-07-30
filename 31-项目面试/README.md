# 项目面试题库

本专题把 GitHub 项目拆成独立题库：一个项目一个文件夹、每个项目 30 题，共 **13 个项目、390 道题**。题目按“项目自述 → 架构 → 核心实现 → 工程化 → 压力追问”排列；每道题都要求回答者回到仓库代码、配置、测试或运行记录，不把 README 当作唯一证据。

## 使用原则

- 先用 90 秒说清业务问题、自己的职责、技术取舍和可量化结果；没有数据时明确说明“尚未验证”，不要编造指标。
- 目录中同时有自研、课程/实验和基于开源项目二次开发的仓库。面试时应主动划清原项目、复用部分和本人新增部分的边界。
- 每题后的“证据”不是标准答案，而是准备回答时应能展示的实现位置或运行制品。

| # | 项目 | 题数 | 侧重点 |
| --- | --- | ---: | --- |
| 01 | [Pokemon AI Toolkit](./01-pokemon-ai-toolkit/README.md) | 30 | 爬虫、数据、KG、QA、微调与 CLIP |
| 02 | [Smart Assistant](./02-smart-assistant/README.md) | 30 | KG + RAG + LLM 编排 |
| 03 | [ForeSight](./03-foresight/README.md) | 30 | 时序预测库、统一接口与回测 |
| 04 | [Realtime Video Analytics](./04-realtime-video-analytics/README.md) | 30 | 32 路视频、推理、追踪与可观测性 |
| 05 | [YOLO26 NCNN](./05-yolo26-ncnn/README.md) | 30 | C++ 端侧部署、检测/分割后处理校验 |
| 06 | [DocPilot](./06-docpilot/README.md) | 30 | 多格式解析服务、异步任务与运维 |
| 07 | [Taroai](./07-taroai/README.md) | 30 | 多租户 Agent 平台与隔离执行 |
| 08 | [Digital Human](./08-digital-human/README.md) | 30 | 实时多模态数字人全链路 |
| 09 | [Ultralight Digital Human](./09-ultralight-digital-human/README.md) | 30 | 唇形驱动训练、采样与推理部署 |
| 10 | [RepoCoach](./10-repocoach/README.md) | 30 | 仓库驱动的 AI 模拟面试产品 |
| 11 | [AirDesk](./11-airdesk/README.md) | 30 | 手势交互、浏览器视觉与 3D UI |
| 12 | [Diffusion Models](./12-diffusion-models/README.md) | 30 | 生成模型复现与对比实验 |
| 13 | [MimirQ](./13-mimirq/README.md) | 30 | 企业 RAG、治理、检索、评测与 Dify 集成 |

## 建议模拟方式

1. 随机抽一题，限制两分钟作答；先给结论，再给仓库事实和取舍。
2. 面试官从该题的追问再选一题；任何数字都要能说明采样口径、环境和复现实验。
3. 最后做“贡献边界”校验：哪些由你设计、哪些来自开源、哪些还只是规划，必须如实区分。
