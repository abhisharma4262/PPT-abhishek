"""
html2pptx: converts an mkit HTML deck into an editable PPTX (shapes, text boxes, native SVG icons).

  python3 html2pptx.py deck.html out_raw.pptx ["Deck title"]

Then put it into the Myridius template:
  python3 merge_into_template.py out_raw.pptx final.pptx --cover "..." ...

Needs: python playwright (Chromium), node with pptxgenjs + sharp.
If node cannot find them:  npm install pptxgenjs sharp  (in this tools folder).
Text is measured with Inter standing in for Segoe UI when Segoe is not installed; Inter is a
little wider, so anything that fits here fits in PowerPoint.
"""
import asyncio, json, os, subprocess, sys, tempfile
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

async def extract(html, out_json, use_inter=True):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1968, 'height': 1100})
        await pg.goto('file://' + os.path.abspath(html))
        if use_inter:
            await pg.add_style_tag(content=":root{--f:'Inter','Segoe UI',sans-serif !important}")
        await pg.evaluate("document.documentElement.style.setProperty('--s',1)")
        await pg.wait_for_timeout(600)
        data = await pg.evaluate(open(os.path.join(HERE, 'extract.js')).read())
        json.dump(data, open(out_json, 'w'))
        await b.close()
        return data

def main():
    html, out = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else 'Myridius deck'
    work = tempfile.mkdtemp(prefix='mkit_')
    js, raw, mid, svgs = (os.path.join(work, n) for n in ('deck.json', 'raw.pptx', 'mid.pptx', 'svgs.json'))
    data = asyncio.run(extract(html, js))
    print('slides:', len(data), 'items:', [len(s) for s in data])
    env = dict(os.environ)
    env['NODE_PATH'] = os.pathsep.join(filter(None, [env.get('NODE_PATH'), os.path.join(HERE, 'node_modules'), '/opt/npm-tools/node_modules']))
    # photos are referenced relative to the HTML file
    subprocess.run(['node', os.path.join(HERE, 'build.js'), js, raw, title, svgs], check=True, env=env, cwd=os.path.dirname(os.path.abspath(html)))
    subprocess.run([sys.executable, os.path.join(HERE, 'postproc.py'), raw, mid, svgs], check=True)
    subprocess.run([sys.executable, os.path.join(HERE, 'round_pics.py'), mid, out], check=True)
    # every dot_list / tick_list becomes one text box with native bullets
    subprocess.run([sys.executable, os.path.join(HERE, 'native_bullets.py'), out, out], check=True)
    print('written', out)

if __name__ == '__main__':
    main()
