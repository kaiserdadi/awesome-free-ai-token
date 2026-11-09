# 数据字段说明

所有条目都在 [`../data/providers.yaml`](../data/providers.yaml)。格式是 YAML 的一个扁平子集，方便 diff 和人工 review，脚本解析不依赖任何第三方库。

## 一条长这样

```yaml
- id: deepseek-harness
  product: DeepSeek
  form: desktop
  name: DeepSeek Harness 桌面端
  region: cn
  type: signup
  offer: 下载 Windows / macOS 安装包，首次登录送 6 元赠金，无需充值
  models: DeepSeek-V4.1-Flash、V4-Pro
  value: 6 元赠金（限量，到账后 7 天有效）
  billing: 赠金 + 按 Token
  expiry: unknown
  reset: once
  realname: yes
  card: no
  difficulty: 2
  url: https://www.deepseek.com
  source: https://www.chinatimes.com/cn/realtimenews/20261018000828-260409
  verified: 2026-11-09
  confidence: high
  notes: 6 元赠金看着少，但 Flash 空闲时段输入只要 1.5 元/百万 Token。
```

## 字段

| 字段 | 必填 | 取值 | 说明 |
|---|---|---|---|
| `id` | ✅ | 小写短横线 | 全局唯一，改动会影响外链，尽量别重命名 |
| `product` | ✅ | 品牌名 | 产品线，用于按产品聚合。**同一产品必须写得一字不差**（如 `DeepSeek`、`WorkBuddy`） |
| `form` | ✅ | `web`/`app`/`desktop`/`api`/`ide`/`cli` | 这是产品的哪个入口，见下 |
| `name` | ✅ | 文本 | 平台名。国内用官方全称，海外用英文名 |
| `region` | ✅ | `cn` / `global` | 中国大陆 / 海外。海外在表格里会带 🌐 |
| `type` | ✅ | `promo` / `daily` / `signup` / `free_model` | 决定进哪张表，见下 |
| `offer` | ✅ | 一句话 | **怎么领**。写清入口路径，别只写「注册送」 |
| `models` | | 文本 | 能白嫖哪些模型。不填表示平台全系 |
| `value` | ✅ | 文本 | **给多少**。写成人能直接比较的量级 |
| `billing` | ✅ | 短语 | 计费方式：`完全免费` / `按 Token` / `积分制` / `订阅制` / `免费算力`。用于产品视图横向对比 |
| `expiry` | ✅ | `YYYY-MM-DD` / `long` / `unknown` | `long` = 额度不过期或无固定截止日；`unknown` = 官方没写死 |
| `reset` | | `daily` / `monthly` / `once` / `window` / `unknown` | 额度刷新节奏。`window` 指按小时窗口滚动（如「5 小时内 N 次」） |
| `realname` | | `yes` / `no` | 是否要实名认证 |
| `card` | | `yes` / `no` | 是否要绑信用卡 |
| `difficulty` | | `1`–`5` | 上手成本。1 = 打开网页点两下；5 = 要绑卡 + 填表 + 等审核 |
| `url` | ✅ | https 链接 | 领取入口 |
| `source` | ✅ | https 链接 | **你从哪看到的**。官方页面优先，其次新闻稿/文档 |
| `verified` | ✅ | `YYYY-MM-DD` | 你最后一次确认它还活着的日期 |
| `confidence` | ✅ | `high` / `medium` / `low` | 见下表 |
| `notes` | | 一段话 | 坑在哪、怎么用最划算。**这栏是整条数据里最值钱的** |

## 为什么要把 product 和 form 分开

因为同一个产品，换个入口，收费方式常常是两回事：

| 产品 | 形态 | 收费方式 |
|---|---|---|
| DeepSeek | 网页版 / App | 完全免费，不限量 |
| DeepSeek | 桌面端 Harness | 首登送 6 元赠金，之后按 Token 扣 |
| DeepSeek | API | 纯付费，Flash 输入 ¥1.5/百万（空闲时段） |

不分层的后果很具体：读者看到「DeepSeek 按 Token 收费」，以为这整个产品要花钱，其实他平时用的网页版一分不收。

规则：

- **一条记录只描述「一个产品的一个入口」**；
- 同一产品有多个入口时写多条，`product` 字段必须一字不差，渲染时会自动聚成一组并用 `↳` 串起来；
- `form` 只填那六个值，不要自创（`浏览器插件` 目前归到 `web`，等真有必要再加枚举）。

## type 怎么选

| 取值 | 含义 | 典型例子 |
|---|---|---|
| `promo` | 限时活动，有明确截止日 | 超算互联网双 11、蚂蚁百灵上线两周免费 |
| `daily` | 每天/每月可反复领，续杯型 | WorkBuddy 加油站、Qoder 每日 Credits、商汤滚动窗口 |
| `signup` | 注册/实名一次性发放 | 智谱 2000 万、百炼 7000 万、TokenHub 每模型 100 万 |
| `free_model` | 模型在价目表上就是 0 元，不靠活动 | GLM-4.7-Flash、Gemini Flash 免费层、9B 以下小模型 |

## confidence 怎么定

| 级别 | 判定标准 |
|---|---|
| `high` | 官方页面、官方文档、官方新闻稿里能直接读到这个数 |
| `medium` | 媒体报道或二手整理，但至少两个独立来源口径一致 |
| `low` | 单一来源，或来源本身对时效有争议。**收录但不背书** |

## 几个约定

- **不写「约」字的地方就要精确**。额度写不准比不写更糟——用户会按错的数量做规划。
- **来源冲突就写进 `notes`**，不要选一个看起来顺眼的悄悄扔掉。冲突本身是信息。
- **`verified` 必须是你自己打开页面看到的日期**，不是抄来源的发布日期。
- **过期不删条目**，让 `check.py` 报出来，读者能看到「这条曾经有过、现在没了」，比凭空消失更有用。
