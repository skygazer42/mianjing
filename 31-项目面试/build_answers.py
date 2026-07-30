#!/usr/bin/env python3
"""Build one evidence-guided answer file for every project interview question.

The question tables are the source of truth. This script deliberately keeps
claims bounded to the repository material listed in PROJECTS: it distinguishes
what the repository shows from a production recommendation or an unverified
metric. Run from the repository root with:

    python 31-项目面试/build_answers.py
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent

PROJECTS = {
    "01-pokemon-ai-toolkit": {
        "title": "Pokemon AI Toolkit",
        "repo": "https://github.com/skygazer42/Pokemon-AI-Toolkit",
        "verified": "仓库 README 展示了官网爬取、CSV 清洗、Tableau、Neo4j 图谱/问答，以及微调和 CLIP 探索这条由数据到应用的链路。",
        "flow": "官网页面与图片 → 原始 CSV/图片资产 → 清洗后的分析数据 → 图谱实体与关系 → Cypher/KGQA → 对话、微调或图文能力。",
        "sources": ["README.md", "Data_cleaning/清洗.ipynb", "KG/ 与 KGQA/ 下的图谱、问答脚本"],
        "boundary": "数据抓取、图谱和模型实验应分别说明；课程代码、公开数据和二次开发不能表述为从零自研。",
        "core": ["稳定图鉴编号与多语言实体消歧", "可追溯的爬取/清洗版本", "Neo4j schema、约束与参数化 Cypher", "检索/图谱证据优先于自由生成", "图文实体关联与 CLIP 评测"],
        "metrics": "抓取覆盖率、字段缺失率、实体/关系重复率、KGQA 端到端正确率、引用正确率和人工抽检。",
        "risks": "网页结构变化、版权/抓取许可、图谱脏数据、实体歧义和模型幻觉。",
    },
    "02-smart-assistant": {
        "title": "Smart Assistant（Meet-Pokémon）",
        "repo": "私有仓库 skygazer42/Smart-Assistant",
        "verified": "README 与依赖清单可验证系统组合了 Neo4j、LangGraph/LangChain、Milvus 或 Chroma、FlagEmbedding、文档解析和本地/在线模型。",
        "flow": "API 请求 → 意图/风险路由 → 图谱查询、文档解析后的检索或工具 → 证据组装 → LLM 生成与引用 → trace、审计和降级。",
        "sources": ["README.md", "requirements.txt", "api.py、scr/server/、scr/qa/ 与图谱导入脚本（回答时应定位实际实现）"],
        "boundary": "应区分系统中自行实现的路由/数据契约与 LangChain、Dify、RAGFlow、预训练模型提供的能力。",
        "core": ["图谱、向量检索和 LLM 的职责路由", "文档/页/块/嵌入的版本和 ACL", "实体关系抽取的置信度与审核", "引用约束与无证据拒答", "多 provider 与任务图状态管理"],
        "metrics": "检索 Recall/nDCG、引用正确率、端到端任务成功率、拒答质量、p95 延迟、token 成本与越权率。",
        "risks": "提示注入、跨租户泄露、图谱/文档冲突、解析噪声、模型限流和依赖版本漂移。",
    },
    "03-foresight": {
        "title": "ForeSight",
        "repo": "https://github.com/skygazer42/ForeSight",
        "verified": "README 和 pyproject.toml 显示这是预测工具包：稳定的 Python/CLI/制品表面、registry、walk-forward 回测、长表数据契约和可选后端 extras。",
        "flow": "长表 unique_id/ds/y → 数据校验与切分 → registry 解析模型/后端 → fit/predict → walk-forward 评测 → leaderboard、区间与可序列化 artifact。",
        "sources": ["README.md", "pyproject.toml", "src/foresight/cli.py、cv.py、models/registry.py、models/runtime.py 与 tests/"],
        "boundary": "模型目录的广度不等于全部同样稳定；回答必须按 stable、beta、experimental 和 CI 覆盖范围区分。",
        "core": ["统一 forecaster/adapter 契约", "时间切分与防未来泄漏", "panel/global 与 local 模型边界", "概率预测、校准和指标口径", "artifact schema 与 optional dependency 管理"],
        "metrics": "MASE/sMAPE/RMSE 等误差指标、区间覆盖率/CRPS、回测耗时、失败率、安装与兼容性矩阵。",
        "risks": "数据频率/时区错误、未来泄漏、后端可选依赖、随机性、序列化兼容和不公平 benchmark。",
    },
    "04-realtime-video-analytics": {
        "title": "Realtime Video Analytics - 32 Streams",
        "repo": "https://github.com/skygazer42/realtime-video-analytics-32streams",
        "verified": "README 描述了 32 路 RTSP/RTMP、异步采集、YOLO/ONNX/OpenVINO/TensorRT/RKNN、追踪、Kafka、Prometheus 与 WebSocket dashboard；仓库为可端到端运行的 Python 参考实现。",
        "flow": "RTSP/RTMP/file source → 解码与帧采样 → detector backend → 坐标还原/NMS → tracker 与 ROI/时序规则 → Kafka/指标/WebSocket/dashboard。",
        "sources": ["README.md", "config/sample-pipeline.yaml、config/pipeline-rtsp.yaml", "src/realtime_analytics/、scripts/run_pipeline.py、docs/deployment.md"],
        "boundary": "README 明确 TensorRT/DeepStream 是可替换的后续优化，不能把参考 Python 实现的吞吐直接表述为生产压测结果。",
        "core": ["多流背压、丢帧和优先级调度", "可替换 detector/tracker contract", "坐标变换、NMS 与轨迹生命周期", "Kafka 事件语义与幂等", "分段延迟和流健康观测"],
        "metrics": "每流 input/processed FPS、drop rate、端到端 p50/p95、GPU/CPU/内存、ID switch、事件漏报/误报和重连率。",
        "risks": "断流重连、编解码压力、队列累积、显存泄漏、模型输出不一致和高基数指标。",
    },
    "05-yolo26-ncnn": {
        "title": "YOLO26 NCNN",
        "repo": "https://github.com/skygazer42/yolo26-NCNN",
        "verified": "README、CMakeLists.txt 和部署文档可验证该项目使用 C++/NCNN/OpenCV 支持检测与分割，含 one-to-many NMS 和 one-to-one raw 输出，以及 TopK、NMS、mask parity 工具。",
        "flow": "PyTorch 权重 → 导出 NCNN param/bin 与元数据 → C++ 预处理 → NCNN extract → decode/TopK 或 NMS → bbox/mask 逆变换 → 渲染/输出。",
        "sources": ["README.md", "CMakeLists.txt", "src/yolo26.cpp、yolo26_preprocess.cpp、yolo26_seg.cpp 与 tools/*_parity.cpp"],
        "boundary": "模型权重和导出制品未提交；任何精度、延迟或量化收益都应以固定模型和设备的实测为准。",
        "core": ["导出图与运行时输出 contract", "letterbox 记录和坐标逆变换", "NMS/TopK/box format 的语义", "prototype mask 解码与 resize", "Python/C++ parity 测试"],
        "metrics": "逐阶段延迟、峰值内存、每类 AP/分割质量、Python-C++ 输出差异、崩溃率和设备兼容性。",
        "risks": "RGB/BGR、layout、类别表、box format、动态尺寸、量化误差和 ABI/依赖不匹配。",
    },
    "06-docpilot": {
        "title": "DocPilot",
        "repo": "https://github.com/skygazer42/DocPilot",
        "verified": "README 和 main.py 可验证这是 Flask/OpenAPI 文档解析服务，提供多格式、多引擎、Markdown/structured/chunks/ingest/assets、异步任务、artifact、审计、限流、指标和健康检查。",
        "flow": "上传文件 → 校验/鉴权/限流 → parser engine 路由 → blocks/assets/manifest → Markdown/JSON/chunks/ingest 输出 → artifact/异步回调/审计/metrics。",
        "sources": ["README.md", "main.py", "common/parse_artifacts.py、common/async_tasks.py、common/ratelimit.py 与 docs/API.md"],
        "boundary": "DocPilot 的明确边界是解析服务；向量化、检索和回答生成是下游系统责任，不能混入成功口径。",
        "core": ["多引擎路由与能力声明", "ParseArtifact/Block/Asset/Manifest 数据合同", "chunk 语义边界和 token 口径", "异步任务、回调和 artifact 生命周期", "admission control、审计和 tracing"],
        "metrics": "格式/引擎成功率、CER/WER、结构 F1、p95 解析时延、队列深度、artifact 成本、限流/拒绝率。",
        "risks": "压缩炸弹、恶意文档、SSRF、OCR 质量退化、模型缺失、存储泄露和任务重复投递。",
    },
    "07-taroai": {
        "title": "Taroai",
        "repo": "https://github.com/skygazer42/Taroai",
        "verified": "README 与 infra/docker-compose.yml 展示了 FastAPI 控制面、agent/trigger workers、PostgreSQL、Redis、MinIO、模型/工具/知识/记忆，以及可选 sandbox 和 browser controller 的多租户 Agent 平台。",
        "flow": "用户/tenant 请求 → auth/policy → agent run 与队列 → model/tool/knowledge/memory/sandbox/browser → artifact/evidence → audit/evaluation/billing。",
        "sources": ["README.md", "infra/docker-compose.yml", "apps/api/、apps/web/、taroai/workers/ 与 docs/operations/"],
        "boundary": "Compose 中的默认密钥和 local profile 仅用于本地 POC；生产安全和可用性需用部署证据另行验证。",
        "core": ["tenant/resource ownership 与 RBAC/ACL", "run 状态机、lease、幂等与重放", "MCP/tool allowlist 和审批", "sandbox/brower 隔离与 secret broker", "触发器、配额、评测和审计"],
        "metrics": "tenant 隔离负向测试、run 成功率、队列等待、provider/tool p95、沙箱资源、策略拒绝率与单位任务成本。",
        "risks": "越权工具调用、秘密泄露、重复执行、队列堆积、跨租户 artifact、webhook 重放和依赖不可用。",
    },
    "08-digital-human": {
        "title": "Digital Human",
        "repo": "私有仓库 skygazer42/digital-human（meta-livehuman 分支）",
        "verified": "README 展示离线优先多模态数字人：Electron/Vue、Python gRPC/WS、FunASR、F5-TTS、llama.cpp、LiveTalking、SRS/WebRTC、知识问答及人脸/声纹/动作识别。",
        "flow": "唤醒/人脸/唇动/VAD → ASR → 对话状态与本地/在线 LLM → TTS → LiveTalking 唇形合成 → SRS/WebRTC → 前端视频与字幕；可被用户打断。",
        "sources": ["README.md", "digital-human-client/、digital-human-server/", "LiveTalking/、srs/、scripts/ 与 docs/"],
        "boundary": "README 描述的是可调试开发栈；实时质量、并发和生物识别安全都必须区分演示能力与已测生产能力。",
        "core": ["ASR/LLM/TTS/lip-sync 的可取消流水线", "音视频统一时间轴与 backpressure", "唤醒、VAD、脸/声纹的多模态门控", "本地模型资产与服务健康", "WebRTC/推流和多页面会话状态"],
        "metrics": "wake FAR/FRR、first transcript/audio/video、端到端 p95、A/V drift、对话打断成功率、GPU 利用率和隐私删除 SLA。",
        "risks": "生物特征隐私、回放攻击、模型冷启动、音画漂移、GPU 争抢、推流重连与多用户归属。",
    },
    "09-ultralight-digital-human": {
        "title": "Ultralight Digital Human",
        "repo": "私有仓库 skygazer42/Ultralight-Digital-Human",
        "verified": "README 和 train.py 显示项目含数据准备、Landmark、HuBERT/Wenet/AVE 分支、SyncNet、UNet、覆盖/困难样本加权采样，以及 PyTorch、ONNX Runtime、TensorRT、MNN 的部署路径。",
        "flow": "视频/音频 → 帧率和 Landmark/音频特征处理 → dataset 与 weighted sampler → UNet + pixel/perceptual/SyncNet loss 训练 → checkpoint → PyTorch/ONNX/TRT/MNN 推理与视频合成。",
        "sources": ["README.md", "train.py", "syncnet.py、unet.py、datasetsss.py、data_utils/ 与 example/"],
        "boundary": "README 所列训练策略和部署示例可以讨论，但质量提升与实时性能只有在明确数据、模型、设备和测量口径时才能作为结论。",
        "core": ["音频特征与视频帧的严格对齐", "SyncNet、像素和感知损失的协作", "WeightedRandomSampler 与困难样本挖掘", "按说话人/源视频切分防泄漏", "多运行时导出与输出 parity"],
        "metrics": "同步分数、LPIPS/重建误差、人工 MOS、身份保持、吞吐/端到端延迟、导出前后差异和 OOM 率。",
        "risks": "A/V 错位、相邻帧泄漏、采样过拟合、模型版本不匹配、精度退化和肖像/声音授权。",
    },
    "10-repocoach": {
        "title": "RepoCoach",
        "repo": "https://github.com/skygazer42/RepoCoach",
        "verified": "README 和 package.json 表明 RepoCoach 以 Next.js/TypeScript/Supabase 实现 GitHub 仓库驱动的模拟面试，含 GitHub App、LLM、Monaco、白板、语音/视频、报告及针对索引、证据、会话、路由和安全的测试。",
        "flow": "GitHub App 授权 → 仓库/提交同步与索引 → 证据化问题生成 → 语音/文字/编程作答 → 追问与评分 → 练习 artifact、报告和恢复。",
        "sources": ["README.md", "package.json", "src/、server/、tests/github-*、tests/repo-ready-*、tests/security-boundaries.test.ts"],
        "boundary": "项目在 Aural OSS 基础上重定位；回答应逐项分清继承能力、RepoCoach 改造、设计目标和已通过的测试。",
        "core": ["commit-pinned repo index 与代码证据", "问题生成/追问/评分的事实约束", "会话状态、流式语音与断线恢复", "Monaco/白板和不信任代码隔离", "GitHub/Supabase/LLM 的安全与可观测性"],
        "metrics": "证据引用准确率、问题相关性、生成 p95/成本、练习完成率、评分一致性、会话恢复率、授权/越权测试覆盖。",
        "risks": "仓库 prompt injection、私有代码泄露、过期索引、模型虚构引用、作弊误判、语音断线和 RLS 漏洞。",
    },
    "11-airdesk": {
        "title": "AirDesk",
        "repo": "https://github.com/skygazer42/AirDesk",
        "verified": "README 和 package.json 可验证该浏览器原型使用 React/TypeScript/Vite、MediaPipe Hand Landmarker、本地 WASM/模型资产、六类手势、Three.js 任务空间、可选本地命令 endpoint，以及 Vitest/Playwright。",
        "flow": "getUserMedia → MediaPipe 21 点 landmarks → 手势特征/状态机 → 统一 command → React/Three.js 任务卡或本地 endpoint → 可视反馈与 telemetry。",
        "sources": ["README.md", "package.json", "src/、public/vendor/mediapipe、tests/ 与 playwright 配置"],
        "boundary": "这是浏览器 MVP；本地 fallback 不能表述为真实 Agent 执行，手势鲁棒性需以设备/环境测试说明。",
        "core": ["landmark 归一化和手势状态机", "去抖/迟滞/冷却时间", "相机坐标到 2D/3D 映射", "React 与 Three.js 的帧循环边界", "本地资产、fallback 与摄像头权限降级"],
        "metrics": "first camera-ready、gesture-to-action、手势 precision/recall、误触发率、FPS、主线程耗时、相机启动失败率。",
        "risks": "光照/遮挡/左右手、主线程卡顿、权限/HTTPS、资源泄露、误操作与摄像头隐私。",
    },
    "12-diffusion-models": {
        "title": "Diffusion Models",
        "repo": "https://github.com/skygazer42/Diffusion-Models",
        "verified": "README 组织了 VAE、β-VAE、VQ-VAE、ELBO、Glow/flow、DDPM 和简化 DALL·E 的学习/比较材料，使用 Notebook 与 PyTorch，覆盖 MNIST/CIFAR-10/CelebA、FID/IS/重建误差等。",
        "flow": "数据与统一预处理 → 生成模型训练/验证 → checkpoint/EMA/采样 → 重建与生成评测 → 可视化、指标、失败样例与实验记录。",
        "sources": ["README.md", "VAE/、Beta-VAE/、VQ-VAE/、DDPM/、Gflow/、DALLE/ 下的 Notebook、训练脚本和配置"],
        "boundary": "README 指向上游 jhlucc；面试开场先说明 fork、复现、改动和独立实验，绝不能把上游实现归为个人原创。",
        "core": ["ELBO/重参数化和 posterior collapse", "VQ codebook 与离散 token", "flow 的可逆变换和 log-det", "DDPM 加噪、去噪、schedule 与采样", "公平实验、FID/IS/重建与定性分析"],
        "metrics": "ELBO/重建、FID、IS、codebook perplexity、采样耗时、显存、人工失败样例与可复现运行成功率。",
        "risks": "notebook 隐式状态、数据/预处理不公平、指标被误读、mode collapse、训练数值不稳定和许可边界。",
    },
}

# One direct, repository-specific answer per table row. The long-form builder
# below turns each into an answer page with code evidence, verification and
# failure modes instead of pretending that a generic architecture checklist is
# sufficient.
DIRECT_ANSWERS = {
    "01-pokemon-ai-toolkit": """
项目的目标是把官网上分散的宝可梦属性、图片和进化信息变成可分析、可查询、可对话的数据产品；应按实际提交说明自己负责的爬取、清洗、图谱、问答或模型实验，不能把整个链路都笼统说成从零完成。
选择官网爬虫的价值是能控制字段、图片和更新节奏，但前提是遵守站点许可与限速；若只需要静态分析，经过许可的公开数据集成本更低。
每个抓取对象应以图鉴编号作为幂等键，抓取任务保存状态、内容 hash、时间和失败原因；重跑时只补缺失或变更记录，并采用限次重试和指数退避。
解析器不能只在报错时才发现页面变化，应对关键 selector 建立样本快照、字段完整率和 schema 校验；异常比例升高就暂停写入并保留原始 HTML 供修复。
图片应通过图鉴编号和来源 URL 关联，而不是仅依赖中文文件名；同时保存下载时间、内容 hash、MIME 类型和原始 URL，才能追溯错配。
清洗的基础门禁是主键唯一、数值范围、单位、缺失率、枚举值和重复率；所有修正规则应版本化，并输出前后行数和分布差异。
身高、体重等字段要同时保留原始值/单位和标准化值/单位；转换规则与缺失、未知值处理应写入数据字典，避免分析阶段二次猜测。
同一实体不应依赖名称识别，图鉴编号才是主键；中文、英文和别名应作为带语言标签的属性，名称歧义时返回候选而不是新建节点。
清洗是否有偏差要靠前后数据分布、删除原因统计、固定抽样和规则审计验证；不能因为没有训练模型就忽略数据泄漏和选择偏差。
仪表盘必须服务于一个可行动问题，例如属性弱点、身高体重分布或进化路径；每个图表都要说明数据版本、筛选口径和结论的边界。
推荐以 Pokémon 为节点，以属性、弱点、进化等为类型化关系；关系方向、基数、来源和版本必须明确，才能同时服务事实查询和路径查询。
导入时先把文本记录解析为带稳定 ID 的节点和边，再用约束与批事务写入 Neo4j；失败批次应可定位、可重放，而不是只依赖一次性脚本。
节点使用图鉴编号唯一约束，边使用两端主键加关系类型/版本去重；Cypher 用 MERGE 时要清楚哪些字段可更新、哪些字段不能覆盖。
KGQA 应先做意图和实体识别，再把受控模板填成参数化 Cypher，执行后用结构化结果作答；自由生成只能用于解释，不能直接编造图查询。
低置信实体应触发澄清或列出候选，只有问题足够明确时才执行查询；直接猜一个同名实体会把错误伪装成确定事实。
Cypher 必须参数化并使用允许的查询模板、索引、结果数和超时上限；禁止把用户原文拼进查询，避免注入和全图扫描。
多跳查询需要限制 hop 数和候选规模，并返回支持结论的路径；否则既会超时，也无法让用户核验“为什么得到这个答案”。
图谱有明确事实时应优先引用图谱结果；模型输出与图谱冲突时要以来源和版本为准，必要时展示冲突而不是强行合并。
KGQA 至少分别评估意图分类、实体链接、Cypher 执行、答案正确和证据完整性；仅报最终准确率无法定位错误环节。
增量数据按数据版本写入，先在影子库或事务中校验差异，再切换读版本；保留旧版本和回滚脚本，避免新代际数据污染历史答案。
微调适合处理图谱不覆盖的表达、多轮交互和风格，而结构化事实仍应走图谱；两者不是互相替代的关系。
训练/验证/测试应按实体、问题模板或来源分组切分，避免同一宝可梦的近似问法同时出现在训练和测试中。
应使用未见实体、改写、拼写错误、对抗问法和人工盲评检查泛化；训练集上的高分只能说明记忆或模板拟合。
CLIP 实验的合理目标是图文检索或图像辅助分类，正负对要由稳定实体 ID 构造；在没有基线和评测集前不能宣称“优化了性能”。
图片缺失或 hash/编号不一致时应阻止进入跨模态索引，并回退到结构化文本答案；错误图片比没有图片更损害可信度。
规模增加一百倍时，最先要拆的是抓取队列、对象存储、批导与图索引；是否上分布式组件应由吞吐和延迟压测决定。
应确认站点 robots/服务条款、图片版权和再分发范围，保留来源并限制用途；课程/研究用途不自动等于可商用。
排查应从用户问题对应的答案和 request ID 反向追到图查询、实体链接、图谱版本、清洗记录和原始网页；先定位哪层错，再改规则或数据。
若重做，应该先交付可追溯的爬取—清洗—图谱事实查询闭环，再决定是否投入微调和 CLIP；后两者在没有评测前不应抢占基础数据质量工作。
证明增益需要固定数据版本和问题集，对比无图谱/无 CLIP 的基线，并报告正确率、引用质量、成本和失败案例；单个 demo 不构成证据。
""".strip().splitlines(),
    "02-smart-assistant": """
一次请求应经过 API 鉴权与 request ID、意图/风险路由、图谱或检索/工具、证据组装、LLM 生成和可观测性；实际回答时应指向具体 `api.py` 与路由代码，而不是只画框图。
图谱适合强结构事实和路径解释，向量检索适合非结构化文档，LLM 负责理解和表达；三者由问题类型、证据质量与成本共同决定。
需要逐项说明本人实现的路由、数据模型和接口，以及 LangGraph、LangChain、Dify、RAGFlow 与基础模型提供的能力；复用不是问题，模糊归属才是问题。
路由应输出意图、置信度和原因，并把事实查询、文档问答、闲聊和联网需求送到受控分支；低置信度优先澄清或多路候选，不能静默猜测。
路由错误时可用保守降级：并行保留少量候选、要求证据、展示不确定性并记录 trace；绝不能让一个错误路由直接产生无来源的肯定答案。
API 需要定义请求 schema、流式/非流式响应、错误码、超时、幂等键和 trace 字段；集成 Dify 或前端时以这一契约而不是内部对象为边界。
模型 provider 应通过统一 adapter 隔离模型名、上下文、tool calling、流式和异常格式；配置、prompt、模型版本和密钥从环境/配置管理读取并写入 run 记录。
LangGraph 状态应包含用户输入、路由结果、证据、工具调用、重试次数和最终引用；循环必须有限次，并为人工审批或失败回退设置中断点。
图数据库、向量库和模型服务不可用时要分别定义超时、缓存、重试和用户提示；只有可验证的局部结果才能返回，不能把依赖错误包装成模型答案。
每次调用都应携带 request/run ID，并在 API、检索、Cypher、模型调用和日志中关联；这样才能将错误答案定位到具体候选或 prompt。
RoBERTa、TF-IDF、规则可分别提供语义、词面和高精度先验，融合前要输出候选和置信度；冲突通过校准、优先级或人工审核处理。
抽取产物必须保存文档版本、span、模型/规则版本、置信度和写入批次；低置信关系进入审核队列而非直接成为图谱事实。
不同格式先被规范为文档、页/工作表、块、资产和文本的统一 schema，再进入 embedding；每一层都必须能回链到源文件和位置。
chunk 应优先尊重标题、表格和段落边界，再在块内按 token 预算切分；大小与 overlap 用标注问答集验证，不靠固定经验值。
Milvus 更适合独立向量服务和规模化索引，Chroma 适合轻量本地开发；无论选哪个都要把 collection、embedding 版本和过滤语义封装起来，便于迁移。
ACL 必须在检索查询中强制注入 tenant/user/document 过滤条件，并由服务端验证；只在 UI 隐藏文档不能防止向量库越权召回。
诊断先保存 query、候选、分数、rerank、chunk 版本和最终引用；候选不在前 K 是召回问题，候选在但排序低才是重排问题。
图谱节点和 chunk 应使用共享的规范实体/文档 ID，并由更新事件同步版本；允许最终一致，但必须能看到两边的版本差异。
Neo4j 应为稳定实体键建唯一约束和索引，所有写入通过受控 MERGE/事务完成；查询参数化并限制 hop、行数与超时。
发生冲突时应比较来源可信度、时间和版本，必要时并列展示；不能让语言模型在缺乏证据时自行“裁决”。
prompt 要将检索内容标为不可信数据而非指令，要求模型引用编号，并规定没有支持证据时拒答或澄清；输出再校验引用确实来自候选集。
文档 prompt injection 和越权工具需要分离系统指令与数据、工具 allowlist、参数 schema、最小权限和审批；模型文本永远不能直接获得执行权。
小模型意图分类通常更快、便宜且可稳定回归，LLM 更灵活；应在同一标注集上比较准确率、拒答、延迟和维护成本后决定路由。
Dify 接口要有请求认证、超时、重试、幂等键和明确的回调/失败语义；下游重放时不能重复写入同一任务。
短期上下文用于当前会话，长期记忆需明确所有者、来源、TTL 和删除入口；摘要应带版本，过期或权限变化时必须失效。
离线评估包括检索、引用、答案、拒答和安全集，在线还要看延迟、成本、满意度和错误反馈；所有指标要按数据版本分桶。
对抗集至少覆盖 prompt injection、同名实体、过期文档、OCR 错字、无权限文档和恶意工具参数，并加入持续回归。
依赖和模型应使用锁定版本、镜像/环境快照、模型 hash 和升级 gate；`requirements.txt` 只是起点，不等于可重复环境。
错误答案排查顺序是请求/路由、权限过滤、候选与重排、图查询、prompt/模型、引用渲染；每层都用 trace 证据排除。
上线前最优先补齐的是服务端 ACL/鉴权、端到端可观测与回归评测/发布门禁；没有这三项，功能越多风险越大。
""".strip().splitlines(),
    "03-foresight": """
ForeSight 的价值不是罗列模型，而是把统计、机器学习和深度模型放进统一的训练、预测、回测、artifact 和 CLI 契约中；应说明自己对该公共表面的具体贡献。
稳定 API、registry、CLI 和 artifact schema 是用户集成点，内部模型实现可演进；这能避免每加一个后端就破坏脚本和已保存的预测制品。
长表用 `unique_id` 区分序列、`ds` 表示时间、`y` 表示目标，可自然表示 panel 数据和附加特征；转换时必须检查排序、频率、重复时间和缺失。
CLI 不应复制业务逻辑，而应解析参数后调用同一 service/API；这样 Python 与命令行的模型解析、错误和 artifact 才能一致。
`foresight doctor` 应检查 Python/依赖 extras、数据目录、模型后端与权限配置，并给出下一步安装或修复建议；它是在真正训练前的 preflight。
核心依赖保持 NumPy/Pandas 能降低安装和导入负担，重后端放在 extras；代价是运行时必须提供准确的 capability 与缺失依赖错误。
每个模型应有唯一名称、参数 schema、所需 extra、支持的数据能力和稳定级别；registry 是防止同名模型或隐式默认值漂移的中心。
artifact 至少包含模型/adapter、训练数据与特征 contract、配置、版本和序列化格式；schema 变化以显式 migration 兼容旧制品。
GPL-3.0-only 会影响闭源集成和分发方式，项目应明确许可证并让使用者与法务核对；技术面试不应给出未经确认的法律结论。
发布 gate 应在干净环境构建 sdist/wheel、安装 smoke、跑核心契约测试和静态检查，并验证版本与文档；失败不可发布。
registry 应先解析 model spec 和 capability，再延迟加载对应 adapter；这样缺少的 optional backend 不会阻止核心包导入。
新模型必须实现一致的 fit/predict、输入校验、随机种子、协变量和序列标识语义，并提供最小 contract test；不能只把第三方预测函数直接暴露出来。
walk-forward 的每一折只能用 cutoff 之前的数据训练，在后续 horizon 上预测，再按 step 滚动；任何标准化和特征统计也必须在训练窗口内拟合。
panel 回测要按 `unique_id` 分组排序，每条序列只能看到自身历史；全局模型可共享训练序列但不能访问测试期的任何目标值。
非等频、DST 和缺失时间不是可静默修复的小问题，框架要声明频率 contract 并让用户选择重采样、插值或拒绝；否则评估没有意义。
概率输出可以是 quantile、样本或分布参数，评估要同时看 coverage、sharpness 和 CRPS/分位数损失；宽区间不自动代表好校准。
指标需要声明最优方向、零值/尺度处理和聚合权重；MASE、sMAPE、RMSE 不能随意平均后比较不同序列。
leaderboard 必须固定数据版本、split、horizon、timeout、硬件/预算和随机种子，并保留失败运行；否则模型排名只是配置差异。
全局模型在多序列共享模式且单序列样本少时通常受益，局部模型在异质性强或隔离要求高时更稳；应通过分组回测选择。
不支持的数据特性应在 preflight 由 capability matrix 解释原因和替代模型；运行到一半才抛底层库异常是差的公共接口。
跨后端测试要重点验证输入/输出、时间切分和 artifact 契约，重依赖后端用可选 CI 或 mock；不要用一个轻量测试冒充全部后端已验证。
stable/beta/experimental 必须在文档、版本策略、CI 覆盖与弃用规则中一致体现；README 标签本身不能形成兼容承诺。
缓存键应包含数据/特征/配置/模型/代码版本 hash，任何一个变化都失效；否则复用旧 artifact 会产生难以发现的错误预测。
大数据场景应避免反复复制 DataFrame，采用分区、向量化、缓存特征和受控并行；先 profile 内存、I/O、fit 和 predict 再优化。
线上监控要看数据到达、缺失、分布漂移、预测误差与区间校准，并有 retrain/告警规则；真实标签延迟到达时需区分实时和回填指标。
可复现性要求记录所有 RNG、后端/硬件非确定性开关、依赖和数据版本；只设置一个 NumPy seed 不足以保证深度后端可重复。
诊断链应把预测点回连到训练 cutoff、原始观测、变换、模型 artifact 和运行配置；这样才能判断是数据还是模型错误。
服务运行时自动安装 extra 会破坏可复现、供应链和权限边界；应在构建/部署阶段安装，并在 doctor/preflight 中报告缺失。
benchmark 要分开统计数据加载、特征、fit、predict、artifact 加载和端到端时间，固定硬件、warmup 和样本规模后报告 p50/p95。
下一步优先级取决于用户痛点：若现有模型的比较不可信，应先补评测/兼容；只有明显能力缺口且有回归集时才增加新模型。
""".strip().splitlines(),
    "04-realtime-video-analytics": """
一帧应沿“采集、解码、采样、检测、坐标还原、追踪、事件、Kafka/指标、WebSocket”流动；回答时要标明每段的队列和时间戳，而不是只列组件。
32 路容量由分辨率、编码、目标 FPS、模型、GPU/CPU、显存、网络和队列共同决定；必须用固定 workload 压测，不能从 README 的上限推导生产吞吐。
异步 capture 能避免单个网络读阻塞主调度，但解码、OpenCV 调用、Python 线程和下游队列仍可能阻塞；需要 profile 后决定线程/进程边界。
断流重连要有流 epoch、指数退避、旧帧丢弃和句柄释放；事件时间线不能把重连前后帧混在一个轨迹里。
H.265 通常节省带宽但解码成本和兼容复杂度更高；应按可用硬解、端到端延迟和摄像头实际码流选择。
每路独立模型/FPS/ROI 让高风险相机获得资源、低优先级流被降采样；配置 schema 必须校验，避免运行时出现无法解释的差异。
处理慢于输入时实时分析通常丢旧帧并保留最新帧，但事件任务可能要最小采样率或临时升频；策略必须由业务漏检成本决定。
优先级调度可用配额/加权轮询加老化，既保证关键流 SLA 又避免普通流永久饥饿；队列等待时间应可观测。
不同摄像头时间戳不可天然比较，应记录源时间、接收时间和时钟质量；跨相机事件需依赖 NTP 或明确的对齐窗口。
端到端延迟需在 capture、decode、queue、inference、event emit、WebSocket/render 分段埋点，并报告 p50/p95/p99；只测模型 forward 不足够。
后端统一接口要固定输入色彩/尺寸、输出坐标/类别/置信度、模型元数据和错误语义；adapter 内消化 Ultralytics、ONNX、TensorRT 等差异。
模型、类别表和预处理必须作为同一 manifest 发布并在启动校验 hash；任一不匹配都可能让模型“正常运行但全错”。
letterbox 时保存 scale 和 pad，后处理先去 pad 再除 scale 并裁剪原图边界；奇数 padding 和非方图要有 golden test。
置信度组合要以模型输出 contract 为准，有的输出已融合 objectness/class；不能假设所有 YOLO 导出格式相同。
class-aware NMS 允许不同类别框共存，agnostic NMS 更激进；是否使用由重复目标与类别混淆的业务代价决定。
confidence、IoU、max-det 是联动参数：阈值过低会放大后处理，过高会漏检；应用离线每类指标和延迟曲线调优。
parity 应比较 box/score/class、排序、阈值和容差，而不是仅比较最终张数；同时固定输入和导出版本。
追踪器需要定义检测匹配、轨迹确认、lost/removed 阈值和 ID 复用策略；遮挡场景要用 ID switch/fragmentation 而非肉眼判断。
ByteTrack/DeepSORT 在拥挤遮挡或外观特征有价值时更合适，但成本更高；轻量 IoU tracker 是合理基线，不应被事后否定。
时序动作模型的帧窗口需与检测/轨迹 ID 和时间戳对齐；缺帧、重连和新轨迹必须显式暖机或拒绝判断。
Kafka 不可用时可按事件优先级选择短时落盘重放、受控丢弃或背压；无限阻塞会拖垮视频主链路。
Prometheus label 应使用有限的 backend/status/tier 等维度，避免把每个 stream ID 或 track ID 都作为 label；单流细节放日志或 trace。
dashboard 应推送聚合状态、节流后的预览和可筛选事件，不能把每帧所有检测都广播给所有浏览器；WebSocket 需有背压和断线重连。
process liveness、服务 readiness 和单个 stream health 是不同语义；后者需结合最后帧、错误率、FPS 和重连状态展示。
FFmpeg 模拟流和固定文件源可复现断流、低 FPS、事件和回归；测试应比较黄金事件而不只检查进程退出码。
Docker 部署要显式管理 GPU runtime、模型挂载、只读配置、secret 和状态卷；镜像里不应固化摄像头 URL 或凭证。
内存/显存增长常来自未限队列、保留 frame/tensor、未释放 capture 或缓存；用分段指标和 heap/GPU profile 定位，而非定期重启掩盖。
在线改 YAML 应先 schema 校验与版本化，在影子/单流验证后原子切换；失败可回滚到上个已知配置。
扩容压测要固定分辨率、码率、模型、目标 FPS 和硬件，从 4 到 32 路记录每流延迟、drop、资源和失败点，得到退化曲线。
迁移 DeepStream/TensorRT 时保留 detector/tracker/event 的输入输出 contract、golden 回放和指标语义；替换加速层不应改变业务事件。
""".strip().splitlines(),
    "05-yolo26-ncnn": """
端侧链路必须把权重、导出参数、NCNN param/bin、类别表、输入尺寸和后处理配置当作同一制品；C++ 端只应加载与该 manifest 匹配的组合。
不提交大模型权重能控制仓库体积和许可风险，但发布必须给出可验证下载来源、hash 和可重复导出命令；否则用户无法复现。
one-to-many 输出通常需要常规 NMS，one-to-one raw 输出则交由应用做 TopK/去重；二者的张量语义和后处理前提不能混用。
`--post=nms` 应只用于输出可按 NMS 解码的模型，`--post=topk` 只用于 raw 约定；启动时检查输出 shape/metadata，比错误结果后再猜更安全。
`cxcywh` 与 `xyxy` 是不同几何 contract，必须由导出元数据或严格 shape/样例确定；用图片“看起来差不多”校验会掩盖系统性偏移。
CMake 将公共 `yolo26` 库与检测 CLI、可选分割 demo 和 parity tools 分开，能让核心代码复用、功能可裁剪、测试不污染主二进制。
NCNN/OpenCV/C++ ABI 问题应先确认 CMake 找到的 include/lib 路径、编译器与架构，再用最小加载程序定位；不要直接把所有报错归为模型问题。
GPU 未必比 CPU 快：小图/单张可能被上传与初始化开销主导；应分别测 warmup 后的 preprocess、extract 和 postprocess。
改变输入尺寸要同步 stride/letterbox、输出 grid 解码、坐标逆变换和 mask resize；模型文件名相同不能保证这些 contract 不变。
发布应生成包含导出命令、环境、模型 hash、类别表、样例和测试结果的 manifest，并在 CI 或设备 smoke 中验证加载。
letterbox 要保留缩放比例与左右/上下 pad，逆变换后裁剪边界；这是检测框和分割 mask 正确映射回原图的必要条件。
score 的计算依赖导出模型，有的含 objectness、有的已是类别概率；解码器应依据 manifest，而不是硬写 `obj * class`。
class-aware NMS 只在同类内压制框，agnostic NMS 跨类压制重叠框；前者保留多类别不确定性，后者减少重复但可能误杀。
`conf`、`iou`、`max-det` 要和类别分布、候选数、延迟共同调优；建议在验证集绘制 AP/延迟曲线，不能只调出“视觉上干净”的结果。
TopK 仅限制数量不保证去重，因此还需定义按类别、IoU 或坐标近似的 dedup 规则，并保持排序稳定。
NMS parity 应逐个比对输出框、类别、分数、排序和阈值边界，允许合理浮点误差；只比最终图片无法定位差异。
分割使用 detection 的 mask coefficient 与 prototype 线性组合，再 sigmoid、crop 和 resize；需要明确每步张量布局和原图尺度。
retina mask 通常在更高分辨率生成/裁剪 mask，质量更好但耗时/内存更高；是否开启应由目标边缘质量和设备预算决定。
mask parity 需固定输入、插值方法、阈值和容差，既比较数值也比较 IoU/可视差；小数差异与语义错位要区分。
Python/C++ 不一致时先 dump 同一预处理 blob，再比较原始输出、decode、NMS/mask、绘制；这比直接改阈值有效得多。
benchmark 必须把读图、预处理、NCNN extract、后处理和写图拆开计时，区分 cold start 和 steady state；端侧用户关心后者的 p95。
线程数/affinity 应按设备核心结构和共存任务测量，避免推理线程挤占采集/UI；吞吐高但 p99 抖动大并不适合实时场景。
量化需在代表性校准集上比较每类检测/分割指标和极端样例，记录 layer fallback；只报告平均速度会掩盖小目标退化。
内存治理靠复用 Mat/blob、限制并发、延迟加载模型和监控峰值；OOM 时要返回可理解错误而非崩溃。
param/bin 损坏、类别数不符、空图和不支持的输出 shape 都应在解析期验证，错误信息要告诉用户期望和实际值。
检测与分割的输出 contract 差异很大，独立 CLI 能降低错误组合；公共库再共享预处理、加载和绘制，避免重复实现。
交叉编译应固定 toolchain、ABI、NCNN/OpenCV 配置和模型资产，设备端用 golden image smoke；宿主机运行通过不能证明移动端正确。
新增姿态或 OBB 应作为新的 task/decoder 和测试集接入，保留原 task 的 CLI 行为；不要让一个万能分支隐式猜输出格式。
最常见的“跑通但全错”是 BGR/RGB、归一化、NHWC/NCHW、box format 或类别表错配；逐阶段 dump 比看最终框更快定位。
发布 gate 至少包含模型加载、preprocess/postprocess parity、golden 图、内存/延迟阈值和失败回滚制品；设备矩阵要单独记录。
""".strip().splitlines(),
    "06-docpilot": """
DocPilot 的职责是把多格式文件稳定地转换为有来源的解析产物，而不是回答问题或建设向量库；清晰边界让解析、检索和生成分别扩缩容和排障。
`/api/v1/parse` 应接收文件与解析/产物选项，小文件可同步返回，大文件或模型密集任务创建可轮询/回调的异步任务；两条路径的 artifact contract 必须一致。
Markdown 面向阅读和下游 LLM，structured JSON 保留层级/坐标，chunks JSONL 面向检索，ingest JSONL 面向批导；它们必须共享 document/block/asset 来源 ID。
部分成功应通过 manifest 标出成功块、失败资产、warning 和可重试原因，同时返回已可信的正文；不能把整份文档伪装成完全解析成功。
artifact 生命周期需要 tenant 范围的 key、创建者/访问策略、TTL、删除/保留规则和审计；下载接口每次都验证访问权限。
OpenAPI 应由实现/测试生成或校验，CI 检查 schema 破坏性变更；SDK 和前端以版本化 schema 集成而不是复制文档样例。
health 说明进程活着，ready 说明关键依赖和模型可服务，metrics 用于观测；把三者混为一个 200 会让编排器做出错误决策。
认证 header、API key 和 CORS 应由环境配置并在服务端验证，开发默认值不能进入生产；CORS 只解决浏览器跨域，不替代授权。
上传入口要做 MIME/魔数、大小、页数、像素、压缩比、解压预算和恶意内容检查，再交给解析器；后置校验无法防止资源耗尽。
request ID 与 tenant ID 应写入请求日志、异步任务、artifact manifest、审计和 metrics/traces；这样才能完成端到端归因。
路由应基于格式、扫描质量、版面复杂度、模型可用性、成本和超时选择 engine，并记录实际选择/回退原因供评测。
兼容 `deepdoc` 可保护旧客户，但要在响应/日志中标记 alias 使用率和弃用日期，迁移完成后删除双维护路径。
可抽取文本 PDF 应优先原生解析，扫描件走 OCR，复杂多栏/表格可路由视觉模型；路由不确定时保留来源并提供质量信号。
每个表格、图片和公式 asset 都要带页码、bbox、父 block 和文件 hash，文本引用也指向同一 provenance；没有这些 ID 就无法审计或渲染回跳。
chunk 以结构 block 为原子，先按标题/列表/表格边界分段，再在安全位置按 token 上限拆分；overlap 只用于连续文本，绝不把一张表切成无上下文碎片。
token 计数必须声明使用的 tokenizer 与版本，或明确为近似字符估算；不同下游模型的上下文预算不能被一个模糊数字掩盖。
网页/邮件等外部资源应在隔离网络和 allowlist 下抓取，限制重定向、大小、DNS 和超时；否则文档解析入口可能成为 SSRF 通道。
多引擎选择靠标注集上的文本 CER/WER、表格/阅读顺序结构 F1、时延和成本对比，并按文档类型分桶；不能凭单份 PDF 判断。
可复现结果要记录输入 hash、engine/模型/代码版本、配置 profile、依赖和运行环境；同一文件的两个结果不同才有可诊断依据。
去重可以在同一 tenant 内按内容 hash 复用安全 artifact，但访问检查、解析 profile 和保留策略仍不能跨 tenant 共享。
异步任务状态机应包含 accepted/queued/running/succeeded/failed/cancelled，并用幂等键和 lease 防止重复执行；用户能查询任务和结果链接。
回调需要签名、超时重试、指数退避、死信和下游幂等消费；否则网络抖动会造成漏通知或重复入库。
rate limit 控制请求速率，admission control 控制昂贵解析的并发/队列；两者要分别反馈配额和重试时间，不能相互代替。
全局 app 初始化会让环境变量和缓存泄漏到测试，宜通过 app factory/依赖注入隔离；至少应让测试能创建独立配置和 store。
模型未下载、GPU 不可用或 Java/Tika 缺失时，readiness 应提前暴露 capability，解析接口返回可操作错误或选择可用回退；不能悄悄产出低质量结果。
metrics label 只能包含有限的格式、引擎、状态、tier 等，文件名、task ID、tenant ID 等高基数字段应放日志/trace。
retention janitor 以 manifest/引用和任务状态判断可删除对象，先标记再延迟删除并写审计；不能只按目录 mtime 清理。
安全回归集应包含密码/畸形/超大/压缩炸弹、复杂表格、提示注入和外部资源样本，测试在隔离环境运行且不含敏感真文档。
排障从 request/task ID 找 manifest、engine 决策、worker/resource、输入 hash 和回调记录；先确定是入口、路由、模型还是存储故障。
十倍吞吐前先用 workload 分布区分 CPU/GPU、队列、存储和模型瓶颈，再针对热点做批处理、路由/缓存或水平扩展；没有压测不应先武断换模型。
""".strip().splitlines(),
    "07-taroai": """
Taroai 应被解释为“控制面负责身份、策略、编排和审计，数据面负责状态、队列和制品，执行面负责 Agent/工具/沙箱”的多租户系统；画图时必须标出跨边界调用和数据所有权。
每个 workspace/resource 都必须有 tenant owner，user 通过角色获得能力，ACL 再控制具体对象；不能仅靠前端选择的 tenant ID 实现隔离。
RBAC 管理角色权限，SSO 建立可信身份，SCIM 同步成员生命周期，资源 ACL 管理细粒度访问；四层应组合而非互相替代。
所有 API/worker 查询都从认证上下文强制注入 tenant scope，存储 key 也按 tenant 分区，并用负向测试验证猜 ID 无法读到其他租户资源。
分享链接应存不可逆 token hash，绑定资源/权限/过期时间，可撤销并记录使用审计；它不是长期的“匿名管理员”入口。
Web、API、worker 拆分能独立扩缩容和限制权限：Web 不应直连数据面，worker 不应拥有管理员 API 权限，失败也不会拖垮所有请求。
两个 agent worker 必须以队列 lease/compare-and-set 领取任务，run 有幂等键和 fencing token；worker 崩溃后过期 lease 才能安全重领。
readiness 不只看 API 进程，而要确认数据库、Redis、对象存储和迁移状态可用；Compose 的启动顺序不能代替运行时探测。
migration 应由单独 job 或分布式锁串行执行，应用副本只在目标 schema ready 后启动；向后兼容迁移和恢复方案先于破坏性变更。
Compose 中的本地默认密钥仅为开发便利，生产必须从 secret manager 注入、禁止弱默认值并在启动时检查；将 `.env` 打进镜像是不安全的。
run 状态机要持久化输入快照、策略决策、模型/工具事件、artifact 和终态；每一次重放都应明确是否允许重做有副作用的步骤。
结果应以可展开的事件时间线呈现：模型文本、工具参数/结果、检索引用和产物各自可追溯；不要把工具过程伪装成模型自述。
动态发现只影响“可见候选”，真正执行仍需 server-side allowlist、tenant policy、参数 schema 和权限检查；MCP 注册不等于自动授权。
重试只能用于幂等或有补偿的操作，并有总次数/预算；邮件、支付、写外部系统等副作用操作需要 idempotency key 或人工审批。
provider adapter 应暴露流式、上下文、tool calling、图像、限流、成本和错误能力；调用记录锁定 provider/model/参数，才能解释行为变化。
摄取链需把文件版本、chunk、embedding、ACL 和删除 tombstone 关联；文档删除/降权必须从检索索引传播，而非只删原文件。
当前会话上下文、用户偏好、团队知识和 Agent 任务记忆有不同 owner/TTL/可见性；检索时按 scope 和新鲜度排序，用户可查看和删除。
沙箱/浏览器是高攻击面和高资源组件，作为可选 profile 有利于按风险启用；默认关闭比默认暴露更安全。
只读 rootfs、删除 Linux capabilities、非 root 用户、PID/CPU/memory 限制是纵深防御；还需要限制挂载、网络 egress、镜像来源和 secret 注入。
Agent 不能因处于受限容器就被信任：网络、共享卷、环境变量和 secret resolver 都可能成为逃逸路径，应逐一做 allowlist 与审计。
调度器计算到期任务，due worker 执行任务可避免长周期调度阻塞执行；两者需使用 schedule occurrence ID 保证错过/重启后的补偿不重复。
webhook 要验证签名、时间戳和 nonce，映射到固定 tenant/trigger，并记录原始事件 hash；重放或未知来源默认拒绝。
配额应覆盖模型 token、工具次数、沙箱 CPU/时长、存储和并发 run，在提交前预估、执行中硬限制、结束后记账；超过配额返回可解释状态。
评测门禁应在 Agent、prompt、skill、模型或工具配置变更后运行，采用版本化任务集和安全集；通过后才发布，不能只看一次聊天 demo。
审批应贴近不可逆副作用的工具调用前，并展示计划、目标和参数；低风险纯读取可免审批，高风险写操作不应等模型输出后才确认。
排障以 run ID 串联前端、API、queue、worker、provider、sandbox 和 artifact 事件，并在时间线上看出等待/失败段；没有跨服务 trace 无法有效定位。
Redis 可短时缓存/队列恢复但不能替代 durable state，Postgres 不可用时拒绝需强一致的写入，对象存储不可靠时不能声称 artifact 已持久化；每种依赖要有明确降级。
灾备需分别定义数据库、对象存储、审计和密钥的 RPO/RTO，做加密备份和恢复演练；仅有备份脚本不等于可恢复。
压测应以不同 token、工具、沙箱比例的真实 mix 驱动，观察队列、provider 限流、worker 和沙箱配额；单一 hello-world 任务测不出瓶颈。
下季度优先级应先保护隔离与数据安全，再补可观测/评测和用户最常用功能；用风险、影响面和可验证里程碑排序，而不是按功能炫酷程度。
""".strip().splitlines(),
    "08-digital-human": """
一轮实时交互应从唤醒/授权开始，经过 VAD 与 ASR、对话状态和 LLM、TTS、唇形生成、SRS/WebRTC，再回到前端字幕/画面；每段都要可取消并带时间戳。
离线优先意味着 ASR、TTS、LLM、知识和唇形能在本地服务路径运行，在线模型只能作为显式配置的可选增强；必须说明模型资产是否已在本机可用。
前端负责设备权限、交互和渲染，Python 控制面负责编排状态和服务调用；gRPC/WS 边界应以消息 contract 和取消语义定义，避免两端同时拥有会话真相。
打断时先传播 cancellation/run version，停止或忽略旧 ASR/LLM/TTS/lip-sync 事件并清理播放队列；新一轮结果不得与旧视频混播。
20 秒窗口应保存与当前任务相关的最近轮次或摘要，超出后按策略压缩/过期；用户身份、隐私和可删除性决定能否保留更久。
实时数字人若承诺视频形象，音频降级不能假装完整成功；应明确显示 degraded state，并允许用户选择继续语音或重试视频。
延迟预算要分成 end-of-speech、ASR final、LLM first token、TTS first audio、首个 lip frame 和 WebRTC 首帧；目标以 p95 而非平均值定义。
字幕、音频和口型应共享单调时间轴，给每段音频/视频加 sequence 和 timestamp，播放器通过小缓冲和 drift correction 对齐；不能依赖“按到达顺序播放”。
WHIP/WHEP/WebRTC 适合低延迟媒体，SRS 负责流服务与转发；NAT、抖动和重连需通过信令、ICE/网络指标和会话重协商处理。
不同页面应复用会话 ID、媒体 ownership 和状态机，一个页面是 producer 还是 observer 要明确；切页时关闭不再拥有的流。
按键、唤醒词、人脸和唇动覆盖不同可用性/安全/免手操作场景；必须允许用户选择和禁用，不应强制生物特征唤醒。
唇动门控先确认可见说话动作，再以 VAD/能量确认语音，在时间窗内同时满足才送 ASR；阈值要用 FAR/FRR 样本调校。
人脸验证应在进入敏感会话前执行，并最小化保留模板/结果；失败只显示授权失败，不暴露身份库或相似度细节。
声纹需要 liveness/反回放、阈值校准和失败降级；它是风险控制信号，不应单独被宣传为绝对身份认证。
摄像头帧、声纹模板和日志必须定义本地存储位置、加密、保留期、访问控制和用户删除流程；调试采样需要显式授权。
用户拒绝摄像头或设备不存在时，系统应保留按键/语音等非视觉入口，并用清晰提示引导权限恢复；不可无限重试浏览器权限。
各视觉模型应有独立采样率/分辨率/优先级，并以共享 GPU 调度和队列限制避免互相挤占；实时对话路径通常优先于展示特效。
多人场景要先做人脸/声源/轨迹的 active subject 选择，并在不确定时询问或拒绝；默认把任意人的声音归给已授权用户有安全风险。
唤醒评测至少报误唤醒 FAR、漏唤醒 FRR、唤醒到响应延迟、不同环境和功耗；仅报告一个准确率会掩盖体验问题。
原始音视频不应默认写入应用日志，日志只保留脱敏事件和统计；需要复现时使用受控短期样本并审计访问。
每个本地模型服务需要独立 liveness/readiness、模型版本与 GPU 资源检查，控制面在依赖未 ready 时不给用户假成功；冷启动时间也要可见。
本地 LLM 慢时应流式显示阶段状态，尽早产生首 token/首音频，并设置超时和取消；最终完整答案慢于用户耐心时需可中断。
知识问答要检索/图谱证据与开放聊天分流，证据答案给出处，无证据时澄清或承认不知道；本地模型不会天然减少幻觉。
gRPC 适合内部强类型 RPC/流，WebSocket 适合前端实时事件；二者都需要 sequence、ack、取消和 backpressure 语义。
模型资产交付应有版本 manifest、hash、磁盘预算、可恢复下载和离线安装包；运行时临时下载会造成不可预测的启动失败。
卡顿排查用端到端 timestamp 与 WebRTC stats 分离生成、编码、推流和播放；先找最长阶段而非盲目降低所有模型质量。
故障注入应模拟 ASR/TTS/LLM/SRS/GPU 各自失效，验证降级、告警、恢复与旧结果不串台；demo 成功不证明故障路径可靠。
性能基线要固定模型、分辨率、帧率、并发、设备和网络，报告 p50/p95 与资源；不同机器的单次录屏无法比较。
威胁建模从生物特征、媒体、模型、网络和控制面资产出发，列出攻击者、入口、影响和缓解；尤其考虑回放、越权和模型/供应链。
应如实把能力分为已自动测试、已人工演示、设计中和未验证四类；这是该类复杂多模态系统最可信的项目表述方式。
""".strip().splitlines(),
    "09-ultralight-digital-human": """
该任务以音频特征、身份/姿态条件和历史视觉信息生成与语音同步的面部帧，监督来自对齐的真实视频帧及同步判别信号；所有样本必须保留源视频与时间索引。
HuBERT、Wenet、AVE 的特征率与视觉分支输入不同，因此 README 中的 25fps/20fps/分辨率要求是数据 contract；重采样必须在生成特征前完成。
错位一个 frame 就可能造成可见的唇形提前/滞后，应以统一时间戳配对并用 SyncNet/人工回放检查；不能只信文件帧数相等。
预处理应从同一原视频切出帧、landmark、音频和特征，使用 sample ID、起止时间和 hash 关联；任一中间文件缺失或换源都应 fail fast。
Landmark 失败、遮挡和侧脸应被质量标记、过滤或单独采样，不能把错误关键点作为正常监督；否则模型会把检测噪声学进生成器。
UNet 通过 encoder 提取身份/上下文、decoder 复原细节、skip connection 保留空间信息，适合图像到图像生成；音频条件的融合位置需要实际消融验证。
160 与 328 的选择是质量、显存、延迟和训练数据量权衡；应在相同测试片段上报告同步、感知质量和设备时延，而不是仅比较分辨率。
像素损失只奖励逐像素相似，不能确保口型与声音同步；SyncNet 提供跨模态同步约束，因此两者互补。
余弦相似度经 BCE 监督时必须确认 similarity 的范围、label 和负样本构造，`sync_w` 控制同步梯度与重建梯度的相对影响；过大可能牺牲视觉质量。
冻结并 eval 的 ImageNet backbone 作为稳定特征空间比较生成/真实帧，避免它在小数据上随生成器漂移；输入归一化和选取层必须一致。
覆盖均衡采样用于降低常见说话人/姿态/音素对训练的支配，让长尾口型被看到；权重来源需要可审计。
replacement 的 WeightedRandomSampler 会重复高权重样本，若权重过尖会过拟合；应限制权重、监控有效样本量并保持独立验证集。
优先使用 `weights_hard.npy` 表示困难样本挖掘的后续阶段，但其生成模型/阈值和更新时间必须记录；陈旧 hard weight 会放大过期错误。
困难样本应在基础模型收敛后按同步/重建错误重加权，并混入常规样本；否则标签噪声和极端失败例会主导训练。
切分必须按源视频/说话人而不是随机帧进行，因为相邻帧和同一身份极易泄漏；测试集应包含未见片段或身份。
`num_workers`、pin memory、persistent workers 影响装载吞吐和系统稳定性，应按机器 CPU/内存测量；数据处理瓶颈不是用更大 batch 就能解决。
梯度裁剪防爆炸，早停防验证集退化，调度器帮助跨越平台期；这些参数需要记录触发时刻，不能神秘化为“训练技巧”。
loss 权重应看各项数值、梯度范数和目标指标的消融，而不是使某一项数值看起来相近；最终以同步/感知质量验证。
除重建误差外，应评估 SyncNet/音画偏移、LPIPS 或感知质量、身份保持和人工 MOS，并按遮挡、姿态、音素等 slice 报告。
复现需要保存代码/数据/权重/配置 hash、seed、CUDA/torch 版本和确定性设置；GPU 算子非确定性也必须披露。
导出时最常见的问题是动态 shape、opset、插值、预后处理和精度不同；ONNX/TRT/MNN 都要以相同特征和输入做输出 parity。
parity 先固定一个 batch 的中间输入和目标，比较 PyTorch、ONNX、TRT 每一步/最终帧的容差和同步分数；只比生成视频主观观感不够。
实时推理要把音频特征与帧请求排队并设最大延迟，落后时按策略丢视觉帧但保持音频时间轴；逐帧同步等待会导致延迟无限累积。
代码的 CPU fallback 能保证功能可启动，但性能预期应明确降级；用户应看到当前 device、模型和实时能力状态。
`map_location` 让 checkpoint 在不同设备加载，`weights_only` 降低任意对象反序列化风险；兼容 fallback 也要限制可信 checkpoint 来源。
模型、SyncNet、ASR 特征模型和预处理版本必须写入 manifest 并在加载时核对 shape/版本；混用版本会产生难察觉的同步差。
移动端 MNN 需测试设备内存、线程、温度、首帧与持续运行，而非只测桌面端导出成功；必要时提供模型档位和温控降级。
人像/声音数据需要授权、用途限制、可删除和访问审计；训练集可用不代表生成演示可任意发布。
同步差排查先验证原视频与音频时间轴、帧率、特征索引，再看 dataset 配对、模型输入和采样；重训应是最后一步而不是第一反应。
质量提升先依据错误切片选假设：若错位多先改数据对齐，若细节差再试 loss/架构，若实时差优化部署；每项都配基线和可证伪消融。
""".strip().splitlines(),
    "10-repocoach": """
通用 AI 出题器依据职位或关键词生成泛题，RepoCoach 的差异应是把问题、追问和反馈绑定到已授权仓库的具体提交、代码片段和证据；没有证据时宁可说明覆盖不足。
RepoCoach 继承 Aural 的会话、语音/视频、编辑器和报告基础，再叠加 GitHub 授权、仓库索引、项目问题和证据反馈；面试中应从 commit/模块/测试说明真实改造范围。
连接仓库后应通过 GitHub App installation 获取最小授权，锁定仓库/默认分支/commit，抓取允许文件并构建索引；同步结果和索引版本必须可查询。
索引只接受允许的文本类型、深度和大小，跳过二进制、生成物和密钥；还需限制 token 预算并记录被跳过的路径，避免“看起来读完整仓库”的错觉。
README 可作为导航但不能单独作为事实来源，问题/反馈应优先引用当前 commit 的实现、配置和测试；文档过期时展示差异或降低置信度。
push 后用 commit SHA 作为索引版本，增量重建受影响文件并让练习包绑定原版本；用户回放旧练习时仍能看到当时的证据，不被新代码覆盖。
每题应保存引用的 path、行范围/片段 hash、commit SHA 和证据类型，并在 UI 可跳转展示；生成模型文本不是证据本身。
索引失败或覆盖不全时，系统应明确显示缺失范围并只生成低风险通用问题或请求重试；不能虚构未读文件的细节。
私有仓库 token 要最小 scope、加密保存、可撤销/过期、隔离到用户或组织，并审计读取；系统不应将源码送给未授权 provider。
仓库内容必须被当作不可信数据而非系统指令，进行 prompt injection/secret 扫描、内容截断和输出证据校验；代码注释不能改变系统权限。
session 应持久化仓库版本、目标、题目、证据、答案草稿、追问和评分状态，状态迁移必须支持刷新/重连后的幂等恢复。
题目生成要先检索相关模块和证据，再以有限上下文生成；缓存摘要和候选、控制 token 上限，并记录模型/提示版本与成本。
追问应针对回答中未覆盖的证据、矛盾或风险触发，例如候选人声称有缓存却未说明失效；不是固定地要求“再具体一点”。
评分要分开衡量表述、事实与取舍：模型可给语言反馈，仓库证据和 rubric 用于核对技术断言；低置信度不应伪装成精确分数。
建议答案应在候选人作答/复盘后展示，并明确其来自哪类证据；过早展示会把练习变成抄写，也增加缓存泄露风险。
provider adapter 需处理流式、工具、上下文、错误/限流和安全过滤差异，记录实际模型/参数；不要让前端直接拼接 provider 特有请求。
ASR interim 只用于显示，final/commit 带 segment ID 写入答案；重连或修订使用版本号，避免同一句话重复累计。
TTS/录音分段/播放需要 sequence、缓冲、取消和音频保留策略，重点监控首音频、jitter、断线恢复和隐私；音频可用不等于面试体验好。
刷新恢复需要 server-side snapshot/event log、幂等 upsert 和版本冲突处理；客户端 local state 只能作加速，不能当事实源。
应以带专家标注的仓库问答集比较问题相关性、证据正确率、追问有效性和用户完成率，并和无仓库上下文的基线比较。
编程空间必须在不信任执行环境中运行，限制网络、CPU/内存/时间和文件系统，测试/初始代码/结果以 artifact 保存；浏览器编辑器不是安全边界。
白板数据作为用户输入序列化存储，需做访问控制、大小限制和 HTML/SVG 清洗；协作或导出路径不能绕过 XSS 防护。
反作弊信号只能作为风险提示，不应宣称能证明作弊；应征得同意、说明采集内容，并提供人工复核和申诉路径。
Supabase/RLS 需要让每张会话、答案、报告和仓库表按组织/用户策略限制，service role 仅在后端使用；负向测试比 UI 隐藏更重要。
source/route 测试覆盖静态契约，真实浏览器 E2E 仍必须验证 OAuth、媒体权限、WebSocket/voice、编辑器和关键恢复路径；两类测试不能互换。
限流应按用户、组织、IP、provider 预算与会话阶段综合控制，流式重连允许短 burst 但不能绕过总配额；响应中给出重试信息。
代码、答案、音频和 PDF 的保留期应按用途和用户/组织策略分别定义，支持删除、加密和审计；GitHub 内容同步后也要可撤销/清除。
故障归因用 request/session/repo/commit ID 串联 GitHub、Supabase、LLM 与 voice relay，并为每个依赖建立 synthetic check；不要仅靠用户截图。
新评分 prompt 先在冻结标注集上评估，再 shadow/A-B 小流量发布，监控一致性和负反馈；保留旧版本作为可回滚基线。
最有价值的自问是要求解释一次真实项目中“证据、设计取舍、失败路径”如何连起来；它能检验是否真的理解代码而非只会复述技术栈。
""".strip().splitlines(),
    "11-airdesk": """
完整数据流是浏览器请求摄像头、MediaPipe 产出 21 点、手势状态机稳定化、统一 command 映射、React/Three.js 更新和可选本地 runner；每步应有权限/错误与帧率边界。
本地打包 WASM/模型可减少 CDN 依赖、支持离线与锁定版本，代价是首包/缓存管理和更新发布责任；不是简单“本地更快”。
手势特征应基于 landmark 的相对距离、角度和手掌尺度归一化，并处理镜像/左右手；绝对像素阈值会随摄像头距离失效。
冲突手势要按置信度、持续时间、当前模式和优先级解析，例如 pinch 处于拖拽状态时不应被一帧 point 抢走；状态机比逐帧 if-else 稳定。
去抖使用最短持续帧、迟滞阈值、cooldown 和状态锁，代价是少量响应延迟；阈值应通过误触发/漏触发样本调节。
slide 映射应先统一相机镜像、视频尺寸和视口坐标，再把归一化位移投影到屏幕或 3D 平面；灵敏度/死区应可调。
circle 需要轨迹窗口、闭合度、半径/方向一致性和最小持续时间，不能仅检测手指移动；否则普通挥手会大量误判。
视频推理和 Three.js 都可能占主线程，应节流分析频率、使用 requestVideoFrameCallback/worker（若可用）并让 React 不在每帧 setState；用 profiler 验证。
多手场景需维护 active hand ID、丢失超时和状态 reset，或要求用户选择主手；手离开画面时必须结束拖拽/按压状态。
无摄像头/权限/WASM 支持时应显示明确原因并提供键鼠或 fallback gesture pad；不能陷入不断请求权限的死循环。
Three.js 的空间卡片能表达任务关系和手势操作，但必须证明其收益大于 2D 列表的学习/性能成本；可访问替代入口是必需的。
React 管理声明式 UI/业务状态，Three.js 用 ref/命令式 scene 更新处理帧循环；每帧更新不应穿透 React reconciliation。
手势应先转换成独立的 command（如 select/drag/confirm），再由权限和业务层执行；这样可以单测、重映射和记录撤销，而非把识别器直接绑定副作用。
endpoint 要有请求 schema、认证/本地信任边界、超时、取消、幂等与响应来源标记；环境变量只提供地址，不能成为安全授权。
浏览器 fallback 只应演示交互流程，并在 UI 标出模拟结果；不能把预置响应声称为本地 Agent 已执行。
高风险操作需要显式确认、可撤销记录和权限检查；手势误判的概率决定默认动作必须保守。
用户需要看见相机状态、当前识别手势、置信度/为什么未识别和当前模式；可见反馈本身能降低误操作和排障成本。
键盘、鼠标、触控和手势应映射到同一 command 层，保留焦点和快捷键；手势是增强输入，不应排斥无障碍操作。
当前若完全本地处理也要明确图像不上传；若接云端模型，必须新增告知、同意、最小化上传、加密、保留期和删除流程。
鲁棒性测试需覆盖光照、背景、相机、距离、左右手、肤色和动作速度，并报告分组失败率；不能只展示理想环境 demo。
`tsc -b` 校验 TypeScript 项目引用和类型，Vite build 校验 bundle/asset 产物；两者通过仍不证明摄像头交互正确。
Vitest 适合手势分类、平滑、坐标映射、command reducer 和 endpoint client 等纯逻辑；媒体和真实渲染应交给集成/E2E。
Playwright 可用 fake media/录像或 mock landmarks 复现权限和交互状态，断言 UI command；真人手势可作补充手工测试，不能是唯一回归方式。
停止相机和卸载组件时必须 track.stop、取消 RAF、释放 Three.js geometry/material/texture 和 listener；否则切页会泄露设备和内存。
WASM/模型 asset 以内容 hash 和版本清单发布，service worker/HTTP cache 要随版本失效；旧前端加载新模型时应有兼容检查。
浏览器将 localhost 视为安全上下文，但局域网 HTTP 通常不允许摄像头；远程访问应部署 HTTPS 并处理证书/权限来源。
体验指标应记录用户点击开始、camera ready、first landmark、gesture recognized、command completed 的时间点，分设备报告 p50/p95。
摄像头故障先检查 enumerateDevices、权限、secure context、选择的 device/格式和控制台错误，再确认 MediaPipe asset；不要先改识别阈值。
双手扩展需要从单 active hand 状态机重构为多指针/手势组合模型，并重新设计 3D 交互冲突与测试集；不能只增加几个 if。
长期价值要用任务完成率、误操作、学习时长、手臂疲劳、留存和访谈验证；手势炫酷不等于适合高频工作流。
""".strip().splitlines(),
    "12-diffusion-models": """
开场先说明该仓库中哪些是 fork、哪些是复现、哪些是本人改动和实验；README 指向上游时尤其不能把模型原始实现、论文或训练结果都归为个人贡献。
将 VAE、flow、diffusion 和简化 DALL·E 放在一起的意义是比较不同概率生成范式，但对比应共享数据、预处理、预算与评测；它们不因都“能生成图”就天然可比。
公平对比固定数据 split、分辨率、augmentation、训练步数/计算预算、随机种子和评测代码，并保存失败 run；不同设置下的分数不能直接排名。
MNIST 适合验证机制，CIFAR-10 增加自然图像复杂度，CelebA 适合人脸/较高分辨率观察；小数据集结果不能外推到高分辨率通用生成。
Notebook 需支持干净内核 restart-run-all、显式依赖/路径/seed 和可下载数据，最好在 CI 做至少一个 smoke；依赖上一步隐式变量的 notebook 不可复现。
实验记录至少含 git SHA、config、数据/model hash、环境、硬件、指标和样本；图片文件名本身不是可追溯实验。
FID 近似比较真实/生成特征分布，IS 只衡量可分类性/多样性，MSE 衡量重建像素；三者都有限制，必须结合定性和切片分析。
mode collapse 可通过类别/特征覆盖、nearest-neighbor、重复率和多样性指标发现；只挑选好看的 sample 会隐藏问题。
数据集许可、人物图像和生成内容的用途/发布范围都需核对；研究/学习用途不自动解除再分发和肖像风险。
若选一个入门基线，VAE 通常最易展示 encoder、latent、decoder 与 ELBO；若目标是扩散工程，应选择极小 DDPM 并明确训练成本。
ELBO 由期望重建对数似然减去后验与先验的 KL 构成，训练时常最小化其负值；重建和 KL 的平衡决定 latent 是否有信息。
重参数化把随机变量写成 `z=mu+sigma*epsilon`，随机性来自独立 epsilon，使梯度可回传到 mu/sigma；方差通常以 logvar 稳定参数化。
提高 beta 强化先验约束，可能改善因子解耦但降低重建并诱发 collapse；应通过 beta sweep、KL 曲线和下游/定性评估选择。
posterior collapse 表现为 KL 接近零、decoder 忽略 latent；可用 KL warm-up、free bits、减弱 decoder 或调整训练日程缓解，并用消融验证。
VQ-VAE 将 encoder 输出量化到 codebook 向量，commitment loss 约束 encoder，codebook 更新可用 EMA；死码通过使用率/perplexity 监控和重初始化处理。
离散 code token 能让 Transformer 在有限词表上建模图像序列，但会引入量化损失和长序列成本；codebook 版本必须与下游 token 模型绑定。
flow 通过可逆变换与 Jacobian log-det 获得精确 likelihood，代价是架构必须可逆且对高维复杂数据的表达/计算受约束。
VAE 使用近似后验和随机 latent，flow 保留精确密度；两者在训练、采样、重建和感知质量上要用同预算数据比较，不能只比一个 likelihood。
应对关键层的 shape、范围、随机种子和梯度建立 assert/最小 batch 测试；数值梯度或固定 golden output 可发现 silent broadcasting bug。
重建 MSE 低只说明 encoder-decoder 能复制输入，不能证明从 prior 采样的质量、多样性或分布覆盖；生成评估必须独立进行。
DDPM 前向过程按 schedule 逐步加高斯噪声，反向模型学习条件去噪分布；训练常从随机 t 直接构造 x_t，提高效率。
预测 epsilon 是常用参数化，因为目标简单且与噪声过程匹配；预测 x0 或 v 也可行，但损失权重、数值稳定和采样公式必须一致。
beta schedule 决定各时间步信噪比，过快会丢失信息、过慢可能浪费步数；应画 SNR/训练曲线并在固定采样预算上比较。
U-Net 的多尺度路径处理不同频率细节，skip 保留空间信息，time embedding 告诉网络当前噪声级别；条件信息应在明确层注入并可消融。
DDIM 使用确定性或较少随机性的非马尔可夫采样路径，可减少步数；速度、随机性和质量的取舍要实际测量，不是免费加速。
classifier-free guidance 混合条件/无条件预测增强条件遵从，过强会造成饱和、多样性下降和伪影；guidance scale 应在验证 prompt 集上选择。
损失下降但采样是噪声时，按数据归一化、timestep/schedule、target 参数化、模型 eval/EMA 和反向采样公式顺序排查；不要仅增加训练轮数。
简化 DALL·E 要明确 VQ-VAE 图像 token 的 codebook/version、文本 tokenizer、序列拼接和 mask；两个阶段的 data contract 变更都会使模型失效。
长训练采用 AMP、gradient accumulation、EMA、原子 checkpoint 与恢复时的 optimizer/RNG 状态保存；恢复后应能复现同一步的损失范围。
从学习代码升级为可信复现，应优先补固定配置/环境、端到端 smoke、指标脚本、对比基线、置信区间和失败案例；漂亮 notebook 不是复现证据。
""".strip().splitlines(),
}

PROJECTS["13-mimirq"] = {
    "title": "MimirQ",
    "repo": "https://github.com/skygazer42/MimirQ",
    "verified": "README、Makefile、FastAPI 入口和 v1 router 可验证 MimirQ 将 parsing、governance、chunking、retrieval、evidence、evaluation、RBAC/SCIM/audit 等作为独立可检查的知识流水线模块；README 的 800 题报告也明确区分检索直连与 Dify 生成链路。",
    "flow": "数据评估 → 解析器路由 → 治理 → 业务切块 → 向量/全文索引 → 混合检索与重排 → 证据/引用 → Golden 回归与发布门禁。",
    "sources": [
        "README.md 与 docs/benchmarks/changzhou_dify.md",
        "Makefile、docker/docker-compose*.yml 与 .env.example",
        "app/main.py、app/api/v1/__init__.py、app/rag/preprocessing/tokenization.py、app/rag/ 与 tests/",
    ],
    "boundary": "README 中的解析器/策略/重排器数量描述实现广度；线上效果只应在固定题集、模型、数据版本与链路条件下解释，尤其不能把检索直连与 Dify 最终生成结果混为同一 benchmark。",
    "core": [
        "解析、治理、切块和索引的版本化数据契约",
        "中文/代码查询的 BM25 与混合检索",
        "重排、引用、Evidence Trace 与配置 hash",
        "ACL/security trimming 和企业身份治理",
        "Golden 回归、admission control 和发布门禁",
    ],
    "metrics": "解析/切块质量、Recall/MRR/nDCG、引用覆盖/正确率、Golden 题集准确与可用率、P50/P95、队列/拒绝率、资源成本和租户隔离负向测试。",
    "risks": "解析器质量错配、chunk 破坏语义、索引/Embedding 版本漂移、跨权限召回、提示注入/SSRF、回归集过拟合、生成链路掩盖检索问题和队列过载。",
}

DIRECT_ANSWERS["13-mimirq"] = """
MimirQ 的核心不是“把文件向量化后聊天”，而是把解析、治理、切块、检索、重排、引用和评测拆成可检查、可替换、可回归的知识流水线；答案错误时能定位到具体阶段而不是归咎于模型。
一次完整路径应产出可追溯状态：数据评估报告、解析 block/assets、治理版本、chunk 与索引版本、候选/重排 trace、引用和 Golden run；每个产物用稳定 ID 和版本关联。
解析前评估扫描页、表格、公式、版式、页数和质量风险，用它估算 GPU/CPU、处理时延和人工抽检成本，再选择轻量或视觉解析器；先批量解析再发现复杂度会造成成本失控。
解析器应有统一 capability（格式、硬件、质量、时延、输出类型、依赖）和健康状态，路由根据文档画像选择并记录原因；失败时只回退到语义可接受的后端，而非悄悄换结果。
所有解析后端都归一化到文档、页、结构 block、表格/图片 asset、bbox、文本和 provenance 的 schema；后续治理、切块和引用只依赖这个 contract。
规则 DSL 适合可声明且可审计的确定性清洗，脚本适合复杂转换，插件适合独立领域扩展；三者都需版本、输入输出快照、审批和可回滚批次。
86 种策略必须以 capability/参数 schema/适用文档类型管理，使用预览和固定评测集选择；策略数量本身不是质量，默认策略也不能覆盖所有业务。
父子切块以小块召回、大块补上下文，章节切块保留语义结构，固定窗口简单但易断表/断句；选择取决于问题粒度、上下文预算和引用要求，不能说 chunk 越小越好。
Embedding 改变向量空间和相似度分布，旧向量不可与新 query 直接比较；需一起版本化 chunk、metadata、collection、模型、索引参数和 retrieval profile，并重建/切换索引。
`tokenization.py` 先用 NFKC 统一全半角，再处理中文分词、ASCII 路径、下划线/连字符、驼峰和版本号 token；这能让 API、文件路径和中英文混合查询不因分词细节漏召回。
混合检索应让稀疏、dense、SPLADE/ColBERT 等产生候选，再用 RRF/LTR 或明确融合规则排序；每段保留候选数、分数、模型和配置 hash，才能解释一次命中。
reranker 上线要在领域标注集上比较 Recall/nDCG/MRR、p95、吞吐、成本和不同语言/文档切片；高相关性模型若压垮延迟预算不适合在线默认路径。
retrieval profile 要将 backend、embedding、sparse、fusion、reranker、top-k、过滤等固化为版本/hash；历史 trace 和 Golden 结果只有绑定该 profile 才可复现和比较。
ACL/security trimming 需要在服务端将用户/组织/文档权限转为检索过滤条件，并在候选、重排、引用所有阶段保持；要用无权限文档的负向测试证明不会越权。
Dify External Knowledge API 适合 Dify 编排/生成而 MimirQ 提供标准检索证据，HTTP 节点适合需要自定义路由和参数的工作流；两者都不能让 Dify 绕过 MimirQ 的 ACL 与 trace。
`knowledge_id` 必须从显式、受校验的 `DIFY_EXTERNAL_KNOWLEDGE_MAP_JSON` 映射到许可的数据集；不能由前端自由传任意 ID，否则很容易路由到错误或越权知识库。
Evidence Trace 应包含 query、授权范围、候选 chunk 的 document/page/block、各阶段分数、profile/config hash、重排变化、最终引用和响应版本；这才支持用户回看和工程诊断。
图谱、关键词和向量冲突时先比较来源、版本、时效和置信度，保留可核验的冲突证据；没有足够依据时应澄清/拒答，而不是让生成模型私自统一事实。
Golden 题集需按场景、难度、文档类型、权限和失败模式分层，保存问题、期望证据/答案、数据和 profile 版本；独立留出集防止只针对 800 题调参。
检索直连输出的是候选证据，Dify 链路输出的是 Dify 编排后的最终生成答案，任务和时延组成不同；README 也明确说明两类准确率不能视为严格横比。
准确、部分准确、证据不足和证据覆盖必须先写清标注准则，再计算准确率/可用率；还要报告标注一致性、失败原因与置信区间，不能只展示一个百分比。
并发 5 的 admission backpressure 说明资源池或队列达到保护阈值，而非系统“随机失败”；需要从队列、服务时间、拒绝/重试和 P95 推导安全并发、SLO 和扩容点。
core-e2e 验证 ready→ingest→retrieval 闭环，live-core-release-gate 验证真实检索服务的隔离/去重/并发，rag-concurrency-gate 对比并发退化，plugin-release-gate 保护插件交付；它们是互补的发布门禁。
`app/main.py` 在生命周期中组织日志、request ID、CORS、Sentry/OTel、数据库/队列、migrations 和 tokenizer/runtime warmup，目的是在服务接流量前建立可观测和可用依赖，并在关闭时释放资源；初始化顺序可影响 readiness 与测试隔离。
进程内后台任务适合轻量本地开发，独立 ARQ worker 适合可扩容的入库；任务必须有状态、幂等键/锁、重试预算、artifact 和 Redis health，worker 崩溃后才可安全恢复。
Milvus 适合规模化向量/过滤服务，FAISS 适合简单本地索引，Chroma 支持轻量持久开发；full/lite/retrieval-dev 的选择要与持久化、ACL、并发和运维目标匹配，而不是只按安装难度。
端到端观测将 request/ingestion/run/document/chunk/profile IDs 写进日志、span、lineage 和评测记录；一次错误应能判断是解析丢失、治理改写、切块、召回、重排、权限还是生成。
InputGuard 防止恶意/越权请求与注入，OutputGuard 控制泄露/不当输出，PII/Secret 脱敏处理敏感内容，SSRF 逐跳校验限制解析或工具访问内网；文档内容同样是不可信输入。
RTBF 负责删除请求及其索引/缓存/产物传播，审计记录可追责事件，RBAC 控制角色能力，SCIM/SSO/SAML 管理企业身份生命周期；它们合在一起才是合规知识库的权限闭环。
full Docker 面向完整服务，lite 用较轻后端验证最小闭环，源码模式利于热更新，Helm 面向集群交付；可验收部署还需 health/ready、migrations、备份恢复、升级回滚和故障演练的证据。
""".strip().splitlines()

ROW = re.compile(r"^\|\s*(\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
LINK = re.compile(r"^\[(.*)\]\(\./\d{2}\.md\)$")


def plain_question(cell: str) -> str:
    match = LINK.match(cell)
    return match.group(1) if match else cell


def answer_mode(question: str) -> tuple[str, str]:
    if "为什么" in question or "为何" in question:
        return (
            "先给出判断，再比较至少一个替代方案。不要把“使用了某技术”当理由；理由应落到数据特性、接口约束、成本、可靠性或用户体验。",
            "把收益和代价放在同一句回答里，并说明什么条件下会改用替代方案。",
        )
    if "如何" in question or "怎样" in question:
        return (
            "按“输入与前置条件 → 核心状态/算法 → 失败处理 → 可观测性 → 验证”组织回答。这样能避免只报出一个库名或架构名。",
            "至少说出一个异常路径和一个可测指标；没有实测数据时明确说明待验证。",
        )
    if "请" in question or "描述" in question or "讲" in question:
        return (
            "用真实调用链或数据流回答：先说边界，再按时间顺序列出组件、状态变化与输出，不用抽象名词替代路径。",
            "在关键转折点给出代码、配置、测试或日志证据；把未验证部分标为设计目标。",
        )
    return (
        "先界定术语和当前仓库可证实的事实，再说明实现机制、取舍与验证方法。",
        "回答应让面试官能据此设计一个反例或测试，而不是只能听到结论。",
    )


def body(project: dict[str, object], number: int, question: str, evidence: str, direct: str) -> str:
    method, warning = answer_mode(question)
    evidence_sentence = evidence.rstrip("。；; ")
    direct_sentence = direct.rstrip("。；; ")
    sources = project["sources"]
    assert isinstance(sources, list)
    source_lines = "\n".join(f"- `{source}`" for source in sources)
    return f"""# {number:02d}. {question}

## 结论先行

{direct}

这不是脱离项目的通用八股。仓库当前可以证实的是：{project['verified']} 若谈到生产化改进、性能或效果，必须使用“建议/需要验证”，不能把设计直接说成线上结果。

## 基于项目代码的回答

可用下面这条链路组织口头回答：

```text
{project['flow']}
```

针对“{question}”，推荐的答法是：{method}

题目给出的准备线索是：{evidence_sentence}。先打开对应实现，确认入口、数据结构、错误分支和测试；再用一条真实请求、一次训练/推理运行或一个最小样本解释行为。这样回答比复述 README 更可靠。

## 实现机制与工程取舍

1. **接口和数据契约**：先写清输入、输出、版本、身份/权限边界与失败语义。对于异步或多阶段流程，所有中间产物都应有稳定 ID 和可追溯来源。
2. **核心机制**：本题的直接结论是：{direct_sentence}。解释时要把状态如何流动、何处做校验、何处形成最终结果说清楚；如果有外部模型、引擎或服务，还要说明适配层如何屏蔽差异。
3. **故障与降级**：不要假定依赖永远可用。超时、输入不合法、版本不匹配、资源不足和部分成功都需要明确的用户可见结果、重试策略或拒绝路径。
4. **取舍**：正确答案通常不是“功能越多越好”，而是根据延迟、成本、精度、可解释性、安全与维护成本选择最小可靠方案。{warning}

## 代码与配置依据

回答前至少应核对以下材料，而不是把它们当作已经完成性能验证的证明：

{source_lines}

建议在面试中展示具体函数、配置键、测试名或一次运行记录。若实际代码与 README 不一致，以当前默认分支的代码和锁定提交为准，并主动指出差异。

## 如何验证这段回答

- 为本题准备一个最小正例和一个失败/边界例；运行路径应能从输入追到输出或错误码。
- 记录相关版本：代码提交、模型/数据/配置 hash、依赖环境和硬件/服务条件。
- 用项目对应指标验证，不用“感觉更快/效果更好”替代证据。本项目适合关注：{project['metrics']}
- 对关键断言保留 trace、日志、测试快照或可复现命令；如果没有这些证据，就将其表述为待验证假设。

## 常见误区

- 只背概念，不说明这题在本项目的入口、状态和输出。
- 混淆“README 中的能力描述”“代码路径可运行”和“已在生产环境验证”。
- 把第三方框架、预训练模型或上游仓库的贡献说成个人实现。{project['boundary']}
- 只讲正常流程，不讲权限、失败、回滚、资源上限或可观测性。

项目特有的高风险点包括：{project['risks']}

## 延伸追问

1. 如果输入规模、并发或数据量增加十倍，最先成为瓶颈的组件是什么？如何证明？
2. 请给出一个会让当前设计失败的反例，以及修复后应加入的回归测试。
3. 哪个结论是仓库代码已经证明的，哪个仍需要通过实验、压测或安全评审验证？
"""


def parse_questions(readme: Path) -> list[tuple[str, str, str]]:
    questions: list[tuple[str, str, str]] = []
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line)
        if not match:
            continue
        number, question, evidence = match.groups()
        questions.append((number, plain_question(question), evidence))
    if len(questions) != 30:
        raise ValueError(f"{readme}: expected 30 questions, found {len(questions)}")
    return questions


def link_questions(readme: Path, questions: list[tuple[str, str, str]]) -> None:
    linked = {number: f"[{question}](./{number}.md)" for number, question, _ in questions}
    lines: list[str] = []
    for line in readme.read_text(encoding="utf-8").splitlines(keepends=True):
        match = ROW.match(line.rstrip("\n"))
        if match and match.group(1) in linked:
            number, _, evidence = match.groups()
            lines.append(f"| {number} | {linked[number]} | {evidence} |\n")
        else:
            lines.append(line)
    readme.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    for folder, project in PROJECTS.items():
        directory = ROOT / folder
        readme = directory / "README.md"
        questions = parse_questions(readme)
        direct_answers = DIRECT_ANSWERS[folder]
        if len(direct_answers) != len(questions):
            raise ValueError(
                f"{folder}: expected {len(questions)} direct answers, found {len(direct_answers)}"
            )
        for number, question, evidence in questions:
            (directory / f"{number}.md").write_text(
                body(project, int(number), question, evidence, direct_answers[int(number) - 1]),
                encoding="utf-8",
            )
        link_questions(readme, questions)
        print(f"built {folder}: {len(questions)} answers")


if __name__ == "__main__":
    main()
