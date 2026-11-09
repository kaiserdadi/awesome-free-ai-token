# 全网免费 AI 额度雷达 · Free AI Token Radar

![license](https://img.shields.io/badge/license-MIT-black)
![data](https://img.shields.io/badge/数据-YAML_驱动-blue)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

> 这不是又一份「2000 万 Token 免费领」的清单。
> **每一条都带截止日、带出处、带可信度，过期了会自动被标出来。**

这类清单最大的问题不是不全，是**过期了还在传**。你照着半年前的文章去注册，页面早就 404；你不确定是自己的操作错了，还是活动没了，白折腾一小时。

所以这个仓库做三件事：

1. **收**：国内外能白拿的 AI 额度，包括 Token、积分、Credits、算力；
2. **标**：每条写清楚截止日、要不要实名、要不要绑卡、出处链接、可信度；
3. **查**：脚本按日期自动体检，把过期的、快过期的、久未复核的挑出来。

数据都在 [`data/providers.yaml`](data/providers.yaml)，README 的表格是脚本渲染的，不是手抄的。

---

## 先看这个：现在最值得动手的 5 条

如果只花十分钟，按这个顺序来：

| # | 去哪 | 拿什么 | 为什么是它 |
|---|---|---|---|
| 1 | [国家超算互联网](https://www.scnet.cn) | 新客 1 亿词元，0.1 元秒杀 5000 万词元包，客户端旗舰模型不限量 | 国家级平台，额度最猛，**11-30 截止** |
| 2 | [智谱开放平台](https://open.bigmodel.cn) | 新客 2000 万 Token（永久）+ GLM-4.7-Flash 永久 0 元 | 注册三分钟搞定，长期兜底首选 |
| 3 | [Google AI Studio](https://aistudio.google.com) | 每天 1000–1500 请求，1M 上下文 | 不要信用卡，模型最新，海外最强免费档 |
| 4 | [火山引擎方舟](https://console.volcengine.com/ark) | 实名后每模型每天 200 万 Token 自动刷新 | 每日续杯，跑批不心疼 |
| 5 | [WorkBuddy](https://www.workbuddy.cn) | 每天 100 积分（连签 7 天再送 1000） | 桌面端点两下，一分钟的事 |

> 第 1 条是限时活动，第 5 条是每日续杯，性质完全不同。**限时的先领，续杯的设成每天顺手点。**

---

## 完整清单

<!-- AUTO:START 由 scripts/render.py 生成，不要手改这一段 -->

> 数据截至 **2026-11-09** ｜ 共 **58** 条（国内 41 · 海外 17） ｜ 每日/每月续杯 13 条 ｜ 限时活动 7 条（**3 条 14 天内到期或已过期**）

| 分类 | 条数 | 一句话 |
|---|---|---|
| 限时活动 | 7 | 抢时间，先领后看 |
| 每日续杯 | 13 | 攒出来的额度最耐用 |
| 注册一次性 | 15 | 一次给一大笔 |
| 长期免费模型 | 23 | 兜底，不依赖活动 |

### 限时活动

*有明确截止日，先领再说。按剩余天数从少到多排。*

| 平台 | 白拿什么 | 额度 | 到期 | 门槛 | 可信 |
|---|---|---|---|---|---|
| [魔芋 AI 双 11](https://moyu.cn) | 新客 1000 万 + 老号回归 5000 万 + 企业认证 1 亿 + 邀请拉满 1.6 亿 | 合计最高约 2.7 亿 | **2026-11-11（剩 2 天）** | 实名 | 低 |
| [WorkBuddy 混元 Hy3 / Hy4 限免](https://www.workbuddy.cn) | Hy3 纯语言任务 0 积分；Hy4 preview 夜间窗口 0 倍率 | 窗口内不扣积分 | **2026-11-15（剩 6 天）** | 无 | 中 |
| [蚂蚁百灵 Ling-3.2-Flash](https://developer.ant-ling.com) | 上线前两周 API 全免费，兼容 OpenAI / Anthropic 双协议 | 期限内不限量 | **2026-11-19（剩 10 天）** | 实名 | 高 |
| [超算互联网客户端（SCNet 智能体客户端 / SClaw）](https://www.scnet.cn) | 双 11 期间客户端内旗舰模型词元不限量、AI 调用不受限；新用户注册另领 1 亿词元科学计算智能体额度 | 活动期内不限量 + 1 亿词元智能体额度 | 2026-11-30（剩 21 天） | 无 | 高 |
| [火山引擎 11.11 AI 智选](https://www.volcengine.com) | 实名后每个模型每天 200 万自动刷新，活动页标总可用 2000 万+/天 | 2000 万+/天（4 模型合计） | 2026-11-30（剩 21 天） | 实名 | 中 |
| [超算互联网 模型服务（MaaS）](https://www.scnet.cn/ui/mall/service/llm) | 新用户注册领 1000 万 Token 包（GLM-5.3-Flash）；0.1 元秒杀 5000 万词元包；Token Plan 订阅 5.4 折 | 1000 万 Token（新客）+ 0.1 元购 5000 万 | 2026-12-31（剩 52 天） | 实名 | 高 |
| [阶跃星辰 Step Plan](https://platform.stepfun.com) | 登录送 15 天 + 完成首次调用再送 15 天 + 每邀 1 人双方各 15 天（上限 3 人） | 最高 75 天（不拉人也有 30 天） | 未公布 | 实名 | 高 |

### 每日 / 每月续杯

*签一次到、点一次领取，就能反复拿。适合当日常主力。*

| 平台 | 白拿什么 | 额度 | 到期 | 门槛 | 可信 |
|---|---|---|---|---|---|
| [WorkBuddy Buddy 加油站](https://www.workbuddy.cn) | 桌面客户端左下角头像 → Buddy 加油站 → 领取今日礼包；连签 7 天额外 1000 | 每天 100 积分（月约 3000） | 未公布 | 无 | 高 |
| [Qoder 每日 100 Credits](https://qoder.com) | 每天 10:00 开放新一轮，桌面端用量面板礼物图标手动领 | 每天 100 Credits（30 天有效） | 未公布 | 无 | 高 |
| [豆包（电脑端签到）](https://www.doubao.com) | 电脑版左侧活动位或「我 → 免费额度」签到 | 每天约 200 额度（周一翻倍） | 未公布 | 实名 | 中 |
| [电信天翼 AI](https://teleai.com.cn) | 下载客户端手机号注册，每天 0 点重置 | 工作日 1.8 亿/天，周末 2 亿/天 | 未公布 | 实名 | 中 |
| [书生·端砚](https://discovery.intern-ai.org.cn) | 微信扫码登录，每月发放墨点，1 墨点最高抵 5000 万 Token | 每月 10 墨点（约 5 亿 Token） | 未公布 | 无 | 中 |
| [商汤日日新 SenseNova](https://platform.sensenova.cn/token-plan) | Token Plan 公测期整体免费，滚动窗口刷新，无需绑卡 | 5 小时 12 万积分 + 每周 120 万积分 | 未公布 | 实名 | 高 |
| [七牛云 Conatus 每日额度](https://www.qiniu.com/ai/models) | 完成认证后每天自动发放，0 点重置 | 每天 1 亿 Token | 2026-11-30（剩 21 天） | 实名 | 中 |
| [魔搭社区 ModelScope 推理 API](https://modelscope.cn) | 绑定阿里云账号后每天免费调用额度 | 每天 2000 次调用 | 长期 | 实名 | 高 |
| [百度 AI Studio（算力）](https://aistudio.baidu.com) | 每天赠送算力点，可跑 V100/A100 环境 | 每天 8 算力点（约 16 V100 小时） | 长期 | 实名 | 高 |
| [腾讯 Cloud Studio（算力）](https://cloudstudio.net) | 标准版每月赠开发时长 + GPU 时长，预装 Ollama 与 DeepSeek | 每月 10000 分钟 + 10000 GPU 分钟（T4 16G） | 长期 | 实名 | 高 |
| [智谱 ZCode / AutoClaw 夜间包](https://z.ai) | 客户端左下角弹窗领取当日额度，23 点生效、次日 9 点过期 | 单日最高约 3 亿 Token（周末包口径 5 亿） | 未公布 | 实名 | 中 |
| [火山方舟协作奖励计划](https://console.volcengine.com/ark) | 调用指定模型并上报推理数据，次日返还等量免费 Token 包 | 每日单模型上限 500 万 Token | 未公布 | 实名 | 中 |
| [xAI Grok API 🌐](https://x.ai/api) | 每月基础免费额度，同意数据用于训练可提到更高档 | $25/月（共享数据 $150/月） | 未公布 | 绑卡 | 低 |

### 注册 / 实名一次性

*开号就发，一辈子一次。国内优先，上手成本从低到高。*

| 平台 | 白拿什么 | 额度 | 到期 | 门槛 | 可信 |
|---|---|---|---|---|---|
| [智谱 AI 开放平台（GLM）](https://open.bigmodel.cn) | 新用户注册赠送 Token 包，永久有效 | 2000 万 Token | 长期 | 实名 | 高 |
| [硅基流动 SiliconFlow](https://cloud.siliconflow.cn) | 新用户注册送额度券，另做新手任务可再加 | 2000 万 Token（约 14 元） | 长期 | 实名 | 高 |
| [七牛云 AI 推理](https://www.qiniu.com/ai/models) | 创建第一个 API Key 即激活资源包 | 300 万 Token（2 年有效） | 2028-12-31（剩 783 天） | 实名 | 高 |
| [Qoder 新用户试用 / 邀请](https://qoder.com/activities) | 新用户免费试用 2 周 Pro；邀请好友注册双方得 Credits | 试用期约 300 Credits；邀请奖励 50–1000 Credits 不等 | 未公布 | 无 | 高 |
| [Kimi 开放平台（月之暗面）](https://platform.moonshot.cn) | 新用户实名后发放代金券，抵扣 API 调用 | 15 元代金券 | 未公布 | 实名 | 高 |
| [DeepSeek 开放平台](https://platform.deepseek.com) | 新用户注册赠送 Token | 100 万 ~ 500 万 Token（30 天有效） | 未公布 | 实名 | 中 |
| [阿里云百炼（DashScope）](https://bailian.console.aliyun.com) | 控制台首页「新手资源」手动领取，每个模型独立 100 万 | 约 7000 万 Token（累计） | 2026-12-31（剩 52 天） | 实名 | 高 |
| [火山引擎方舟（豆包）](https://console.volcengine.com/ark) | 新用户每个模型 50 万 Token 安心体验额度 | 每模型 50 万 Token | 长期 | 实名 | 高 |
| [腾讯云 TokenHub / 混元](https://cloud.tencent.com/product/tokenhub) | 新用户每个模型各领 100 万 Token 免费体验包 | 每模型 100 万 Token | 2026-12-31（剩 52 天） | 实名 | 高 |
| [DeepSeek Harness 桌面端](https://www.deepseek.com) | 下载 Windows / macOS 安装包，首次登录送 6 元赠金，无需充值 | 6 元赠金（限量，到账后 7 天有效） | 未公布 | 实名 | 高 |
| [移动云 MoMA](https://ecloud.10086.cn) | 新用户控制台手动领取（限自营模型） | 2500 万 Tokens | 2026-12-31（剩 52 天） | 实名 | 中 |
| [小米 MiMo 开放平台](https://ai.xiaomi.com) | 新用户注册赠试用额度 | 未公开固定数值 | 未公布 | 实名 | 低 |
| [NVIDIA NIM (build.nvidia.com) 🌐](https://build.nvidia.com) | 邮箱注册后在 API Keys 页生成密钥，兼容 OpenAI 格式 | 1000 credits（约 40 RPM） | 未公布 | 无 | 高 |
| [OpenAI API 试用额度 🌐](https://platform.openai.com) | 新账号赠送 API 额度 | $5（3 个月有效） | 未公布 | 绑卡 | 中 |
| [Anthropic API 试用额度 🌐](https://console.anthropic.com) | 新账号赠送 API 额度 | 约 $5（14 天有效） | 未公布 | 绑卡 | 低 |

### 长期 0 元模型

*价目表上就是 0 元，不靠活动。最适合当兜底。*

| 平台 | 白拿什么 | 额度 | 到期 | 门槛 | 可信 |
|---|---|---|---|---|---|
| [智谱 GLM-Flash 系列](https://open.bigmodel.cn) | 价目表 0 元，输入输出全免 | 无限量（受 QPS 限制） | 长期 | 实名 | 高 |
| [硅基流动小模型免费档](https://cloud.siliconflow.cn) | 9B 参数以下模型长期免费不限量 | 无限量 | 长期 | 实名 | 高 |
| [百度智能云千帆](https://console.bce.baidu.com/qianfan) | ERNIE-Speed / Lite / Tiny 永久免费，QPS 50 | 无限量（QPS 50） | 长期 | 实名 | 高 |
| [讯飞星火 Spark Lite](https://xinghuo.xfyun.cn) | Spark Lite / X2.5-1.7B 长期免费，X2.5-4B 限时免费 | 无限量 | 长期 | 实名 | 中 |
| [WorkBuddy 网页版](https://www.workbuddy.cn) | 浏览器打开官网直接对话，不用安装 | 可用，但没有签到与成长计划 | 长期 | 无 | 高 |
| [豆包网页版](https://www.doubao.com) | 浏览器打开直接对话，部分功能免登录可试 | 不限量（有频率限制） | 长期 | 实名 | 中 |
| [Kimi 网页版](https://kimi.com) | 网页端直接对话，长上下文与联网搜索免费 | 不限量（有频率限制） | 长期 | 实名 | 中 |
| [DeepSeek 网页版](https://chat.deepseek.com) | 打开网页登录即可对话，深度思考与联网搜索默认可用 | 不限量（有频率限制） | 长期 | 实名 | 高 |
| [DeepSeek 手机 App](https://www.deepseek.com) | 应用商店搜索安装，登录即用，与网页版同一套额度 | 不限量（有频率限制） | 长期 | 实名 | 高 |
| [快手万擎 StreamLake](https://streamlake.com) | 编码模型输入输出全免费 | 无限量 | 未公布 | 实名 | 中 |
| [Google AI Studio / Gemini API 🌐](https://aistudio.google.com) | Flash / Flash-Lite 系列免费层，每天配额重置，无需信用卡 | 每天 1000–1500 请求，1M 上下文 | 长期 | 无 | 高 |
| [Groq Cloud 🌐](https://console.groq.com) | 免费层按模型给每日请求上限，邮箱注册即可 | 30 RPM，1000 请求/天，20 万 Token/天 | 长期 | 无 | 高 |
| [Cerebras Inference 🌐](https://cloud.cerebras.ai) | 免费层每天固定 Token 额度，无需信用卡 | 每天 100 万 Token（5 RPM，8K 上下文） | 长期 | 无 | 中 |
| [OpenRouter 🌐](https://openrouter.ai) | 带 :free 后缀的模型免费调用，一个 Key 通吃多家 | 20 RPM，50 请求/天（历史充值过 $10 升到 1000/天） | 长期 | 无 | 高 |
| [GitHub Models 🌐](https://github.com/marketplace/models) | 用 GitHub 账号直接调 GPT / Llama / Phi 等模型 | 10 RPM 起，50–150 请求/天 | 未公布 | 无 | 低 |
| [Cohere 🌐](https://dashboard.cohere.com) | 试用 Key，无需信用卡 | 每月 1000 次调用 | 长期 | 无 | 高 |
| [OpenCode Zen 🌐](https://opencode.ai) | 客户端自带若干免费模型，装完即可用，不需自备 Key | 免费模型不限量（有限速） | 未公布 | 无 | 中 |
| [Kilo Code 🌐](https://kilocode.ai) | 开源 AI 编程 Agent，内含十余个免费模型，不要 Key、不要卡 | 约 200 请求/小时 | 未公布 | 无 | 中 |
| [GitHub Copilot Free 🌐](https://github.com/features/copilot) | 个人免费档，含代码补全与 Chat | 每月 2000 次补全 + 50 次 Chat | 长期 | 无 | 高 |
| [Mistral La Plateforme 🌐](https://console.mistral.ai) | Experiment 免费档，限速可用全系模型 | 约 10 亿 Token/月（官方已不公布具体数值，看控制台） | 长期 | 无 | 中 |
| [Cloudflare Workers AI 🌐](https://developers.cloudflare.com/workers-ai/) | 免费套餐每天赠 Neurons，按模型换算成调用量 | 每天 10000 Neurons | 长期 | 无 | 高 |
| [Hugging Face Inference Providers 🌐](https://huggingface.co/docs/inference-providers) | 免费账户每月极小额度的推理额度，可路由数千个社区模型 | 约 $0.10/月 | 长期 | 无 | 高 |
| [SambaNova Cloud 🌐](https://cloud.sambanova.ai) | 免费层，须先绑卡 | 每天 20 万 Token（20 RPM） | 长期 | 绑卡 | 中 |

> 🌐 = 海外平台，通常需要自备网络环境。门槛列只写「注册时要过什么关」，实际折腾程度另见 `data/providers.yaml` 的 `difficulty` 字段（1 最省事，5 最费劲）。
>
> 到期列的「长期」指额度不过期或活动无固定截止日；「未公布」指官方没写死，随时可能停——两类都不代表可以放心囤。

<!-- AUTO:END -->

---

## 按产品看：同一个 AI，不同形态差多少

上面那张表是按「怎么领」分的。但真正容易踩坑的是这一层：**同一个产品，换个入口，收费方式完全变了。**

DeepSeek 是最典型的例子——网页版全功能免费，桌面端 Harness 送 6 元赠金，API 纯按 Token 收钱。很多人试了一下 API 觉得「这玩意儿要花钱」，其实他只是用错了入口。

<!-- PRODUCTS:START 由 scripts/render.py 生成，不要手改这一段 -->
> 只列**有两个以上入口**的产品：10 家、25 条形态记录。完整 43 家见 [docs/products.md](docs/products.md)。

| 产品 | 形态 | 白拿到什么 | 计费方式 | 备注 |
|---|---|---|---|---|
| **DeepSeek** | 网页版 | 不限量（有频率限制） | 完全免费 | 网页版和 App 是全功能免费，只有 API 按 Token 收钱。想省钱就用网页版，要把… |
| ↳ | 手机 App | 不限量（有频率限制） | 完全免费 | iOS / Android 都有，功能与网页版基本一致，适合手机上随手问。 |
| ↳ | 桌面客户端 | 6 元赠金（限量，到账后 7 天有效） | 赠金 + 按 Token | 6 元赠金看着少，但 Flash 空闲时段输入只要 1.5 元/百万 Token，够跑二十… |
| ↳ | API | 100 万 ~ 500 万 Token（30 天有效） | 按 Token | 送多少口径不一（100 万 / 500 万都有人写），但官方单价本来就是全网最低之一，百万… |
| **WorkBuddy** | 网页版 | 可用，但没有签到与成长计划 | 积分制（无签到） | 网页版定位是「随手用一下」：不碰本地文件、不能跑自动化、没有签到入口。为了领积分去装客户端… |
| ↳ | 桌面客户端 | 每天 100 积分（月约 3000） | 积分制 | 只在电脑客户端有，网页版和手机端都没有。0 点刷新，当天不领作废。体验版另每月赠 500 … |
| ↳ | 桌面客户端 | 窗口内不扣积分 | 积分制 | 截止日口径冲突（一说 10-31 已到期，一说延至 11-15），以客户端模型选择器是否显… |
| **智谱 GLM** | 桌面客户端 | 单日最高约 3 亿 Token（周末包口径 5 亿） | 活动免费 | 量极大但只能夜间用，且是活动制随时停。适合睡前挂长任务。额度仅客户端内可用，导不出标准 A… |
| ↳ | API | 2000 万 Token | 按 Token | 国内最常被当兜底的一家，额度永久有效、并发 30。OpenAI 兼容，改 Base URL… |
| ↳ | API | 无限量（受 QPS 限制） | 0 元 | 长期免费档里中文代码能力最能打的一档。注意并发约 1，适合小流量常驻。 |
| **火山方舟** | API | 每模型 50 万 Token | 按 Token | 安心体验模式超额自动暂停，不会产生意外账单，但要记得关掉自动转付费。 |
| ↳ | API | 2000 万+/天（4 模型合计） | 按 Token | 活动页没写死截止日，按大厂惯例 11 月中旬收尾，别等。每日刷新是国内最舒服的续杯形态。 |
| ↳ | API | 每日单模型上限 500 万 Token | 按 Token | 用多少返多少，返还额度 30 天有效。适合持续跑 Agent 迭代的人，本质是拿数据换额度。 |
| **Kimi** | 网页版 | 不限量（有频率限制） | 完全免费 | 网页版免费，API 才要买券。注意 K2 自 10-31 起不再对 API 新用户开放，网… |
| ↳ | API | 15 元代金券 | 按 Token | 券 3 个月有效。注意 Kimi K2 自 10-31 起不再对新注册用户开放，脚本里的模… |
| **Qoder** | 桌面客户端 | 每天 100 Credits（30 天有效） | Credits 制 | 领取窗口到次日 10:00，错过不补，不累积。Qwen3.8-Flash 在 Qoder … |
| ↳ | 桌面客户端 | 试用期约 300 Credits；邀请奖励 50–1000 Credits 不等 | Credits 制 | 网传「国际版免费 2000 积分」与官方文档口径不符（官方写 2 周 Pro 试用共 30… |
| **七牛云** | API | 300 万 Token（2 年有效） | 按 Token | 一个 Key 通吃国内外模型，OpenAI / Anthropic 双协议。有效期 2 年… |
| ↳ | API | 每天 1 亿 Token | 按 Token | 单日额度国内前列。历史充值满 100 元可升到 10 亿/天。 |
| **国家超算互联网** | 桌面客户端 | 活动期内不限量 + 1 亿词元智能体额度 | 活动期免费（仅限客户端内） | 关键区别——「不限量」锁在自家客户端里，不是一个能随便接的通用 API。支持 Window… |
| ↳ | API | 1000 万 Token（新客）+ 0.1 元购 5000 万 | 赠金 + 按 Token 计费（或 Token Plan 包月） | 真 API，兼容 OpenAI 与 Anthropic 协议，base_url 是 htt… |
| **硅基流动** | API | 2000 万 Token（约 14 元） | 按 Token | 国内低延迟，OpenAI 兼容，支持微信/支付宝。新手任务能再拿一笔，别忘了做。 |
| ↳ | API | 无限量 | 0 元 | 小模型当分类器、意图识别、批量打标非常够用，零成本挂着跑。 |
| **豆包** | 网页版 | 不限量（有频率限制） | 完全免费 | 网页版免费，签到领额度只在电脑客户端。两个入口别搞混：网页版是「随便用」，客户端签到是「攒… |
| ↳ | 桌面客户端 | 每天约 200 额度（周一翻倍） | 免费额度 | 官方没公布具体数值，200 是实测口径。只在电脑端，漏签一天少 200。 |
<!-- PRODUCTS:END -->

> `↳` 表示同一产品的另一个入口。全量产品清单见 [`docs/products.md`](docs/products.md)。

---

## 怎么组合：四层结构，基本不用花钱

单看「哪家额度大」会被带偏。真正省钱的用法是分层——不同层的失效风险不一样，混着用才稳。

```mermaid
flowchart LR
    Q["今天要干的活"] --> A{"是什么类型"}
    A -->|"写代码"| B["编码层<br/>Copilot Free / Kilo Code / Qoder"]
    A -->|"卡住的难题"| C["兜底层<br/>GLM-4.7-Flash / Gemini Flash"]
    A -->|"跑批打标"| D["弹药层<br/>百炼 / 火山 / TokenHub"]
    A -->|"日常轻量"| E["续杯层<br/>WorkBuddy / Qoder / 商汤"]
```

| 层 | 作用 | 失效风险 | 用哪些 |
|---|---|---|---|
| **兜底层** | 永远有得用，活动停了也不影响 | 低（写在价目表里） | GLM-4.7-Flash、硅基流动 9B 以下、Gemini Flash、Cerebras、ERNIE-Speed |
| **续杯层** | 每天点一下，覆盖日常轻中度用量 | 中（活动制，随时换期） | WorkBuddy、Qoder、商汤日日新、七牛、天翼 AI、豆包、智谱 ZCode |
| **弹药层** | 一次性大额，跑批、压测、长任务 | 高（领完就没了） | 阿里云百炼、火山方舟、腾讯 TokenHub、SCNet、NVIDIA NIM、七牛 300 万 |
| **编码层** | IDE 里直接写代码，不用自己配 Key | 中 | GitHub Copilot Free、Kilo Code、OpenCode、Qoder |

一个普通工作日长这样：

- **写代码** → 编码层的客户端（Qoder / Kilo Code / Copilot Free），零配置；
- **遇到难问题** → 切兜底层的 GLM-4.7-Flash 或 Gemini Flash，免费且够强；
- **跑批量任务**（清洗数据、打标、翻译）→ 弹药层的大额度，或者续杯层里当天攒下来的量；
- **要顶级模型跑 Agent** → 这时候才该花钱，前面的层解决不了。

**一句话：兜底层当水电，续杯层当零钱，弹药层当红包。别拿红包当工资。**

---

## 避坑：这 8 条比额度本身重要

**1. 免费层可能在拿你的数据训练模型。**
Gemini 免费层、OpenCode Zen 的免费模型、Grok 的低价档，官方条款里都写着内容「可能用于改进产品」。付费档通常不这么写。**涉密代码、客户资料、未公开的方案，别往免费层喂。**

**2. 赠送额度到期清零，平台不会提醒你。**
百炼 90 天、TokenHub 1 年、Qoder Credits 30 天、签到积分约 180 天。开通当天就跑一次能跑通的调用，把链路打通；别等「以后再用」，结果悄悄过期。

**3. 限流比额度更早把你拦住。**
免费档普遍 20–30 RPM、并发 1–2。写个 for 循环批量跑，第三次就撞 429。真要跑批，拆到多家平台分摊，或者本地 Ollama 顶高峰。

**4. 「倍率」不是「次数」。**
WorkBuddy、Qoder 这类按倍率扣：模型标 0.65× 表示一次调用扣 0.65 个积分，标 0.0× 才是不扣。看到「每天 100 积分」先确认你要用的模型倍率是多少，否则以为能用一百次，实际用了十几次就没了。

**5. 客户端内的额度，导不出标准 API。**
ZCode 夜间包、天翼 AI、豆包客户端额度，基本只能在它自己的客户端里花。想接进自己的 Agent 或 Cursor，先确认它给的是**标准 API Key**，而不是平台内代币。

**6. 领取页默认勾着「用完自动续费」。**
典型是讯飞星辰的大额礼包：弹窗底部那行默认打勾，10 亿烧完就开始扣真钱。**领之前先把勾去掉。** 火山的「安心体验模式」相对安全（超额自动暂停），但也要确认没开自动转付费。

**7. 二手清单会骗你，而且骗得很自然。**
本仓库自己就留了个活例子：GitHub Models 有信源说 2026-07-30 已退役，也有当月清单仍在推荐。所以每条都标了 `confidence`（高/中/低）和 `verified` 日期。**看到「低」，先去官网确认再动手。**

**8. 网售「新人激活码」「内部兑换码」一律当钓鱼。**
这类平台没有通用兑换码。花钱买码 = 送钱 + 送账号。

---

## 数据怎么维护

```
data/providers.yaml     单一数据源，50+ 条，改这里
data/schema.md          字段含义
scripts/render.py       渲染 README 的两张表 + docs/products.md
scripts/check.py        体检：过期 / 快过期 / 久未复核
scripts/_data.py        极简加载器（零第三方依赖）
docs/products.md        按产品聚合的视图（自动生成，勿手改）
```

改完数据跑两条命令：

```bash
python3 scripts/render.py     # 重生成 README 表格
python3 scripts/check.py      # 看看有多少过期了
```

`check.py` 默认退出码是 0——**过期是常态，不是错误**。CI 里想拿它当红线，加 `--strict`。

GitHub Actions 每周一自动跑一次体检，把结果贴进 Issue（见 `.github/workflows/check.yml`）。

### 可信度怎么定

| 级别 | 含义 |
|---|---|
| **高** | 官方页面 / 官方新闻稿 / 官方文档里能直接看到 |
| **中** | 媒体报道或二手整理，但被两个以上来源交叉印证过 |
| **低** | 只有一个来源，或来源本身有时效争议，**动手前必须自己核** |

### 收录标准

- 必须能**零成本**拿到（0 元付费秒杀也算，因为成本约等于 0）；
- 必须有**可访问的官方链接**，不接受纯转述；
- 必须写清**拿到的是标准 API 还是平台内额度**；
- 限时活动必须写**截止日**，写不清的进 `low` 并注明。

不收录：纯聊天 App 的免费版（没有 API）、需要企业资质审核才发的定向计划、教程搬运号。

---

## 贡献

欢迎 PR，规则很短：

1. 改 `data/providers.yaml`，一条一个 `- id:` 块；
2. **必须填 `source`**（你从哪看到的），没有出处的条目会被拒；
3. 跑 `python3 scripts/_data.py` 过校验，再跑 `render.py` 更新 README；
4. 发现过期条目：不用删，把 `expiry` 留着，或直接提交 `expired` Issue。

字段说明见 [`data/schema.md`](data/schema.md)，逐条领取步骤见 [`docs/claim-guide.md`](docs/claim-guide.md)，调用代码见 [`docs/api-examples.md`](docs/api-examples.md)。

---

## 免责声明

所有额度、价格、活动规则随时可能变，**以各平台官方页面为准**。本仓库只做信息索引，不对额度到账、活动延续、账号安全做任何担保。签到刷量、多开小号、批量注册这类操作通常会触发风控并回收积分，别为了几十块钱把号搭进去。

数据截至 **2026-11-09**。

## License

[MIT](LICENSE)
