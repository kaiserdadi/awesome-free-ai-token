#!/usr/bin/env python3
"""把 data/providers.yaml 编译成一个自包含的单文件网页 site/index.html。

零依赖、零外链、双击即用。数据以 JSON 内联，改完数据重跑本脚本即可。

用法：
    python3 scripts/build_site.py
"""

from __future__ import annotations

import base64
import datetime as dt
import json
import os
import sys

import _data

OUT_DIR = os.path.join(_data.ROOT, "site")
OUT_FILE = os.path.join(OUT_DIR, "index.html")
QR_FILE = os.path.join(_data.ROOT, "assets", "qq-group.png")
QQ_GROUP = "2154085627"
QQ_NAME = "新时代领鸡蛋 token"

# 炫酷变体（--cool）：把「旋转描边」做成全站的边框语言。
# 只加样式，不动结构与数据，原版 index.html 不受影响。
COOL_CSS = r"""
@property --ang{syntax:"<angle>";initial-value:0deg;inherits:false}
@keyframes angspin{to{--ang:360deg}}
@keyframes flowslide{to{background-position:200% 0}}

body{
  background:
    radial-gradient(1100px 520px at 72% -12%, #fdf0e0 0%, rgba(253,240,224,0) 62%),
    var(--bg);
}
@supports (background-attachment:fixed){
  body{background-attachment:fixed}
}

.top::after{
  content:""; position:absolute; left:0; right:0; bottom:-1px; height:1.5px;
  pointer-events:none; background-size:200% 100%;
  background-image:linear-gradient(90deg,rgba(180,83,10,0) 0%,#b4530a 16%,#ffc38a 32%,#b4530a 48%,rgba(180,83,10,0) 64%);
  animation:flowslide 7s linear infinite;
}

.tab{border:1px solid transparent}
.tab[aria-selected="true"]{
  background:
    linear-gradient(var(--panel),var(--panel)) padding-box,
    conic-gradient(from var(--ang),#b4530a,#ffc38a 22%,#b4530a 45%,#f0a15c 68%,#b4530a) border-box;
  animation:angspin 3.6s linear infinite;
}

.card{
  border:1.5px solid transparent !important;
  background:
    linear-gradient(var(--panel),var(--panel)) padding-box,
    conic-gradient(from var(--ang),#f7ecdb 0deg,#eed6ae 60deg,#cf7a25 128deg,#ffb373 172deg,#eed6ae 236deg,#f7ecdb 360deg) border-box;
}
.card::after{
  content:""; position:absolute; left:14px; right:14px; top:0; height:2px; border-radius:0 0 2px 2px;
  background-image:linear-gradient(90deg,rgba(180,83,10,0),#b4530a 12%,#ff9d4d 50%,#b4530a 88%,rgba(180,83,10,0));
  background-size:200% 100%; opacity:.8; transition:opacity .25s; pointer-events:none;
}
.card:hover::after{opacity:1; animation:flowslide 2.6s linear infinite}
.card:hover{
  animation:angspin 2.6s linear infinite;
  box-shadow:0 1px 2px rgba(27,24,21,.04), 0 14px 34px -18px rgba(180,83,10,.45);
}

.lede{
  border:1px solid transparent !important;
  background:
    linear-gradient(180deg,#fffdfa,#fdf8f0) padding-box,
    conic-gradient(from var(--ang),#f2ddc4 0deg,#e9c9a2 70deg,#c8762a 130deg,#ffcf9c 170deg,#e9c9a2 240deg,#f2ddc4 360deg) border-box;
  animation:angspin 9s linear infinite;
}

.qrimg{
  border:1px solid transparent !important;
  background:
    linear-gradient(#fff,#fff) padding-box,
    conic-gradient(from var(--ang),#e8dccb,#cf8a45 42%,#f7d3a6 58%,#e8dccb) border-box;
  animation:angspin 8s linear infinite;
}

.sectionhead h2::before{background:linear-gradient(180deg,#b4530a,#e2a463)}
.sectionhead.soon h2::before{background:linear-gradient(180deg,#b3352a,#e08a80)}

.stat b{
  background:linear-gradient(165deg,#8a3f06,#c8661a 58%,#e0973f);
  -webkit-background-clip:text; background-clip:text; color:transparent;
}

.qcopy{
  border:1px solid transparent !important; color:var(--copper);
  background:
    linear-gradient(var(--panel),var(--panel)) padding-box,
    conic-gradient(from var(--ang),#b4530a,#ffd0a3 24%,#b4530a 48%,#f0a15c 72%,#b4530a) border-box;
  animation:angspin 3s linear infinite;
}
.qcopy:hover{color:#8a3f06}
.qcopy.done{
  animation:none; color:#4d7a41; border-color:#7a9e6f !important;
  background:#f4f9f1;
}

.links a{position:relative}
.links a::after{
  content:""; position:absolute; left:0; right:0; bottom:-1px; height:1px;
  background:linear-gradient(90deg,#b4530a,#ffc38a);
  transform:scaleX(0); transform-origin:left; transition:transform .25s ease;
}
.links a:hover::after{transform:scaleX(1)}

.pgroup{transition:transform .25s ease}
.pgroup:hover{transform:translateY(-1px)}

@media (prefers-reduced-motion: reduce){
  .top::after,.tab[aria-selected="true"],.card:hover,.qcopy{animation:none !important}
}
"""

# 深空宇宙变体（--cosmic）：整站换成深色星际底，视觉冲击优先。
# 与 COOL_CSS 互斥，只加样式不动结构与数据，原版 index.html 不受影响。
COSMIC_CSS = r"""
@property --ang{syntax:"<angle>";initial-value:0deg;inherits:false}
@keyframes angspin{to{--ang:360deg}}
@keyframes flowline{to{background-position:220% 0}}
@keyframes nebreathe{0%,100%{opacity:.85} 50%{opacity:1}}
@keyframes twinkle{0%,100%{opacity:.72} 50%{opacity:1}}
@keyframes pulseGlow{0%,100%{opacity:.55} 50%{opacity:1}}

:root{
  --bg:#04060e;
  --panel:#0b1224;
  --ink:#e9f1ff;
  --ink2:#a6b6d6;
  --ink3:#6b7c9d;
  --line:rgba(122,158,232,.17);
  --line2:rgba(122,158,232,.09);
  --copper:#5ecbff;
  --copper-soft:rgba(94,203,255,.12);
  --copper-line:rgba(94,203,255,.34);
  --red:#ff6272;
  --red-soft:rgba(255,98,114,.14);
  --green:#3ce0a6;
  --green-soft:rgba(60,224,166,.13);
  --blue:#6aa8ff;
  --blue-soft:rgba(106,168,255,.14);
  --violet:#b18bff;
  --violet-soft:rgba(177,139,255,.15);
  --shadow:0 24px 60px -34px rgba(0,0,0,.98);
  --radius:16px;
  color-scheme:dark;
}

html{background:#010206}
html,body{overflow-x:clip}
body{
  background:
    radial-gradient(1080px 460px at 50% -14%, rgba(126,186,255,.50) 0%, rgba(92,142,255,.14) 34%, rgba(92,142,255,0) 62%),
    radial-gradient(720px 380px at 102% -10%, rgba(192,112,255,.36) 0%, rgba(192,112,255,0) 62%),
    radial-gradient(480px 320px at -6% 4%, rgba(0,212,255,.18) 0%, rgba(0,212,255,0) 64%),
    #010206;
  background-attachment:fixed;
}
@supports not (background-attachment: fixed){
  body{background:#010206}
}

/* 星云层（只做透明度呼吸，不重绘） */
body::before{
  content:""; position:fixed; inset:-8% -8% -8% -8%; z-index:0; pointer-events:none;
  background:
    radial-gradient(40% 24% at 50% -4%, rgba(150,215,255,.30), transparent 72%),
    radial-gradient(26% 18% at 88% 6%, rgba(190,150,255,.24), transparent 74%),
    radial-gradient(30% 20% at 4% 34%, rgba(255,86,176,.08), transparent 76%),
    radial-gradient(110% 18% at 50% 118%, rgba(94,203,255,.10), transparent 66%);
  filter:blur(24px);
  animation:nebreathe 26s ease-in-out infinite;
}

/* 星点层：硬边圆点，锐利不发虚；少量亮星带光晕 */
body::after{
  content:""; position:fixed; inset:0; z-index:0; pointer-events:none;
  background-image:
    radial-gradient(circle at 26px 44px, #fff 0 1.2px, transparent 1.4px),
    radial-gradient(circle at 152px 96px, rgba(210,234,255,.95) 0 1px, transparent 1.2px),
    radial-gradient(circle at 248px 210px, #fff 0 1.4px, transparent 1.6px),
    radial-gradient(circle at 88px 168px, rgba(180,212,255,.9) 0 .9px, transparent 1.1px),
    radial-gradient(circle at 196px 268px, #fff 0 1.5px, transparent 1.7px),
    radial-gradient(circle at 40px 236px, rgba(214,232,255,.85) 0 .9px, transparent 1.1px),
    radial-gradient(circle at 300px 130px, rgba(255,255,255,.8) 0 .8px, transparent 1px),

    radial-gradient(circle at 64px 132px, #fff 0 1.2px, transparent 1.4px),
    radial-gradient(circle at 318px 58px, #fff 0 1.6px, transparent 1.8px),
    radial-gradient(circle at 412px 306px, rgba(198,224,255,.92) 0 1.1px, transparent 1.3px),
    radial-gradient(circle at 202px 414px, #fff 0 1.4px, transparent 1.6px),
    radial-gradient(circle at 466px 196px, rgba(206,232,255,.85) 0 .9px, transparent 1.1px),
    radial-gradient(circle at 128px 448px, rgba(255,236,250,.9) 0 1.3px, transparent 1.5px),

    radial-gradient(circle at 112px 476px, rgba(220,238,255,.9) 0 1.1px, transparent 1.3px),
    radial-gradient(circle at 402px 664px, #fff 0 1.5px, transparent 1.7px),
    radial-gradient(circle at 764px 336px, rgba(206,232,255,.85) 0 1px, transparent 1.2px),
    radial-gradient(circle at 236px 782px, rgba(255,238,252,.9) 0 1.3px, transparent 1.5px),
    radial-gradient(circle at 706px 542px, rgba(198,224,255,.88) 0 1.1px, transparent 1.3px),
    radial-gradient(circle at 88px 620px, rgba(255,255,255,.82) 0 .9px, transparent 1.1px),

    /* 三颗亮星：核心 + 光晕 */
    radial-gradient(circle at 586px 168px, #fff 0 1.4px, rgba(150,205,255,.55) 2.2px, rgba(120,180,255,.10) 6px, transparent 11px),
    radial-gradient(circle at 180px 340px, #fff 0 1.2px, rgba(190,215,255,.45) 2px, rgba(120,180,255,.08) 5.5px, transparent 10px),
    radial-gradient(circle at 830px 470px, #fff 0 1.3px, rgba(255,200,240,.45) 2px, rgba(255,150,220,.08) 6px, transparent 11px);
  background-size:
    320px 320px, 320px 320px, 320px 320px, 320px 320px, 320px 320px, 320px 320px, 320px 320px,
    520px 520px, 520px 520px, 520px 520px, 520px 520px, 520px 520px, 520px 520px,
    820px 820px, 820px 820px, 820px 820px, 820px 820px, 820px 820px, 820px 820px,
    1180px 1180px, 1180px 1180px, 1180px 1180px;
  background-repeat:repeat;
  animation:twinkle 13s ease-in-out infinite;
}

/* 内容抬到星层之上 */
main,footer{position:relative; z-index:1}

::selection{background:rgba(94,203,255,.32); color:#fff}
::-webkit-scrollbar{width:11px; height:11px}
::-webkit-scrollbar-track{background:#04060e}
::-webkit-scrollbar-thumb{
  background:linear-gradient(180deg,#22315a,#182340); border-radius:8px; border:2px solid #04060e;
}
::-webkit-scrollbar-thumb:hover{background:#2e4478}

/* ── 顶栏 ───────────────────────────── */
.top{
  background:rgba(3,5,13,.62);
  backdrop-filter:saturate(150%) blur(26px); -webkit-backdrop-filter:saturate(150%) blur(26px);
  border-bottom:1px solid rgba(122,158,232,.18);
  box-shadow:0 24px 60px -48px #000;
}
.top::after{
  content:""; position:absolute; left:0; right:0; bottom:-1px; height:1px;
  pointer-events:none; background-size:220% 100%;
  background-image:linear-gradient(90deg,
    rgba(94,203,255,0) 0%, rgba(94,203,255,.85) 18%,
    rgba(177,139,255,.9) 42%, rgba(255,142,203,.75) 64%,
    rgba(94,203,255,0) 88%);
  animation:flowline 11s linear infinite;
}

.brand{color:#f5f9ff; font-size:22px; letter-spacing:-.02em; text-shadow:0 0 32px rgba(94,203,255,.55)}
.brand em{
  color:transparent;
  background:linear-gradient(100deg,#7ee0ff 0%,#b18bff 58%,#ff8ecb 100%);
  -webkit-background-clip:text; background-clip:text;
  filter:drop-shadow(0 0 16px rgba(126,224,255,.75));
}
.brand-tag{
  color:#9fe6ff; background:rgba(94,203,255,.10);
  border-color:rgba(94,203,255,.30);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
}
.brand-sub{color:var(--ink3)}

.search input{
  background:rgba(9,14,27,.82); border-color:rgba(122,158,232,.20); color:var(--ink);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.04);
}
.search input::placeholder{color:#5f7092}
.search input:focus{
  border-color:rgba(94,203,255,.62);
  box-shadow:0 0 0 3px rgba(94,203,255,.13), 0 0 28px -8px rgba(94,203,255,.75);
}
.search kbd{background:#0a1122; border-color:rgba(122,158,232,.20); color:var(--ink3)}

select{
  background-color:rgba(9,14,27,.82); border-color:rgba(122,158,232,.20); color:var(--ink);
}
select option{background:#0a1020; color:#e9f1ff}

.tabs{background:rgba(8,12,24,.72); border:1px solid rgba(122,158,232,.16)}
.tab{color:#94a6c8}
.tab[aria-selected="true"]{
  background:linear-gradient(180deg,rgba(94,203,255,.22),rgba(94,203,255,.07));
  color:#eaf8ff;
  box-shadow:
    0 0 0 1px rgba(94,203,255,.45),
    0 0 26px -8px rgba(94,203,255,.85),
    inset 0 1px 0 rgba(255,255,255,.10);
}

.chip{
  border-color:rgba(122,158,232,.20); background:rgba(13,19,35,.78); color:var(--ink2);
}
.chip:hover{
  border-color:rgba(94,203,255,.52); color:#8fe6ff;
  box-shadow:0 0 20px -6px rgba(94,203,255,.65);
}
.chip[aria-pressed="true"]{
  background:linear-gradient(180deg,#2f9fd6,#1d6f9c);
  border-color:rgba(120,214,255,.62); color:#f2fbff; font-weight:700;
  box-shadow:0 0 20px -8px rgba(94,203,255,.75), inset 0 1px 0 rgba(255,255,255,.22);
}

/* ── 首屏说明卡：视觉中心 ─────────────── */
.lede{
  position:relative; overflow:hidden;
  padding:34px 32px;
  gap:32px;
  background:
    radial-gradient(95% 70% at 50% -32%, rgba(170,235,255,.20), transparent 62%),
    radial-gradient(110% 180% at 4% -50%, rgba(94,203,255,.14), transparent 62%),
    radial-gradient(85% 150% at 98% 140%, rgba(177,139,255,.12), transparent 64%),
    linear-gradient(180deg,rgba(152,192,255,.10),rgba(10,18,40,.44));
  backdrop-filter:blur(22px) saturate(150%); -webkit-backdrop-filter:blur(22px) saturate(150%);
  border:1px solid rgba(140,220,255,.52);
  border-radius:20px;
  box-shadow:
    0 0 0 1px rgba(94,203,255,.12),
    0 0 140px -20px rgba(126,224,255,.72),
    0 0 56px -16px rgba(177,139,255,.52),
    0 44px 96px -54px #000,
    inset 0 1px 0 rgba(255,255,255,.12);
}
.lede::before{
  content:""; position:absolute; left:0; right:0; top:0; height:1px; z-index:2;
  background-image:linear-gradient(90deg,
    rgba(94,203,255,0), rgba(94,203,255,.95) 22%, rgba(177,139,255,.95) 52%,
    rgba(255,142,203,.8) 76%, rgba(94,203,255,0));
  background-size:220% 100%;
  animation:flowline 8s linear infinite;
}
.lede::after{
  content:""; position:absolute; inset:0; pointer-events:none; z-index:0; opacity:.55;
  background-image:
    radial-gradient(1px 1px at 12% 26%, rgba(255,255,255,.9), transparent 62%),
    radial-gradient(1.4px 1.4px at 47% 14%, rgba(198,226,255,.85), transparent 62%),
    radial-gradient(1px 1px at 68% 74%, rgba(255,255,255,.8), transparent 62%),
    radial-gradient(1.6px 1.6px at 88% 36%, rgba(255,214,244,.8), transparent 62%),
    radial-gradient(1px 1px at 28% 86%, rgba(168,206,255,.75), transparent 62%);
}
.lede > *{position:relative; z-index:1}
.lede h2{
  font-size:28px; font-weight:800; letter-spacing:-.015em; line-height:1.25;
  margin-bottom:10px;
  color:transparent;
  background:linear-gradient(94deg,#ffffff 0%,#9fe6ff 44%,#c3a5ff 100%);
  -webkit-background-clip:text; background-clip:text;
  filter:drop-shadow(0 0 22px rgba(94,203,255,.42));
}
.lede p{font-size:13.5px; line-height:1.8; max-width:720px}
.lede .k{color:#8fe6ff; text-shadow:0 0 18px rgba(94,203,255,.55)}
.lede-q a{color:#8fe6ff; border-bottom-color:rgba(94,203,255,.42)}
.lede-q a:hover{border-bottom-color:#8fe6ff}

.statrow{gap:34px}
.stat b{
  font-size:32px; letter-spacing:.01em; line-height:1.1;
  color:transparent;
  background:linear-gradient(180deg,#ffffff 0%,#8fe6ff 62%,#3fa9ff 100%);
  -webkit-background-clip:text; background-clip:text;
  filter:drop-shadow(0 0 16px rgba(94,203,255,.6));
}
.stat span{color:#8ea3c6; font-size:12px; letter-spacing:.02em}

@media (max-width:640px){
  .lede{padding:22px 18px; gap:18px}
  .lede h2{font-size:20px}
  .stat b{font-size:24px}
  .statrow{gap:18px}
}

/* ── 分区标题 ───────────────────────── */
.sectionhead{border-bottom-color:rgba(122,158,232,.17)}
.sectionhead h2{color:#eaf2ff}
.sectionhead h2::before{
  content:""; display:inline-block; width:3px; height:12px; border-radius:2px;
  margin-right:8px; vertical-align:-1px;
  background:linear-gradient(180deg,#7ee0ff,#b18bff);
  box-shadow:0 0 12px rgba(126,224,255,.8);
}
.sectionhead.soon h2{color:#ff828e; text-shadow:0 0 22px rgba(255,98,114,.45)}
.sectionhead.soon h2::before{background:linear-gradient(180deg,#ff8b96,#ff4f63); box-shadow:0 0 12px rgba(255,98,114,.8)}
.sectionhead .hint,.sectionhead .cnt{color:var(--ink3)}

/* ── 临期条 ─────────────────────────── */
.urgent{
  background:rgba(122,158,232,.10);
  border-color:rgba(255,98,114,.22);
  box-shadow:0 0 46px -26px rgba(255,98,114,.75);
}
.urow{background:rgba(12,17,32,.90)}
.urow:hover{background:rgba(30,20,38,.92)}
.urow .d{color:#ff7d89}
.urow .d.warn{color:#ffc06a}

/* ── 产品组标题 ─────────────────────── */
.phead h3{color:#f2f7ff}
.phead .pill{
  background:rgba(122,158,232,.11);
  border-color:rgba(122,158,232,.22);
  color:#95a8ca;
}
.phead .deadline{color:#ff7d89}

/* ── 卡片：深空玻璃 ─────────────────── */
.card{
  background:
    radial-gradient(140% 90% at 50% -24%, rgba(126,186,255,.11), transparent 60%),
    linear-gradient(180deg,rgba(146,180,255,.075),rgba(16,26,52,.34));
  border:1px solid rgba(152,186,242,.17);
  border-radius:16px;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.08),
    0 20px 48px -34px rgba(0,0,0,1);
  transition:border-color .22s, transform .22s, box-shadow .22s, background .22s;
}
.card::before{
  content:""; position:absolute; left:15px; right:15px; top:0; height:1px;
  pointer-events:none; opacity:.6; transition:opacity .22s;
  background:linear-gradient(90deg,
    rgba(94,203,255,0), rgba(94,203,255,.75) 30%,
    rgba(177,139,255,.75) 68%, rgba(94,203,255,0));
}
.card::after{
  content:""; position:absolute; inset:0; border-radius:inherit; pointer-events:none;
  background:linear-gradient(180deg,rgba(94,203,255,.13),transparent 44%);
  opacity:0; transition:opacity .26s;
}
.card:hover{
  transform:translateY(-2px);
  border-color:transparent;
  background:
    linear-gradient(180deg,rgba(25,35,62,.94),rgba(10,15,29,.96)) padding-box,
    conic-gradient(from var(--ang),
      rgba(94,203,255,.95), rgba(177,139,255,.95) 26%,
      rgba(94,203,255,.30) 52%, rgba(255,142,203,.85) 76%,
      rgba(94,203,255,.95)) border-box;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.08),
    0 0 0 1px rgba(94,203,255,.16),
    0 0 46px -12px rgba(94,203,255,.55),
    0 34px 76px -44px #000;
  animation:angspin 3.4s linear infinite;
}
.card:hover::before{opacity:1}
.card:hover::after{opacity:1}
.card[data-status="expired"]{opacity:.42; filter:grayscale(.5)}
.card[data-status="expired"]:hover{opacity:.72}

.card h4{color:#f4f8ff; letter-spacing:-.005em}
.big{
  color:#8fe6ff;
  text-shadow:0 0 24px rgba(94,203,255,.42), 0 0 2px rgba(143,230,255,.6);
}
.big small{color:var(--ink3)}

.cd{color:var(--ink3)}
.cd.hot{color:#ff7d89; text-shadow:0 0 16px rgba(255,98,114,.5)}
.cd.warn{color:#ffc06a}

.tag.form{
  background:rgba(122,158,232,.15); color:#b9c9e6; border-color:rgba(122,158,232,.24);
}
.tag.promo{background:rgba(255,98,114,.17); color:#ff929c; border-color:rgba(255,98,114,.32)}
.tag.daily{background:rgba(60,224,166,.16); color:#63f2bf; border-color:rgba(60,224,166,.32)}
.tag.signup{background:rgba(106,168,255,.17); color:#93c4ff; border-color:rgba(106,168,255,.32)}
.tag.free_model{background:rgba(177,139,255,.18); color:#c8adff; border-color:rgba(177,139,255,.32)}

.kv{border-top-color:rgba(122,158,232,.12)}
.kv b{color:#b8c8e6}
.kv .warn{color:#ff7d89}

details .body{
  background:rgba(6,10,21,.94);
  border-color:rgba(122,158,232,.14);
}
details summary{color:var(--ink2)}
details summary:hover{color:#8fe6ff}
.links a{color:#7eb8ff; text-shadow:0 0 18px rgba(106,168,255,.35)}

/* ── 底部群卡 ───────────────────────── */
footer{border-top-color:rgba(122,158,232,.22); color:#93a6c8}
.qgroup{border-bottom-color:rgba(122,158,232,.20)}
.qrimg{
  background:#fff; padding:5px; border-radius:12px;
  border:1px solid rgba(94,203,255,.55);
  box-shadow:0 0 34px -8px rgba(94,203,255,.75);
}
.qtitle{color:#f4f8ff}
.qnum b{color:#fff; text-shadow:0 0 18px rgba(94,203,255,.55)}
.qcopy{
  background:rgba(10,16,30,.88); border-color:rgba(122,158,232,.26); color:var(--ink2);
}
.qcopy:hover{
  border-color:rgba(94,203,255,.62); color:#8fe6ff;
  box-shadow:0 0 22px -6px rgba(94,203,255,.7);
}
.qcopy.done{
  border-color:rgba(60,224,166,.7); color:#63f2bf; background:rgba(60,224,166,.13);
}
.qtip{color:#93a6c8}
.lede-q{color:#8fa3c6 !important}

@keyframes orbPulse{0%,100%{opacity:.88} 50%{opacity:1}}


/* 顶部极光带：横贯全屏的彩色辉光，让顶栏变成"舷窗玻璃" */
.sky-aurora{
  position:fixed; z-index:0; pointer-events:none;
  left:0; right:0; top:-60px; height:400px;
  background:
    radial-gradient(58% 100% at 18% 0%, rgba(94,203,255,.34), transparent 70%),
    radial-gradient(52% 92% at 54% -8%, rgba(158,122,255,.32), transparent 72%),
    radial-gradient(44% 84% at 86% 2%, rgba(255,118,198,.20), transparent 72%),
    radial-gradient(70% 60% at 50% 40%, rgba(120,190,255,.12), transparent 76%);
  filter:blur(46px);
  animation:auroraShift 26s ease-in-out infinite;
}
@keyframes auroraShift{
  0%,100%{transform:translateX(-2.5%) scaleY(1)}
  50%{transform:translateX(2.5%) scaleY(1.14)}
}

/* 星野封面：顶栏与内容之间的一段太空，底部托着一颗巨行星的边缘 */
.sky-hero{
  position:relative; height:262px; overflow:hidden; pointer-events:none;
  margin-bottom:10px;
  background-image:
    radial-gradient(circle at 8% 18%, #fff 0 1.3px, transparent 1.5px),
    radial-gradient(circle at 23% 42%, rgba(210,234,255,.9) 0 1px, transparent 1.2px),
    radial-gradient(circle at 41% 12%, #fff 0 1.5px, transparent 1.7px),
    radial-gradient(circle at 58% 34%, rgba(200,228,255,.85) 0 1.1px, transparent 1.3px),
    radial-gradient(circle at 72% 9%, #fff 0 1.2px, transparent 1.4px),
    radial-gradient(circle at 88% 27%, rgba(255,240,250,.9) 0 1.4px, transparent 1.6px),
    radial-gradient(circle at 15% 62%, rgba(190,220,255,.8) 0 .9px, transparent 1.1px),
    radial-gradient(circle at 34% 74%, #fff 0 1.1px, transparent 1.3px),
    radial-gradient(circle at 66% 66%, rgba(210,234,255,.8) 0 .9px, transparent 1.1px),
    radial-gradient(circle at 82% 56%, #fff 0 1.2px, transparent 1.4px),
    radial-gradient(circle at 94% 72%, rgba(200,228,255,.75) 0 .9px, transparent 1.1px);
}
/* 星云（先绘制，压在球之下） */
.sky-hero::before{
  content:""; position:absolute; inset:-40px -10% 0 -10%;
  background:
    radial-gradient(44% 110% at 20% 0%, rgba(94,203,255,.26), transparent 70%),
    radial-gradient(40% 100% at 62% -14%, rgba(158,122,255,.30), transparent 72%),
    radial-gradient(34% 88% at 92% 2%, rgba(255,118,198,.18), transparent 72%);
  filter:blur(40px);
}
/* 巨行星：2600px 直径，只露顶部一段弧 */
.sky-hero::after{
  content:""; position:absolute; left:50%; top:110px; transform:translateX(-50%);
  width:10000px; height:10000px; border-radius:50%;
  background:
    radial-gradient(circle at 50% 50%,
      rgba(3,6,16,1) 0 68.9%,
      rgba(10,28,68,1) 69.9%,
      rgba(30,76,158,1) 70.26%,
      rgba(72,146,226,.98) 70.42%,
      rgba(172,230,255,1) 70.53%,
      rgba(190,212,255,.62) 70.61%,
      rgba(130,178,255,.20) 70.74%,
      rgba(94,203,255,0) 71.04%);
  animation:orbPulse 18s ease-in-out infinite;
  -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);
  -webkit-mask-size:100vw 100%; -webkit-mask-position:center top; -webkit-mask-repeat:no-repeat;
  mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);
  mask-size:100vw 100%; mask-position:center top; mask-repeat:no-repeat;
}

@media (max-width:640px){
  .sky-hero{height:140px}
  .sky-hero::after{height:3200px; width:3200px; top:74px}
}
.sky-vignette{
  position:fixed; inset:0; z-index:0; pointer-events:none;
  background:radial-gradient(118% 86% at 50% 20%, transparent 34%, rgba(0,0,0,.42) 74%, rgba(0,0,0,.72) 100%);
}

@media (max-width:640px){
  .sky-aurora{height:300px; filter:blur(34px)}
}

@media (prefers-reduced-motion: reduce){
  body::before,body::after,.sky-hero::after,.sky-aurora,.top::after,.lede::before,.tab[aria-selected="true"],.card:hover,.qcopy{
    animation:none !important;
  }
}
"""

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>免费 AI API 额度雷达 · 免费 token / 积分 / Credits 清单</title>
<meta name="description" content="全网免费 AI API 额度清单：免费 token、免费积分、免费 Credits，国内外 __NPROD__ 家平台、__NTOTAL__ 个入口。每条带截止日、出处、可信度，过期自动报警。免费 API 白嫖必备。">
<meta name="keywords" content="免费api,免费 API,免费token,免费额度,白嫖,免费AI,大模型,API,free api,free tier,LLM">
<meta property="og:type" content="website">
<meta property="og:title" content="免费 AI API 额度雷达">
<meta property="og:description" content="__NPROD__ 家平台、__NTOTAL__ 个入口的国内外免费 API 额度：免费 token、积分、Credits。带截止日、出处、可信度，过期自动报警。">
<style>
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#faf8f4; --panel:#fffefc; --ink:#1b1815; --ink2:#57504a; --ink3:#918a80;
  --line:#e9e3d9; --line2:#f3eee6;
  --copper:#b4530a; --copper-soft:#fdf2e4; --copper-line:#f0d9bb;
  --red:#b3352a; --red-soft:#fceceb;
  --green:#2c7355; --green-soft:#eaf4ee;
  --blue:#2c5f8a; --blue-soft:#ecf2f8;
  --violet:#5b4b8a; --violet-soft:#f0edf8;
  --shadow:0 1px 2px rgba(27,24,21,.04), 0 8px 24px -12px rgba(27,24,21,.12);
  --radius:14px;
}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:15px; line-height:1.6; -webkit-font-smoothing:antialiased;
}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer}
input,select{font-family:inherit;font-size:14px;color:var(--ink)}

/* ── 顶栏 ───────────────────────────── */
.top{
  position:sticky; top:0; z-index:50;
  background:rgba(250,248,244,.86);
  backdrop-filter:saturate(180%) blur(14px); -webkit-backdrop-filter:saturate(180%) blur(14px);
  border-bottom:1px solid var(--line);
}
.top-inner{max-width:1280px; margin:0 auto; padding:14px 24px 0}
.brandline{display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; margin-bottom:14px}
.brand{font-size:19px; font-weight:700; letter-spacing:-.02em}
.brand em{font-style:normal; color:var(--copper)}
.brand-sub{font-size:12.5px; color:var(--ink3)}
.brand-tag{
  font-size:11.5px; color:var(--copper); background:var(--copper-soft);
  border:1px solid var(--copper-line); border-radius:999px; padding:1px 9px;
  white-space:nowrap;
}
.spacer{flex:1}

.controls{display:flex; gap:10px; align-items:center; flex-wrap:wrap; padding-bottom:12px}
.search{position:relative; flex:1; min-width:200px; max-width:340px}
.search input{
  width:100%; padding:8px 12px 8px 32px; border:1px solid var(--line);
  border-radius:9px; background:var(--panel); outline:none; transition:.15s;
}
.search input:focus{border-color:var(--copper-line); box-shadow:0 0 0 3px var(--copper-soft)}
.search svg{position:absolute; left:10px; top:50%; transform:translateY(-50%); opacity:.4}
.search kbd{
  position:absolute; right:8px; top:50%; transform:translateY(-50%);
  font-size:11px; color:var(--ink3); border:1px solid var(--line);
  border-radius:4px; padding:0 5px; background:var(--bg); font-family:inherit;
}
select{
  padding:8px 26px 8px 10px; border:1px solid var(--line); border-radius:9px;
  background:var(--panel) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='6'><path d='M0 0l5 6 5-6z' fill='%23918a80'/></svg>") no-repeat right 9px center;
  appearance:none; outline:none;
}

/* ── 地区切换 ───────────────────────── */
.tabs{display:flex; gap:4px; background:#eee8dd; padding:3px; border-radius:10px}
.tab{
  border:0; background:transparent; padding:7px 15px; border-radius:8px;
  font-size:13.5px; font-weight:600; color:var(--ink2); transition:.15s; white-space:nowrap;
}
.tab .n{font-size:11.5px; opacity:.55; margin-left:4px; font-weight:500}
.tab .u{font-size:11px; opacity:.4; margin-left:1px; font-weight:400}
.tab[aria-selected="true"]{background:var(--panel); color:var(--ink); box-shadow:0 1px 3px rgba(27,24,21,.1)}
.tab[aria-selected="true"] .n{opacity:.75}

/* ── 筛选 chips ─────────────────────── */
.filters{
  max-width:1280px; margin:0 auto; padding:0 24px 11px;
  display:flex; gap:18px; flex-wrap:wrap; align-items:center;
  font-size:13px;
}
.fgroup{display:flex; gap:6px; align-items:center; flex-wrap:wrap; row-gap:6px; min-width:0}
.flabel{color:var(--ink3); font-size:12px; margin-right:2px; white-space:nowrap}
.chip{
  border:1px solid var(--line); background:var(--panel); color:var(--ink2);
  padding:4px 11px; border-radius:999px; font-size:12.5px; transition:.15s;
}
.chip:hover{border-color:var(--copper-line); color:var(--copper)}
.chip[aria-pressed="true"]{background:var(--ink); border-color:var(--ink); color:#fff}
.chip.sm{padding:3px 9px; font-size:12px}

/* ── 主体 ───────────────────────────── */
main{max-width:1280px; margin:0 auto; padding:26px 24px 80px}
.lede{
  display:flex; gap:26px; flex-wrap:wrap; align-items:center;
  padding:18px 20px; margin-bottom:24px;
  background:linear-gradient(180deg,#fffdfa,#fdf8f0);
  border:1px solid var(--copper-line); border-radius:var(--radius);
}
.lede h2{margin:0 0 4px; font-size:15px; font-weight:700}
.lede p{margin:0; font-size:13px; color:var(--ink2); line-height:1.75}
.lede .k{color:var(--copper); font-weight:700; white-space:nowrap}
.lede-q{margin-top:7px !important; font-size:12.5px !important; color:var(--ink3) !important}
.lede-q a{color:var(--copper); border-bottom:1px solid var(--copper-line); font-weight:600}
.lede-q a:hover{border-bottom-color:var(--copper)}
.statrow{display:flex; gap:20px; margin-left:auto}
.stat{text-align:center}
.stat b{display:block; font-size:20px; line-height:1.2; font-variant-numeric:tabular-nums}
.stat span{font-size:11.5px; color:var(--ink3)}

.sectionhead{
  display:flex; align-items:baseline; gap:10px; margin:30px 0 14px; padding-bottom:9px;
  border-bottom:1px solid var(--line);
}
.sectionhead h2{margin:0; font-size:14px; font-weight:700; letter-spacing:.01em; white-space:nowrap; flex:0 0 auto}
.sectionhead .hint{font-size:12.5px; color:var(--ink3); min-width:0}
.sectionhead .cnt{margin-left:auto; font-size:12px; color:var(--ink3); font-variant-numeric:tabular-nums; white-space:nowrap; flex:0 0 auto}
.sectionhead.soon h2{color:var(--red)}
.sectionhead.soon h2::before{content:""; display:inline-block; width:3px; height:12px;
  background:var(--red); border-radius:2px; margin-right:7px; vertical-align:-1px}

/* 临期条 */
.urgent{display:grid; grid-template-columns:minmax(0,1fr); gap:1px; background:var(--line2); border:1px solid var(--line); border-radius:var(--radius); overflow:hidden}
.urow{
  display:flex; align-items:center; gap:12px; padding:11px 15px; min-width:0;
  background:var(--panel); font-size:13.5px; transition:.12s;
}
.urow:hover{background:#fffaf3}
.urow .d{
  font-variant-numeric:tabular-nums; font-weight:700; font-size:12px;
  min-width:56px; flex:0 0 auto; color:var(--red);
}
.urow .d.warn{color:var(--copper)}
.urow .pn{
  font-weight:600; white-space:nowrap; max-width:56%; min-width:0;
  flex:0 1 auto; overflow:hidden; text-overflow:ellipsis;
}
.urow .vn{color:var(--ink2); overflow:hidden; text-overflow:ellipsis; white-space:nowrap; min-width:0; flex:1}
.urow .go{margin-left:auto; flex:0 0 auto; color:var(--ink3); font-size:12px; white-space:nowrap}

/* 产品组：入口多的独占整行，入口少的并排铺满 */
.clusters{
  display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
  gap:26px 14px; align-items:start; grid-auto-flow:dense;
}
.pgroup{min-width:0}
.phead{display:flex; align-items:center; gap:8px; margin-bottom:10px; flex-wrap:wrap}
.phead h3{margin:0; font-size:15px; font-weight:700; letter-spacing:-.01em}
.phead .pill{
  font-size:11px; color:var(--ink3); border:1px solid var(--line);
  border-radius:999px; padding:1px 8px; background:var(--panel);
}
.phead .deadline{margin-left:auto; font-size:12px; color:var(--red); font-weight:600}

.grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:12px}
.card{
  background:var(--panel); border:1px solid var(--line); border-radius:var(--radius);
  padding:15px 16px 13px; box-shadow:var(--shadow);
  display:flex; flex-direction:column; gap:9px; position:relative;
  transition:border-color .15s, transform .15s, box-shadow .15s;
}
.card:hover{transform:translateY(-1px); border-color:var(--copper-line); box-shadow:0 2px 4px rgba(27,24,21,.05), 0 14px 30px -16px rgba(27,24,21,.22)}
.card[data-status="expired"]{opacity:.55; filter:grayscale(.4)}
.card[data-status="expired"]:hover{opacity:.8}

.ctop{display:flex; align-items:center; gap:6px; flex-wrap:wrap}
.tag{
  font-size:11px; font-weight:600; padding:2px 7px; border-radius:5px;
  border:1px solid transparent; letter-spacing:.01em;
}
.tag.form{background:#f4f1ea; color:var(--ink2); border-color:#ece6db}
.tag.promo{background:var(--red-soft); color:var(--red)}
.tag.daily{background:var(--green-soft); color:var(--green)}
.tag.signup{background:var(--blue-soft); color:var(--blue)}
.tag.free_model{background:var(--violet-soft); color:var(--violet)}
.cd{margin-left:auto; font-size:11.5px; font-variant-numeric:tabular-nums; color:var(--ink3); white-space:nowrap}
.cd.hot{color:var(--red); font-weight:700}
.cd.warn{color:var(--copper); font-weight:600}

.card h4{margin:0; font-size:14.5px; font-weight:700; line-height:1.45; letter-spacing:-.005em}
.big{
  font-size:17px; font-weight:700; color:var(--copper); line-height:1.35;
  letter-spacing:-.01em;
}
.big small{font-size:12px; color:var(--ink3); font-weight:500; margin-left:6px}
.billing{font-size:12.5px; color:var(--ink2)}
.offer{font-size:13px; color:var(--ink2); margin:0; line-height:1.65}

.kv{display:flex; gap:14px; flex-wrap:wrap; font-size:11.5px; color:var(--ink3); border-top:1px solid var(--line2); padding-top:9px; margin-top:auto}
.kv b{font-weight:600; color:var(--ink2)}
.kv .warn{color:var(--red)}

details{font-size:12.5px; color:var(--ink2)}
details summary{
  cursor:pointer; color:var(--ink2); outline:none; list-style:none;
  user-select:none; display:inline-flex; align-items:center; gap:5px;
  font-size:12.5px; padding:1px 0;
}
details summary:hover{color:var(--copper)}
details summary::-webkit-details-marker{display:none}
details summary::before{content:"›"; display:inline-block; transition:.18s; font-size:14px}
details[open] summary::before{transform:rotate(90deg)}
details .body{margin-top:7px; padding:9px 11px; background:#fbf9f4; border-radius:8px; line-height:1.7; border:1px solid var(--line2)}
details .body .lbl{color:var(--ink3); font-size:11px}

.links{display:flex; gap:12px; font-size:12px; padding-top:2px}
.links a{color:var(--blue); border-bottom:1px solid transparent}
.links a:hover{border-bottom-color:var(--blue)}
.empty{padding:60px 20px; text-align:center; color:var(--ink3); font-size:14px}
footer{
  max-width:1280px; margin:0 auto; padding:24px; border-top:1px solid var(--line);
  font-size:12px; color:var(--ink3); display:flex; gap:16px; flex-wrap:wrap;
  scroll-margin-top:150px;
}
.qgroup{
  display:flex; gap:16px; align-items:center; flex-wrap:wrap; min-width:0;
  width:100%; padding-bottom:18px; margin-bottom:2px; border-bottom:1px dashed var(--line);
}
.qrimg{
  width:120px; height:auto; flex:0 0 auto; display:block; border-radius:10px;
  border:1px solid var(--line); background:#fff; padding:4px;
}
.qmeta{min-width:0; flex:1 1 220px}
.qtitle{font-size:13px; font-weight:700; color:var(--ink)}
.qnum{margin:6px 0 7px; font-size:12.5px; color:var(--ink2); display:flex; align-items:center; gap:8px; flex-wrap:wrap}
.qnum b{font-size:14.5px; letter-spacing:.03em; color:var(--ink); font-variant-numeric:tabular-nums}
.qcopy{
  border:1px solid var(--line); background:var(--panel); color:var(--ink2);
  padding:2px 9px; border-radius:999px; font-size:11.5px; line-height:1.6;
}
.qcopy:hover{border-color:var(--copper-line); color:var(--copper)}
.qcopy.done{border-color:#7a9e6f; color:#4d7a41; background:#f4f9f1}
.qtip{margin:0; font-size:12px; line-height:1.7; color:var(--ink3)}
@media (max-width:640px){
  .qrimg{width:96px}
  /* 手机端 footer 太高会被吸顶栏遮住顶部，隐藏面向维护者的两行说明 */
  footer > span{display:none}
  /* 窄屏放不下「标题 + 说明 + 计数」三截，说明文字是给桌面看的，手机上去掉 */
  .sectionhead .hint{display:none}
}

@media (max-width:640px){
  .top-inner,.filters,main,footer{padding-left:14px; padding-right:14px}
  .grid{grid-template-columns:1fr}
  .clusters{grid-template-columns:1fr}
  .pgroup,.pgroup.wide{grid-column:1 / -1 !important}
  .statrow{width:100%; justify-content:space-between; margin-left:0; gap:8px}
  .lede{gap:14px; padding:14px 15px}
  .search{max-width:none}
  .filters{gap:10px}
  .urow{flex-wrap:wrap; gap:4px 10px; padding:10px 13px}
  .urow .d{min-width:52px}
  .urow .pn{max-width:100%; white-space:normal; overflow:visible; flex:1 1 100%; order:2}
  .urow .vn{display:none}
  .urow .go{order:1; margin-left:auto; font-size:11.5px}
}
</style>
</head>
<body>

<div class="top">
  <div class="top-inner">
    <div class="brandline">
      <div class="brand">免费 <em>AI</em> API 额度雷达</div>
      <span class="brand-tag">token · 积分 · Credits</span>
      <div class="brand-sub" id="buildInfo">数据截至 —</div>
      <div class="spacer"></div>
      <div class="tabs" role="tablist" id="tabs">
        <button class="tab" role="tab" data-region="cn">国内<span class="n"></span><span class="u">家</span></button>
        <button class="tab" role="tab" data-region="global">海外<span class="n"></span><span class="u">家</span></button>
        <button class="tab" role="tab" data-region="all">全部<span class="n"></span><span class="u">家</span></button>
      </div>
    </div>
    <div class="controls">
      <label class="search">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="7" cy="7" r="5"/><path d="M11 11l4 4"/></svg>
        <input id="q" type="search" placeholder="搜产品、模型、额度…" autocomplete="off">
        <kbd>/</kbd>
      </label>
      <select id="sort">
        <option value="urgent">紧急优先</option>
        <option value="count">入口多优先</option>
        <option value="easy">难度低优先</option>
        <option value="name">按名称</option>
      </select>
    </div>
  </div>
  <div class="filters">
    <div class="fgroup" id="fType">
      <span class="flabel">领取方式</span>
      <button class="chip" data-v="">全部</button>
      <button class="chip" data-v="promo">限时活动</button>
      <button class="chip" data-v="daily">每日续杯</button>
      <button class="chip" data-v="signup">注册一次性</button>
      <button class="chip" data-v="free_model">长期 0 元</button>
    </div>
    <div class="fgroup" id="fForm">
      <span class="flabel">形态</span>
      <button class="chip sm" data-v="">全部</button>
      <button class="chip sm" data-v="api">API</button>
      <button class="chip sm" data-v="desktop">客户端</button>
      <button class="chip sm" data-v="web">网页</button>
      <button class="chip sm" data-v="app">App</button>
      <button class="chip sm" data-v="ide">IDE</button>
      <button class="chip sm" data-v="cli">CLI</button>
    </div>
    <div class="fgroup">
      <button class="chip" id="tHideExpired" aria-pressed="true">隐藏已过期</button>
      <button class="chip" id="tNoRealname" aria-pressed="false">免实名</button>
    </div>
  </div>
</div>

<main>
  <div class="lede" id="lede"></div>
  <div id="out"></div>
</main>

<footer id="qgroup">
  <div class="qgroup">
    <img class="qrimg" src="data:image/png;base64,__QR__" alt="QQ 群二维码：__QQNAME__，群号 __QQNUM__" loading="lazy" decoding="async">
    <div class="qmeta">
      <div class="qtitle">QQ 群 · __QQNAME__</div>
      <div class="qnum">群号 <b>__QQNUM__</b><button class="qcopy" id="copyQ" type="button">复制群号</button></div>
      <p class="qtip">领到好用的、发现哪条失效了、想催更某个平台，都可以丢到群里一起聊。二维码会过期——过期了直接在 QQ 里搜上面的群号。</p>
    </div>
  </div>
  <span>数据源 <b>data/providers.yaml</b>，改数据后跑 <b>python3 scripts/build_site.py</b> 重新生成本页</span>
  <span>每条标了出处与可信度，低可信条目请自行核实后再用</span>
</footer>

<script>
const DATA = __DATA__;
const META = __META__;

const FORM = {web:"网页版", app:"手机 App", desktop:"桌面客户端", ide:"IDE 插件", cli:"命令行", api:"API"};
const TYPE = {promo:"限时活动", daily:"每日续杯", signup:"注册一次性", free_model:"长期 0 元"};
const DIFF = ["","★","★★","★★★","★★★★","★★★★★"];

const state = {region:"cn", q:"", type:"", form:"", hideExpired:true, noRealname:false, sort:"urgent"};

const $ = s => document.querySelector(s);
const esc = s => String(s==null?"":s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));

// 平台数按 product 去重：WorkBuddy 有 12 个入口，只算 1 家
const pcount = arr => new Set(arr.map(d => d.product)).size;

function counts(){
  const c = {cn:pcount(DATA.filter(d=>d.region==="cn")), global:pcount(DATA.filter(d=>d.region==="global")), all:pcount(DATA)};
  document.querySelectorAll("#tabs .tab").forEach(t => {
    t.querySelector(".n").textContent = c[t.dataset.region];
  });
}

function cdText(d){
  if(d.status==="expired") return "已过期";
  if(d.days===null||d.days===undefined) return d.expiry==="long"?"长期":"未公布";
  if(d.days===0) return "今天到期";
  return "剩 "+d.days+" 天";
}
function cdClass(d){
  if(d.status==="expired") return "hot";
  if(d.days===null||d.days===undefined) return "";
  if(d.days<=7) return "hot";
  if(d.days<=21) return "warn";
  return "";
}

function passes(d){
  if(state.region!=="all" && d.region!==state.region) return false;
  if(state.type && d.type!==state.type) return false;
  if(state.form && d.form!==state.form) return false;
  if(state.hideExpired && d.status==="expired") return false;
  if(state.noRealname && d.realname==="yes") return false;
  if(state.q){
    const hay = (d.product+" "+d.name+" "+d.offer+" "+d.models+" "+d.billing+" "+d.value+" "+d.notes).toLowerCase();
    if(!hay.includes(state.q.toLowerCase())) return false;
  }
  return true;
}

function card(d){
  const gates = [];
  if(d.realname==="yes") gates.push('<span class="warn">需实名</span>');
  if(d.card==="yes") gates.push('<span class="warn">需绑卡</span>');
  if(!gates.length) gates.push("免实名免绑卡");
  const modelBlock = d.models ? '<div><span class="lbl">可用模型</span><br>'+esc(d.models)+'</div>' : "";
  const noteBlock = d.notes ? '<div style="margin-top:'+(d.models?"8px":"0")+'"><span class="lbl">备注</span><br>'+esc(d.notes)+'</div>' : "";
  const detail = (modelBlock||noteBlock)
    ? '<details><summary>'+(d.models?"模型与备注":"备注")+'</summary><div class="body">'+modelBlock+noteBlock+'</div></details>'
    : "";
  return '<article class="card" data-status="'+d.status+'">'
    + '<div class="ctop">'
    +   '<span class="tag form">'+esc(FORM[d.form]||d.form)+'</span>'
    +   '<span class="tag '+d.type+'">'+esc(TYPE[d.type]||d.type)+'</span>'
    +   '<span class="cd '+cdClass(d)+'">'+cdText(d)+'</span>'
    + '</div>'
    + '<h4>'+esc(d.name)+'</h4>'
    + '<div class="big">'+esc(d.value)+'</div>'
    + '<div class="billing">'+esc(d.billing)+'</div>'
    + '<p class="offer">'+esc(d.offer)+'</p>'
    + detail
    + '<div class="kv"><span>门槛 '+gates.join(" / ")+'</span>'
    +   '<span>难度 <b>'+(DIFF[+d.difficulty]||"")+'</b></span>'
    +   '<span>复核 <b>'+esc(d.verified.slice(5))+'</b></span>'
    +   '<span>可信 <b class="'+(d.confidence==="low"?"warn":"")+'">'+({high:"高",medium:"中",low:"低"}[d.confidence]||"")+'</b></span>'
    + '</div>'
    + '<div class="links">'
    +   '<a href="'+esc(d.url)+'" target="_blank" rel="noopener">官网 ↗</a>'
    +   '<a href="'+esc(d.source)+'" target="_blank" rel="noopener">出处 ↗</a>'
    + '</div>'
    + '</article>';
}

// 按容器实际列数给产品组分配跨列，避免 span 超出列数生成隐式列
function applySpans(){
  const wrap = document.querySelector(".clusters");
  if (!wrap) return;
  const GAP = 14, MIN = 320;
  const cols = Math.max(1, Math.floor((wrap.clientWidth + GAP) / (MIN + GAP)));
  wrap.querySelectorAll(".pgroup").forEach(g=>{
    const n = parseInt(g.dataset.n || "1", 10);
    const span = Math.min(n, cols);
    g.style.gridColumn = (span >= cols) ? "1 / -1" : ("span " + span);
  });
}
window.addEventListener("resize", ()=>{ applySpans(); });

function render(){
  const list = DATA.filter(passes);

  // 临期提醒
  const urgent = list.filter(d => d.days!==null && d.days!==undefined && d.days>=0 && d.days<=21)
                     .sort((a,b)=>a.days-b.days);
  let html = "";
  if(urgent.length){
    html += '<div class="sectionhead soon"><h2>临期提醒</h2>'
         +  '<span class="hint">21 天内截止，先领再说</span>'
         +  '<span class="cnt">'+urgent.length+' 条</span></div><div class="urgent">';
    urgent.forEach(d => {
      html += '<a class="urow" href="'+esc(d.url)+'" target="_blank" rel="noopener" title="'+esc(d.product+" · "+d.name+" · "+d.value)+'">'
           +  '<span class="d'+(d.days>7?" warn":"")+'">'+(d.days===0?"今天":"剩 "+d.days+" 天")+'</span>'
           +  '<span class="pn">'+esc(d.name)+'</span>'
           +  '<span class="vn">'+esc(d.value)+' · '+esc(d.billing)+'</span>'
           +  '<span class="go">'+esc(FORM[d.form]||d.form)+' ↗</span></a>';
    });
    html += '</div>';
  }

  // 按产品分组
  const groups = new Map();
  list.forEach(d => {
    if(!groups.has(d.product)) groups.set(d.product, []);
    groups.get(d.product).push(d);
  });

  const arr = [...groups.entries()].map(([p, its])=>{
    const days = its.map(d=>d.days).filter(x=>x!==null&&x!==undefined);
    return {p, its, minDays: days.length?Math.min(...days):Infinity, maxDiff: Math.max(...its.map(d=>+d.difficulty||3))};
  });

  if(state.sort==="count") arr.sort((a,b)=> b.its.length-a.its.length || a.p.localeCompare(b.p,"zh"));
  else if(state.sort==="easy") arr.sort((a,b)=> a.maxDiff-b.maxDiff || b.its.length-a.its.length);
  else if(state.sort==="name") arr.sort((a,b)=> a.p.localeCompare(b.p,"zh"));
  else arr.sort((a,b)=> a.minDays-b.minDays || b.its.length-a.its.length);

  if(!arr.length){
    html += '<div class="empty">没有符合条件的条目，换个筛选条件试试。</div>';
  }

  if (arr.length) {
    html += '<div class="sectionhead"><h2>按产品看</h2>'
         +  '<span class="hint">同一产品的不同入口分开写，展开可看模型与备注</span>'
         +  '<span class="cnt">'+arr.length+' 家平台 · '+list.length+' 个入口</span></div>';
  }

  if (arr.length) html += '<div class="clusters">';
  arr.forEach(g => {
    const order = ["web","app","desktop","ide","cli","api"];
    g.its.sort((a,b)=> order.indexOf(a.form)-order.indexOf(b.form) || (a.days??999)-(b.days??999));
    const soon = g.its.filter(d=>d.days!==null&&d.days!==undefined&&d.days>=0&&d.days<=21);
    const dl = soon.length ? '<span class="deadline">最近截止 '+soon[0].expiry+'</span>' : "";
    const npromo = g.its.filter(d=>d.type==="promo").length;
    html += '<div class="pgroup" data-n="'+g.its.length+'"><div class="phead">'
         +  '<h3>'+esc(g.p)+'</h3>'
         +  '<span class="pill">'+g.its.length+' 个入口'+(npromo?' · 限时 '+npromo:'')+'</span>'
         +  dl
         +  '</div><div class="grid">'+ g.its.map(card).join("") +'</div></div>';
  });
  if (arr.length) html += '</div>';

  $("#out").innerHTML = html;
  applySpans();

  const n = list.length;
  const longFree = list.filter(d=>d.type==="free_model").length;
  const live = list.filter(d=>d.type==="daily").length;
  const prom = list.filter(d=>d.type==="promo" && d.status!=="expired").length;
  const regionLabel = state.region === "cn" ? `国内 ${pcount(list)} 家平台 · ${n} 个入口`
                    : state.region === "global" ? `海外 ${pcount(list)} 家平台 · ${n} 个入口`
                    : `全部 ${pcount(list)} 家平台 · ${n} 个入口`;
  $("#lede").innerHTML = `
    <div>
      <h2>${regionLabel}</h2>
      <p>免费 API、免费 token、签到积分、Credits 都在这里。同一个 AI 在不同入口的免费政策完全不同，所以按 <b class="k">产品 × 形态</b> 拆开写，一条只讲一个入口。</p>
      <p class="lede-q">发现哪条失效了、或者挖到新羊毛，欢迎来 <a href="#qgroup">QQ 群 __QQNUM__</a> 说一声，一起交流。</p>
    </div>
    <div class="statrow">
      <div class="stat"><b>${longFree}</b><span>长期 0 元</span></div>
      <div class="stat"><b>${live}</b><span>可续杯</span></div>
      <div class="stat"><b>${prom}</b><span>限时在跑</span></div>
    </div>`;
}

// 事件
document.querySelectorAll("#tabs .tab").forEach(t=>{
  t.addEventListener("click",()=>{
    state.region = t.dataset.region;
    document.querySelectorAll("#tabs .tab").forEach(x=>x.setAttribute("aria-selected", x===t));
    render();
  });
});
document.querySelectorAll("#tabs .tab").forEach(x=>{
  x.setAttribute("aria-selected", x.dataset.region===state.region);
});

function bindChips(sel, key){
  document.querySelectorAll(sel+" .chip").forEach(c=>{
    c.addEventListener("click",()=>{
      state[key] = c.dataset.v;
      document.querySelectorAll(sel+" .chip").forEach(x=>x.setAttribute("aria-pressed", x===c));
      render();
    });
  });
}
bindChips("#fType","type");
bindChips("#fForm","form");

$("#tHideExpired").addEventListener("click",e=>{
  state.hideExpired = !state.hideExpired;
  e.currentTarget.setAttribute("aria-pressed", state.hideExpired);
  render();
});
$("#tNoRealname").addEventListener("click",e=>{
  state.noRealname = !state.noRealname;
  e.currentTarget.setAttribute("aria-pressed", state.noRealname);
  render();
});
$("#sort").addEventListener("change",e=>{ state.sort = e.target.value; render(); });

let timer;
$("#q").addEventListener("input",e=>{
  clearTimeout(timer);
  timer = setTimeout(()=>{ state.q = e.target.value.trim(); render(); }, 120);
});
document.addEventListener("keydown",e=>{
  if(e.key==="/" && document.activeElement!==$("#q")){ e.preventDefault(); $("#q").focus(); }
  if(e.key==="Escape" && document.activeElement===$("#q")){ $("#q").value=""; state.q=""; render(); $("#q").blur(); }
});

$("#buildInfo").textContent = "数据截至 " + META.built
  + " · " + pcount(DATA) + " 家平台 / " + DATA.length + " 个入口";
counts();
render();

/* 复制群号：file:// 下 clipboard API 不可用，回退到 execCommand */
(function(){
  const btn = $("#copyQ");
  if(!btn) return;
  const NUM = "__QQNUM__";
  const mark = txt => { btn.textContent = txt; btn.classList.add("done"); setTimeout(()=>{ btn.textContent="复制群号"; btn.classList.remove("done"); }, 1700); };
  const fallback = () => {
    const ta = document.createElement("textarea");
    ta.value = NUM; ta.setAttribute("readonly","");
    ta.style.cssText = "position:fixed;top:-1000px;opacity:0";
    document.body.appendChild(ta); ta.select();
    let ok = false;
    try { ok = document.execCommand("copy"); } catch(err) { ok = false; }
    ta.remove();
    mark(ok ? "已复制" : "请手动记下");
  };
  btn.addEventListener("click", ()=>{
    if(navigator.clipboard && window.isSecureContext){
      navigator.clipboard.writeText(NUM).then(()=>mark("已复制")).catch(fallback);
    } else { fallback(); }
  });
})();
</script>
</body>
</html>
"""


def prepare(items: list[dict], today: dt.date) -> list[dict]:
    out = []
    for it in items:
        d = _data.parse_date(it.get("expiry", ""))
        days = (d - today).days if d else None
        row = dict(it)
        row["days"] = days
        row["status"] = _data.status(it, today)
        out.append(row)
    return out


def main() -> int:
    items = _data.load()
    errs = _data.validate(items)
    if errs:
        print("数据有错，先修再生成：", file=sys.stderr)
        for e in errs:
            print("  !", e, file=sys.stderr)
        return 1

    today = dt.date.today()
    data = prepare(items, today)
    meta = {"built": today.isoformat(), "total": len(data)}

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # 防 </script> 提前闭合
    payload = payload.replace("</", "<\\/")

    if not os.path.exists(QR_FILE):
        print(f"缺少群二维码图片：{QR_FILE}", file=sys.stderr)
        return 1
    with open(QR_FILE, "rb") as fh:
        qr_b64 = base64.b64encode(fh.read()).decode("ascii")

    html = (
        TEMPLATE.replace("__DATA__", payload)
        .replace("__META__", json.dumps(meta, ensure_ascii=False))
        .replace("__QR__", qr_b64)
        .replace("__QQNAME__", QQ_NAME)
        .replace("__QQNUM__", QQ_GROUP)
        .replace("__NPROD__", str(len({d["product"] for d in data})))
        .replace("__NTOTAL__", str(len(data)))
    )

    os.makedirs(OUT_DIR, exist_ok=True)
    # 三种皮：默认暖白 / --cool 铜色描边 / --cosmic 深空宇宙
    skin = "cosmic" if "--cosmic" in sys.argv else ("cool" if "--cool" in sys.argv else "")
    out_file = os.path.join(OUT_DIR, skin + ".html") if skin else OUT_FILE
    css = {"cool": COOL_CSS, "cosmic": COSMIC_CSS}.get(skin)
    if css:
        html = html.replace("</head>", "<style>\n" + css + "\n</style>\n</head>", 1)
    if skin == "cosmic":
        # 仅深空版插入背景装饰层，原版结构不受影响
        html = html.replace(
            "<body>",
            '<body>\n<div class="sky-aurora" aria-hidden="true"></div>'
            '<div class="sky-vignette" aria-hidden="true"></div>',
            1,
        )
        html = html.replace(
            "<main>", '<div class="sky-hero" aria-hidden="true"></div>\n<main>', 1
        )
    with open(out_file, "w", encoding="utf-8") as fh:
        fh.write(html)

    size = os.path.getsize(out_file) / 1024
    cn = sum(1 for d in data if d["region"] == "cn")
    prods = {d["product"] for d in data}
    label = ("site/%s.html（%s）" % (skin, {"cool": "炫酷版", "cosmic": "深空版"}[skin])) if skin else "site/index.html"
    print(f"已生成 {label}：{len(data)} 个入口 / {len(prods)} 家平台（国内 {cn} / 海外 {len(data) - cn}），{size:.0f} KB")
    externals = html.count('src="http')
    print(f"外链数量：{externals} 个（应为 0）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
