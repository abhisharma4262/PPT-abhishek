// mkit extractor: runs inside the page, returns one array per .slide of paint-ordered items (px, slide-relative).
// Runs inside the page. Returns an array (one per slide) of paint-ordered items in px relative to the slide.
(() => {
  const out = [];
  const parseColor = (c) => {
    if (!c || c === 'none' || c === 'transparent') return null;
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) {
      if (c[0] === '#') { let h = c.slice(1); if (h.length === 3) h = h.split('').map(x => x + x).join(''); return { hex: h.toUpperCase(), a: 1 }; }
      return null;
    }
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    const a = p.length > 3 ? p[3] : 1;
    if (a === 0) return null;
    const hex = p.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase();
    return { hex, a };
  };
  const px = (v) => parseFloat(v) || 0;
  const effOpacity = (el) => { let o = 1; while (el && el.nodeType === 1) { o *= parseFloat(getComputedStyle(el).opacity); el = el.parentElement; } return o; };

  for (const slide of document.querySelectorAll('.slide')) {
    const S = slide.getBoundingClientRect();
    const items = [];
    const rel = (r) => ({ x: r.left - S.left, y: r.top - S.top, w: r.width, h: r.height });

    // ---------- boxes ----------
    function radii(el, cs, r) {
      let rr = [px(cs.borderTopLeftRadius), px(cs.borderTopRightRadius), px(cs.borderBottomRightRadius), px(cs.borderBottomLeftRadius)];
      // inherit corner rounding from an overflow:hidden rounded parent when corners coincide
      let p = el.parentElement;
      if (p && p !== slide) {
        const pcs = getComputedStyle(p);
        if (pcs.overflow === 'hidden') {
          const pr = p.getBoundingClientRect();
          const prr = [px(pcs.borderTopLeftRadius), px(pcs.borderTopRightRadius), px(pcs.borderBottomRightRadius), px(pcs.borderBottomLeftRadius)];
          const near = (a, b) => Math.abs(a - b) < 2.5;
          const L = near(r.left, pr.left), R = near(r.right, pr.right), T = near(r.top, pr.top), B = near(r.bottom, pr.bottom);
          if (L && T) rr[0] = Math.max(rr[0], prr[0]);
          if (R && T) rr[1] = Math.max(rr[1], prr[1]);
          if (R && B) rr[2] = Math.max(rr[2], prr[2]);
          if (L && B) rr[3] = Math.max(rr[3], prr[3]);
        }
      }
      const lim = Math.min(r.width, r.height) / 2;
      return rr.map(v => Math.min(v, lim));
    }
    function emitBox(el, cs, opacity, rect) {
      const r = rect || el.getBoundingClientRect();
      if (r.width < 0.5 || r.height < 0.5) return;
      const b = rel(r);
      let fill = parseColor(cs.backgroundColor);
      const bi = cs.backgroundImage;
      if (bi && bi !== 'none' && bi.includes('repeating-linear-gradient')) fill = { hex: '0C2226', a: 0.035 };
      const rr = radii(el, cs, r);
      const isCircle = Math.abs(b.w - b.h) < 1 && rr.every(v => v >= b.w / 2 - 0.6);
      const kind = isCircle ? 'ellipse' : 'rect';
      // spread shadows (rings)
      let shadowSpec = null;
      const startIdx = items.length;
      const bs = cs.boxShadow;
      if (bs && bs !== 'none') {
        const parts = bs.split(/,(?![^(]*\))/);
        for (const part of parts) {
          const col = parseColor((part.match(/rgba?\([^)]+\)/) || [])[0]);
          const nums = part.replace(/rgba?\([^)]+\)/, '').trim().split(/\s+/).map(px);
          const [ox, oy, blur, spread] = nums;
          if (col && blur > 0) { shadowSpec = { color: col.hex, a: col.a, blur, oy: oy || 0 }; }
          if (col && !blur && spread > 0 && !ox && !oy) {
            items.push({ t: 'shape', kind, x: b.x - spread, y: b.y - spread, w: b.w + 2 * spread, h: b.h + 2 * spread,
              radii: rr.map(v => v > 0 ? v + spread : 0), fill: { hex: col.hex, a: col.a * opacity }, line: null });
          }
        }
      }
      const bw = [px(cs.borderTopWidth), px(cs.borderRightWidth), px(cs.borderBottomWidth), px(cs.borderLeftWidth)];
      const bc = [cs.borderTopColor, cs.borderRightColor, cs.borderBottomColor, cs.borderLeftColor].map(parseColor);
      const bst = [cs.borderTopStyle, cs.borderRightStyle, cs.borderBottomStyle, cs.borderLeftStyle];
      const has = bw.map((w, i) => w > 0 && bst[i] !== 'none' && bc[i]);
      const uniform = has.every(Boolean) && bw.every(w => w === bw[0]) && bc.every(c => c.hex === bc[0].hex && c.a === bc[0].a) && bst.every(s => s === bst[0]);
      const op = (c) => c ? { hex: c.hex, a: c.a * opacity } : null;
      if (uniform) {
        const w = bw[0];
        items.push({ t: 'shape', shadow: shadowSpec, name: el.classList && el.classList.contains('ph') ? 'Screenshot placeholder' : '', kind, x: b.x + w / 2, y: b.y + w / 2, w: b.w - w, h: b.h - w, radii: rr.map(v => Math.max(0, v - w / 2)),
          fill: op(fill), line: { hex: bc[0].hex, a: bc[0].a * opacity, w, dash: bst[0] === 'dashed' ? 'dash' : (bst[0] === 'dotted' ? 'sysDot' : null) } });
        return;
      }
      const any = has.some(Boolean);
      if (any && fill && fill.a > 0.99 && rr.some(v => v > 0)) {
        // outer shape in border colour, inner shape in background colour
        const c = bc[has.findIndex(Boolean)];
        items.push({ t: 'shape', kind: 'rect', ...b, radii: rr, fill: op(c), line: null });
        const ix = b.x + (has[3] ? bw[3] : 0), iy = b.y + (has[0] ? bw[0] : 0);
        const iw = b.w - (has[3] ? bw[3] : 0) - (has[1] ? bw[1] : 0), ih = b.h - (has[0] ? bw[0] : 0) - (has[2] ? bw[2] : 0);
        items.push({ t: 'shape', kind: 'rect', x: ix, y: iy, w: iw, h: ih, radii: rr.map(v => Math.max(0, v - Math.max(...bw))), fill: op(fill), line: null });
        return;
      }
      if (fill) items.push({ t: 'shape', shadow: shadowSpec, kind, ...b, radii: rr, fill: op(fill), line: null });
      // individual sides as thin bars
      if (has[0]) items.push({ t: 'shape', kind: 'rect', x: b.x, y: b.y, w: b.w, h: bw[0], radii: [0,0,0,0], fill: op(bc[0]), line: null, dash: bst[0] });
      if (has[2]) items.push({ t: 'shape', kind: 'rect', x: b.x, y: b.y + b.h - bw[2], w: b.w, h: bw[2], radii: [0,0,0,0], fill: op(bc[2]), line: null });
      if (has[3]) items.push({ t: 'shape', kind: 'rect', x: b.x, y: b.y, w: bw[3], h: b.h, radii: [0,0,0,0], fill: op(bc[3]), line: null });
      if (has[1]) items.push({ t: 'shape', kind: 'rect', x: b.x + b.w - bw[1], y: b.y, w: bw[1], h: b.h, radii: [0,0,0,0], fill: op(bc[1]), line: null });
    }
    function emitPseudo(el) {
      const ps = getComputedStyle(el, '::before');
      if (!ps || ps.content === 'none' || ps.display === 'none') return;
      const r = el.getBoundingClientRect();
      const w = px(ps.width), h = px(ps.height);
      if (!w || !h) return;
      const x = r.left + px(ps.left), y = r.top + px(ps.top);
      const fake = { left: x, top: y, width: w, height: h, right: x + w, bottom: y + h };
      emitBox(el, ps, effOpacity(el), fake);
    }

    // ---------- text ----------
    function fontOf(cs) {
      const w = parseInt(cs.fontWeight);
      // Segoe UI family on Windows: Light (300), Semilight (350), Regular, Semibold (600), Bold
      const face = w >= 650 ? 'Segoe UI' : w >= 550 ? 'Segoe UI Semibold' : w <= 320 ? 'Segoe UI Light' : w <= 380 ? 'Segoe UI Semilight' : 'Segoe UI';
      return { face, bold: w >= 650 };
    }
    const consumed = new Set();
    function collectRuns(el, runs, nodes, hl) {
      for (const n of el.childNodes) {
        if (n.nodeType === 3) {
          let t = n.textContent.replace(/[ \t\n\r\f]+/g, ' ');
          if (!t.trim() && !runs.length) continue;
          if (!t) continue;
          const cs = getComputedStyle(n.parentElement);
          const c = parseColor(cs.color) || { hex: '000000', a: 1 };
          if (cs.textTransform === 'uppercase') t = t.toUpperCase();
          const f = fontOf(cs);
          const lk = n.parentElement.closest('a[href]');
          const strike = (cs.textDecorationLine || '').includes('line-through') || !!n.parentElement.closest('.strike');
          runs.push({ text: t, face: f.face, bold: f.bold, italic: cs.fontStyle === 'italic', size: px(cs.fontSize),
            color: c.hex, alpha: c.a * effOpacity(n.parentElement), spacing: cs.letterSpacing === 'normal' ? 0 : px(cs.letterSpacing), hl,
            link: lk ? lk.getAttribute('href') : null, strike, underline: (cs.textDecorationLine || '').includes('underline') });
          nodes.push(n);
        } else if (n.nodeType === 1) {
          if (n.tagName === 'BR') { runs.push({ br: true }); continue; }
          const cs = getComputedStyle(n);
          if (cs.display === 'inline' && !n.querySelector('svg') && n.tagName !== 'svg') {
            consumed.add(n);
            const isHl = hl || n.classList.contains('hl');
            const before = runs.length;
            collectRuns(n, runs, nodes, isHl);
            if (px(cs.marginRight) >= 3 && runs.length > before) runs[runs.length - 1].text += '\u00A0';
            if (px(cs.marginLeft) >= 3 && runs.length > before) runs[before].text = '\u00A0' + runs[before].text;
          }
        }
      }
    }
    function emitText(el, cs) {
      const runs = [], nodes = [];
      collectRuns(el, runs, nodes, false);
      // trim
      while (runs.length && (runs[0].br || !runs[0].text.trim())) runs.shift();
      while (runs.length && (runs[runs.length - 1].br || !runs[runs.length - 1].text.trim())) runs.pop();
      if (!runs.length) return;
      runs[0].text = runs[0].text.replace(/^\s+/, '');
      const last = runs.filter(r => !r.br).pop(); last.text = last.text.replace(/\s+$/, '');
      const rects = [];
      for (const n of nodes) { const rg = document.createRange(); rg.selectNodeContents(n); for (const rr of rg.getClientRects()) if (rr.width > 0.1) rects.push(rr); }
      if (!rects.length) return;
      const L = Math.min(...rects.map(r => r.left)), T = Math.min(...rects.map(r => r.top));
      const R = Math.max(...rects.map(r => r.right)), B = Math.max(...rects.map(r => r.bottom));
      const tops = new Set(rects.map(r => Math.round(r.top / 4)));
      const lines = tops.size;
      let lh = cs.lineHeight === 'normal' ? px(cs.fontSize) * 1.2 : px(cs.lineHeight);
      let align = cs.textAlign;
      align = (align === 'center') ? 'center' : ((align === 'right' || align === 'end') ? 'right' : 'left');
      items.push({ t: 'text', x: L - S.left, y: T - S.top, w: R - L, h: B - T, lines, lh, align, runs,
        nowrap: cs.whiteSpace === 'nowrap', name: el.tagName === 'H1' ? 'Title' : '' });
    }
    function hasDirectText(el) { for (const n of el.childNodes) if (n.nodeType === 3 && n.textContent.trim()) return true; return false; }

    // ---------- svg ----------
    const serializer = new XMLSerializer();
    function iconSvg(svgEl) {
      const r = svgEl.getBoundingClientRect();
      const c = svgEl.cloneNode(true);
      c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      c.removeAttribute('class'); c.removeAttribute('style');
      c.setAttribute('width', r.width); c.setAttribute('height', r.height);
      items.push({ t: 'img', ...rel(r), svg: serializer.serializeToString(c) });
    }
    const markerColor = { ah: '0C2226', ahl: '194247', ahm: 'D2F0C6', aht: '09A78D', ahs: '337077' };
    function paint(el) {
      const cs = getComputedStyle(el);
      const fill = parseColor(cs.fill);
      const stroke = parseColor(cs.stroke);
      const fo = parseFloat(cs.fillOpacity), so = parseFloat(cs.strokeOpacity), o = effOpacity(el);
      const me = el.getAttribute('marker-end');
      const da = cs.strokeDasharray;
      let dash = null;
      if (da && da !== 'none') { const d = da.split(/[ ,]+/).map(px); dash = d[0] <= 2.5 ? 'sysDot' : (d[0] <= 3.5 ? 'sysDash' : 'dash'); }
      return {
        fill: fill ? { hex: fill.hex, a: fill.a * fo * o } : null,
        stroke: stroke && px(cs.strokeWidth) > 0 ? { hex: stroke.hex, a: stroke.a * so * o, w: px(cs.strokeWidth), dash, cap: cs.strokeLinecap } : null,
        arrow: me ? (markerColor[(me.match(/#(\w+)/) || [])[1]] || '0C2226') : null,
      };
    }
    function toSlide(el, x, y) {
      const m = el.getScreenCTM();
      const p = new DOMPoint(x, y).matrixTransform(m);
      return [p.x - S.left, p.y - S.top];
    }
    function parsePath(d) {
      const toks = d.match(/[MLHVQCZAmlhvqcza]|-?\d*\.?\d+(?:e-?\d+)?/g);
      const segs = []; let i = 0, cmd = null, cx = 0, cy = 0, sx = 0, sy = 0;
      const num = () => parseFloat(toks[i++]);
      while (i < toks.length) {
        if (/[A-Za-z]/.test(toks[i])) cmd = toks[i++];
        switch (cmd) {
          case 'M': cx = num(); cy = num(); sx = cx; sy = cy; segs.push({ c: 'M', p: [cx, cy] }); cmd = 'L'; break;
          case 'L': cx = num(); cy = num(); segs.push({ c: 'L', p: [cx, cy] }); break;
          case 'H': cx = num(); segs.push({ c: 'L', p: [cx, cy] }); break;
          case 'V': cy = num(); segs.push({ c: 'L', p: [cx, cy] }); break;
          case 'Q': { const a = [num(), num()]; cx = num(); cy = num(); segs.push({ c: 'Q', p: [cx, cy], c1: a }); break; }
          case 'C': { const a = [num(), num()], b = [num(), num()]; cx = num(); cy = num(); segs.push({ c: 'C', p: [cx, cy], c1: a, c2: b }); break; }
          case 'Z': case 'z': segs.push({ c: 'Z' }); cx = sx; cy = sy; cmd = null; break;
          default: i++;
        }
      }
      return segs;
    }
    function emitGeom(el, segs) {
      const pt = paint(el);
      const tseg = segs.map(s => {
        const o = { c: s.c };
        if (s.p) o.p = toSlide(el, ...s.p);
        if (s.c1) o.c1 = toSlide(el, ...s.c1);
        if (s.c2) o.c2 = toSlide(el, ...s.c2);
        return o;
      });
      items.push({ t: 'path', segs: tseg, ...pt });
    }
    function handleSvgOverlay(svg) {
      const walk = (node) => {
        for (const el of node.children) {
          const tag = el.tagName.toLowerCase();
          if (tag === 'defs' || tag === 'marker') continue;
          const cs = getComputedStyle(el);
          if (cs.display === 'none') continue;
          const st = items.length;
          try { walkOne(el, tag, cs); } finally { tagFrom(st, el); }
        }
      };
      const walkOne = (el, tag, cs) => {
        {
          if (tag === 'g') {
            if (el.getAttribute('transform')) {
              // a placed icon: rebuild as a standalone 24x24 svg
              const m = el.transform.baseVal.consolidate().matrix;
              const s = m.a, x = m.e, y = m.f;
              const [X, Y] = toSlide(svg, x, y);
              const g = el.cloneNode(true); g.removeAttribute('transform');
              const wrap = `<svg xmlns="http://www.w3.org/2000/svg" width="${24 * s}" height="${24 * s}" viewBox="0 0 24 24">${serializer.serializeToString(g)}</svg>`;
              items.push({ t: 'img', x: X, y: Y, w: 24 * s, h: 24 * s, svg: wrap });
            } else walk(el);
            return;
          }
          if (tag === 'circle') {
            const cx = +el.getAttribute('cx'), cy = +el.getAttribute('cy'), r = +el.getAttribute('r');
            const [X, Y] = toSlide(el, cx, cy);
            items.push({ t: 'circle', cx: X, cy: Y, r, ...paint(el) });
          } else if (tag === 'rect') {
            const x = +el.getAttribute('x'), y = +el.getAttribute('y'), w = +el.getAttribute('width'), h = +el.getAttribute('height'), rx = +(el.getAttribute('rx') || 0);
            const [X, Y] = toSlide(el, x, y);
            items.push({ t: 'rrect', x: X, y: Y, w, h, rx, ...paint(el) });
          } else if (tag === 'polygon') {
            const pts = el.getAttribute('points').trim().split(/\s+/).map(p => p.split(',').map(Number));
            emitGeom(el, [{ c: 'M', p: pts[0] }, ...pts.slice(1).map(p => ({ c: 'L', p })), { c: 'Z' }]);
          } else if (tag === 'path') {
            if (!el.getAttribute('d')) return;
            const pt = paint(el);
            if (!pt.fill && !pt.stroke) return;
            emitGeom(el, parsePath(el.getAttribute('d')));
          } else if (tag === 'text') {
            const tcs = getComputedStyle(el);
            const n = el.getNumberOfChars();
            // SVG collapses runs of whitespace before laying out characters; match that so the
            // character index lines up with getStartPositionOfChar (double spaces used to drop letters)
            const txt = el.textContent.replace(/\s+/g, ' ').trim();
            const fs = px(tcs.fontSize);
            const f = fontOf(tcs);
            const col = parseColor(tcs.fill);
            for (let k = 0; k < n; k++) {
              const ch = txt[k];
              if (!ch || !ch.trim()) continue;
              const a = el.getStartPositionOfChar(k), b = el.getEndPositionOfChar(k);
              const rot = el.getRotationOfChar(k);
              const th = rot * Math.PI / 180;
              const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
              const up = 0.36 * fs;
              const gx = mx + Math.sin(th) * up, gy = my - Math.cos(th) * up;
              const [X, Y] = toSlide(el, gx, gy);
              items.push({ t: 'char', cx: X, cy: Y, rot, ch, size: fs, face: f.face, bold: f.bold, color: col.hex, alpha: col.a * parseFloat(tcs.opacity || 1) });
            }
          }
        }
      };
      walk(svg);
    }

    // ---------- group tags: data-grp (rotation group, optional data-rot) and data-anim (entrance step) ----------
    function gname(el) {
      if (!el || !el.closest) return '';
      const g = el.closest('[data-grp]'), a = el.closest('[data-anim]');
      let s = '';
      if (g) s += 'g:' + g.getAttribute('data-grp') + (g.getAttribute('data-rot') ? '@' + g.getAttribute('data-rot') : '');
      if (a) s += (s ? '|' : '') + 'a:' + a.getAttribute('data-anim');
      return s;
    }
    function tagFrom(st, el) {
      const g = gname(el);
      if (!g) return;
      for (let k = st; k < items.length; k++) if (!items[k].gn) items[k].gn = g;
    }

    // ---------- traversal ----------
    function visit(el) {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') return;
      if (el.classList && el.classList.contains('tpl')) return;   // preview-only template furniture
      const st = items.length;
      if (el.tagName === 'IMG') { const r = el.getBoundingClientRect(); const rr = radii(el, cs, r); items.push({ t: 'photo', src: el.getAttribute('src'), radius: Math.max(...rr), ...rel(r) }); tagFrom(st, el); return; }
      if (el.tagName.toLowerCase() === 'svg') {
        if (el.classList.contains('abs')) handleSvgOverlay(el); else { iconSvg(el); tagFrom(st, el); }
        return;
      }
      if (el !== slide) emitBox(el, cs, effOpacity(el));
      emitPseudo(el);
      if (hasDirectText(el)) emitText(el, cs);
      tagFrom(st, el);
      for (const c of el.children) if (!consumed.has(c)) visit(c);
    }
    visit(slide);
    out.push(items);
  }
  return out;
})()
