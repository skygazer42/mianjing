# RepoCoach：项目面试题

仓库：[`skygazer42/RepoCoach`](https://github.com/skygazer42/RepoCoach)。RepoCoach 将 GitHub 仓库转化为模拟面试：基于 Next.js/TypeScript/Supabase，提供仓库理解、AI 追问、Monaco 编程、白板、语音/视频会话、证据化反馈与报告。README 说明其基于 MIT 许可的 Aural 平台再定位；`package.json` 显示包含 GitHub App、LLM、语音、练习状态、安全边界等大量定向测试。

## 产品边界与仓库理解

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [RepoCoach 与通用“AI 出题器”的本质差异是什么？](./01.md) | 必须回答 repo-grounded 的证据链和个性化追问。 |
| 02 | [继承 Aural 的哪些能力，RepoCoach 自研/改造了哪些部分？](./02.md) | 主动说明 fork/二次开发边界和 MIT 义务。 |
| 03 | [用户连接一个 GitHub 仓库后，系统如何获得、存储并更新代码上下文？](./03.md) | GitHub App、installation、同步、默认分支和 commit SHA。 |
| 04 | [如何界定可索引的文件类型、大小和深度，避免成本与提示注入失控？](./04.md) | allowlist、大小预算、二进制跳过和安全扫描。 |
| 05 | [仓库 README 与实际代码冲突时，系统为何要以代码/测试为证据？](./05.md) | commit pin、证据片段和不确定性表达。 |
| 06 | [同一仓库新 push 后，问题与反馈如何避免引用旧代码？](./06.md) | commit/version 绑定、增量索引和旧练习可回放。 |
| 07 | [怎样为生成的问题附上可核验的文件、行号与提交证据？](./07.md) | `question-evidence` 相关测试、snippet hash 与 UI。 |
| 08 | [如果索引失败或只拿到部分代码，AI 应怎样诚实地出题？](./08.md) | coverage 状态、降级和拒绝伪造证据。 |
| 09 | [私有仓库授权范围和 token 生命周期如何设计？](./09.md) | 最小 scopes、encrypted tokens、撤销和审计。 |
| 10 | [如何阻止仓库内的恶意 README/源码劫持出题 prompt 或泄露密钥？](./10.md) | data/instruction 分离、secret scanning、输出校验。 |

## 面试会话、AI 与评测

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [从选择仓库到生成第一题的 session state machine 是什么？](./11.md) | prep、生成、作答、追问、评分、报告、恢复。 |
| 12 | [如何在题目质量、生成延迟和 LLM 成本间设置预算？](./12.md) | repo 摘要、检索、缓存和 token accounting。 |
| 13 | [AI 追问应该根据什么触发，如何避免机械地“再说具体一点”？](./13.md) | 声明、证据、遗漏维度与难度自适应。 |
| 14 | [回答评分如何区分表达流畅与技术事实正确？](./14.md) | rubric、repo evidence、模型 judge 与人工校准。 |
| 15 | [“建议答案”为什么可能伤害练习效果，何时展示才合理？](./15.md) | 延迟揭示、证据引用、缓存与作弊风险。 |
| 16 | [如何处理多模型 provider 的工具调用、流式输出与错误格式差异？](./16.md) | provider abstraction、fallback 与 conformance tests。 |
| 17 | [语音 ASR 的 interim/final transcript 如何避免重复写入答案？](./17.md) | 片段 ID、commit 时机和重连协议。 |
| 18 | [TTS、录音分段与播放 jitter buffer 如何影响一场口语面试体验？](./18.md) | 延迟、取消、音频 retention 与质量指标。 |
| 19 | [用户中途刷新或断网，练习如何准确恢复？](./19.md) | event sourcing/快照、幂等 upsert 和 version conflict。 |
| 20 | [如何用标注集验证“基于仓库的问题”比泛化问题更有价值？](./20.md) | 相关性、证据准确率、完成率和用户评分。 |

## 编程空间、安全与运营追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [Monaco 编程题的初始代码、测试、执行环境和评测结果如何隔离？](./21.md) | 不信任代码、资源限制、无网络和 artifact。 |
| 22 | [白板/Excalidraw 内容如何保存、协作并避免 XSS？](./22.md) | 序列化、访问控制、sanitization。 |
| 23 | [Tab monitoring、粘贴限制、多屏检测有哪些局限，如何避免虚假“反作弊”承诺？](./23.md) | consent、可解释性和风险分级。 |
| 24 | [Supabase/Postgres 的组织、项目、会话、答案、报告 schema 怎么保证 RLS 正确？](./24.md) | 正向/负向 RLS 测试和 service role 边界。 |
| 25 | [`package.json` 有大量 source/route 测试，但哪些还必须跑真实浏览器 E2E？](./25.md) | 授权跳转、媒体权限、WebSocket、关键用户路径。 |
| 26 | [如何做 API rate limiting，既防滥用又不误伤一场流式面试？](./26.md) | user/org/IP 三维、burst 与重连。 |
| 27 | [PDF 导出、音频记录、答案和 GitHub 代码的保留期限如何设置？](./27.md) | 个人数据删除、加密与合法目的。 |
| 28 | [生产故障时如何判断根因在 GitHub、Supabase、LLM provider 还是 voice relay？](./28.md) | trace ID、依赖 dashboard、synthetic check。 |
| 29 | [如何逐步上线一个新的评分 prompt，避免全量用户反馈被破坏？](./29.md) | 离线 benchmark、shadow、A/B、回滚。 |
| 30 | [你最想用 RepoCoach 反过来问自己哪个项目问题？为什么该问题能暴露真实薄弱点？](./30.md) | 把产品价值与本题库的证据化原则连起来。 |
