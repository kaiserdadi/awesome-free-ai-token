"""极简数据加载器：不依赖 PyYAML，零第三方包。

数据格式是 YAML 的一个扁平子集（每项一组 `key: value`），
好处是 PR 时人眼可读、diff 干净、CI 不需要装依赖。
"""

from __future__ import annotations

import datetime as dt
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, "data", "providers.yaml")

REQUIRED = ("id", "product", "form", "name", "region", "type", "offer", "value", "expiry", "url", "source", "verified", "confidence")
VALID_REGION = {"cn", "global"}
VALID_TYPE = {"daily", "signup", "promo", "free_model"}
VALID_CONF = {"high", "medium", "low"}
VALID_FORM = {"web", "app", "desktop", "api", "ide", "cli"}


def load(path: str = DATA_FILE) -> list[dict]:
    items: list[dict] = []
    cur: dict | None = None
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("- "):
                if cur is not None:
                    items.append(cur)
                cur = {}
                stripped = stripped[2:]
            if cur is None:
                raise ValueError(f"{path}:{lineno} 数据必须以 '- ' 开头的条目起始")
            key, sep, val = stripped.partition(":")
            if not sep:
                raise ValueError(f"{path}:{lineno} 缺少冒号：{stripped!r}")
            cur[key.strip()] = val.strip()
    if cur is not None:
        items.append(cur)

    for it in items:
        it.setdefault("tags", "")
        it.setdefault("notes", "")
        it.setdefault("billing", "")
        for k in ("realname", "card"):
            it.setdefault(k, "no")
        it.setdefault("difficulty", "3")
        it.setdefault("models", "")
        it.setdefault("reset", "unknown")
    return items


def parse_date(value: str) -> dt.date | None:
    """把 expiry 解析成日期；long/unknown 等返回 None。"""
    value = (value or "").strip()
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def status(item: dict, today: dt.date, soon_days: int = 14) -> str:
    """返回 expired / expiring / ok / long / unknown"""
    raw = (item.get("expiry") or "").strip().lower()
    if raw in ("long", "permanent"):
        return "long"
    d = parse_date(item.get("expiry", ""))
    if d is None:
        return "unknown"
    if d < today:
        return "expired"
    if (d - today).days <= soon_days:
        return "expiring"
    return "ok"


def validate(items: list[dict]) -> list[str]:
    """返回问题列表；空列表表示通过。CI 里跑这个。"""
    problems: list[str] = []
    seen: set[str] = set()
    for i, it in enumerate(items, 1):
        ident = it.get("id") or f"#{i}"
        for key in REQUIRED:
            if not it.get(key):
                problems.append(f"[{ident}] 缺少必填字段 {key}")
        if it.get("id") in seen:
            problems.append(f"[{ident}] id 重复")
        seen.add(it.get("id", ""))
        if it.get("region") not in VALID_REGION:
            problems.append(f"[{ident}] region 非法：{it.get('region')}")
        if it.get("type") not in VALID_TYPE:
            problems.append(f"[{ident}] type 非法：{it.get('type')}")
        if it.get("form") not in VALID_FORM:
            problems.append(f"[{ident}] form 非法：{it.get('form')}（可选 web/app/desktop/api/ide/cli）")
        prod = it.get("product", "")
        if prod != prod.strip():
            problems.append(f"[{ident}] product 前后有空格")
        if not it.get("billing"):
            problems.append(f"[{ident}] 缺少 billing（计费方式）")
        if it.get("confidence") not in VALID_CONF:
            problems.append(f"[{ident}] confidence 非法：{it.get('confidence')}")
        for key in ("url", "source"):
            v = it.get(key, "")
            if v and not v.startswith("http"):
                problems.append(f"[{ident}] {key} 不是 http(s) 链接：{v}")
        if it.get("verified") and parse_date(it.get("verified", "")) is None:
            problems.append(f"[{ident}] verified 必须是 YYYY-MM-DD")
        if it.get("expiry", "").lower() not in ("long", "permanent", "unknown") and parse_date(it.get("expiry", "")) is None:
            problems.append(f"[{ident}] expiry 必须是 YYYY-MM-DD 或 long/unknown：{it.get('expiry')}")
        diff = it.get("difficulty", "3")
        if not (diff.isdigit() and 1 <= int(diff) <= 5):
            problems.append(f"[{ident}] difficulty 必须是 1-5")
    return problems


if __name__ == "__main__":
    data = load()
    errs = validate(data)
    print(f"条目数：{len(data)}")
    for e in errs:
        print("  !", e)
    sys.exit(1 if errs else 0)
