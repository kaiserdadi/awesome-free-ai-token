# 调用示例：同一段代码打十家

国内主流平台基本都兼容 OpenAI 协议，**换个 `base_url` 和 `model` 就能跑**。下面这份表可以直接改配置用。

## Base URL 速查

| 平台 | base_url | 备注 |
|---|---|---|
| 智谱 GLM | `https://open.bigmodel.cn/api/paas/v4` | OpenAI 兼容 |
| 硅基流动 | `https://api.siliconflow.cn/v1` | |
| 阿里云百炼 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | 一定要带 `/compatible-mode` |
| 火山方舟 | `https://ark.cn-beijing.volces.com/api/v3` | model 要填「接入点 ID」而非模型名 |
| DeepSeek | `https://api.deepseek.com/v1` | |
| Kimi | `https://api.moonshot.cn/v1` | |
| 阶跃星辰 | `https://api.stepfun.com/v1` | **Step Plan 赠送额度必须用** `https://api.stepfun.com/step_plan/v1` |
| 蚂蚁百灵 | `https://api.ant-ling.com/v1` | 同时兼容 Anthropic Messages API |
| 七牛云 | 见[控制台](https://www.qiniu.com/ai/models) | 双协议，一个 Key 通吃 |
| 商汤日日新 | 见[Token Plan 文档](https://platform.sensenova.cn/token-plan) | OpenAI 兼容 |
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | |
| Groq | `https://api.groq.com/openai/v1` | |
| Cerebras | `https://api.cerebras.ai/v1` | |
| OpenRouter | `https://openrouter.ai/api/v1` | 免费模型名带 `:free` |
| Mistral | `https://api.mistral.ai/v1` | |
| Gemini | `https://generativelanguage.googleapis.com/v1beta/openai/` | OpenAI 兼容端点 |

> 火山方舟的坑最多：`model` 要填你在控制台创建的**接入点 ID**（形如 `ep-2024xxxx-xxxxx`），直接写 `doubao-pro-32k` 会报错。

## curl

```bash
curl https://open.bigmodel.cn/api/paas/v4/chat/completions \
  -H "Authorization: Bearer $ZHIPU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-4.7-flash",
    "messages": [{"role": "user", "content": "用三句话解释什么是 MoE 架构"}]
  }'
```

## Python：一家跑通，十家轮流跑

```python
import os
import time
from openai import OpenAI

# 换成你领到的平台；key 从环境变量读，别写死在代码里
PROVIDERS = {
    "zhipu":      ("https://open.bigmodel.cn/api/paas/v4", "glm-4.7-flash",      "ZHIPU_API_KEY"),
    "siliconflow":("https://api.siliconflow.cn/v1",         "Qwen/Qwen3-8B",     "SILICONFLOW_API_KEY"),
    "groq":       ("https://api.groq.com/openai/v1",        "gpt-oss-120b",      "GROQ_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1",          "deepseek/deepseek-chat-v3:free", "OPENROUTER_API_KEY"),
    "nim":        ("https://integrate.api.nvidia.com/v1",   "deepseek-ai/deepseek-v4.1-flash", "NVIDIA_API_KEY"),
}

PROMPT = "用一句话说明：为什么免费额度要做分层使用？"

for name, (base, model, env) in PROVIDERS.items():
    key = os.getenv(env)
    if not key:
        print(f"{name:<12} 跳过（没设 {env}）")
        continue
    client = OpenAI(base_url=base, api_key=key)
    t0 = time.time()
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": PROMPT}],
            max_tokens=200,
        )
        cost = time.time() - t0
        usage = r.usage
        print(f"{name:<12} {cost:5.2f}s  in={usage.prompt_tokens:<6} out={usage.completion_tokens:<6}")
        print(f"             {r.choices[0].message.content[:80]}...")
    except Exception as e:
        print(f"{name:<12} 失败：{type(e).__name__}: {e}")
```

跑之前：

```bash
pip install openai
export ZHIPU_API_KEY=xxx
export GROQ_API_KEY=xxx
python3 compare.py
```

## 检查一个 Key 到底还能不能用

配额被悄悄清空是常事。这个最小探针能同时验证「Key 有效 + 模型可用 + 还有余额」：

```python
from openai import OpenAI

client = OpenAI(base_url="https://open.bigmodel.cn/api/paas/v4", api_key="你的key")
try:
    r = client.chat.completions.create(
        model="glm-4.7-flash",
        messages=[{"role": "user", "content": "hi"}],
        max_tokens=1,
    )
    print("✅ 可用")
except Exception as e:
    msg = str(e)
    if "401" in msg or "invalid" in msg.lower():
        print("❌ Key 无效或已吊销")
    elif "402" in msg or "quota" in msg.lower() or "balance" in msg.lower():
        print("⚠️ Key 有效，但额度用完了")
    elif "429" in msg:
        print("⚠️ 被限流了（不是没额度，是请求太快）")
    else:
        print("？未知错误：", msg[:200])
```

`max_tokens=1` 是关键——花最少的量，拿到最明确的状态。

## 用 Claude Code 路由到免费后端

Claude Code 认 `ANTHROPIC_BASE_URL`。指向兼容 Anthropic 协议的免费端点，就能用它的 Agent 外壳跑别家的免费模型：

```bash
export ANTHROPIC_BASE_URL=https://api.ant-ling.com   # 举例：蚂蚁百灵兼容 Anthropic 协议
export ANTHROPIC_AUTH_TOKEN=你的key
claude
```

> 非官方玩法，随时可能失效，也可能违反服务条款。自己权衡，别用在生产上。
