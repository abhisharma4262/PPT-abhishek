"""
patterns: brochure-style visuals for Myridius decks (the look AI product companies use in their decks).

These are starting points, not a menu. Pick a pattern only when it is the clearest picture of the slide's
message, and do not repeat one pattern across a deck by default. Every pattern exports as editable shapes.

  scatter_hub_card()  messy inputs (slightly rotated chips, noise struck through) converge on a hub, and one
                      clean output card comes out. Message: "AI turns scattered X into one clean Y".
                      Used and liked: knowledge sources to one trusted answer (A1); support tickets to a
                      triaged queue (C1). Animates well (inputs, lines, hub, output, notes).
  out_card()          the clean output card on its own: header, tag, sections of rows. Also good as a
                      product-style "result" panel next to any diagram.
  ui_window()         a product window (title bar with three dots and a name) that frames panes, so a
                      process reads as one tool. Used for "one agent desktop, three moments". Keep static.
  flow_ribbons()      a source splitting into ribbons whose widths show where volume lands (Sankey style).
                      Tried for L1/L2 support and the owner preferred scatter_hub_card there; use it when
                      proportions between destinations are the message, label it "Illustrative".

Building blocks (from the visual style catalogue, examples/style_catalogue.py). Use them to build any new
picture the content calls for; they are parts, not slide layouts:
  text_box()   positioned text block (children flow inside it)       anim()        wrap HTML in one entrance step
  chat_bubble(), avatar()   chat messages for conversation mock-ups   node()        workflow / action card (ai, hu, dc)
  port(), edge()            connector dots and arrows (SVG)           mini_row()    small beige row with icon and status
  bento_cell()              card with icon, title, line and a body    steps_track() progress dots with labels
  iso_plate()               one 3D (isometric) layer for stacks       ring_points(), orbit_pill()  nodes on a ring
  loop_arcs()               arrowed arcs between nodes on a circle    waffle()      10 x 10 grid for one percentage

Animation rule: add data-anim steps only when motion carries the meaning (things converging, a flow
building up). Structural pictures (windows, grids, tables, stacks) stay static.

Usage:
    from mkit import *
    from patterns import PATTERN_CSS, scatter_hub_card, out_card, ui_window, flow_ribbons
    write_deck(path, slides, EXTRA_CSS + PATTERN_CSS, title)
"""
import math
from mkit import icon, ico, gicon, arc_c, MOSS, LEAF, SLATE, TEAL, MINT, PULSE, WHITE

PATTERN_CSS = r'''
.flow{position:absolute}
.flow *{position:static}
.t{position:absolute}
.t *{position:static}
[data-anim]>.card,[data-anim]>.band,[data-anim]>.panel{position:absolute}
.nh{font:700 21px/1.2 var(--f);color:var(--leaf)}
.ns{font:400 18px/1.3 var(--f);color:var(--slate)}
.bub{position:absolute;border-radius:20px;padding:13px 20px;font:400 20px/1.4 var(--f);color:var(--moss)}
.bub.c{background:var(--mint);border-bottom-right-radius:6px}
.bub.a{background:var(--beige);border-bottom-left-radius:6px}
.node{position:absolute;border-radius:14px;background:#fff;border:1.5px solid var(--m16);display:flex;align-items:center;gap:14px;padding:0 16px}
.node>*{position:static}
.node.ai{background:var(--moss);border-color:var(--moss)}
.node.ai .nh{color:#fff} .node.ai .ns{color:var(--mint)}
.node.hu{background:var(--mint);border-color:var(--mint)}
.node.dc{border-style:dashed;border-color:var(--slate)}
.tkt{border-radius:14px;background:#fff;border:1.5px solid var(--m10);box-shadow:0 8px 22px rgba(12,34,38,.08);display:flex;align-items:center;gap:12px;padding:0 18px;font:500 19px/1.2 var(--f);color:var(--leaf);white-space:nowrap}
.tkt>*{position:static}
.tkt.nz{background:#FBFAF8;box-shadow:none;color:var(--slate);opacity:.62}
.oc>*{position:absolute}
.oc{border-radius:22px;background:#fff;border:1.5px solid var(--m10);box-shadow:0 18px 44px rgba(12,34,38,.12)}
.orow{border-radius:12px;background:var(--beige);display:flex;align-items:center;gap:12px;padding:0 16px;font:400 18px/1.2 var(--f);color:var(--leaf);white-space:nowrap}
.orow>*{position:static}
.osec{display:flex;align-items:center;gap:10px;font:700 21px/1 var(--f);color:var(--leaf)}
.osec>*{position:static}
.odot{width:10px;height:10px;border-radius:50%;background:var(--teal);display:inline-block;flex:none}
.otag{border-radius:999px;background:var(--mint);padding:7px 14px;font:600 18px/1 var(--f);color:var(--leaf);white-space:nowrap}
.win{border-radius:18px;background:#fff;border:1.5px solid var(--m16);box-shadow:0 18px 44px rgba(12,34,38,.10)}
.wbar{border-radius:18px 18px 0 0;background:var(--m04);border-bottom:1.5px solid var(--m10)}
.wd{width:12px;height:12px;border-radius:50%;display:inline-block;background:rgba(12,34,38,.16)}
'''


def chip_width(text, size=19):
    """Rough width of a chip for its text (Inter metrics; Segoe UI is narrower, so it fits in PowerPoint)."""
    return int(len(text) * size * 0.53 + 74)


def out_card(x, y, w, h, ic, title, sub, tag, sections, foot=None):
    """Clean output card. sections: [(heading or None, [(icon, text, right_icon or None), ...]), ...].
    Rows are 40 px high and single-line: keep row text under about 38 characters at w = 484."""
    inner = [f'<div class="flow" style="left:26px;top:22px;right:24px;display:flex;align-items:center;gap:16px">'
             f'<span class="ico dk" style="width:56px;height:56px;border-radius:14px">{icon(ic, 32, PULSE)}</span>'
             f'<div style="flex:1"><div style="font:700 25px/1.15 var(--f);color:var(--moss);white-space:nowrap">{title}</div>'
             f'<div style="display:flex;align-items:center;margin-top:6px"><span style="font:400 18px/1.3 var(--f);color:var(--slate);white-space:nowrap">{sub}</span>'
             + (f'<span class="otag" style="margin-left:auto">{tag}</span>' if tag else '') + '</div></div></div>',
             f'<div style="left:26px;top:100px;width:{w - 52}px;height:1.5px;background:var(--m10)"></div>']
    yy = 116
    for head, rows in sections:
        if head:
            inner.append(f'<div class="osec" style="left:26px;top:{yy}px;height:30px"><span class="odot"></span><span>{head}</span></div>')
            yy += 34
        for ric, t, mark in rows:
            right = f'<span style="margin-left:auto;display:flex">{icon(mark, 22, TEAL)}</span>' if mark else ''
            inner.append(f'<div class="orow" style="left:26px;top:{yy}px;width:{w - 52}px;height:40px">{icon(ric, 20, SLATE)}<span>{t}</span>{right}</div>')
            yy += 45
        yy += 8
    if foot:
        inner.append(f'<div style="left:26px;top:{h - 40}px;font:italic 400 18px/1.2 var(--f);color:var(--slate)">{foot}</div>')
    return f'<div class="oc" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px">{"".join(inner)}</div>'


def scatter_hub_card(chips, hub, hub_icon, hub_title, hub_sub, card, notes=None, animate=True):
    """Messy inputs converge on a hub; one clean card comes out.
    chips: [(x, y, text, icon, rotation_deg, is_noise), ...] (6 to 8 chips; 1 or 2 noise; rotations within +-3).
    Keep chip right edges at least 60 px left of the hub glow, and the lowest chip's line clear of the hub caption.
    hub: (cx, cy). card: html from out_card(). notes: (y, [(icon, text), ...]) small lines under the chips.
    animate: entrance steps 1 inputs, 2 lines (wipe), 3 hub, 4 output, 5 notes."""
    a = (lambda n: f' data-anim="{n}"') if animate else (lambda n: '')
    hx, hy = hub
    real = [c for c in chips if not c[5]]
    n = len(real)
    lines = []
    for k, (x, y, t, ic, rot, nz) in enumerate(real):
        sx, sy = x + chip_width(t) + 4, y + 27
        ey, ex = hy + (k - (n - 1) / 2) * 12, hx - 70
        lines.append(f'<path d="M{sx},{sy} C{sx + (ex - sx) * 0.55:.0f},{sy} {ex - (ex - sx) * 0.45:.0f},{ey:.0f} {ex},{ey:.0f}" '
                     f'stroke="{TEAL}" stroke-opacity=".55" stroke-width="2" fill="none"/>')
    o = [f'<svg class="abs"{a("2w")} style="left:0;top:0" width="1920" height="1080">{"".join(lines)}</svg>']
    cs = []
    for k, (x, y, t, ic, rot, nz) in enumerate(chips):
        txt = f'<span class="strike">{t}</span>' if nz else f'<span>{t}</span>'
        cs.append(f'<div class="tkt{" nz" if nz else ""}" data-grp="chip{k}" data-rot="{rot}" style="position:absolute;left:{x}px;top:{y}px;width:{chip_width(t)}px;height:54px">'
                  f'{icon(ic, 22, SLATE if nz else LEAF)}{txt}</div>')
    o.append(f'<div{a(1)} style="left:0;top:0;width:0;height:0">{"".join(cs)}</div>')
    o.append(f'<svg class="abs"{a(3)} style="left:0;top:0" width="1920" height="1080">'
             f'<circle cx="{hx}" cy="{hy}" r="98" fill="{MINT}" fill-opacity=".32"/>'
             f'<circle cx="{hx}" cy="{hy}" r="78" fill="{MINT}" fill-opacity=".7"/>'
             f'<circle cx="{hx}" cy="{hy}" r="60" fill="{MOSS}"/>' + gicon(hub_icon, hx, hy, 50, PULSE, 2) + '</svg>')
    o.append(f'<div class="flow"{a(3)} style="left:{hx - 140}px;top:{hy + 108}px;width:280px;text-align:center">'
             f'<div style="font:700 19px/1.2 var(--f);letter-spacing:.08em;text-transform:uppercase;color:var(--teal)">{hub_title}</div>'
             f'<div style="font:400 18px/1.35 var(--f);color:var(--slate);margin-top:6px">{hub_sub}</div></div>')
    o.append(f'<svg class="abs"{a(4)} style="left:0;top:0" width="1920" height="1080">'
             f'<path d="M{hx + 102},{hy} L{hx + 142},{hy}" stroke="{TEAL}" stroke-width="3" marker-end="url(#ah)"/></svg>')
    o.append(f'<div{a(4)} style="left:0;top:0;width:0;height:0">{card}</div>')
    if notes:
        ny, items = notes
        x0 = min(c[0] for c in chips)
        o.append(f'<div class="flow"{a(5)} style="left:{x0}px;top:{ny}px;width:470px">'
                 + ''.join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;font:400 18px/1.3 var(--f);color:var(--slate)">{icon(ic, 22, SLATE)}<span>{t}</span></div>' for ic, t in items)
                 + '</div>')
    return '\n'.join(o)


def ui_window(x, y, w, h, name, inner_html):
    """A product window frame (title bar, three dots, window name) around positioned content.
    inner_html is positioned in slide coordinates; leave 70 px at the top for the bar."""
    return (f'<div class="win" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
            f'<div class="wbar" style="left:{x}px;top:{y}px;width:{w}px;height:48px"></div>'
            f'<div class="flow" style="left:{x + 22}px;top:{y}px;height:48px;display:flex;align-items:center;gap:8px">'
            '<span class="wd"></span><span class="wd"></span><span class="wd"></span>'
            f'<span style="margin-left:16px;font:600 18px/1 var(--f);color:var(--slate)">{name}</span></div>' + inner_html)


def flow_ribbons(src_x, mid_x, dst_x, y0, total_h, tiers, gap=18, node_w=26, label_x=None):
    """Source band into a middle node, then ribbons to destinations sized by share.
    tiers: [(title, description, height_px, colour, opacity), ...]; heights add up to total_h.
    Returns (svg_parts, html_parts). Label the visual "Illustrative" unless the widths are real data."""
    s, body = [], []
    mid = (mid_x + node_w + dst_x) / 2
    s.append(f'<rect x="{src_x}" y="{y0}" width="{node_w}" height="{total_h}" rx="6" fill="{MOSS}"/>')
    s.append(f'<path d="M{src_x + node_w},{y0} L{mid_x},{y0} L{mid_x},{y0 + total_h} L{src_x + node_w},{y0 + total_h} Z" fill="{MINT}" fill-opacity=".75"/>')
    span = total_h + gap * (len(tiers) - 1)
    ty, dy = y0, y0 - (span - total_h) / 2
    lx = label_x or dst_x + 44
    for t, d, hh, col, op in tiers:
        a0, a1, b0, b1 = ty, ty + hh, dy, dy + hh
        x0 = mid_x + node_w
        s.append(f'<path d="M{x0},{a0} C{mid:.0f},{a0} {mid:.0f},{b0:.0f} {dst_x},{b0:.0f} L{dst_x},{b1:.0f} C{mid:.0f},{b1:.0f} {mid:.0f},{a1} {x0},{a1} Z" fill="{col}" fill-opacity="{op}"/>')
        s.append(f'<rect x="{dst_x}" y="{b0:.0f}" width="{node_w}" height="{hh}" rx="6" fill="{col}"/>')
        body.append(f'<div class="flow" style="left:{lx}px;top:{b0 + hh / 2 - 30:.0f}px;height:60px;width:410px;display:flex;flex-direction:column;justify-content:center">'
                    f'<div style="font:700 21px/1.2 var(--f);color:var(--leaf)">{t}</div>'
                    f'<div style="font:400 18px/1.3 var(--f);color:var(--slate);margin-top:3px">{d}</div></div>')
        ty += hh; dy += hh + gap
    s.append(f'<rect x="{mid_x}" y="{y0}" width="{node_w}" height="{total_h}" rx="6" fill="{TEAL}"/>')
    return s, body


# ---------------------------------------------------------------- building blocks (style catalogue)
def text_box(x, y, w, inner, style=''):
    """Positioned text block; everything inside flows normally. Wrap each text run in its own element when
    mixing it with icons or swatches in a flex row (bare text nodes merge into one text box on export)."""
    return f'<div class="t" style="left:{x}px;top:{y}px;width:{w}px;{style}">{inner}</div>'


def anim(step, html):
    """Wrap positioned HTML in one entrance step (e.g. anim(2, ...) or anim('3w', ...)). Cards and bands inside
    (and panels) stay absolutely positioned. Keep each step's blocks next to each other in the slide's paint order."""
    return f'<div data-anim="{step}" style="left:0;top:0;width:0;height:0">{html}</div>'


def chat_bubble(x, y, w, text, who='customer', bg=None):
    """Chat message. who: 'customer' (mint, right-hand speaker) or 'agent' (beige; pass bg='#fff' on dark panels).
    Height follows the text (20 px, line height 1.4, 13 px padding): about 56 px per line plus 28 px per extra line."""
    cls = 'c' if who == 'customer' else 'a'
    b = f'background:{bg};' if bg else ''
    return f'<div class="bub {cls}" style="left:{x}px;top:{y}px;width:{w}px;{b}">{text}</div>'


def avatar(x, y, ic='agent', size=40):
    """Small round avatar beside an agent's chat bubble."""
    return f'<span class="ico lt" style="position:absolute;left:{x}px;top:{y}px;width:{size}px;height:{size}px">{icon(ic, int(size * .7), LEAF)}</span>'


def node(x, y, w, h, ic, title, sub='', kind='', tile=50, step=None):
    """Workflow or action card: icon tile, bold title, slate line. kind: '' system (white), 'ai' (Moss, Pulse icon),
    'hu' person (Mint), 'dc' decision (dashed), 'act' (white with a dark icon tile, for actions an agent took)."""
    v = {'ai': 'pu', 'hu': 'wh', 'act': 'dk'}.get(kind, 'lt')
    cls = {'ai': ' ai', 'hu': ' hu', 'dc': ' dc'}.get(kind, '')
    a = f' data-anim="{step}"' if step is not None else ''
    s = f'<div class="ns">{sub}</div>' if sub else ''
    return (f'<div class="node{cls}"{a} style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{ico(ic, v, tile)}'
            f'<div><div class="nh">{title}</div>{s}</div></div>')


def port(x, y):
    """Connector dot on the edge of a node (SVG; put inside an svg() or edge() layer)."""
    return f'<circle cx="{x}" cy="{y}" r="7" fill="{WHITE}" stroke="{SLATE}" stroke-width="2"/>'


def edge(d, step=None, color=LEAF, marker='ahl', extra='', dash=None, width=2.5):
    """One arrowed connector as its own SVG layer (so it can be a separate animation step).
    d: path with M, L, C, Q only. marker: ahl (Leaf), aht (Teal), ahs (Slate), ah (Moss), or None."""
    a = f' data-anim="{step}"' if step is not None else ''
    m = f' marker-end="url(#{marker})"' if marker else ''
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<svg class="abs"{a} style="left:0;top:0" width="1920" height="1080"><path d="{d}" stroke="{color}" '
            f'stroke-width="{width}" fill="none"{ds}{m}/>{extra}</svg>')


def mini_row(x, y, w, ic, text, right=''):
    """Small beige row (icon, text, optional teal status on the right) for mock-ups inside cards."""
    rt = f'<span style="margin-left:auto;font:600 18px/1 var(--f);color:var(--teal)">{right}</span>' if right else ''
    return (f'<div class="t" style="left:{x}px;top:{y}px;width:{w}px;height:42px;border-radius:10px;background:var(--beige);'
            f'display:flex;align-items:center;gap:10px;padding:0 14px;font:400 18px/1 var(--f);color:var(--leaf)">{icon(ic, 20, TEAL)}<span>{text}</span>{rt}</div>')


def bento_cell(x, y, w, h, ic, title, line, body=''):
    """Bento card: icon tile and title, one slate line, then any body (mini rows, a small chart, a track)."""
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
            + text_box(x + 26, y + 24, w - 52,
                       f'<div style="display:flex;align-items:center;gap:14px">{ico(ic, "lt", 52)}<span class="nh" style="font-size:23px">{title}</span></div>'
                       f'<div style="font:400 19px/1.35 var(--f);color:var(--slate);margin-top:12px">{line}</div>') + body)


def steps_track(x0, y, labels, done, gap=104):
    """Progress dots joined by a line, labels under each dot; the first `done` dots are filled.
    Returns (svg_fragment, html) so the caller can place the SVG in a layer."""
    s = [f'<path d="M{x0},{y} L{x0 + (len(labels) - 1) * gap},{y}" stroke="{TEAL}" stroke-width="3"/>']
    lab = ''
    for k, st in enumerate(labels):
        x = x0 + k * gap
        s.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{TEAL if k < done else WHITE}" stroke="{TEAL}" stroke-width="3"/>')
        lab += text_box(x - gap // 2, y + 22, gap, f'<div style="text-align:center;font:400 18px/1.2 var(--f);color:var(--slate)">{st}</div>')
    return ''.join(s), lab


def iso_plate(cx, cy, hw, hd, th, ic=None, dark=False, icon_size=50):
    """One isometric layer: a diamond top (half-width hw, half-depth hd) with two side faces of thickness th.
    Draw lower plates first; leave about 1.75 x hd between plates so each top stays readable.
    Light plates: mint-tinted top, neutral sides. dark=True marks the layer Myridius runs."""
    top = f'{cx - hw},{cy} {cx},{cy - hd} {cx + hw},{cy} {cx},{cy + hd}'
    lf = f'{cx - hw},{cy} {cx},{cy + hd} {cx},{cy + hd + th} {cx - hw},{cy + th}'
    rf = f'{cx},{cy + hd} {cx + hw},{cy} {cx + hw},{cy + th} {cx},{cy + hd + th}'
    if dark:
        f = (f'fill="{LEAF}"', f'fill="{SLATE}"', f'fill="{MOSS}"'); col = PULSE
    else:
        f = (f'fill="#E9F8E3" stroke="{TEAL}" stroke-opacity=".35" stroke-width="1.5"', 'fill="#E7E9E9"', 'fill="#D3D7D8"'); col = LEAF
    s = f'<polygon points="{lf}" {f[1]}/><polygon points="{rf}" {f[2]}/><polygon points="{top}" {f[0]}/>'
    return s + (gicon(ic, cx, cy + 14, icon_size, col) if ic else '')


def ring_points(cx, cy, r, angles_deg):
    """(x, y) for each angle on a circle; 0 degrees is 3 o'clock, -90 is 12 o'clock."""
    return [(round(cx + r * math.cos(math.radians(a))), round(cy + r * math.sin(math.radians(a)))) for a in angles_deg]


def orbit_pill(cx, cy, ic, text, variant='w'):
    """Pill node centred on a ring: icon and label. variant 'w' (white, Moss outline) or 'm' (mint)."""
    w = int(len(text) * 19 * 0.55 + 78)
    bg = 'background:#fff;border:1.5px solid var(--moss)' if variant == 'w' else 'background:var(--mint);border:1.5px solid var(--mint)'
    return (f'<div class="t" style="left:{cx - w // 2}px;top:{cy - 24}px;width:{w}px;height:48px;border-radius:24px;{bg};'
            f'display:flex;align-items:center;justify-content:center;gap:10px;font:600 19px/1 var(--f);color:var(--leaf)">{icon(ic, 24, LEAF)}<span>{text}</span></div>')


def loop_arcs(cx, cy, r, angles_deg, gap=0.26, color=TEAL, marker='aht'):
    """Arrowed arcs from each node to the next around a circle (a flywheel or cycle). gap: radians kept clear
    at each node. Returns SVG paths."""
    out = []
    n = len(angles_deg)
    for k in range(n):
        a0 = math.radians(angles_deg[k]) + gap
        a1 = math.radians(angles_deg[(k + 1) % n] + (360 if k == n - 1 else 0)) - gap
        sx, sy = cx + r * math.cos(a0), cy + r * math.sin(a0)
        out.append(f'<path d="M{sx:.2f},{sy:.2f}{arc_c(cx, cy, r, a0, a1)}" stroke="{color}" stroke-width="3" fill="none" marker-end="url(#{marker})"/>')
    return ''.join(out)


def waffle(x, y, n, on, off, off_op=1, step=27, size=22):
    """10 x 10 grid of squares with the first n filled: a percentage people can see at a glance."""
    s = []
    for i in range(100):
        r, c = divmod(i, 10)
        f, op = (on, 1) if i < n else (off, off_op)
        s.append(f'<rect x="{x + c * step}" y="{y + r * step}" width="{size}" height="{size}" rx="5" fill="{f}" fill-opacity="{op}"/>')
    return ''.join(s)
