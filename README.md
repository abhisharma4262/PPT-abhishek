# Myridius deck kit

Everything Claude needs to build Myridius decks the way you like them. The rules live in the
**myridius-slide-decks** skill (saved in your Claude account; a copy is in `SKILL.md` here).
This folder holds the files the skill uses.

| Folder | What it is |
|---|---|
| `template/Myridius_Template_2026.pptx` | The 2026 template: cover, content sample, divider, end slide (keep this order) |
| `tools/mkit.py` | HTML slide kit: palette, header at template positions (eyebrow and subtitle optional), icons (house size and thin stroke by default), `banner()`, `band_items()`, `link()`, `sources_line()`, `metric_list()`, `badge()`, `dot_list()`, `legend()`, ring and arc helpers |
| `tools/patterns.py` | Brochure-style patterns (scatter to hub to card, output card, product window, flow ribbons) and building blocks for new pictures (chat bubbles, workflow nodes, 3D layers, orbit pills, loop arrows, waffle grids and more) |
| `tools/html2pptx.py` | HTML deck to editable PPTX (shapes, text boxes, native SVG icons, hyperlinks, strikethrough) |
| `tools/merge_into_template.py` | Puts the slides into the template with cover, dividers, end slide, logo and page numbers |
| `tools/group_anim.py` | Groups tagged shapes, rotates them and adds light entrance animations (After Previous, fade or wipe) |
| `tools/add_slide_link.py` | Makes a text box or button jump to another slide (for example the services slide to the deep dives) |
| `tools/insert_slides.py` | Adds, replaces or patches slides in a deck you have already edited, without rebuilding it |
| `tools/lint_text.py` | Flags em dashes, dot separators, emojis, hype words, long titles, text below 9 pt, and statistics on request |
| `tools/render_qa.py` | Renders every slide and a contact sheet for review |
| `examples/example_deck.py` | Four slide patterns, end to end (including the client stories caselet) |
| `examples/patterns_demo.py` | The brochure patterns with linked sources, rotation and animation |
| `examples/style_catalogue.py` | Source of the visual style catalogue: twelve styles built from the building blocks |
| `Claude outputs/Myridius_Visual_Style_Catalogue_v1.pptx` | The catalogue deck: a reference for the quality bar, not a menu |
| `SKILL.md` | Copy of the skill text, for versioning or packaging as a plugin later |

## How to use it
1. Start a **new Cowork task** for each new deck. A fresh task starts clean and loads the skill;
   long threads get compacted and lose detail.
2. Connect two folders: this kit folder (or the `_Claude` folder that holds it and the reference decks)
   and the project folder that holds the documents for that deck. Saved output goes to the project folder.
3. Brief Claude as you normally would: deck type, audience, the decision it should drive, what to
   cover, which documents to read, and whether to research. You can say "use my Myridius deck skill"
   to be sure it is applied.
4. Claude agrees the storyline with you first, then builds, checks and saves the PPTX. Give feedback
   on the slides as usual; edit in PowerPoint whenever you like and tell Claude to work from your file.
5. When you notice a new preference or a repeated correction, say "update my deck skill with this".
   Claude proposes the updated skill for you to save and refreshes `SKILL.md` here. If a deck is open
   in PowerPoint when Claude saves, it writes `<name>_updated.pptx` beside it instead.

## Sharing with colleagues (later)
- **Simplest:** share this folder from OneDrive and send colleagues the skill. Each of them saves the
  skill in their own Claude account and connects the shared folder. The skill's folder path points to
  your OneDrive, so they would need the same folder name or an edited path.
- **Better for a team:** package the skill and this kit as a Cowork plugin. A plugin carries its own
  files, so nobody needs to connect folders, and your Claude admin can publish it in the Myridius
  plugin catalog so colleagues install it in one click. A private GitHub repository in the Myridius
  organisation is a good home for the plugin's source and versions.
- **Avoid a public repository.** The template carries Myridius brand assets, and the reference decks
  and skill examples mention Disney and Fiserv. Before any wider sharing, replace client names in the skill with
  generic examples and keep client decks out of the shared package.

## Run it yourself (optional)
```
cd examples
python3 example_deck.py
python3 ../tools/html2pptx.py example.html example_raw.pptx "Example deck"
python3 ../tools/merge_into_template.py example_raw.pptx example_merged.pptx --kicker "Discussion with Client" --title "Myridius|Example proposal" --date "October 2026" --divider "Appendix@3"
python3 ../tools/group_anim.py example_merged.pptx example_final.pptx
python3 ../tools/lint_text.py example_final.pptx
python3 ../tools/render_qa.py example_final.pptx qa

# brochure patterns, links and animation
python3 patterns_demo.py demo.html
python3 ../tools/html2pptx.py demo.html demo_raw.pptx "Patterns demo"
python3 ../tools/merge_into_template.py demo_raw.pptx demo_merged.pptx --kicker "Kit test" --title "Patterns|demo" --date "October 2026"
python3 ../tools/group_anim.py demo_merged.pptx demo.pptx

# add new slides to a deck you have edited, after slide 8
python3 ../tools/insert_slides.py my_deck.pptx new_raw.pptx my_deck_updated.pptx --after 8 --take 1,2

# make "use case deep dive" on slide 8 jump to slide 13
python3 ../tools/add_slide_link.py my_deck.pptx my_deck.pptx --on 8 --text "deep dive" --to 13
```
Needs Python 3 with python-pptx, lxml, playwright (Chromium) and Pillow; Node with pptxgenjs and sharp
(`npm install pptxgenjs sharp` inside `tools`); LibreOffice and poppler for rendering. Animations play
in PowerPoint; LibreOffice renders show the final state only.
