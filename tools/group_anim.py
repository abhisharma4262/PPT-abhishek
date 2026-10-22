"""
group_anim: turns tagged shapes into PowerPoint groups, applies rotation, and adds entrance animations.

Tag elements in the mkit HTML, then run this on the final deck (after merge_into_template.py):

  <div data-grp="chip3" data-rot="-3"> ... </div>   all shapes inside become one group, rotated -3 degrees
  <div data-anim="1"> ... </div>                     everything inside appears in step 1
  <svg class="abs" data-anim="2w"> ... </svg>        step 2, wiped in from the left (w); default is a fade

  python3 group_anim.py deck.pptx out.pptx [--step-ms 450] [--gap-ms 150]

Steps play automatically one after another when the slide opens (After Previous), so a presenter does not
need extra clicks. Keep each data-anim block contiguous in paint order (one HTML block per step) so grouping
does not change what sits on top of what. Everything stays editable: groups can be ungrouped in PowerPoint.
"""
import argparse, copy, re
from pptx import Presentation
from lxml import etree

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
NS = {'p': P, 'a': A}
q = lambda ns, t: '{%s}%s' % (ns, t)
SHAPE_TAGS = {q(P, 'sp'), q(P, 'pic'), q(P, 'grpSp'), q(P, 'cxnSp'), q(P, 'graphicFrame')}
TAG_RE = re.compile(r'~(.*)$')


def tags_of(el):
    c = el.find('.//p:cNvPr', NS)
    if c is None:
        return None, None, None, None
    m = TAG_RE.search(c.get('name', ''))
    if not m:
        return None, None, None, c
    g = rot = an = None
    for part in m.group(1).split('|'):
        if part.startswith('g:'):
            g = part[2:]
            if '@' in g:
                g, r = g.split('@', 1)
                rot = float(r)
        elif part.startswith('a:'):
            an = part[2:]
    return g, rot, an, c


def xfrm_of(el):
    if el.tag == q(P, 'grpSp'):
        return el.find('p:grpSpPr/a:xfrm', NS)
    return el.find('.//p:spPr/a:xfrm', NS) if el.tag != q(P, 'graphicFrame') else el.find('p:xfrm', NS)


def bbox(els):
    xs, ys, xe, ye = [], [], [], []
    for el in els:
        x = xfrm_of(el)
        if x is None:
            continue
        off, ext = x.find('a:off', NS), x.find('a:ext', NS)
        X, Y, W, H = int(off.get('x')), int(off.get('y')), int(ext.get('cx')), int(ext.get('cy'))
        xs.append(X); ys.append(Y); xe.append(X + W); ye.append(Y + H)
    return min(xs), min(ys), max(xe) - min(xs), max(ye) - min(ys)


def make_group(tree, members, name, rot=None):
    x, y, w, h = bbox(members)
    g = etree.Element(q(P, 'grpSp'))
    nv = etree.SubElement(g, q(P, 'nvGrpSpPr'))
    etree.SubElement(nv, q(P, 'cNvPr'), id='0', name=name)
    etree.SubElement(nv, q(P, 'cNvGrpSpPr'))
    etree.SubElement(nv, q(P, 'nvPr'))
    sp = etree.SubElement(g, q(P, 'grpSpPr'))
    xf = etree.SubElement(sp, q(A, 'xfrm'))
    if rot:
        xf.set('rot', str(int(round((rot % 360) * 60000))))
    etree.SubElement(xf, q(A, 'off'), x=str(x), y=str(y))
    etree.SubElement(xf, q(A, 'ext'), cx=str(w), cy=str(h))
    etree.SubElement(xf, q(A, 'chOff'), x=str(x), y=str(y))
    etree.SubElement(xf, q(A, 'chExt'), cx=str(w), cy=str(h))
    first = members[0]
    first.addprevious(g)
    for m in members:
        g.append(m)
    return g


def clean_name(c):
    n = c.get('name', '')
    c.set('name', TAG_RE.sub('', n) or n)


def effect(ctn_id, spid, kind, dur, delay):
    """One entrance effect (After Previous). kind: 'f' fade, 'w' wipe from left, 'u' wipe from bottom."""
    pid, sub, filt = {'f': ('10', '0', 'fade'), 'w': ('22', '8', 'wipe(left)'), 'u': ('22', '4', 'wipe(down)')}[kind]
    i = ctn_id
    return (f'<p:par><p:cTn id="{i}" fill="hold"><p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>'
            f'<p:par><p:cTn id="{i + 1}" presetID="{pid}" presetClass="entr" presetSubtype="{sub}" fill="hold" grpId="0" nodeType="afterEffect">'
            f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            f'<p:set><p:cBhvr><p:cTn id="{i + 2}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
            f'<p:to><p:strVal val="visible"/></p:to></p:set>'
            f'<p:animEffect transition="in" filter="{filt}"><p:cBhvr><p:cTn id="{i + 3}" dur="{dur}"/>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
            f'</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>'), i + 4


def timing_xml(steps, step_ms, gap_ms):
    """steps: list of (spid, kind). Builds a main sequence that starts with the slide and plays every step in turn."""
    nid = 4
    pars, t = [], 0
    for spid, kind in steps:
        x, nid = effect(nid, spid, kind, step_ms, t)
        pars.append(x)
        t += step_ms + gap_ms
    return (f'<p:timing xmlns:p="{P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
            f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
            f'<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite"/><p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond></p:stCondLst>'
            f'<p:childTnLst>{"".join(pars)}</p:childTnLst></p:cTn></p:par>'
            f'</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
            f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
            f'</p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')


def process_slide(slide, step_ms, gap_ms):
    tree = slide.shapes._spTree
    # slides with no tagged shapes are left exactly as they are (ids and any existing animation untouched)
    if not any('~' in (c.get('name') or '') for c in tree.iter(q(P, 'cNvPr'))):
        return 0
    # 1. rotation groups
    groups = {}
    for el in list(tree):
        if el.tag not in SHAPE_TAGS:
            continue
        g, rot, an, c = tags_of(el)
        if g:
            groups.setdefault(g, {'els': [], 'rot': rot, 'an': an})['els'].append(el)
    for g, d in groups.items():
        name = f'{g}~' + (f'a:{d["an"]}' if d['an'] else '')
        make_group(tree, d['els'], name.rstrip('~'), d['rot'])
    # 2. animation steps
    steps = {}
    for el in list(tree):
        if el.tag not in SHAPE_TAGS:
            continue
        g, rot, an, c = tags_of(el)
        if an:
            steps.setdefault(an, []).append(el)
    order = sorted(steps, key=lambda s: (int(re.match(r'\d+', s).group()), s))
    anim_targets = []
    for an in order:
        els = steps[an]
        kind = 'w' if 'w' in an else ('u' if 'u' in an else 'f')
        if len(els) == 1:
            tgt = els[0]
        else:
            tgt = make_group(tree, els, f'Step {an}')
        anim_targets.append((tgt, kind))
    # 3. clean names, renumber ids
    for c in tree.iter(q(P, 'cNvPr')):
        clean_name(c)
    n = 2
    for c in tree.iter(q(P, 'cNvPr')):
        c.set('id', str(n)); n += 1
    if not anim_targets:
        return 0
    steps_ids = [(t.find('.//p:cNvPr', NS).get('id'), k) for t, k in anim_targets]
    sld = slide._element
    old = sld.find('p:timing', NS)
    if old is not None:
        sld.remove(old)
    tm = etree.fromstring(timing_xml(steps_ids, step_ms, gap_ms))
    anchor = sld.find('p:transition', NS)
    if anchor is None:
        anchor = sld.find('p:clrMapOvr', NS)
    if anchor is None:
        anchor = sld.find('p:cSld', NS)
    anchor.addnext(tm)
    return len(steps_ids)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('out')
    ap.add_argument('--step-ms', type=int, default=450)
    ap.add_argument('--gap-ms', type=int, default=120)
    a = ap.parse_args()
    prs = Presentation(a.src)
    for i, s in enumerate(prs.slides, 1):
        k = process_slide(s, a.step_ms, a.gap_ms)
        if k:
            print(f'slide {i}: {k} animation steps')
    prs.save(a.out)
    print('written', a.out)


if __name__ == '__main__':
    main()
