#!/usr/bin/env python3
"""从 data/providers.yaml 渲染 README 的自动区块。

用法：
    python3 scripts/render.py            # 写回 README.md
    python3 scripts/render.py --stdout   # 只打印，不写文件
"""

from __future__ import annotations

import datetime as dt
import os
import sys

import _data

BEGIN = "<!-- AUTO:START 由 scripts/render.py 生成，不要手改这一段 -->"
END = "<!-- AUTO:END -->"

GROUP_TITLES = {
    "promo": ("限时活动", "有明确截止日，先领再说。按剩余天数从少到多排。"),
    "daily": ("每日 / 每月续杯", "签一次到、点一次领取，就能反复拿。适合当日常主力。"),
    "signup": ("注册 / 实名一次性", "开号就发，一辈子一次。国内优先，上手成本从低到高。"),
    "free_model": ("长期 0 元模型", "价目表上就是 0 元，不靠活动。最适合当兜底。"),
}

DIFF = {"1": "★", "2": "★★", "3": "★★★", "4": "★★★★", "5": "★★★★★"}
CONF = {"high": "高", "medium": "中", "low": "低"}


def esc(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def fmt_expiry(item: dict, today: dt.date) -> str:
    raw = (item.get("expiry") or "").strip()
    if raw.lower() in ("long", "permanent"):
        return "长期"
    d = _data.parse_date(raw)
    if d is None:
        return "未公布"
    delta = (d - today).days
    if delta < 0:
        return f"**{raw} 已过期**"
    if delta <= 14:
        return f"**{raw}（剩 {delta} 天）**"
    return f"{raw}（剩 {delta} 天）"


def fmt_gate(item: dict) -> str:
    bits = []
    if item.get("realname") == "yes":
        bits.append("实名")
    if item.get("card") == "yes":
        bits.append("绑卡")
    return " · ".join(bits) if bits else "无"


def sort_key(item: dict, kind: str):
    today = dt.date.today()
    if kind == "promo":
        d = _data.parse_date(item.get("expiry", ""))
        return (d is None, d or dt.date.max, int(item.get("difficulty", "3")))
    if kind == "signup":
        return (0 if item.get("region") == "cn" else 1, int(item.get("difficulty", "3")))
    if kind == "daily":
        return (0 if item.get("region") == "cn" else 1, int(item.get("difficulty", "3")))
    return (0 if item.get("region") == "cn" else 1, int(item.get("difficulty", "3")))


def table(items: list[dict], today: dt.date) -> str:
    head = "| 平台 | 白拿什么 | 额度 | 到期 | 门槛 | 可信 |\n|---|---|---|---|---|---|"
    rows = []
    for it in items:
        name = esc(it["name"])
        if it.get("region") == "global":
            name = f"{name} 🌐"
        rows.append(
            "| [{n}]({u}) | {o} | {v} | {e} | {g} | {c} |".format(
                n=name,
                u=it["url"],
                o=esc(it["offer"]),
                v=esc(it["value"]),
                e=fmt_expiry(it, today),
                g=fmt_gate(it),
                c=CONF.get(it["confidence"], "?"),
            )
        )
    return head + "\n" + "\n".join(rows)


def build(items: list[dict]) -> str:
    today = dt.date.today()
    cn = sum(1 for i in items if i["region"] == "cn")
    gl = len(items) - cn
    by_type = {k: [i for i in items if i["type"] == k] for k in GROUP_TITLES}
    soon = [
        i
        for i in items
        if _data.status(i, today, 14) in ("expiring", "expired")
    ]
    expired = [i for i in items if _data.status(i, today, 14) == "expired"]
    last_verified = max(i["verified"] for i in items if i.get("verified"))

    out: list[str] = []
    out.append(BEGIN)
    out.append("")
    out.append(
        f"> 数据截至 **{last_verified}** ｜ 共 **{len(items)}** 条（国内 {cn} · 海外 {gl}）"
        f" ｜ 每日/每月续杯 {len(by_type['daily'])} 条"
        f" ｜ 限时活动 {len(by_type['promo'])} 条（**{len(soon)} 条 14 天内到期或已过期**）"
    )
    out.append("")
    out.append("| 分类 | 条数 | 一句话 |")
    out.append("|---|---|---|")
    out.append(f"| 限时活动 | {len(by_type['promo'])} | 抢时间，先领后看 |")
    out.append(f"| 每日续杯 | {len(by_type['daily'])} | 攒出来的额度最耐用 |")
    out.append(f"| 注册一次性 | {len(by_type['signup'])} | 一次给一大笔 |")
    out.append(f"| 长期免费模型 | {len(by_type['free_model'])} | 兜底，不依赖活动 |")
    out.append("")

    if expired:
        names = "、".join(i["name"] for i in expired)
        out.append(f"⚠️ **已过期需下架**：{names} —— 请提交 PR 修正，或跑 `python3 scripts/check.py`。")
        out.append("")

    for kind, (title, desc) in GROUP_TITLES.items():
        group = by_type[kind]
        if not group:
            continue
        out.append(f"### {title}")
        out.append("")
        out.append(f"*{desc}*")
        out.append("")
        out.append(table(sorted(group, key=lambda x: sort_key(x, kind)), today))
        out.append("")

    out.append("> 🌐 = 海外平台，通常需要自备网络环境。门槛列只写「注册时要过什么关」，"
               "实际折腾程度另见 `data/providers.yaml` 的 `difficulty` 字段（1 最省事，5 最费劲）。")
    out.append(">")
    out.append("> 到期列的「长期」指额度不过期或活动无固定截止日；「未公布」指官方没写死，"
               "随时可能停——两类都不代表可以放心囤。")
    out.append("")
    out.append(END)
    return "\n".join(out)


def main() -> int:
    to_stdout = "--stdout" in sys.argv
    items = _data.load()
    problems = _data.validate(items)
    if problems:
        print("数据校验未通过：", file=sys.stderr)
        for p in problems:
            print("  !", p, file=sys.stderr)
        return 1

    block = build(items)
    if to_stdout:
        print(block)
        return 0

    readme_path = os.path.join(_data.ROOT, "README.md")
    with open(readme_path, encoding="utf-8") as fh:
        text = fh.read()
    if BEGIN not in text or END not in text:
        print("README.md 里找不到 AUTO 标记，未写入。", file=sys.stderr)
        return 1
    head, _, rest = text.partition(BEGIN)
    _, _, tail = rest.partition(END)
    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write(head + block + tail)
    print(f"已更新 README.md：{len(items)} 条")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
