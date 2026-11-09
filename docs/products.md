# 按产品看：同一个 AI，不同形态怎么收费

> 本文件由 `scripts/render.py` 自动生成，**不要手改**。
> 要改请动 [`data/providers.yaml`](../data/providers.yaml)，然后跑 `python3 scripts/render.py`。

> 共 66 家平台、108 个入口。同一个 AI 换个入口，免费政策和计费方式可能完全不同——**日常用免费的网页版，要把能力接进程序才上 API**。

| 产品 | 形态 | 白拿到什么 | 计费方式 | 备注 |
|---|---|---|---|---|
| **WorkBuddy** | 网页版 · 网页版 | 可用，但没有签到与成长计划 | 积分制（无签到） | 网页版定位是「随手用一下」：不碰本地文件、不能跑自动化、没有签到入口。为了领积分去装客户端… |
| ↳ | 网页版 · 社区投稿 | 普通稿 500，精选最高 3000 | 积分或成长值（口径冲突） | 记一笔冲突——有信源说这篇奖励的是「成长值」而不是 AI 积分，也有信源说官方明确表示暂无… |
| ↳ | 桌面客户端 · Buddy 加油站 | 每天 100 积分（月约 3000） | 积分制 | 只在电脑客户端有，网页版和手机端都没有。0 点刷新，当天不领作废。加油站是活动制，分期换期… |
| ↳ | 桌面客户端 · 体验版月赠积分 | 每月 500 积分 | 积分制 | 每月 1 日刷新，当月有效、用不完清零。这是「底薪」，加油站和任务才是主力。500 积分大… |
| ↳ | 桌面客户端 · 派 Buddy 去旅行 | 每天 5~10 积分 + 盲盒 | 积分制 | 收益看 Buddy 稀有度，R 级约 5~6 分，UR 级（暴富喵）8~10 分，10 分… |
| ↳ | 桌面客户端 · 福利抽奖 | 10 或 100 积分 | 积分制 | 抽奖次数每日刷新，当天有就用掉，别攒过期。中 100 的概率不高，别算进固定收入。 |
| ↳ | 桌面客户端 · 成长计划任务中心 | 单任务 100~300，一次性合计 1000+ | 积分制 | 先清两个 300 分的大头（新建任务并发起对话、设计创意模式建 1 个画布），再顺手做 1… |
| ↳ | 桌面客户端 · 连续登录活跃地图 | 最高 150 积分/档 + 补登卡 | 积分制 | 硬规则——当天必须真的跟 Buddy 对话过一次才算打卡，只打开不算，断一天连击清零。7 … |
| ↳ | 桌面客户端 · 关联账号一次性积分 | 100 积分 | 积分制 | 最容易漏的一条，藏在设置里而不是活动页。关联免费，但暂不支持解绑，绑之前确认是你常用的账号。 |
| ↳ | 桌面客户端 · 限时专家体验任务 | 100 积分/个，另有实物或云资源 | 积分制 | 成长计划任务里带截止日的那批，随版本更新换一批。11 月这一期看到三条——腾讯轻量云专家（… |
| ↳ | 桌面客户端 · 混元 Hy4 限时免费 | 夜间窗口 0 倍率 | 积分制 | 截止日口径冲突（一说 10-31 已到期，一说延至 11-15），以客户端模型选择器是否显… |
| ↳ | 桌面客户端 · 邀约好友 | 最高 650 积分/人 | 积分制 | 650 里最后 500 要先付费，别为了这点专门开订阅。协议明确禁止批量刷邀请，异常 IP… |
| **火山方舟** | API · 方舟 安心体验模式（防扣费） | 防扣费开关（不额外给额度） | 超出免费额度即停，不转付费 | 账号维度的开关，只有「没开通过模型服务」的新账号能开，而且一旦关掉就再也开不回来，务必想清… |
| ↳ | API · 火山引擎方舟（豆包） | 每模型 50 万 Token | 按 Token | 安心体验模式超额自动暂停，不会产生意外账单，但要记得关掉自动转付费。 |
| ↳ | API · 火山引擎 11.11 AI… | 2000 万+/天（4 模型合计） | 按 Token | 活动页没写死截止日，按大厂惯例 11 月中旬收尾，别等。每日刷新是国内最舒服的续杯形态。 |
| ↳ | API · 方舟 每模型 50 万 T… | 每模型 50 万 Token（累计 2500 万+） | 一次性赠额，超出转按量付费 | 每个模型单独一份，不是共享池，所以得挨个点「开通服务」才拿得满。官方活动页原话是「单个模型… |
| ↳ | API · 方舟 图像 / 语音 / … | 生图 50~200 张 + 语音 20 小时 + 联网 2 万次/月 | 一次性赠额 | 这些和文本模型的 50 万 Token 完全分开算，互不挤占。做多模态 demo 基本够用… |
| ↳ | API · 协作奖励计划 | 每日单模型上限 500 万 Token | 按 Token | 用多少返多少，返还额度 30 天有效。适合持续跑 Agent 迭代的人，本质是拿数据换额度。 |
| ↳ | API · 方舟 每日 200 万 T… | 每天 200 万 Token | 每日免费额度，超出按量付费 | 入口名字各说不一（有叫「协作奖励计划」的），且必须手动开通模型才生效。**两个二手源都提到… |
| **DeepSeek** | 网页版 | 不限量（有频率限制） | 完全免费 | 网页版和 App 是全功能免费，只有 API 按 Token 收钱。想省钱就用网页版，要把… |
| ↳ | 手机 App | 不限量（有频率限制） | 完全免费 | iOS / Android 都有，功能与网页版基本一致，适合手机上随手问。 |
| ↳ | 桌面客户端 | 6 元赠金（限量，到账后 7 天有效） | 赠金 + 按 Token | 6 元赠金看着少，但 Flash 空闲时段输入只要 1.5 元/百万 Token，够跑二十… |
| ↳ | API | 100 万 ~ 500 万 Token（30 天有效） | 按 Token | 送多少口径不一（100 万 / 500 万都有人写），但官方单价本来就是全网最低之一，百万… |
| **智谱 GLM** | 网页版 | 最高 2 亿 Token（累计口径） | 按 Token（赠金） | 官方落地页写「最高可领取总计 2 亿 Tokens 资源包」，这是邀请累加的上限，不是单人… |
| ↳ | 桌面客户端 | 单日最高约 3 亿 Token（周末包口径 5 亿） | 活动免费 | 量极大但只能夜间用，且是活动制随时停。适合睡前挂长任务。额度仅客户端内可用，导不出标准 A… |
| ↳ | API · 新客赠额 | 2000 万 Token | 按 Token | **额度要实名认证之后才到账**，只注册不认证就一直是 0，这是「感觉没免费」最常见的原因… |
| ↳ | API · Flash 免费档 | 不限量，受并发限制 | 0 元 | 官方价格页 FAQ 明确只点了两个——文本 GLM-4.7-Flash（200K）和视觉 … |
| **国家超算互联网** | 桌面客户端 | 活动期内不限量 + 1 亿词元智能体额度 | 活动期免费（仅限客户端内） | 关键区别——「不限量」锁在自家客户端里，不是一个能随便接的通用 API。支持 Window… |
| ↳ | API · 新客 1000 万 Tok… | 1000 万 Token | 一次性赠金，用完后按 Token 从余额扣 | 注册即到账，30 天有效，活动整体到 12-31。这个包本身锁定 GLM-5.3-Flas… |
| ↳ | API · 0.1 元秒杀 5000 … | 5000 万词元（0.1 元） | 一次性买断词元包 | 每天 10:00 开售、每账号限一次、到账后 30 天有效，过 30 天作废。有二手源说它… |
| **百度千帆** | API · 百度智能云千帆 | 无限量（QPS 50） | 0 元 | 能力不算第一梯队，但 QPS 50 是国内免费档里最宽的，适合高并发打杂。 |
| ↳ | API · 千帆 每模型 100 万 … | 每模型 100 万 Token | 一次性赠额，用完转按量付费 | 读并同意协议后系统自动开通并发额度，不用手动领。第三方模型（DeepSeek、Qwen）也… |
| ↳ | API · 千帆 ERNIE-Spee… | 不限量（QPS 约 50） | 0 元 | QPS 50 在免费档里算很宽，适合做常驻小服务。有信源说 ERNIE-3.5-8K 也永… |
| **硅基流动** | API · SiliconFlow | 2000 万 Token（约 14 元） | 按 Token | 国内低延迟，OpenAI 兼容，支持微信/支付宝。新手任务能再拿一笔，别忘了做。 |
| ↳ | API · 小模型免费档 | 无限量 | 0 元 | 小模型当分类器、意图识别、批量打标非常够用，零成本挂着跑。 |
| ↳ | API · 7 个永久 0 元模型 | 不限量（受速率限制） | 0 元 | 真正的天花板是限速不是额度——0 元档跑在固定速率上，充值也不会提升，批量跑几分钟就 42… |
| **腾讯云 TokenHub** | API · / 混元 | 每模型 100 万 Token | 按 Token | 领取日起算 1 年有效。只领近期要用的模型，领了不用会白过期。 |
| ↳ | API · 混元 Lite 永久免费 | 不限量（受速率限制） | 0 元 | 轻量任务够用（写正则、翻译段落、改注释），复杂推理别指望它。注意混元已经换代到 Tence… |
| ↳ | API · 腾讯混元 首次开通 100… | 100 万 Token + 100 万 Embedding | 一次性资源包，1 年内有效 | 有效期 1 年，是国内少见的长期包。**额度耗尽后默认不会自动转后付费**，得手动开通，这… |
| **讯飞星火** | API · Spark Lite | 无限量 | 0 元 | 中文与语音能力强。另有大额实名礼包（流传 10 亿 Token 口径），领取弹窗会默认勾选… |
| ↳ | API · 星火 Spark Lite… | 不限量（QPS 2） | 0 元 | 国内免费档里门槛最低的一档——有信源说免实名免绑卡，OpenAI 格式兼容。QPS 2 只… |
| ↳ | API · 星火 新客 Token 包 | 20 万（个人）/ 100 万（企业） | 一次性赠额 | 额度口径最乱的一家：20 万/100 万来自分梯整理，另有信源说 500 万、也有说 20… |
| **阿里云百炼** | API · （DashScope） | 约 7000 万 Token（累计） | 按 Token | 领到后 90 天有效，仅北京地域。双 11 宣传口径称「超 1 亿」，以控制台实发为准。 |
| ↳ | API · 百炼 新客各模型 100 … | 每模型 100 万 Token（合计约 8000 万） | 一次性赠额，用完自动转按量付费 | 只在华北2（北京）地域发放，其他地域没有。开通前必须先实名，不实名不发额度。额度有效期 9… |
| ↳ | API · 百炼 国际站（新加坡）免实… | 每模型 100 万 Token（90 天） | 一次性赠额，用完需实名才能继续付费使用 | 这条和国内站正好相反——国内站必须先实名，国际站新加坡地域明确写「无需实名认证即可获取和使… |
| **Kimi** | 网页版 | 不限量（有频率限制） | 完全免费 | 网页版免费，API 才要买券。注意 K2 自 10-31 起不再对 API 新用户开放，网… |
| ↳ | API | 15 元代金券 | 按 Token | 券 3 个月有效。注意 Kimi K2 自 10-31 起不再对新注册用户开放，脚本里的模… |
| **MiniMax** | 手机 App | 每日免费额度（视频按条数） | 完全免费（超出需订阅） | 视频生成这一档基本是国内最便宜的免费入口。C 端额度和开放平台 API 的额度是两套，不能… |
| ↳ | API | 15 元（约 350 万~700 万 Token） | 代金券抵扣，用完转按量付费 | 全模态是这个平台的特点——文本、语音、视频同一套 API，原生多 SDK 与 MCP 兼容… |
| **Qoder** | 桌面客户端 · 每日 100 Credits | 每天 100 Credits（30 天有效） | Credits 制 | 领取窗口到次日 10:00，错过不补，不累积。Qwen3.8-Flash 在 Qoder … |
| ↳ | 桌面客户端 · 新用户试用 / 邀请 | 试用期约 300 Credits；邀请奖励 50–1000 Credits 不等 | Credits 制 | 网传「国际版免费 2000 积分」与官方文档口径不符（官方写 2 周 Pro 试用共 30… |
| **TRAE** | IDE 插件 · 国内版 免费档 | 每月 500 积分 + 2 个云端任务并发 | 订阅制（积分） | 国内版 trae.cn 与国际版 trae.ai 是两套独立计费，别混着看。SOLO 与 … |
| ↳ | IDE 插件 · 国际版 Free | 每月 5000 次补全 + 一次性用量额度 + 2 个云端任务 | 订阅制 | 最容易踩的坑——补全按月刷新，但 Agent / Chat 的用量额度是一次性的，用完不补… |
| **七牛云** | API · AI 推理 | 300 万 Token（2 年有效） | 按 Token | 一个 Key 通吃国内外模型，OpenAI / Anthropic 双协议。有效期 2 年… |
| ↳ | API · Conatus 每日额度 | 每天 1 亿 Token | 按 Token | 单日额度国内前列。历史充值满 100 元可升到 10 亿/天。 |
| **豆包** | 网页版 | 不限量（有频率限制） | 完全免费 | 网页版免费，签到领额度只在电脑客户端。两个入口别搞混：网页版是「随便用」，客户端签到是「攒… |
| ↳ | 桌面客户端 | 每天约 200 额度（周一翻倍） | 免费额度 | 官方没公布具体数值，200 是实测口径。只在电脑端，漏签一天少 200。 |
| **阶跃星辰** | API · Step Plan | 最高 75 天（不拉人也有 30 天） | 订阅制 | 送的是 99 元 Flash Mini 档权益，能调全部旗舰模型。坑：Base URL 必… |
| ↳ | API · 阶跃 stepaudio … | 限时免费（不限量） | 活动期 0 元 | 只覆盖音频多模态这一条线，不是全模型免费，别把标题读成「整站免费」。CORS 通配符全开，… |
| **AWS Kiro** | IDE 插件 | 每月 50 credits + 新用户 500 赠送 | 订阅制（credits） | 强制先写需求（EARS 格式）、设计文档、任务清单，再让 Agent 动手，专治 AI 写… |
| **Anthropic** | API | 约 $5（14 天有效） | 按 Token | 额度小、时效短、门槛高。同类需求更建议走 OpenRouter 的 :free 或 Clo… |
| **Bolt.new** | 网页版 | 每月 100 万 token，日限 30 万 | 订阅制（token） | 不用填卡。免费档会给站点挂 Bolt 品牌标识，不能绑自定义域名，文件上传限 10MB。两… |
| **Cerebras** | API | 每天 100 万 Token（5 RPM，8K 上下文） | 按 Token | 输出速度最快的一档（约 3000 tokens/s），但 8K 上下文是硬伤，长文档别指望… |
| **Cline** | IDE 插件 | 工具免费无限制，只付模型钱 | 自带 Key（BYOK） | 它本身不送 token——价值在于能把你白嫖到的所有免费 API key 接进同一个壳子里… |
| **Cloudflare** | API | 每天 10000 Neurons | 按 Neurons | 计量单位是 Neurons 不是 Token，不同模型换算差别大，按实测排预算。UTC 0… |
| **CodeGeeX** | IDE 插件 | 免费版全功能不限量 | 订阅制 | VS Code / JetBrains 插件形态，也提供 Lingma 之外的另一条路。P… |
| **Cohere** | API | 每月 1000 次调用 | 按调用次数 | 按次数不按 Token，RAG / 检索场景（Embed、Rerank）比对话更值。 |
| **Cursor** | IDE 插件 | 每月 2000 次补全 + 50 次慢请求 | 订阅制 | 50 次请求摊到每天只有 2~3 次，活跃开发一两周就见底——免费档是试用档，不是日常档。… |
| **GitHub Copilot** | IDE 插件 | 每月 2000 次补全 + 50 次 Chat | 订阅制 | 轻度用户完全够用。学生认证后可直接免费用 Pro（GitHub Student Pack）。 |
| **GitHub Models** | API | 10 RPM 起，50–150 请求/天 | 免费层 | 状态存疑：有信源称 2026-07-30 已退役，也有当月清单仍在列。用之前先打开页面确认… |
| **Google Antigravity** | IDE 插件 | 每周配额（具体数字官方未公示） | 免费预览 | 目前最划算的白嫖入口之一——不花钱就能用 Claude Sonnet 4.6 和 Gemi… |
| **Google Gemini** | API | 每天 1000–1500 请求，1M 上下文 | 免费层 + 按量 | 综合最强免费档：模型最新、上下文 1M、不要卡。代价是免费层内容官方明说可能用于改进产品，… |
| **Groq** | API | 30 RPM，1000 请求/天，20 万 Token/天 | 按 Token | LPU 推理速度极快，适合 Agent 里的高频小调用（意图分类、工具选择）。限流按组织算… |
| **Hugging Face** | API | 约 $0.10/月 | 按量 | 典型「有免费层但不能用」：两次真实请求就见底。这里列出来是为了提醒你别把它当方案。 |
| **JetBrains AI** | IDE 插件 | 每月 3 credits（本地补全不限） | 订阅制 | 只对本来就买了 IDEA / PyCharm 的人有意义——本地补全免费无限，3 cred… |
| **Kilo Code** | IDE 插件 | 约 200 请求/小时 | 免费模型 | VS Code / JetBrains / CLI 都有。免费模型列表是活的，新模型上线会… |
| **Lovable** | 网页版 | 5 credits/天，30/月 | 订阅制（credits） | 一次像样的构建大概 0.5~1.5 credit，免费档一天能做 3~4 次真改动。免费档… |
| **Mistral** | API | 约 10 亿 Token/月（官方已不公布具体数值，看控制台） | 按 Token | 欧洲厂商，1 请求/秒。免费能摸到旗舰模型，做横向评测很划算。 |
| **NVIDIA NIM** | API | 1000 credits（约 40 RPM） | 按 Token | 2026-11 新开的大额免费口子，+86 手机号可注册，Location 选 China… |
| **OpenAI** | API | $5（3 个月有效） | 按 Token | 通常需绑卡，且部分区号不发。$5 跑不了几次旗舰模型，只够验证联通性。 |
| **OpenCode** | 命令行 | 免费模型不限量（有限速） | 免费模型 | 免费档数据条款写明「可能用于改进模型」，涉密代码别用。模型会随平台调整，别写死模型名。 |
| **OpenRouter** | API | 20 RPM，50 请求/天（历史充值过 $10 升到 1000/天） | 按 Token | 最省事的多模型对比入口。免费模型名单经常变，且常被上游限流。国内访问偶有波动。 |
| **Qoder CN（原通义灵码）** | IDE 插件 | 补全与问答不限次，编程智能体对话 50 轮次/月 | 订阅制（Credits） | 重要时间点——通义灵码已于 2026-05-20 正式更名为 Qoder CN，「个人专业… |
| **Roo Code** | IDE 插件 | 工具免费无限制 | 自带 Key（BYOK） | 比 Cline 多了 Orchestrator / Architect / Code 等角… |
| **SambaNova** | API | 每天 20 万 Token（20 RPM） | 按 Token | RDU 芯片速度很快，但要绑卡，免费档近年收紧过。不想留卡信息就跳过。 |
| **Strix** | 命令行 | 工具完全免费，只付模型钱（配本地模型可零成本） | 自带 Key（BYOK） | 7.3 万 star，Agent 跑在 Docker 沙箱里（Kali 镜像），自带 Ca… |
| **Windsurf（现 Devin Desktop）** | IDE 插件 | 每月 25 Cascade credits + 无限补全 | 订阅制 | 2026-06-02 起 Windsurf 更名为 Devin Desktop，老链接会跳… |
| **Zed** | IDE 插件 | 每月 2000 次编辑预测 + 自带 key 不限 | 订阅制 | GPL-3.0 / Apache-2.0 双协议，编辑器本身开源。真正的玩法是自带 API… |
| **v0 by Vercel** | 网页版 | 7 条消息/天 + $5 首充额度 | 订阅制（credits） | 只出前端（React + Next.js + Tailwind + shadcn/ui），… |
| **xAI Grok** | API | $25/月（共享数据 $150/月） | 按 Token | 与 OpenAI 类似属「绑卡 + 数据换额度」模式。单一来源，需自行核。 |
| **书生端砚** | 网页版 | 每月 10 墨点（约 5 亿 Token） | 墨点制 | 按月清零。换算比例取决于模型，别直接按 5 亿规划。 |
| **商汤日日新** | API | 5 小时 12 万积分 + 每周 120 万积分 | 公测免费 | 10-27 把 5h 上限从 6 万翻到 12 万，长期公测。多模态（OCR、识图）免费额… |
| **天翼 AI** | 桌面客户端 | 工作日 1.8 亿/天，周末 2 亿/天 | 免费额度 | 单日额度国内最高档。但额度限客户端内使用，导不出标准 API，适合当「白嫖型 ChatGP… |
| **小米 MiMo** | API | 未公开固定数值 | 按 Token | 另有 MiMo Orbit 创造者激励计划，需提交项目审核，通过后给大额 Token 包（… |
| **快手万擎** | API | 无限量 | 0 元 | 只标「免费」没承诺期限。新版 Air-V2.5 已转收费，认准 V1。 |
| **文心快码 Comate** | IDE 插件 | 个人标准版免费 + ¥10 体验金 | 订阅制 | 免费层给得比较实在，Multi-Agent 与 Figma2Code 不限次。付费专业版 … |
| **百川智能** | API | 80 元（约 500 万 Token） | 代金券抵扣 | 80 元在国产平台里算给得多的，但模型能力和生态比头部弱一档。医疗场景是它的差异点。 |
| **百度 AI Studio** | 网页版 | 每天 8 算力点（约 16 V100 小时） | 免费算力 | 这是算力不是 Token，但对「自己部署开源模型 = 零调用成本」这条路是关键拼图。 |
| **移动云** | API | 2500 万 Tokens | 按 Token | 自领取起 30 天有效，限流 3000 tokens/分钟。运营商系里额度最实在的一家，模… |
| **美团 CatPaw** | 桌面客户端 | 每日重置（Flash-Lite 额度很大） | 公测期 0 元 | 信源只有单一聚合站，公测随时可能结束或转收费，**动身前先去官网确认还在公测**。IDE … |
| **腾讯 Cloud Studio** | 网页版 | 每月 10000 分钟 + 10000 GPU 分钟（T4 16G） | 免费算力 | 浏览器里就是 VS Code，空闲约 10 分钟自动关，同时最多 2 个空间。 |
| **腾讯 CodeBuddy** | IDE 插件 | 每月 500 积分 + 无限补全 | 订阅制（积分） | 国产几家里免费额度偏紧的一档，重度用很快见底。标准版 ¥99/月（连续包月 ¥70），国际… |
| **腾讯元宝** | 手机 App | 不限量（有频率限制） | 完全免费 | 混元本身不是 C 端产品，普通用户免费用的是元宝。缺点是不能接工作流、不能自动化跑任务，只… |
| **蚂蚁百灵** | API | 期限内不限量 | 按 Token | 11-05 发布，两周免费约到 11-19（按发布日推算，以控制台为准）。同期基准号称超过… |
| **蛙池 AI** | 桌面客户端 | 2200 蛙蛙币（约合 220 元），积分制 10 元 = 100 积分 | 积分（蛙蛙币） | 需要内测邀请码（官网或白帽交流群领）。Windows / macOS 双端客户端，内置蛙伴… |
| **通义千问** | 手机 App | 不限量（有频率限制） | 完全免费 | C 端产品，和百炼 API 完全是两套东西——这里的免费额度不能变成 API Key。想写… |
| **魔搭社区** | API | 每天 2000 次调用 | 按次免费 | 按「次」不按 Token，跑短 prompt 很划算；长 prompt 会很快吃满。 |
| **魔芋 AI** | API | 合计最高约 2.7 亿 | 按 Token | 数字好看但拆分条件多（连签 11 天那档现在起步已经签不满）。单一来源，建议只当线索，自己… |

## 可用模型一览

> `models` 字段的可读版。同一产品下多个入口共用同一批模型时只列一次。

**AWS Kiro**

- Claude Sonnet 4.5、DeepSeek 3.2、Qwen3、GLM-5（Auto 模式路由）

**Anthropic**

- Claude 系列

**Bolt.new**

- 平台自动路由（Claude / GPT 等）

**Cerebras**

- gpt-oss-120b、Gemma-4-31B、Qwen 系列

**Cline**

- 任意（OpenAI / Anthropic / Gemini / DeepSeek / Ollama 本地）

**Cloudflare**

- Llama 4、Qwen、Mistral 等 50+

**CodeGeeX**

- GLM 系列

**Cohere**

- Command A+ 系列

**Cursor**

- 自有多模型（Claude / GPT / Gemini 系列）

**DeepSeek**

- DeepSeek-V4.1-Flash、V4-Pro
- DeepSeek V4 / V3.2

**GitHub Copilot**

- GPT / Claude Sonnet 可选

**GitHub Models**

- GPT-5、GPT-4.1、Llama、Phi

**Google Antigravity**

- Gemini 3.1 Pro / Flash、Claude Sonnet 4.6、GPT-OSS

**Google Gemini**

- Gemini 3 Flash、3.5 Flash-Lite、2.5 Flash

**Groq**

- gpt-oss-120b、gpt-oss-20b、Qwen3.6-27B、Llama 系列

**Hugging Face**

- 社区模型（含 Llama、Qwen、DeepSeek 蒸馏版）

**JetBrains AI**

- 内置本地模型 + 云端 Claude / GPT

**Kilo Code**

- NVIDIA Nemotron 3 Ultra、Nex-N2.5-Pro、MiniMax M2.7、腾讯混元 Hy3

**Kimi**

- Kimi K3、K2.5
- Kimi K3 系列、K2.5

**Lovable**

- 平台自带（Claude 等）

**MiniMax**

- MiniMax M 系列、海螺视频、海螺语音
- MiniMax-M3 / M3.1-Flash / M2.7 全模态系列、海螺语音与视频模型

**Mistral**

- Mistral Large、Codestral 等

**NVIDIA NIM**

- DeepSeek-V4.1-Flash、GLM-5.3-Flash 等百余模型

**OpenAI**

- GPT 系列

**OpenCode**

- DeepSeek V4 Flash、MiMo-V2.6-Flash-Free、LongCat-2.0、Nemotron 3 Ultra

**OpenRouter**

- DeepSeek、Llama、Qwen 等 20+ 免费模型

**Qoder**

- Qoder 全系（含 Qwen3.8-Flash 0 倍率）
- 全部旗舰模型

**Qoder CN（原通义灵码）**

- Qwen 系列为主，可切 GLM / DeepSeek / Kimi / MiniMax

**Roo Code**

- 任意（BYOK）

**SambaNova**

- DeepSeek-V3、Llama 系列

**Strix**

- OpenAI / Anthropic / Google / Bedrock / Vertex / OpenRouter / 本地 Ollama

**TRAE**

- 豆包 Seed 2.1、DeepSeek-V4.1、GLM-5.3、Kimi、MiniMax 可切
- Auto 模式自动路由（Claude / GPT / Gemini 等）

**Windsurf（现 Devin Desktop）**

- 自有 Cascade 多模型

**WorkBuddy**

- 平台在售模型
- 平台内全模型（仅用于兑换积分）
- 平台内全模型（含限时 0 倍率模型）
- 平台内全模型
- Hunyuan Hy3、Hy4-preview

**Zed**

- Claude、GPT、Gemini、Grok（自选）

**v0 by Vercel**

- Vercel 路由（Claude / GPT / Gemini）

**xAI Grok**

- Grok 系列

**七牛云**

- DeepSeek、GLM、Qwen、Kimi、豆包等 50+
- 平台在售模型

**书生端砚**

- 书生系列

**商汤日日新**

- SenseNova-6.8-Flash-Lite、U1.5-Fast、DeepSeek-V4-Flash 等 7 款

**国家超算互联网**

- 平台旗舰模型（GLM-5.3 / DeepSeek-V4.1 / Kimi-K3 / Qwen3.8 / MiniMax-M3 等）+ 自研科学计算智能体
- DeepSeek（V4.1-Flash、V4.1-Flash-1017、V4-Pro-0813、V4-Flash-0731）/ 通义千问（Qwen3.8-Max、Qwen3.8-Flash）/ 智谱 GLM（5.3、5.3-Flash、5.2、5.1、5）/ 月之暗面 Kimi（K3、K3.1-Pro、K2.7-Code、K2.6、K2.5）/ MiniMax（M3、M3.1-Flash、M2.7、M2.5）/ 其他（Auto 自动路由、OCR、ASR、文生图、图像编辑、Embedding）

**天翼 AI**

- 星辰系列

**小米 MiMo**

- MiMo 推理系列

**快手万擎**

- KAT-Coder-Air-V1、KAT-Coder-Exp-72B-1010

**文心快码 Comate**

- 文心 ERNIE 系列 + DeepSeek

**智谱 GLM**

- GLM 全系
- GLM-5.3-Flash
- GLM-4.7-Flash（200K，文本）、GLM-4.6V-Flash（视觉）、GLM-4-Flash-250414（128K）、GLM-Z1-Flash（128K）

**火山方舟**

- Doubao-Seed 系列、DeepSeek、Kimi、GLM
- Doubao-Seed-Evolving 等指定模型
- Kimi-K3.1-Pro、DeepSeek-V4.1、GLM-5.3、Doubao-Seed-2.1
- Doubao-Seed-2.1-pro / 2.1-turbo / Evolving / Character、DeepSeek 系、Kimi 系等
- 除多模态向量化与同声传译外的全部模型
- Doubao-Seedream-5.0-lite / 4.5 / 4.0、Doubao-语音合成、Doubao-声音复刻、Doubao-流式语音识别、Doubao-embedding-vision
- 豆包 Doubao-Seed 系列主力模型

**百川智能**

- Baichuan4 系列、Baichuan4-Air、医疗增强模型 M3

**百度 AI Studio**

- 免费 GPU 算力（非 Token）

**百度千帆**

- ERNIE-Speed-8K 等
- ERNIE-4.5-Turbo（128K/32K/VL）、ERNIE-X1-Turbo、DeepSeek-V3/R1、Qwen3、Kimi-K2-Instruct、bge-large 等
- ERNIE-Speed-8K、ERNIE-Lite

**硅基流动**

- DeepSeek / Qwen / GLM 等开源模型
- Qwen2.5-7B、GLM-4-9B、DeepSeek-R1-Distill-8B 等
- Qwen3-8B、Qwen3.5-4B、Qwen2.5-7B-Instruct、GLM-4-9B-0414、GLM-Z1-9B-0414、DeepSeek-R1-0528-Qwen3-8B、Xing4.0-29B

**移动云**

- 移动自营模型

**美团 CatPaw**

- LongCat / Flash-Lite 系列自研模型

**腾讯 Cloud Studio**

- 免费 GPU 算力（非 Token）

**腾讯 CodeBuddy**

- 混元 + DeepSeek + GLM 可切

**腾讯云 TokenHub**

- DeepSeek、Kimi、GLM、混元、MiniMax
- Hunyuan Hy3 / Hy4 preview、role-latest、translation、Hunyuan-a13b、Hunyuan-embedding 等
- Hunyuan-Lite（256K 上下文）

**腾讯元宝**

- 混元 Hy3 / Hy4、DeepSeek 系（可切换）

**蚂蚁百灵**

- Ling-3.2-flash（560B MoE，1M 上下文，多模态）

**蛙池 AI**

- DeepSeek-V4-Pro / Flash、GLM-5.2、MiniMax-M3、Kimi-K2.7-Code、Qwen3.7-Max、豆包 Seed 2.0

**讯飞星火**

- Spark Lite、Spark-X2.5-1.7B
- Spark Lite（端侧小模型）
- Spark X2-Flash（192K）、Spark Ultra、Spark Pro

**豆包**

- 豆包系列

**通义千问**

- Qwen3.8-Max、Qwen3-Max-Thinking 等旗舰模型

**阶跃星辰**

- Step-5-Preview、Step-3.7-Flash、StepAudio-3
- stepaudio-3 系列（语音理解与生成）

**阿里云百炼**

- 通义千问全系 + DeepSeek + Kimi + GLM 等 70+
- 通义千问全系（Qwen3.8-Max / Plus / Flash、Qwen3-Max-Thinking）、DeepSeek 系、Kimi 系、GLM 系、MiniMax 系等 150+ 模型
- 通义千问国际版全系（Qwen3.8 系列、Qwen-Max 等）

**魔搭社区**

- Qwen 系列及社区开源模型

**魔芋 AI**

- 聚合多模型
