#!/usr/bin/env python3
"""把 data/providers.yaml 编译成一个自包含的单文件网页 site/index.html。

零依赖、零外链、双击即用。数据以 JSON 内联，改完数据重跑本脚本即可。

用法：
    python3 scripts/build_site.py
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys

import _data

OUT_DIR = os.path.join(_data.ROOT, "site")
OUT_FILE = os.path.join(OUT_DIR, "index.html")

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>免费 AI API 额度雷达 · 免费 token / 积分 / Credits 清单</title>
<meta name="description" content="全网免费 AI API 额度清单：免费 token、免费积分、免费 Credits，国内外 69 条。每条带截止日、出处、可信度，过期自动报警。免费 API 白嫖必备。">
<meta name="keywords" content="免费api,免费 API,免费token,免费额度,白嫖,免费AI,大模型,API,free api,free tier,LLM">
<meta property="og:type" content="website">
<meta property="og:title" content="免费 AI API 额度雷达">
<meta property="og:description" content="69 条国内外免费 API 额度：免费 token、积分、Credits。带截止日、出处、可信度，过期自动报警。">
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
.statrow{display:flex; gap:20px; margin-left:auto}
.stat{text-align:center}
.stat b{display:block; font-size:20px; line-height:1.2; font-variant-numeric:tabular-nums}
.stat span{font-size:11.5px; color:var(--ink3)}

.sectionhead{
  display:flex; align-items:baseline; gap:10px; margin:30px 0 14px; padding-bottom:9px;
  border-bottom:1px solid var(--line);
}
.sectionhead h2{margin:0; font-size:14px; font-weight:700; letter-spacing:.01em}
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
        <button class="tab" role="tab" data-region="cn">国内<span class="n"></span></button>
        <button class="tab" role="tab" data-region="global">海外<span class="n"></span></button>
        <button class="tab" role="tab" data-region="all">全部<span class="n"></span></button>
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

<footer>
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

function counts(){
  const c = {cn:0, global:0, all:DATA.length};
  DATA.forEach(d => c[d.region]++);
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
         +  '<span class="cnt">'+arr.length+' 个产品</span></div>';
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
  const regionLabel = state.region === "cn" ? `国内 ${n} 条`
                    : state.region === "global" ? `海外 ${n} 条`
                    : `全部 ${n} 条`;
  $("#lede").innerHTML = `
    <div>
      <h2>${regionLabel}</h2>
      <p>免费 API、免费 token、签到积分、Credits 都在这里。同一个 AI 在不同入口的免费政策完全不同，所以按 <b class="k">产品 × 形态</b> 拆开写，一条只讲一个入口。</p>
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

$("#buildInfo").textContent = "数据截至 " + META.built + " · 共 " + DATA.length + " 条 · 国内 " + DATA.filter(d=>d.region==="cn").length + " / 海外 " + DATA.filter(d=>d.region==="global").length;
counts();
render();
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
    html = TEMPLATE.replace("__DATA__", payload).replace(
        "__META__", json.dumps(meta, ensure_ascii=False)
    )

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(html)

    size = os.path.getsize(OUT_FILE) / 1024
    cn = sum(1 for d in data if d["region"] == "cn")
    print(f"已生成 site/index.html：{len(data)} 条（国内 {cn} / 海外 {len(data) - cn}），{size:.0f} KB")
    print(f"外链数量：{html.count('src=\"http')} 个（应为 0）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
