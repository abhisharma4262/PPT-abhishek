"""
style_catalogue: twelve visual styles for Myridius decks, each shown on a customer service example.
Source of "Myridius_Visual_Style_Catalogue_v1.pptx". These are references for the quality bar, not a menu;
the parts they are built from live in tools/patterns.py (building blocks).

  python3 examples/style_catalogue.py cat.html
  python3 tools/html2pptx.py cat.html raw.pptx "Visual style catalogue"
  python3 tools/merge_into_template.py raw.pptx merged.pptx --kicker "Myridius deck kit" --title "Visual style|catalogue" --date "October 2026"
  python3 tools/group_anim.py merged.pptx cat.pptx
  python3 tools/add_slide_link.py cat.pptx cat.pptx --on 2 --text "Bento grid" --to 3     # and so on for each style
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
from mkit import *
from patterns import (PATTERN_CSS, ui_window, text_box as T, anim, chat_bubble, avatar, node, port, edge, mini_row,
                      bento_cell, steps_track, iso_plate, ring_points, orbit_pill, loop_arcs, waffle)

N = 12
STY = [
    ('Bento grid', 'Many parts of one offer, in one view', False),
    ('Conversation and actions', 'What AI does during one interaction', True),
    ('Agent trace', 'Each AI step, with the evidence behind it', True),
    ('Workflow canvas', 'Branching logic, and where people step in', True),
    ('Swimlane handoffs', 'Work moving between customer, AI and teams', True),
    ('Before and after', 'The change a solution makes to a task', True),
    ('Layered stack', 'What sits on what, and who runs each layer', True),
    ('Orbit', 'One core connected to many parts', False),
    ('Horizon staircase', 'Maturity and phases over time', False),
    ('Bubble matrix', 'Options compared on two criteria', False),
    ('Flywheel', 'A cycle that improves with each turn', False),
    ('Stat hero', 'One or two sourced numbers that frame the issue', False),
]

CSS = ''   # the shared classes (.t, .nh, .ns, .bub, .node) live in PATTERN_CSS


def eb(n):
    return f'Style {n}/{N} | {STY[n - 1][0]}'


def note(use, motion, seen):
    items = [('target', 'Use it for', use), ('bolt', 'Motion', motion), ('eye', 'Seen in', seen)]
    cells = ''.join(f'<div style="display:flex;align-items:center;gap:12px;flex:1">{ico(ic, "wh", 44)}'
                    f'<div><div style="font:700 18px/1.2 var(--f);letter-spacing:.08em;text-transform:uppercase;color:var(--teal)">{lab}</div>'
                    f'<div style="font:400 18px/1.3 var(--f);color:var(--leaf);margin-top:2px">{t}</div></div></div>' for ic, lab, t in items)
    return (f'<div class="t" style="left:59px;top:872px;width:1801px;height:80px;border-radius:14px;background:var(--beige);'
            f'display:flex;align-items:center;gap:24px;padding:0 24px">{cells}</div>')


def A(n):
    return f' data-anim="{n}"'


# ------------------------------------------------------------------ index
def s_index():
    o = [header('Style catalogue', 'Twelve visual styles, picked by the relationship a slide shows',
                accent='picked by the relationship a slide shows')]
    w, h, g = 432, 212, 24
    for i, (name, shows, anim) in enumerate(STY):
        r, c = divmod(i, 4)
        x, y = 59 + c * (w + g), 168 + r * (h + 20)
        mot = ('bolt', 'Builds in steps') if anim else ('minus', 'Static')
        o.append(f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>')
        o.append(T(x + 24, y + 24, w - 48,
                   f'<div style="display:flex;align-items:center;gap:14px">{badge(str(i + 1), "dk", 42)}'
                   f'<span style="font:700 23px/1.2 var(--f);color:var(--leaf)">{name}</span></div>'
                   f'<div style="font:400 20px/1.35 var(--f);color:var(--leaf);margin-top:16px">{shows}</div>'))
        o.append(T(x + 24, y + h - 50, w - 48,
                   f'<div style="display:flex;align-items:center;gap:8px;font:400 18px/1.2 var(--f);color:var(--slate)">{icon(mot[0], 22, TEAL)}<span>{mot[1]}</span></div>'))
    o.append(T(59, 880, 1801, '<div style="font:400 18px/1.4 var(--f);color:var(--slate)">All examples are illustrative, set in customer service operations for a financial services firm. '
                              'Click a style name to jump to it. The beige strip on each slide is catalogue guidance, not part of the style.</div>'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 1 bento grid
def s_bento():
    o = [header(eb(1), 'One AI service layer covers the whole customer service operation',
                accent='the whole customer service operation')]
    c = [59, 515, 971, 1427]
    r0, r1, h = 168, 512, 322
    # hero cell
    o.append(f'<div class="card dk" style="left:59px;top:{r0}px;width:888px;height:{2 * h + 22}px"></div>')
    o.append(T(99, r0 + 40, 800,
               f'<div style="display:flex;align-items:center;gap:14px">{ico("agent", "pu", 56)}'
               '<span style="font:700 18px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--pulse)">AI agents</span></div>'
               '<div style="font:700 36px/1.2 var(--f);color:#fff;margin-top:22px">Requests resolved end to end</div>'
               '<div style="font:400 21px/1.4 var(--f);color:var(--mint);margin-top:10px">Agents act across your systems to finish the request</div>'))
    o.append(f'<div class="card" style="left:99px;top:{r0 + 250}px;width:808px;height:376px;background:var(--leaf);border-color:var(--leaf)"></div>')
    o.append(chat_bubble(367, r0 + 282, 510, 'Can you move my payment date to the 15th?'))
    o.append(chat_bubble(129, r0 + 376, 560, 'Done. Your next payment is due on the 15th, and I have sent you a confirmation.', 'agent', '#fff'))
    o.append(T(129, r0 + 524, 760, f'<div style="display:flex;align-items:center;gap:10px;font:600 19px/1.2 var(--f);color:var(--pulse)">{icon("check", 24, PULSE)}<span>Resolved in chat; no transfer, no callback</span></div>'))
    o.append(T(129, r0 + 566, 760, f'<div style="display:flex;align-items:center;gap:10px;font:400 18px/1.2 var(--f);color:var(--mint)">{icon("plug", 22, MINT)}<span>Updated in the loan platform and the CRM</span></div>'))

    o.append(bento_cell(c[2], r0, 432, h, 'compass', 'Agent assist', 'Next best step and wrap-up drafted for every contact',
                  mini_row(c[2] + 26, r0 + 196, 380, 'bulb', 'Offer fee refund', 'Eligible') + mini_row(c[2] + 26, r0 + 250, 380, 'doc', 'Summary drafted', 'Review')))
    o.append(bento_cell(c[3], r0, 432, h, 'book', 'Knowledge', 'One approved source for people and AI agents',
                  mini_row(c[3] + 26, r0 + 196, 380, 'doc', 'Card servicing SOP', 'Approved') + mini_row(c[3] + 26, r0 + 250, 380, 'doc', 'Fee policy', 'Approved')))
    # disputes progress
    s, lab = steps_track(c[2] + 60, r1 + 220, ['Intake', 'Investigate', 'Credit', 'Close'], 3)
    o.append(bento_cell(c[2], r1, 432, h, 'shield', 'Disputes', 'Deadlines tracked; letters go out on time', svg(s) + lab))
    # quality bars
    bars = [118, 92, 74, 52, 36]
    bx, by = c[3] + 40, r1 + 286
    s = [f'<path d="M{bx - 8},{by} L{bx + 350},{by}" stroke="{SLATE}" stroke-opacity=".4" stroke-width="1.5"/>']
    for k, bh in enumerate(bars):
        s.append(f'<rect x="{bx + k * 70}" y="{by - bh * .9:.0f}" width="44" height="{bh * .9:.0f}" rx="6" fill="{TEAL}"/>')
    o.append(bento_cell(c[3], r1, 432, h, 'chart', 'Quality and insight', 'Every contact reviewed; top reasons spotted early', svg(''.join(s))))
    o.append(note('An overview of a platform or portfolio', 'Static; the grid is the message', 'Product pages of SaaS and AI firms'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 2 conversation and actions
def s_convo():
    o = [header(eb(2), 'While the customer chats, the AI agent does the work behind it', accent='does the work behind it')]
    o.append(ui_window(100, 168, 780, 684, 'Customer chat', ''))
    o.append(T(124, 778, 732, f'<div style="height:52px;border-radius:26px;border:1.5px solid var(--m16);display:flex;align-items:center;padding:0 22px;font:400 18px/1 var(--f);color:var(--slate)">Type a message</div>'))
    av = lambda y: avatar(120, y)
    # step 1
    o.append(f'<div{A(1)} style="left:0;top:0;width:0;height:0"><div class="bub c" style="left:290px;top:240px;width:560px">I don\'t recognise an $84.20 charge from last night.</div></div>')
    # step 2: reply + first actions
    o.append(f'<div{A(2)} style="left:0;top:0;width:0;height:0">{av(372)}<div class="bub a" style="left:172px;top:330px;width:600px">I can see it: Metro Fuel at 9:42 pm, on your card ending 4471. Was this you?</div></div>')
    o.append(f'<svg class="abs"{A(2)} style="left:0;top:0" width="1920" height="1080"><path d="M790,372 L934,372" stroke="{TEAL}" stroke-width="2.5" stroke-dasharray="7 6" marker-end="url(#aht)"/>'
             f'<path d="M948,300 L948,452" stroke="{TEAL}" stroke-width="2.5"/></svg>')
    def act(y, ic, t, s, n):
        return node(964, y, 896, 76, ic, t, s, 'act', 48, n)
    o.append(act(300, 'search', 'Found the transaction', 'Card platform', 2))
    o.append(act(386, 'shield', 'Checked fraud signals', 'Risk engine', 2))
    o.append(f'<div{A(3)} style="left:0;top:0;width:0;height:0"><div class="bub c" style="left:520px;top:450px;width:330px">No, I was at home all evening.</div></div>')
    o.append(f'<div{A(4)} style="left:0;top:0;width:0;height:0">{av(606)}<div class="bub a" style="left:172px;top:536px;width:640px">I have blocked the card, opened a dispute and credited $84.20 while we look into it. A new card is on its way.</div></div>')
    o.append(f'<svg class="abs"{A(4)} style="left:0;top:0" width="1920" height="1080"><path d="M830,592 L934,592" stroke="{TEAL}" stroke-width="2.5" stroke-dasharray="7 6" marker-end="url(#aht)"/>'
             f'<path d="M948,520 L948,672" stroke="{TEAL}" stroke-width="2.5"/></svg>')
    o.append(f'<div{A(4)} style="left:0;top:0;width:0;height:0"><div class="t" style="left:240px;top:676px;width:500px;height:52px;border-radius:26px;border:1.5px solid var(--teal);'
             f'display:flex;align-items:center;justify-content:center;gap:10px;font:600 18px/1 var(--f);color:var(--teal)">{icon("check", 22, TEAL)}<span>Dispute 48213 opened; new card ordered</span></div></div>')
    o.append(act(520, 'lock', 'Blocked the card and opened a dispute', 'Card platform and case system', 4))
    o.append(act(606, 'money', 'Issued a provisional credit', 'Core banking; dispute deadlines set', 4))
    o.append(f'<div class="node hu"{A(5)} style="left:964px;top:722px;width:896px;height:76px">{ico("person", "wh", 48)}'
             '<div><div class="nh">A person reviews only above the auto-credit limit</div><div class="ns">Everything else completes in the chat</div></div></div>')
    o.append(T(964, 196, 896, '<div style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--teal)">Behind the conversation</div>'
                              '<div style="font:400 19px/1.3 var(--f);color:var(--slate);margin-top:10px">What the AI agent did, in the systems you already run</div>'))
    o.append(note('What AI does during one interaction', 'Builds message by message', 'AI agent product pages and demos'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 3 agent trace
def s_trace():
    o = [header(eb(3), 'Every AI decision leaves a trace a supervisor can read', accent='a trace a supervisor can read')]
    o.append('<div class="card" style="left:59px;top:168px;width:1131px;height:684px"></div>')
    o.append('<div class="t" style="left:59px;top:168px;width:1131px;height:68px;border-radius:16px 16px 0 0;background:var(--beige)"></div>')
    o.append(T(91, 168, 1067, f'<div style="height:68px;display:flex;align-items:center;gap:14px">{icon("evals", 28, TEAL)}'
                              '<span class="nh">Trace</span><span class="ns">Card dispute, case 48213</span>'
                              f'<span style="margin-left:auto;display:flex;align-items:center;gap:8px;font:600 18px/1 var(--f);color:var(--leaf)">{icon("clock", 22, LEAF)}1 min 52 s</span></div>'))
    rows = [('00:01', 'bulb', 'Understood the request', 'Unrecognised card charge; intent is a dispute', 'Reasoning'),
            ('00:03', 'search', 'Looked up the transaction', 'Card platform; one match at Metro Fuel', 'Tool call'),
            ('00:05', 'book', 'Checked the dispute policy', 'Policy v12, section 3: provisional credit', 'Knowledge'),
            ('00:08', 'shield', 'Scored fraud risk', 'Risk engine: high; card blocked', 'Tool call'),
            ('00:41', 'person', 'Asked a supervisor to approve', 'Credit is above the auto-approval limit', 'Person'),
            ('01:52', 'check', 'Credited and confirmed', 'Letter sent; dispute deadlines tracked', 'Outcome')]
    y0, rh = 262, 94
    o.append(svg(f'<path d="M206,{y0 + 30} L206,{y0 + 5 * rh + 30}" stroke="{TEAL}" stroke-opacity=".45" stroke-width="2.5"/>'))
    for k, (tm, ic, t, d, typ) in enumerate(rows):
        y = y0 + k * rh
        hu = typ == 'Person'
        bg = (f'<div class="t" style="left:79px;top:{y - 8}px;width:1091px;height:{rh - 12}px;border-radius:12px;background:var(--mint)"></div>' if hu else '')
        o.append(f'<div{A(k + 1)} style="left:0;top:0;width:0;height:0">{bg}'
                 + T(84, y + 18, 90, f'<div style="font:600 18px/1 var(--f);color:var(--slate)">{tm}</div>')
                 + f'<span class="ico {"dk" if hu else "lt"}" style="position:absolute;left:182px;top:{y + 6}px;width:48px;height:48px">{icon(ic, 34, PULSE if hu else LEAF)}</span>'
                 + T(252, y + 2, 700, f'<div class="nh">{t}</div><div class="ns" style="margin-top:4px">{d}</div>')
                 + T(960, y + 18, 190, f'<div style="text-align:right;font:600 18px/1 var(--f);color:{"var(--moss)" if hu else "var(--teal)"}">{typ}</div>')
                 + '</div>')
    o.append(f'<div{A(7)} style="left:0;top:0;width:0;height:0">'
             + T(1236, 172, 624, '<div style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--teal)">What a supervisor can see</div>'))
    for k, (ic, t, d) in enumerate([('eye', 'Why it acted', 'Each step shows its reasoning and the policy it cited'),
                                    ('plug', 'What it touched', 'Every system call, with inputs and results'),
                                    ('person', 'Where a person decided', 'Approvals and overrides, with who and when')]):
        y = 222 + k * 212
        o.append(f'<div class="card soft" style="left:1236px;top:{y}px;width:624px;height:190px"></div>'
                 + T(1264, y + 28, 568, f'{ico(ic, "lt", 56)}<div class="nh" style="font-size:23px;margin-top:16px">{t}</div>'
                                        f'<div class="ns" style="font-size:19px;margin-top:6px">{d}</div>'))
    o.append('</div>')
    o.append(note('Auditability, trust and control of AI', 'Steps appear in order', 'Trace views in AI agent platforms'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 4 workflow canvas
def s_flow():
    o = [header(eb(4), 'Onboarding runs as one workflow, with people only where needed', accent='with people only where needed')]
    o.append('<div class="t" style="left:59px;top:168px;width:1801px;height:684px;border-radius:18px;background:var(--beige)"></div>')
    g = ''.join(f'<path d="M{x},{176} L{x},{844}" stroke="{MOSS}" stroke-opacity=".05" stroke-width="1.5"/>' for x in range(139, 1860, 80))
    g += ''.join(f'<path d="M{67},{y} L{1852},{y}" stroke="{MOSS}" stroke-opacity=".05" stroke-width="1.5"/>' for y in range(248, 852, 80))
    o.append(svg(g))
    o.append(T(100, 196, 600, '<div style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--slate)">Merchant onboarding</div>'))
    leg = ''.join(f'<span style="display:flex;align-items:center;gap:8px;margin-left:{0 if i == 0 else 26}px"><span style="width:22px;height:22px;border-radius:6px;background:{bg};border:1.5px solid {bd}"></span>{t}</span>'
                  for i, (bg, bd, t) in enumerate([('var(--moss)', 'var(--moss)', 'AI agent'), ('#fff', 'var(--m16)', 'System'), ('var(--mint)', 'var(--mint)', 'Person')]))
    o.append(T(1220, 192, 610, f'<div style="display:flex;justify-content:flex-end;font:400 18px/1 var(--f);color:var(--leaf)">{leg}</div>'))
    W, H = 300, 100

    nd = lambda x, y, ic, t, s, kind='': node(x, y, W, H, ic, t, s, kind)

    o.append(f'<div{A(1)} style="left:0;top:0;width:0;height:0">' + nd(100, 462, 'doc', 'Application received', 'Trigger: portal upload') + '</div>')
    o.append(edge('M400,512 L462,512', 2, extra=port(400, 512)))
    o.append(f'<div{A(2)} style="left:0;top:0;width:0;height:0">' + nd(470, 462, 'agent', 'Extract and check', 'Documents and KYC data', 'ai') + '</div>')
    o.append(edge('M770,512 L832,512', 3, extra=port(770, 512)))
    o.append(f'<div{A(3)} style="left:0;top:0;width:0;height:0">' + nd(840, 462, 'target', 'Complete, low risk?', 'Rules and risk score', 'dc') + '</div>')
    o.append(edge('M1140,512 C1180,512 1170,312 1202,312', 4, extra=port(1140, 512)))
    o.append(f'<div{A(4)} style="left:0;top:0;width:0;height:0">' + nd(1210, 262, 'gear', 'Configure accounts', 'Core platform') +
             T(1060, 372, 100, '<div style="font:700 18px/1 var(--f);color:var(--teal);text-align:right">Yes</div>') + '</div>')
    o.append(edge('M1510,312 L1532,312', 4))
    o.append(f'<div{A(4)} style="left:0;top:0;width:0;height:0">' + nd(1540, 262, 'rocket', 'Welcome and go live', 'Emails and checks', 'ai').replace(f'width:{W}px', 'width:290px') + '</div>')
    o.append(edge('M1140,512 C1180,512 1170,712 1202,712', 5))
    o.append(f'<div{A(5)} style="left:0;top:0;width:0;height:0">' + nd(1210, 662, 'person', 'Analyst review', 'Missing or risky items', 'hu') +
             T(1060, 636, 100, '<div style="font:700 18px/1 var(--f);color:var(--slate);text-align:right">No</div>') + '</div>')
    o.append(edge('M1360,662 L1360,370', 5))
    o.append(f'<div{A(5)} style="left:0;top:0;width:0;height:0">' + T(1376, 500, 160, '<div style="font:700 18px/1 var(--f);color:var(--slate)">Approved</div>') + '</div>')
    o.append(note('Branching processes and routing logic', 'Builds left to right, branch by branch', 'Workflow builders and agent canvases'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 5 swimlane handoffs
def s_lanes():
    o = [header(eb(5), 'Context travels with the customer across every handoff', accent='across every handoff')]
    lanes = [('person', 'Customer'), ('agent', 'AI agent'), ('users', 'Service team'), ('gear', 'Back office')]
    ly, lh, lg = 168, 134, 10
    for k, (ic, t) in enumerate(lanes):
        y = ly + k * (lh + lg)
        o.append(f'<div class="t" style="left:59px;top:{y}px;width:1801px;height:{lh}px;border-radius:14px;background:{"var(--m04)" if k % 2 == 0 else "var(--beige)"}"></div>')
        o.append(T(83, y, 230, f'<div style="height:{lh}px;display:flex;align-items:center;gap:14px">{ico(ic, "dk" if k == 1 else "lt", 50)}<span class="nh">{t}</span></div>'))
    cw, ch = 262, 86
    cy = lambda lane: ly + lane * (lh + lg) + lh // 2
    bnd = lambda lane: ly + lane * (lh + lg) - lg // 2          # boundary above a lane
    steps = [(0, 330, 'Reports a lost card in the app'), (1, 640, 'Blocks the card; reviews recent spend'),
             (2, 950, 'Confirms two charges to dispute'), (3, 1260, 'Opens disputes; orders a new card'),
             (1, 1300, 'Keeps the customer updated'), (0, 1590, 'New card active; disputes closed')]
    # connector paths into each step (None for the first), and where the handoff marker sits
    conn = [None,
            (f'M592,{cy(0)} L690,{cy(0)} L690,{cy(1) - ch // 2 - 6}', 690, bnd(1)),
            (f'M902,{cy(1)} L1000,{cy(1)} L1000,{cy(2) - ch // 2 - 6}', 1000, bnd(2)),
            (f'M1212,{cy(2)} L1310,{cy(2)} L1310,{cy(3) - ch // 2 - 6}', 1310, bnd(3)),
            (f'M1480,{cy(3) - ch // 2} L1480,{cy(1) + ch // 2 + 6}', 1480, bnd(3)),
            (f'M1562,{cy(1)} L1640,{cy(1)} L1640,{cy(0) + ch // 2 + 6}', 1640, bnd(1))]
    for k, (lane, x, t) in enumerate(steps):
        y = cy(lane) - ch // 2
        parts = []
        if conn[k]:
            d, mx, my = conn[k]
            mk = f'<circle cx="{mx}" cy="{my}" r="20" fill="{MINT}" stroke="{WHITE}" stroke-width="3"/>' + gicon('doc', mx, my, 26, LEAF)
            parts.append(f'<svg class="abs" style="left:0;top:0" width="1920" height="1080"><path d="{d}" stroke="{TEAL}" stroke-width="2.5" fill="none" marker-end="url(#aht)"/>{mk}</svg>')
        dark = lane == 1
        parts.append(f'<div class="node{" ai" if dark else ""}" style="left:{x}px;top:{y}px;width:{cw}px;height:{ch}px">'
                     f'<div class="nh" style="font-size:19px;font-weight:600;{"color:#fff" if dark else ""}">{t}</div></div>')
        o.append(f'<div{A(k + 1)} style="left:0;top:0;width:0;height:0">' + ''.join(parts) + '</div>')
    o.append(f'<div{A(7)} style="left:0;top:0;width:0;height:0">'
             + band_items(59, 756, 1801, 84, 'doc', 'Passed at every handoff', [('lock', 'Verified identity'), ('chat', 'Conversation so far'), ('evals', 'Case notes and evidence')], fs=20) + '</div>')
    o.append(note('Work moving between parties', 'Builds step by step along the path', 'Service blueprints and journey maps'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 6 before and after
def s_beforeafter():
    o = [header(eb(6), 'After-contact work shrinks from seven tasks to one review', accent='from seven tasks to one review')]
    tasks = ['Write call notes', 'Pick a disposition code', 'Update CRM fields', 'Send the follow-up email',
             'Log a complaint, if any', 'Raise a back-office request', 'Book a callback']
    o.append('<div class="card soft" style="left:59px;top:168px;width:800px;height:676px"></div>')
    o.append(T(95, 200, 730, f'<div style="display:flex;align-items:center;gap:12px">{icon("clock", 28, SLATE)}'
                             '<span style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--slate)">Today</span></div>'
                             '<div class="h3" style="margin-top:16px">The agent does every task after the call</div>'))
    for k, t in enumerate(tasks):
        y = 330 + k * 66
        o.append(f'<div class="t" style="left:95px;top:{y}px;width:728px;height:54px;border-radius:12px;background:#fff;border:1.5px solid var(--m10);'
                 f'display:flex;align-items:center;gap:12px;padding:0 16px;font:400 20px/1 var(--f);color:var(--leaf)">{icon("person", 24, SLATE)}<span>{t}</span>'
                 f'<span style="margin-left:auto;font:400 18px/1 var(--f);color:var(--slate)">Typed by hand</span></div>')
    o.append(f'<svg class="abs"{A("1w")} style="left:0;top:0" width="1920" height="1080">'
             f'<path d="M884,470 L944,470 L944,446 L992,506 L944,566 L944,542 L884,542 Z" fill="{TEAL}"/></svg>')
    inner = [f'<div class="card" style="left:1016px;top:168px;width:844px;height:676px;border:2.5px solid var(--teal)"></div>',
             T(1052, 200, 772, f'<div style="display:flex;align-items:center;gap:12px">{icon("agent", 28, TEAL)}'
                               '<span style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--teal)">With an AI assistant</span></div>'
                               '<div class="h3" style="margin-top:16px">The agent reviews one summary</div>'),
             '<div class="t" style="left:1052px;top:330px;width:772px;height:356px;border-radius:16px;background:var(--beige)"></div>',
             T(1078, 350, 720, '<div class="nh">Contact summary, ready to approve</div>')]
    done = ['Notes written', 'Disposition coded', 'CRM updated', 'Follow-up drafted', 'No complaint flagged', 'Request raised', 'Callback booked']
    for k, t in enumerate(done):
        r, c = divmod(k, 2)
        inner.append(f'<div class="t" style="left:{1078 + c * 366}px;top:{404 + r * 66}px;width:346px;height:52px;border-radius:12px;background:#fff;'
                     f'display:flex;align-items:center;gap:10px;padding:0 14px;font:400 19px/1 var(--f);color:var(--leaf)">{icon("check", 24, TEAL)}<span>{t}</span></div>')
    inner.append(f'<div class="t" style="left:1052px;top:712px;width:772px;height:96px;border-radius:16px;background:var(--moss);'
                 f'display:flex;align-items:center;gap:16px;padding:0 24px">{ico("hand", "pu", 56)}'
                 '<div><div style="font:700 22px/1.2 var(--f);color:#fff">Agent checks and approves</div>'
                 '<div style="font:400 18px/1.3 var(--f);color:var(--mint)">Then takes the next contact</div></div></div>')
    o.append(f'<div{A("1w")} style="left:0;top:0;width:0;height:0">' + ''.join(inner) + '</div>')
    o.append(note('The change a solution makes to a task', 'The after side wipes in', 'Product launch pages and case studies'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 7 layered stack (isometric)
def s_stack():
    o = [header(eb(7), 'Five layers turn AI agents into a service you can run', accent='a service you can run')]
    cx, W, D, TH, S, base = 520, 340, 70, 18, 124, 752
    layers = [('run', 'Run, govern and improve', 'Monitoring, evaluations, changes and support', True),
              ('gear', 'Workflow and systems of record', 'CRM, core banking, card and case systems', False),
              ('book', 'Knowledge and context', 'Approved answers, customer history and policies', False),
              ('agent', 'AI agents and assistants', 'Customer-facing agents and agent assist', False),
              ('chat', 'Channels', 'Chat, voice, app, web and branch', False)]
    for i, (ic, t, d, dark) in enumerate(layers):
        cy = base - i * S
        s = (iso_plate(cx, cy, W, D, TH, ic, dark)
             + f'<path d="M{cx + W + 14},{cy} L{985},{cy}" stroke="{TEAL}" stroke-width="2"/><circle cx="990" cy="{cy}" r="6" fill="{TEAL}"/>')
        o.append(f'<div{A(i + 1)} style="left:0;top:0;width:0;height:0"><svg class="abs" style="left:0;top:0" width="1920" height="1080">{s}</svg>'
                 + T(1012, cy - 32, 840, f'<div class="nh" style="font-size:23px">{t}</div><div class="ns" style="font-size:19px;margin-top:4px">{d}</div>') + '</div>')
    for lx, sw, lt in ((1012, 'background:var(--leaf)', 'Run by Myridius'), (1240, 'background:#E9F8E3;border:1.5px solid var(--teal)', 'Your platforms and partners')):
        o.append(T(lx, 812, 300, f'<div style="display:flex;align-items:center;gap:10px;font:400 18px/1 var(--f);color:var(--leaf)">'
                                 f'<span style="width:22px;height:22px;border-radius:5px;{sw}"></span><span>{lt}</span></div>'))
    o.append(note('Architecture; what sits on what; ownership', 'Builds from the bottom up (optional)', 'Platform pages of cloud and data firms'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 8 orbit
def s_orbit():
    o = [header(eb(8), 'Every channel and platform connects to one service core', accent='one service core')]
    cx, cy, ri, ro = 620, 510, 186, 310
    o.append(svg(f'<circle cx="{cx}" cy="{cy}" r="{ro}" fill="none" stroke="{MOSS}" stroke-opacity=".18" stroke-width="2" stroke-dasharray="8 8"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{ri}" fill="none" stroke="{TEAL}" stroke-opacity=".5" stroke-width="2" stroke-dasharray="8 8"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="112" fill="{MINT}" fill-opacity=".4"/><circle cx="{cx}" cy="{cy}" r="94" fill="{MOSS}"/>'
                 + gicon('agent', cx, cy - 26, 50, PULSE)))
    o.append(T(cx - 90, cy + 14, 180, '<div style="text-align:center;font:700 21px/1.2 var(--f);color:#fff">Service core</div>'))
    inner = [(-90, 'chat', 'Chat'), (-18, 'app', 'Mobile app'), (54, 'pulse', 'Voice'), (126, 'users', 'Branch'), (198, 'globe', 'Web')]
    outer = [(-60, 'person', 'CRM'), (0, 'db', 'Core banking'), (60, 'money', 'Card platform'),
             (120, 'book', 'Knowledge base'), (180, 'calendar', 'Workforce planning'), (240, 'chart', 'Analytics')]
    for (px, py), (a, ic, t) in zip(ring_points(cx, cy, ri, [a for a, _, _ in inner]), inner):
        o.append(orbit_pill(px, py, ic, t, 'w'))
    for (px, py), (a, ic, t) in zip(ring_points(cx, cy, ro, [a for a, _, _ in outer]), outer):
        o.append(orbit_pill(px, py, ic, t, 'm'))
    rows = [('target', 'The core', 'One set of rules, knowledge and controls for every agent', 'dk'),
            ('chat', 'Inner ring: channels', 'Where customers reach you; the same answer everywhere', 'ol'),
            ('plug', 'Outer ring: platforms', 'Where agents act; connected once, used by every channel', 'lt')]
    for k, (ic, t, d, v) in enumerate(rows):
        y = 236 + k * 196
        o.append(T(1180, y, 680, f'<div style="display:flex;gap:20px;align-items:flex-start">{ico(ic, v, 60)}'
                                 f'<div><div class="nh" style="font-size:23px">{t}</div><div class="ns" style="font-size:20px;margin-top:6px">{d}</div></div></div>'))
    o.append(note('One core connected to many parts', 'Static', 'Integration pages; orbit components'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 9 horizon staircase
def s_horizons():
    o = [header(eb(9), 'Three horizons take service from assisted to autonomous', accent='from assisted to autonomous')]
    hz = [('Now', 'Assisted', 'AI helps people do the work', ['Agent assist and wrap-up', 'One approved knowledge source', 'Every contact quality-checked'],
           'Answers proven accurate on live contacts'),
          ('Next', 'Automated', 'AI completes routine requests', ['Self-service that finishes the task', 'Dispute and onboarding steps automated', 'People handle the exceptions'],
           'Automation runs within agreed controls'),
          ('Later', 'Autonomous', 'AI agents run most journeys end to end', ['Agents act across systems', 'People supervise and improve', 'Run and governed as a service'],
           'Business outcomes, not activity')]
    w, tops, bot = 587, [470, 350, 230], 844
    for k, (lab, name, desc, ticks, gate) in enumerate(hz):
        x, y = 59 + k * (w + 20), tops[k]
        dk = k == 2
        o.append(f'<div class="card{" dk" if dk else ""}" style="left:{x}px;top:{y}px;width:{w}px;height:{bot - y}px"></div>')
        tc, sc, kc = ('#fff', 'var(--mint)', PULSE) if dk else ('var(--leaf)', 'var(--slate)', TEAL)
        tl = ''.join(f'<div style="display:flex;align-items:center;gap:10px;margin-top:16px;font:400 20px/1.25 var(--f);color:{tc}">{icon("check", 24, kc)}<span>{t}</span></div>' for t in ticks)
        o.append(T(x + 30, y + 26, w - 60,
                   f'<div style="font:700 19px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;color:{"var(--pulse)" if dk else "var(--teal)"}">{lab}</div>'
                   f'<div style="font:700 30px/1.2 var(--f);color:{tc};margin-top:12px">{name}</div>'
                   f'<div style="font:400 20px/1.3 var(--f);color:{sc};margin-top:6px">{desc}</div>{tl}'))
        wm = [None, ('bolt', 130), ('agent', 230)][k]
        if wm:
            o.append(svg(gicon(wm[0], x + w - 40 - wm[1] / 2, bot - 100 - wm[1] / 2, wm[1], PULSE if dk else TEAL).replace('<g ', '<g opacity=".35" ', 1)))
        o.append(f'<div class="t" style="left:{x + 30}px;top:{bot - 78}px;width:{w - 60}px;height:1.5px;background:{"rgba(210,240,198,.3)" if dk else "var(--m10)"}"></div>')
        o.append(T(x + 30, bot - 60, w - 60, f'<div style="display:flex;align-items:center;gap:10px;font:400 18px/1.25 var(--f);color:{sc}">{icon("flag", 22, kc)}'
                                              f'<span><b style="font-weight:600;color:{tc}">{"Judged by:" if dk else "Move on when:"}</b> {gate}</span></div>'))
    o.append(f'<div class="t" style="left:89px;top:408px;height:44px;border-radius:22px;background:var(--moss);display:flex;align-items:center;gap:10px;padding:0 18px;'
             f'font:600 18px/1 var(--f);color:var(--pulse)">{icon("target", 22, PULSE)}<span>You are here (illustrative)</span></div>')
    o.append(note('Maturity, phases and ambition over time', 'Static', 'Strategy decks and maturity models'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 10 bubble matrix
def s_matrix():
    o = [header(eb(10), 'Start where the value is high and the path is short', accent='value is high and the path is short')]
    x0, x1, y0, y1, mx, my = 200, 1180, 180, 790, 690, 485
    s = [f'<rect x="{mx}" y="{y0}" width="{x1 - mx}" height="{my - y0}" fill="{MINT}" fill-opacity=".45"/>',
         f'<path d="M{mx},{y0} L{mx},{y1}" stroke="{MOSS}" stroke-opacity=".2" stroke-width="1.5" stroke-dasharray="6 6"/>',
         f'<path d="M{x0},{my} L{x1},{my}" stroke="{MOSS}" stroke-opacity=".2" stroke-width="1.5" stroke-dasharray="6 6"/>',
         f'<path d="M{x0},{y1} L{x0},{y0 + 6}" stroke="{LEAF}" stroke-width="2.5" marker-end="url(#ahl)"/>',
         f'<path d="M{x0},{y1} L{x1 - 6},{y1}" stroke="{LEAF}" stroke-width="2.5" marker-end="url(#ahl)"/>']
    bubbles = [(810, 300, 58, 'Disputes', 'b', True), (1020, 262, 46, 'Knowledge foundation', 'b', True), (1080, 418, 40, 'Agent assist', 'l', True),
               (440, 320, 56, 'Implementations', 'b', False), (910, 620, 42, 'Repeat contacts', 'b', False),
               (540, 600, 50, 'L1 and L2 support', 'b', False), (300, 716, 30, 'AI quality operations', 'r', False)]
    lab = []
    for bx, by, r, t, pos, hot in bubbles:
        s.append(f'<circle cx="{bx}" cy="{by}" r="{r}" fill="{MOSS if hot else MINT}" stroke="{MOSS if hot else TEAL}" stroke-width="2"/>')
        st = 'font:600 19px/1.2 var(--f);color:var(--leaf)'
        if pos == 'b':
            lab.append(T(bx - 130, by + r + 8, 260, f'<div style="text-align:center;{st}">{t}</div>'))
        elif pos == 'l':
            lab.append(T(bx - r - 270, by - 12, 260, f'<div style="text-align:right;{st}">{t}</div>'))
        else:
            lab.append(T(bx + r + 10, by - 12, 260, f'<div style="{st}">{t}</div>'))
    o.append(svg(''.join(s)))
    o += lab
    ax = 'font:600 18px/1.2 var(--f);color:var(--slate)'
    o.append(T(59, 182, 128, f'<div style="text-align:right;{ax}">Higher value</div>'))
    o.append(T(59, 744, 128, f'<div style="text-align:right;{ax}">Lower value</div>'))
    o.append(T(200, 804, 300, f'<div style="{ax}">Harder to start</div>'))
    o.append(T(880, 804, 300, f'<div style="text-align:right;{ax}">Easier to start</div>'))
    o.append(T(880, 198, 284, '<div style="text-align:right;font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--teal)">Start here</div>'))
    o.append(T(200, 836, 900, '<div style="font:400 18px/1.2 var(--f);color:var(--slate)">Bubble size shows contact volume; positions are illustrative</div>'))
    o.append(T(1240, 186, 620, '<div style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--teal)">Start here, in this order</div>'))
    for k, (t, d) in enumerate([('Disputes', 'High value; rules and deadlines already defined'),
                                ('Knowledge foundation', 'Quick to start; every later use case depends on it'),
                                ('Agent assist', 'Visible to agents early; builds trust in AI')]):
        y = 240 + k * 150
        o.append(f'<div class="card soft" style="left:1240px;top:{y}px;width:620px;height:130px"></div>')
        o.append(T(1266, y + 26, 570, f'<div style="display:flex;gap:16px;align-items:flex-start"><span class="num" style="background:var(--moss);color:var(--pulse);border-color:var(--moss)">{k + 1}</span>'
                                      f'<div><div class="nh" style="font-size:23px">{t}</div><div class="ns" style="font-size:19px;margin-top:6px">{d}</div></div></div>'))
    o.append(T(1240, 700, 620, '<div style="font:400 18px/1.35 var(--f);color:var(--slate)">We would calibrate positions with you in a working session.</div>'))
    o.append(note('Choosing between options on two criteria', 'Static', 'Consulting decks; prioritisation work'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 11 flywheel
def s_flywheel():
    o = [header(eb(11), 'AI agents stay accurate when they are run as a continuous loop', accent='run as a continuous loop')]
    cx, cy, r = 600, 528, 250
    steps = [(-90, 'eye', 'Observe', 'Live conversations, outcomes and escalations'),
             (-18, 'evals', 'Evaluate', 'Scored for accuracy, compliance and tone'),
             (54, 'tools', 'Improve', 'Knowledge, prompts and workflows updated'),
             (126, 'shield', 'Test', 'Changes proven on past cases before release'),
             (198, 'rocket', 'Release', 'Shipped with approval and a way to roll back')]
    s = [f'<circle cx="{cx}" cy="{cy}" r="132" fill="{MINT}" fill-opacity=".4"/><circle cx="{cx}" cy="{cy}" r="114" fill="{MOSS}"/>' + gicon('loop', cx, cy - 38, 44, PULSE)]
    s.append(loop_arcs(cx, cy, r, [a for a, _, _, _ in steps]))
    labs = []
    for a, ic, t, _ in steps:
        ra = math.radians(a)
        nx, ny = cx + r * math.cos(ra), cy + r * math.sin(ra)
        s.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="48" fill="{MINT}"/>' + gicon(ic, nx, ny, 64, LEAF))
        st = 'font:700 23px/1 var(--f);color:var(--leaf)'
        if a == -90:
            labs.append(T(round(nx - 110), round(ny - 48 - 40), 220, f'<div style="text-align:center;{st}">{t}</div>'))
        elif math.cos(ra) > 0.2:
            labs.append(T(round(nx + 62), round(ny - 12), 220, f'<div style="{st}">{t}</div>'))
        else:
            labs.append(T(round(nx - 62 - 220), round(ny - 12), 220, f'<div style="text-align:right;{st}">{t}</div>'))
    o.append(svg(''.join(s)))
    o += labs
    o.append(T(cx - 105, cy - 4, 210, '<div style="text-align:center;font:700 21px/1.2 var(--f);color:#fff">Run as a service</div>'
                                     '<div style="text-align:center;font:400 18px/1.3 var(--f);color:var(--mint);margin-top:4px">Managed by Myridius</div>'))
    o.append(T(1120, 186, 740, '<div style="font:700 19px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:var(--teal)">Each turn of the loop</div>'))
    for k, (a, ic, t, dsc) in enumerate(steps):
        y = 232 + k * 124
        o.append(T(1120, y, 740, f'<div style="display:flex;gap:18px;align-items:center">{ico(ic, "lt", 56)}'
                                 f'<div><div class="nh" style="font-size:22px">{t}</div><div class="ns" style="font-size:19px;margin-top:4px">{dsc}</div></div></div>'))
    o.append(note('Cycles, continuous improvement, operating models', 'Static', 'Operating model and flywheel diagrams'))
    return '\n'.join(o)


# ------------------------------------------------------------------ 12 stat hero
G1 = 'https://www.gartner.com/en/newsroom/press-releases/2025-03-05-gartner-predicts-agentic-ai-will-autonomously-resolve-80-percent-of-common-customer-service-issues-without-human-intervention-by-20290'
G2 = 'https://www.gartner.com/en/newsroom/press-releases/2026-08-04-gartner-survey-finds-87-percent-of-customers-say-companies-using-genai-for-customer-service-must-provide-access-to-a-human-agent0'


def s_stat():
    o = [header(eb(12), 'Customers expect AI to resolve issues, and a person within reach', accent='and a person within reach')]
    o.append('<div class="card dk" style="left:59px;top:168px;width:881px;height:592px"></div>')
    o.append('<div class="card" style="left:979px;top:168px;width:881px;height:592px"></div>')
    o.append(svg(waffle(586, 206, 80, PULSE, LEAF, 1, 31, 25) + waffle(1506, 206, 87, TEAL, MOSS, .1, 31, 25)))
    o.append(T(99, 196, 460, '<div style="font:700 150px/1 var(--f);color:var(--pulse);letter-spacing:-.02em">80%</div>'
                             '<div style="font:400 25px/1.4 var(--f);color:#fff;margin-top:26px">of common customer service issues will be resolved by agentic AI without a person, by 2029¹</div>'))
    o.append(T(1019, 196, 460, '<div style="font:700 150px/1 var(--f);color:var(--teal);letter-spacing:-.02em">87%</div>'
                               '<div style="font:400 25px/1.4 var(--f);color:var(--leaf);margin-top:26px">of customers say firms using GenAI must offer a way to reach a person²</div>'))
    o.append('<div class="t" style="left:99px;top:574px;width:801px;height:1.5px;background:rgba(210,240,198,.3)"></div>')
    o.append('<div class="t" style="left:1019px;top:574px;width:801px;height:1.5px;background:var(--m10)"></div>')
    o.append(T(99, 598, 801, f'<div style="display:flex;align-items:center;gap:14px;font:400 21px/1.35 var(--f);color:var(--mint)">{icon("money", 30, PULSE)}'
                             '<span><b style="color:#fff;font-weight:600">30%</b> lower operational costs expected as a result¹</span></div>'))
    o.append(T(1019, 598, 801, f'<div style="display:flex;align-items:center;gap:14px;font:400 21px/1.35 var(--f);color:var(--leaf)">{icon("agent", 30, TEAL)}'
                               '<span><b style="font-weight:600">58%</b> of customers who use GenAI have had it complete a task for them²</span></div>'))
    o.append(T(99, 700, 800, f'<div style="font:400 18px/1.2 var(--f);color:var(--mint)">Source: {link(G1, "¹ Gartner predictions")}</div>'))
    o.append(T(1019, 700, 800, f'<div style="font:400 18px/1.2 var(--f);color:var(--slate)">Source: {link(G2, "² Gartner customer survey")}</div>'))
    o.append(banner(59, 784, 1801, 66, 'target', 'So what', 'Design for both: AI that resolves the request, and a clear path to a person'))
    o.append(note('One or two sourced numbers that frame the issue', 'Static', 'Analyst and investor decks'))
    return '\n'.join(o)


# ------------------------------------------------------------------ already in the kit
def s_kit():
    o = [header('Already in the kit', 'Patterns we already have, and where each one has worked', accent='where each one has worked')]
    items = [('layers', 'Scatter to hub to card', 'Knowledge foundation (A1); support triage (C1)', 'Liked; animates well'),
             ('app', 'Product window', 'Agent desktop: before, during and after the contact', 'Keep it static'),
             ('swap', 'From/to lanes', 'Three shifts on the hook slide', 'Liked'),
             ('plus', 'Equation', 'Where we fit: platforms + layers = outcomes', 'Chosen for a first executive meeting'),
             ('grid', 'Services matrix', 'Advise, build and run across the themes', 'The services anchor slide'),
             ('users', 'Client stories', 'Situation, solution and outcomes in three columns', 'House template'),
             ('clock', 'Deadline-bound process', 'Disputes: stages, where people decide, always-on band', 'Used for disputes (B1)'),
             ('chart', 'Flow ribbons', 'Tried for L1 and L2 support', 'Scatter preferred; use when shares matter')]
    w, h = 432, 324
    for i, (ic, name, where, verdict) in enumerate(items):
        r, c = divmod(i, 4)
        x, y = 59 + c * (w + 24), 168 + r * (h + 20)
        o.append(f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>')
        o.append(T(x + 26, y + 26, w - 52, f'{ico(ic, "lt", 56)}<div class="nh" style="font-size:23px;margin-top:18px">{name}</div>'
                                           f'<div style="font:400 19px/1.35 var(--f);color:var(--leaf);margin-top:8px">{where}</div>'))
        o.append(T(x + 26, y + h - 62, w - 52, f'<div style="display:flex;align-items:flex-start;gap:8px;font:400 18px/1.3 var(--f);color:var(--slate)">{icon("star", 22, TEAL)}<span>{verdict}</span></div>'))
    o.append(T(59, 880, 1801, '<div style="font:400 18px/1.4 var(--f);color:var(--slate)">These live in tools/patterns.py and the Fiserv deck; the styles you pick from this catalogue join them.</div>'))
    return '\n'.join(o)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'cat.html'
    slides = [s_index(), s_bento(), s_convo(), s_trace(), s_flow(), s_lanes(), s_beforeafter(), s_stack(),
              s_orbit(), s_horizons(), s_matrix(), s_flywheel(), s_stat(), s_kit()]
    write_deck(out, slides, PATTERN_CSS + CSS, 'Visual style catalogue')
    print('written', out, len(slides))
