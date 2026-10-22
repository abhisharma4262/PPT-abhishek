"""
mkit: HTML slide kit for Myridius decks.

Design each slide as absolutely positioned HTML on a 1920 x 1080 canvas (144 px = 1 inch,
1 pt = 2 px), preview it in a browser, then run html2pptx.py and merge_into_template.py.

The header (eyebrow, title, subtitle) is drawn at the exact positions used in the
Myridius 2026 template, so slides drop into the template without moving anything.
The template layout supplies the Myridius logo (bottom left) and the copyright + page
number (bottom right). Never draw your own logo, footer or page number.

Safe zones (px):  content x 59..1860, y 190..958 (y 160.. when there is no subtitle).
Keep y > 965 empty: the logo and footer live there.
Type floor: nothing below 18 px (9 pt), including labels, chips, badges and source lines.

Export features: <a href> becomes a clickable link; class "strike" or line-through becomes strikethrough;
data-grp="name" (+ data-rot="-2") groups and rotates shapes; data-anim="1", "2w"... adds entrance steps
(run tools/group_anim.py after merge_into_template.py). See tools/patterns.py for brochure-style visuals.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icons import IC

# ---------------------------------------------------------------- palette (Myridius 2026 theme)
MOSS, LEAF, SLATE, TEAL = '#0C2226', '#194247', '#337077', '#09A78D'
MINT, PULSE, SAGE, BEIGE = '#D2F0C6', '#52E081', '#CBEBBD', '#F6F3F0'
WHITE = '#FFFFFF'

# ---------------------------------------------------------------- icons
# House style (from the deck owner's own edits): the glyph fills about three quarters of its round
# tile and the line is thin, about 1/2 to 3/4 pt whatever the icon size. Dark teal (Leaf) on mint
# tiles, Pulse on dark tiles. Pass sw only when a slide needs something different.
STROKE_PT = 0.75       # rendered stroke width in points (1 pt = 2 px on the canvas)
ICON_RATIO = 0.72      # glyph size relative to its round tile

def _sw(size):
    """viewBox stroke width that renders at STROKE_PT for an icon drawn at `size` px."""
    return STROKE_PT * 2 * 24 / size

def icon(name, size=22, color=LEAF, sw=None):
    """Inline SVG icon (exports as an editable SVG picture). sw is in viewBox units (24 grid)."""
    sw = _sw(size) if sw is None else sw
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw:.2f}" stroke-linecap="round" stroke-linejoin="round">{IC[name]}</svg>')

def ico(name, v='lt', size=40, isz=None, sw=None):
    """Icon inside a round tile. v: lt (mint tile), dk (moss tile), lf (leaf tile), pu (pulse tile), ol (outline), wh (white).
    Size the tile to the need (40 to 76 px is typical); the glyph follows at ICON_RATIO."""
    isz = isz or int(round(size * ICON_RATIO))
    col = {'lt': LEAF, 'dk': PULSE, 'ol': LEAF, 'lf': MINT, 'pu': MOSS, 'wh': LEAF}[v]
    return f'<span class="ico {v}" style="width:{size}px;height:{size}px">{icon(name, isz, col, sw)}</span>'

def gicon(name, cx, cy, size=22, color=MOSS, sw=None):
    """Icon inside an SVG layer, centred on (cx, cy). sw is the rendered stroke in canvas px."""
    s = size / 24
    sw = STROKE_PT * 2 if sw is None else sw
    return (f'<g transform="translate({cx-size/2:.1f},{cy-size/2:.1f}) scale({s:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw/s:.2f}" stroke-linecap="round" stroke-linejoin="round">{IC[name]}</g>')

ARROW_DEFS = f'''<defs>
<marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="{MOSS}"/></marker>
<marker id="ahl" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="{LEAF}"/></marker>
<marker id="ahm" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="{MINT}"/></marker>
<marker id="aht" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="{TEAL}"/></marker>
<marker id="ahs" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="{SLATE}"/></marker>
</defs>'''

def svg(content):
    """Full-slide SVG layer. Paths use M/L/Q/C/Z only (arcs: use arc_c). Put it first in the slide
    list to draw beneath HTML, last to draw above."""
    return f'<svg class="abs" style="left:0;top:0" width="1920" height="1080">{ARROW_DEFS}{content}</svg>'

# ---------------------------------------------------------------- header (template geometry)
def header(eyebrow, title, sub=None, accent=None, two_line=False):
    """eyebrow: 1-3 words, shown in caps (section of the story), or None when the slide does not need one.
    title: the message of the slide, one line (two only when the user asks).
    sub: one line of context, only when the slide needs it.
    accent: phrase inside the title to colour teal; use it wherever a phrase carries the message."""
    t = title
    if accent and accent in t:
        t = t.replace(accent, f'<em>{accent}</em>', 1)
    o = ([f'<div class="eyebrow">{eyebrow}</div>'] if eyebrow else []) + \
        [f'<h1 class="title{" t2" if two_line else ""}"><span>{t}</span></h1>']
    if sub:
        o.append(f'<p class="sub{" s2" if two_line else ""}">{sub}</p>')
    return '\n'.join(o)

# ---------------------------------------------------------------- text and band helpers
def banner(x, y, w, h, ic, label, msg='', fs=21):
    """Takeaway band (dark Leaf strip). Order is always: icon, then the label, then the message."""
    m = f'<span style="font-size:{fs}px;white-space:normal;margin-left:10px">{msg}</span>' if msg else ''
    return (f'<div class="band" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;padding:0 30px;gap:16px">'
            f'{icon(ic, 30, PULSE)}<span class="lbl" style="color:var(--pulse);font-size:18px">{label}</span>{m}</div>')

def band_items(x, y, w, h, ic, label, items, fs=21):
    """Band with a label and separate items, each with its own icon, split by thin divider lines.
    Use this instead of joining items with dots or bullets (the owner reads separator dots as AI slop).
    items: [(icon, text), ...]"""
    o = [f'<div class="band" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;padding:0 30px;gap:16px">'
         f'{icon(ic, 30, PULSE)}<span class="lbl" style="color:var(--pulse);font-size:18px">{label}</span>']
    for i, (iic, t) in enumerate(items):
        if i:
            o.append('<span style="width:1.5px;height:34px;background:rgba(210,240,198,.35);flex:none;margin:0 6px"></span>')
        o.append(f'<span style="display:flex;align-items:center;gap:10px;font-size:{fs}px;color:#fff;margin-left:{6 if i else 18}px">'
                 f'{icon(iic, 26, MINT)}<span>{t}</span></span>')
    return ''.join(o) + '</div>'

def link(url, text):
    """Hyperlinked text (exports as a clickable PowerPoint link, underlined, in the surrounding colour)."""
    return f'<a href="{url}">{text}</a>'

def sources_line(x, y, items, w=1800, prefix='Sources: '):
    """Source line with every source linked. items: [(label, url), ...]. Labels name the source only, no
    dates ("Gartner predictions", "Fiserv Investor Day"); the link carries the detail. For several sources on
    one slide, put superscripts on the claims and here: [('¹ Fiserv Investor Day', url), ...]."""
    body = '; '.join(link(u, t) if u else t for t, u in items)
    return f'<div class="src" style="left:{x}px;top:{y}px;width:{w}px">{prefix}{body}</div>'

def metric_list(items):
    """'What it moves': metrics with their direction, as a two-column list (instead of pills).
    items: [('up' | 'down', text), ...]"""
    cells = ''.join(f'<div class="mv"><span class="mva">{"&#8593;" if d == "up" else "&#8595;"}</span><span>{t}</span></div>' for d, t in items)
    return f'<div class="mvg">{cells}</div>'

def badge(letter, v='dk', size=42):
    """Small square theme badge (A, B, C). v: dk (moss with pulse letter) or pu (pulse with moss letter)."""
    return (f'<span class="thb {v}" style="width:{size}px;height:{size}px;font-size:{size // 2}px;line-height:{size}px;'
            f'border-radius:{max(6, size // 4)}px">{letter}</span>')

def dot_list(items, size=20, gap=10, color=None):
    """Bulleted list with teal dots. Use this instead of <ul>/<li>: list markers are lost in the PPTX export."""
    c = f';color:{color}' if color else ''
    return ''.join(f'<div class="sli" style="font-size:{size}px;margin-bottom:{gap}px{c}"><span class="dot"></span><span>{t}</span></div>'
                   for t in items)

def tick_list(items, size=20, gap=12, color=TEAL):
    """List with a thin check icon before each item."""
    return ''.join(f'<div class="tick" style="font-size:{size}px;margin-bottom:{gap}px">{icon("check", 22, color)}<span>{t}</span></div>'
                   for t in items)

def legend(x, y, items):
    """Ownership key, e.g. legend(59, 206, [('dk', 'Myridius'), ('lt', 'Client and partners')])."""
    parts = ''.join(f'<span style="display:flex;align-items:center;gap:8px"><span class="sw {k}"></span>{t}</span>' for k, t in items)
    return (f'<div style="left:{x}px;top:{y}px;display:flex;align-items:center;gap:22px;'
            f'font:400 18px/1 var(--f);color:var(--slate)">{parts}</div>')

# ---------------------------------------------------------------- geometry helpers
def arc_c(cx, cy, r, t0, t1):
    """Cubic bezier segments for an arc t0 -> t1 (radians). Returns a path fragment without M."""
    out = ''
    n = max(1, math.ceil(abs(t1 - t0) / (math.pi / 2) - 1e-9))
    d = (t1 - t0) / n
    for i in range(n):
        a, b = t0 + i * d, t0 + (i + 1) * d
        k = 4 / 3 * math.tan((b - a) / 4)
        p0 = (cx + r * math.cos(a), cy + r * math.sin(a)); p3 = (cx + r * math.cos(b), cy + r * math.sin(b))
        p1 = (p0[0] - k * r * math.sin(a), p0[1] + k * r * math.cos(a))
        p2 = (p3[0] + k * r * math.sin(b), p3[1] - k * r * math.cos(b))
        out += f' C{p1[0]:.2f},{p1[1]:.2f} {p2[0]:.2f},{p2[1]:.2f} {p3[0]:.2f},{p3[1]:.2f}'
    return out

def seg_path(cx, cy, ro, ri, a0, a1):
    """Donut segment between angles a0 and a1 (degrees, 0 = 3 o'clock, clockwise)."""
    t0, t1 = math.radians(a0), math.radians(a1)
    s = f'M{cx + ro*math.cos(t0):.2f},{cy + ro*math.sin(t0):.2f}' + arc_c(cx, cy, ro, t0, t1)
    s += f' L{cx + ri*math.cos(t1):.2f},{cy + ri*math.sin(t1):.2f}' + arc_c(cx, cy, ri, t1, t0) + ' Z'
    return s

def curved_label(pid, cx, cy, r, a0, a1, text, size=15, color=WHITE, upright_bottom=None):
    """Text along an arc (exports as per-letter rotated text boxes). Returns (defs, text)."""
    t0, t1 = math.radians(a0), math.radians(a1)
    bottom = (a0 % 360) < 180 if upright_bottom is None else upright_bottom
    if not bottom:
        d = f'M{cx + r*math.cos(t0):.1f},{cy + r*math.sin(t0):.1f} A{r},{r} 0 0 1 {cx + r*math.cos(t1):.1f},{cy + r*math.sin(t1):.1f}'
    else:
        d = f'M{cx + r*math.cos(t1):.1f},{cy + r*math.sin(t1):.1f} A{r},{r} 0 0 0 {cx + r*math.cos(t0):.1f},{cy + r*math.sin(t0):.1f}'
    return (f'<path id="{pid}" d="{d}"/>',
            f'<text class="arct" fill="{color}" font-size="{size}" dy="{size*0.35:.0f}"><textPath href="#{pid}" startOffset="50%" text-anchor="middle">{text}</textPath></text>')

def harvey(cx, cy, q, r=12, dark=False):
    """Harvey ball, q = 0..4 quarters. Use only when the user wants scoring."""
    ring_c = MINT if dark else MOSS
    fillc = PULSE if dark else MOSS
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{MOSS if dark else WHITE}" stroke="{ring_c}" stroke-width="2"/>'
    if q >= 4:
        out += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fillc}" stroke="{ring_c}" stroke-width="2"/>'
    elif q > 0:
        d = f'M{cx},{cy} L{cx},{cy - r}' + arc_c(cx, cy, r, math.radians(-90), math.radians(-90 + 90 * q)) + ' Z'
        out += f'<path d="{d}" fill="{fillc}"/>'
    return out

def chevron_down(cx, cy, r=12):
    return (f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="{WHITE}" stroke="{LEAF}" stroke-width="1.5"/>'
            f'<path d="M{cx-4.5:.1f},{cy-2:.1f} L{cx:.1f},{cy+3:.1f} L{cx+4.5:.1f},{cy-2:.1f}" fill="none" stroke="{LEAF}" stroke-width="2"/>')

# ---------------------------------------------------------------- CSS
CSS = r'''
:root{--moss:#0C2226;--leaf:#194247;--slate:#337077;--teal:#09A78D;--mint:#D2F0C6;--pulse:#52E081;--sage:#CBEBBD;--beige:#F6F3F0;
--m04:rgba(12,34,38,.04);--m06:rgba(12,34,38,.06);--m10:rgba(12,34,38,.10);--m16:rgba(12,34,38,.16);
--f:'Segoe UI','Segoe UI Web (West European)',-apple-system,Roboto,'Helvetica Neue',Arial,sans-serif}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#E7ECEC;font-family:var(--f);color:var(--moss);-webkit-font-smoothing:antialiased;padding:28px 0}
.frame{position:relative;margin:0 auto 28px;width:calc(1920px*var(--s));height:calc(1080px*var(--s));box-shadow:0 12px 40px rgba(12,34,38,.10);background:#fff}
.slide{position:absolute;left:0;top:0;width:1920px;height:1080px;transform:scale(var(--s));transform-origin:0 0;background:#fff;overflow:hidden;font-family:var(--f)}
.slide>*,.card>*,.panel>*{position:absolute}
.abs{position:absolute!important}
.ic{flex:none}
/* preview-only template furniture (not exported: class "tpl") */
.tpl{pointer-events:none}
.tpl.logo{left:49px;bottom:28px;font:700 34px/1 var(--f);color:var(--moss);letter-spacing:-.02em}
.tpl.logo i{font-style:normal;color:var(--pulse)}
.tpl.copy{right:66px;bottom:36px;font:400 13px/1 var(--f);color:#9AA7A9}
.tpl.copy b{color:var(--teal);font-weight:400;margin-left:40px}
/* header: positions match the Myridius 2026 template */
.eyebrow{left:63px;top:30px;height:24px;display:flex;align-items:center;font:700 20px/1 var(--f);letter-spacing:4.2px;text-transform:uppercase;color:var(--teal);white-space:nowrap}
h1.title{left:59px;top:52px;width:1800px;margin:0;font:700 56px/1.15 var(--f);letter-spacing:-.01em;color:var(--leaf);white-space:nowrap}
h1.title em{font-style:normal;color:var(--teal)}
h1.title.t2{white-space:normal}
.sub{left:62px;top:132px;width:1780px;margin:0;font:400 24px/1.35 var(--f);color:var(--leaf);white-space:nowrap}
.sub.s2{top:196px}
/* text helpers */
.lbl{font:700 22px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;color:var(--teal);white-space:nowrap}
.lbl.sl{color:var(--slate)}
.h3{font:700 26px/1.2 var(--f);color:var(--leaf)}
.p{font:400 21px/1.4 var(--f);color:var(--leaf)}
.sm{font:400 18px/1.4 var(--f);color:var(--slate)}
/* icon tiles */
.ico{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;flex:none;position:relative}
.ico.lt{background:var(--mint)} .ico.dk{background:var(--moss)} .ico.lf{background:var(--leaf)}
.ico.pu{background:var(--pulse)} .ico.ol{border:1.5px solid var(--moss);background:#fff} .ico.wh{background:#fff}
/* cards and panels */
.card{border-radius:16px;background:#fff;border:1.5px solid var(--m16)}
.card.soft{background:var(--m04);border-color:var(--m10)}
.card.dk{background:var(--moss);border-color:var(--moss)}
.panel{border-radius:18px;background:var(--moss)}
.band{border-radius:14px;background:var(--leaf);display:flex;align-items:center;gap:16px;padding:0 26px;font:400 20px/1.35 var(--f);color:var(--mint)}
.band b{color:#fff}
.chip{display:inline-flex;align-items:center;gap:8px;border-radius:999px;background:var(--mint);padding:7px 14px;font:600 18px/1 var(--f);color:var(--moss);white-space:nowrap}
.chip.ol{background:#fff;border:1.5px solid var(--m16)}
.tag{display:inline-block;border-radius:999px;padding:6px 12px;font:700 18px/1 var(--f);letter-spacing:.1em;text-transform:uppercase;background:var(--pulse);color:var(--moss)}
.num{width:44px;height:44px;border-radius:50%;border:2px solid var(--moss);display:flex;align-items:center;justify-content:center;font:700 20px/1 var(--f);color:var(--moss);background:#fff}
.tick{display:flex;gap:10px;align-items:flex-start;margin-bottom:10px;font:400 20px/1.4 var(--f);color:var(--leaf)}
.tick svg{margin-top:4px}
.sli{display:flex;gap:12px;align-items:flex-start;font-weight:400;line-height:1.4;color:var(--leaf)}
.dot{width:8px;height:8px;border-radius:50%;background:var(--teal);flex:none;margin-top:.55em;display:inline-block}
.sw{width:18px;height:18px;border-radius:4px;display:inline-block}
.sw.dk{background:var(--moss)} .sw.lt{background:var(--m04);border:1.5px solid var(--m16)}
.sw>*,.band>*{position:static}
.arct{font-family:var(--f);font-weight:700;letter-spacing:5px}
/* links, strike, sources, metrics, badges */
a{color:inherit;text-decoration:underline}
.strike{text-decoration:line-through}
.src{font:400 18px/1.35 var(--f);color:var(--slate)}
.src a{color:var(--slate)}
.mvg{display:grid;grid-template-columns:1fr 1fr;column-gap:22px;row-gap:12px}
.mv{display:flex;align-items:center;gap:10px;font:600 19px/1.25 var(--f);color:var(--leaf)}
.mva{width:28px;height:28px;border-radius:8px;background:var(--mint);color:var(--leaf);font:700 18px/28px var(--f);text-align:center;flex:none;display:inline-block}
.thb{display:inline-block;text-align:center;flex:none;font-family:var(--f);font-weight:700}
.thb.dk{background:var(--moss);color:var(--pulse)} .thb.pu{background:var(--pulse);color:var(--moss)}
'''

JS = r'''
(function(){
  function fit(){var s=Math.min(1,(window.innerWidth-48)/1920);document.documentElement.style.setProperty('--s',s);}
  fit();window.addEventListener('resize',fit);
})();
'''

PREVIEW_FURNITURE = '<div class="tpl logo">myridius<i>.</i></div><div class="tpl copy">©2026 Myridius. All rights reserved<b>{n}</b></div>'

def write_deck(path, slides, extra_css='', title='Myridius deck', preview_furniture=True):
    """slides: list of HTML strings (one per slide). Writes a browsable HTML deck.
    Preview furniture shows where the template logo and footer will sit; it is skipped on export."""
    body = []
    for i, s in enumerate(slides, 1):
        furn = PREVIEW_FURNITURE.format(n=i + 1) if preview_furniture else ''
        body.append(f'<section class="frame" id="s{i}"><div class="slide">{s}{furn}</div></section>')
    html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{title}</title><style>{CSS}{extra_css}</style></head><body style="--s:1">\n' + '\n'.join(body) +
            f'\n<script>{JS}</script></body></html>')
    open(path, 'w', encoding='utf-8').write(html)
    return path
