# 装客户端，还是接 API？

一句话：**只想用 → 装客户端；想接进自己的程序、或者用第三方客户端 → 拿 API Key。**

这两条路不冲突，DeepSeek 是最典型的例子——**官方 App / 网页版全功能免费，只有 API 按 Token 收钱**。所以「想要 DeepSeek」这件事，先问自己一句：你是要一个能聊天的窗口，还是要一个能塞进脚本的接口？

---

## 三十秒决策

| 你的情况 | 走哪条 | 从哪开始 |
|---|---|---|
| 我就想聊天、问文档、写点东西 | 装客户端（网页版也算） | DeepSeek App、腾讯元宝、通义千问 |
| 我要写代码，让 AI 自己读文件、改代码 | 装 IDE / Agent 客户端 | TRAE 国内版、Qoder CN、腾讯 CodeBuddy |
| 我要把 AI 接进自己的脚本、网站、机器人 | 拿 API Key | 硅基流动、七牛云、火山方舟 |
| 我想用 Cherry Studio / Chatbox 这类壳子玩 DeepSeek | 拿 API Key + 填 Base URL | 见[第四节](#四拿到-key-之后装哪个壳子) |
| 我不想实名、不想绑卡 | 只选这几家 | DeepSeek 官方、腾讯元宝、TRAE、Qoder CN、OpenRouter、NVIDIA NIM |

---

## 一、带客户端、开箱即用的（不用碰 Key）

### 1.1 聊天 / 干活：装完登录就能用

| 客户端 | 白拿到什么 | 有 DeepSeek 吗 | 说明 |
|---|---|---|---|
| **DeepSeek 手机 App** | 不限量（有频率限制） | 就是它本体 | iOS / Android，功能与网页版一致，**完全免费**，不用实名 |
| **DeepSeek 网页版** | 不限量（有频率限制） | 就是它本体 | 浏览器直接开，最省事的一条路 |
| **DeepSeek Harness 桌面端** | 6 元赠金（到账 7 天过期） | V4.1-Flash / V4-Pro | 注意它**不是聊天窗口**，是 Agent 工作台，能读本地文件、跑定时任务 |
| **腾讯元宝**（App / 网页） | 不限量（有频率限制） | 混元 Hy3/Hy4 + DeepSeek 可切 | 不用实名；缺点是纯对话，接不了工作流 |
| **通义千问 App / 网页** | 不限量（有频率限制） | 否（Qwen 系） | 日常问答够用，多模态也能打 |
| **豆包电脑端** | 每天约 200 额度（周一翻倍） | 否（豆包 Seed 系） | 签到在客户端里，顺手点一下 |
| **超算互联网客户端（SClaw）** | 活动期内旗舰模型**不限量** + 1 亿词元智能体额度 | 有（DS-V4.1） | **11-30 截止**；「不限量」只在自家客户端里，不能当 API 用 |
| **蛙池 AI 桌面端** | 2200 蛙蛙币（约 220 元） | V4-Pro / Flash | 需要内测邀请码；Windows / macOS 双端，偏渗透场景 |
| **WorkBuddy** | 每天 100 积分（连签 7 天再送 1000） | 可在模型里选 | 通用 Agent 桌面端，积分制 |

### 1.2 写代码：IDE 里直接带模型，不用配 Key

| 客户端 | 白拿到什么 | 模型 | 说明 |
|---|---|---|---|
| **TRAE 国内版** | 每月 500 积分 + 2 个云端任务并发 | 豆包 Seed 2.1 / **DeepSeek-V4.1** / GLM-5.3 / Kimi / MiniMax 可切 | 国内版 trae.cn 与国际版 trae.ai 是两套独立计费，别混着看 |
| **Qoder CN**（原通义灵码） | 补全与问答不限次 + 编程智能体 50 轮/月 | Qwen 为主，可切 GLM / **DeepSeek** / Kimi | 2026-05-20 已更名，「个人专业版限时免费」同日结束 |
| **腾讯 CodeBuddy 体验版** | 每月 500 积分 + 无限补全 | 内置多模型 | VS Code / JetBrains 插件 |
| **文心快码 Comate 个人标准版** | 免费 + ¥10 体验金 | 文心系 + **DeepSeek** | 个人版免费是长期政策 |
| **GitHub Copilot Free** | 每月 2000 次补全 + 50 次 Chat | GPT / Claude 系 | 不需要付费，但国内网络要自己解决 |
| **Cursor Hobby** | 每月 2000 次补全 + 50 次慢请求 | 多模型 | 慢请求排队明显 |
| **Google Antigravity** | 每周配额（官方未公示数字） | Gemini / Claude Sonnet 4.6 | 免费预览期，配额够玩不够跑量 |

> 一句话挑：**就想聊天 → DeepSeek App；想白用 DeepSeek 写代码 → TRAE 国内版；想要长上下文又不想实名 → 元宝切 DeepSeek。**

---

## 二、先认清一件事：「客户端内不限量」不等于 API

超算互联网的「旗舰模型不限量」、WorkBuddy 的积分、蛙池的蛙蛙币，都是**锁在自家壳子里**的额度。你可以拿它干活，但不能把它抽出来接自己的程序。

**判断方法只有一条：能不能拿到 `sk-` 开头的 Key。** 能拿到才是 API，拿不到就只是「一个免费好用的软件」。

---

## 三、只给 API 的：想要 DeepSeek 就走这几家

按「拿到手快不快」排的，不是按额度大小排。

### 3.1 国内

| 平台 | 免费额度 | 门槛 | 有效期 | 备注 |
|---|---|---|---|---|
| **硅基流动** | 2000 万 Token（约 14 元） | 实名 | 一次性 | 上手最快，OpenAI 兼容，微信/支付宝都能绑；新手任务还有一笔 |
| **七牛云 AI 推理** | 300 万 Token | 实名 | **2 年** | 一个 Key 通吃 50+ 模型，OpenAI / Anthropic 双协议，少见的慢过期额度 |
| **火山方舟** | 每模型 50 万 Token（累计 2500 万+）；11.11 活动每天 2000 万+ | 实名 | 一次性 / 每日刷新 | 每个模型要**单独点开通**才拿得满；先开「安心体验模式」防扣费 |
| **阿里云百炼** | 每模型 100 万（合计约 8000 万） | 实名 | 90 天 | 只在**华北2（北京）**发；每个模型额度独立，用完不会自动切 |
| **百度千帆** | 每模型 100 万 | 实名 | 一次性 | 第三方模型（DeepSeek-V3/R1、Qwen）也在同一个池子里 |
| **腾讯云 TokenHub** | 每模型 100 万 | 实名 | **1 年** | 额度耗尽默认**不**转后付费，安全 |
| **商汤日日新** | 5 小时 12 万积分 + 每周 120 万积分 | 实名 | 窗口刷新 | 含 DeepSeek-V4-Flash；多模态（OCR、识图）免费额度里最好用 |
| **国家超算互联网 MaaS** | 1000 万 Token（新客） | 实名 | 30 天 | 兼容 OpenAI 与 Anthropic，base_url 是 `https://api.scnet.cn/api/llm/v1` |
| **DeepSeek 官方开放平台** | 100 万 ~ 500 万 Token（口径不一） | 实名 | 30 天 | 官方单价本来就是全网最低之一，百万 Token 几毛钱，不必太纠结 |

### 3.2 海外（需要自备网络环境）

| 平台 | 免费额度 | 门槛 | 备注 |
|---|---|---|---|
| **NVIDIA NIM** | 1000 credits（约 40 RPM） | 免实名，**+86 手机号可注册** | 2026-11 新开的大额口子，Location 选 China；Key 默认 12 个月有效，只显示一次 |
| **OpenRouter** | 50 请求/天（20 RPM） | 免实名 | 20+ 免费模型，免费模型名带 `:free`；常被上游限流 |
| **Groq** | 每日免费额度 | 免实名 | 速度最快，模型偏开源系 |
| **Cerebras** | 每日免费额度 | 免实名 | 同样是速度牌 |
| **SambaNova** | 每天 20 万 Token | **要绑卡** | 不想留卡信息就跳过 |
| ~~Hugging Face~~ | 约 $0.10/月 | 免实名 | **反例**：两次真实请求就见底，别当方案 |

---

## 四、拿到 Key 之后，装哪个壳子

API 只有接口，聊天窗口得自己配。下面几个是全平台、免费、填三项就能跑：

| 客户端 | 平台 | 适合谁 |
|---|---|---|
| **Cherry Studio** | Win / macOS / Linux | 最推荐。多模型并排、知识库、MCP、提示词库都有，中文界面 |
| **Chatbox** | Win / macOS / Linux / **手机** | 更轻，只想要个干净对话框的选它 |
| **Open WebUI** | 自建（Docker） | 团队共用、要给同事开账号 |
| **LobeChat** | Web / 自建 | 界面最像 ChatGPT，插件生态好 |
| **NextChat** | 单文件 / 自建 | 部署最省事，丢一个文件就能跑 |

**配置就三步**：Base URL → API Key → 模型名。各家 base_url 已经在 [`docs/api-examples.md`](api-examples.md) 里列好了，照抄即可。

几个常见填法：

| 你想用 | Base URL | 模型名 |
|---|---|---|
| DeepSeek 官方 | `https://api.deepseek.com/v1` | `deepseek-chat` |
| 硅基流动 | `https://api.siliconflow.cn/v1` | `deepseek-ai/DeepSeek-V3` |
| 阿里云百炼 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `deepseek-v3` |
| 火山方舟 | `https://ark.cn-beijing.volces.com/api/v3` | **接入点 ID**（`ep-xxxx`），不是模型名 |
| OpenRouter | `https://openrouter.ai/api/v1` | `deepseek/deepseek-chat-v3:free` |
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | `deepseek-ai/deepseek-v4.1-flash` |

---

## 五、三个最容易踩的坑

1. **「不限量」基本都在客户端里。** 想要 API 的不限量，只有硅基流动小模型免费档、百度千帆 ERNIE-Speed、七牛云 Conatus 每日额度这几家，而且都限速。
2. **赠金是会过期的。** 超算互联网 30 天、百炼 90 天、DeepSeek Harness 只有 7 天。先领近期要用的，别当存款囤。
3. **Key 别写进前端和公开仓库。** 放进环境变量，`.env` 记得进 `.gitignore`；免费 Key 被人刷爆，账号是要连带处理的。

---

> 所有额度以各平台官方页面为准，本页只是选型索引。完整清单见[项目 README](../README.md)，逐条领取步骤见 [`docs/claim-guide.md`](claim-guide.md)。
