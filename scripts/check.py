#!/usr/bin/env python3
"""体检脚本：找出已过期、快过期、久未复核的条目。

用法：
    python3 scripts/check.py                # 打印报告
    python3 scripts/check.py --days 7       # 自定义「快到期」窗口
    python3 scripts/check.py --report X.md  # 同时写一份 markdown
    python3 scripts/check.py --strict       # 有已过期条目时退出码 1（CI 用）

设计取向：默认退出码 0。过期是常态不是错误，报出来就行；
要不要把它当红线，由调用方用 --strict 决定。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os

import _data

STALE_DAYS = 60


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14, help="几天内到期算「快过期」")
    ap.add_argument("--report", default="", help="markdown 报告输出路径")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出")
    ap.add_argument("--strict", action="store_true", help="有已过期条目时退出码为 1")
    args = ap.parse_args()

    today = dt.date.today()
    items = _data.load()
    problems = _data.validate(items)

    buckets: dict[str, list[dict]] = {"expired": [], "expiring": [], "stale": [], "long": [], "unknown": []}
    for it in items:
        st = _data.status(it, today, args.days)
        if st == "long":
            buckets["long"].append(it)
        elif st == "unknown":
            buckets["unknown"].append(it)
        elif st in ("expired", "expiring"):
            buckets[st].append(it)
        v = _data.parse_date(it.get("verified", ""))
        if v and (today - v).days > STALE_DAYS:
            buckets["stale"].append(it)

    for key in ("expired", "expiring"):
        buckets[key].sort(key=lambda i: i.get("expiry", "9999"))

    if args.json:
        print(
            json.dumps(
                {
                    "date": today.isoformat(),
                    "total": len(items),
                    "problems": problems,
                    **{k: [i["id"] for i in v] for k, v in buckets.items()},
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    lines: list[str] = []
    lines.append(f"# 免费额度体检报告 · {today.isoformat()}")
    lines.append("")
    lines.append(f"共 {len({i['product'] for i in items})} 家平台 / {len(items)} 个入口 ｜ "
                 f"已过期 {len(buckets['expired'])} ｜ "
                 f"{args.days} 天内到期 {len(buckets['expiring'])} ｜ "
                 f"超 {STALE_DAYS} 天未复核 {len(buckets['stale'])} ｜ "
                 f"长期 {len(buckets['long'])} ｜ 未公布期限 {len(buckets['unknown'])}")
    lines.append("")

    if problems:
        lines.append("## 数据格式问题")
        lines.append("")
        for p in problems:
            lines.append(f"- {p}")
        lines.append("")

    if buckets["expired"]:
        lines.append("## 已过期（建议下架，或确认活动是否延期）")
        lines.append("")
        lines.append("| 平台 | 截止 | 距今 | id |")
        lines.append("|---|---|---|---|")
        for it in buckets["expired"]:
            d = _data.parse_date(it.get("expiry", ""))
            lines.append(f"| {it['name']} | {it['expiry']} | 过期 {(today - d).days} 天 | `{it['id']}` |")
        lines.append("")

    if buckets["expiring"]:
        lines.append(f"## {args.days} 天内到期（抓紧领 / 或准备改状态）")
        lines.append("")
        lines.append("| 平台 | 截止 | 剩余 | id |")
        lines.append("|---|---|---|---|")
        for it in buckets["expiring"]:
            d = _data.parse_date(it.get("expiry", ""))
            lines.append(f"| {it['name']} | {it['expiry']} | {(d - today).days} 天 | `{it['id']}` |")
        lines.append("")

    if buckets["stale"]:
        lines.append(f"## 超过 {STALE_DAYS} 天未复核（去官网看一眼还在不在）")
        lines.append("")
        for it in buckets["stale"][:25]:
            lines.append(f"- {it['name']}（verified {it['verified']}，`{it['id']}`）")
        if len(buckets["stale"]) > 25:
            lines.append(f"- …另有 {len(buckets['stale']) - 25} 条")
        lines.append("")

    text = "\n".join(lines)
    print(text)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        print(f"\n（已写入 {args.report}）", flush=True)

    if args.strict and (buckets["expired"] or problems):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
