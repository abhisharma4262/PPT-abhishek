#!/usr/bin/env python3
"""Refresh the colleague (plugin) copy of the deck skill from the root SKILL.md.

Run this before you push, from the kit folder:

    python scripts/sync_plugin_skill.py

It reads SKILL.md (your copy, which stays exactly as it is) and writes
skills/myridius-slide-decks/SKILL.md, the copy colleagues get when they install
the plugin. The only differences are:

  * the kit folder points to the kit bundled with the plugin, not your OneDrive path
  * "remember this" asks colleagues to send feedback to you instead of editing
    their read-only copy
  * the reference decks are marked as not bundled

Nothing else is changed. If a line this script looks for has been reworded, it
stops (for the kit folder) or warns (for the rest) instead of guessing.
Standard library only.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "SKILL.md")
DST = os.path.join(ROOT, "skills", "myridius-slide-decks", "SKILL.md")
PLUGIN_NAME = "myridius-slide-decks"
OWNER = "Abhishek Sharma"

BANNER = (
    "<!-- Shared copy for the myridius-slide-decks plugin. Generated from the root SKILL.md "
    "by scripts/sync_plugin_skill.py: edit the root SKILL.md, then run the script. -->"
)

KIT_FOLDER = (
    "Kit folder: the kit ships with this plugin. Its root is the plugin folder two levels above "
    "this file (this file sits in `skills/myridius-slide-decks/`; the same folder as "
    "`${CLAUDE_PLUGIN_ROOT}` when that is set), with `template/`, `tools/`, `examples/` and "
    "`Claude outputs/` in it. The installed copy may be read-only, so copy the whole kit folder "
    "to a scratch folder and run the pipeline there; if node cannot find pptxgenjs or sharp, run "
    "`npm install pptxgenjs sharp` in the copy's `tools` folder. If the user has connected their "
    "own copy of the kit, use that instead."
)

# (description, pattern, replacement, required)
RULES = [
    (
        "skill name",
        r'(?m)^name:\s*"?[^"\n]*"?\s*$',
        f'name: "{PLUGIN_NAME}"',
        True,
    ),
    (
        "kit folder",
        r"Kit folder: `[^`]*`.*?If neither is connected, ask the user to connect it\.",
        KIT_FOLDER,
        True,
    ),
    (
        "'remember this' in the opening",
        r"Memory may be off in a session, so this skill is where the user's standing feedback "
        r"lives: when the user says \"remember this\", record it here \(section 7, last bullet\)\.",
        "This is the shared copy of the skill, installed as a plugin, and each update replaces it, "
        "so do not edit it. When the user says \"remember this\", apply it for the rest of the "
        f"session and suggest they send it to the skill's owner ({OWNER}) so it can be added "
        "for everyone.",
        False,
    ),
    (
        "'remember a preference' rule",
        r"(?m)^- When the user asks you to remember a preference,.*$",
        "- When the user asks you to remember a preference, do not edit this shared copy: apply "
        f"it for the rest of the session and suggest they send it to the skill's owner ({OWNER}) "
        "so it can be added for everyone.",
        False,
    ),
    (
        "reference decks",
        r"- Reference decks in `_Claude`:",
        "- Reference decks (kept by the skill's owner and not bundled with this plugin; use them "
        "only if the user has them, otherwise use the style catalogue above as the reference):",
        False,
    ),
    (
        "pipeline staging line",
        r"Stage the kit into the cloud workspace \(it needs Chromium, node and LibreOffice\), then:",
        "Work from your scratch copy of the kit (it needs Chromium, node and LibreOffice), then:",
        False,
    ),
]


def main():
    with open(SRC, encoding="utf-8", newline="") as f:
        text = f.read()
    newline = "\r\n" if "\r\n" in text else "\n"
    text = text.replace("\r\n", "\n")

    problems = []
    for desc, pattern, repl, required in RULES:
        text, n = re.subn(pattern, lambda _m: repl, text, count=1)
        if n == 0 and required:
            problems.append(f"ERROR: could not find the {desc} line in SKILL.md")
        elif n == 0:
            print(f"warning: could not find the {desc} line in SKILL.md (left as it is)")
    if problems:
        for p in problems:
            print(p)
        print("Nothing written. Update the pattern in scripts/sync_plugin_skill.py to match the new wording.")
        sys.exit(1)

    # banner right after the frontmatter
    m = re.match(r"(---\n.*?\n---\n)", text, flags=re.S)
    if not m:
        print("ERROR: SKILL.md has no frontmatter. Nothing written.")
        sys.exit(1)
    text = m.group(1) + BANNER + "\n" + text[m.end():]
    text = text.replace("\n", newline)

    old = None
    if os.path.exists(DST):
        with open(DST, encoding="utf-8", newline="") as f:
            old = f.read()
    if old == text:
        print("Plugin copy already up to date.")
        return
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Updated {os.path.relpath(DST, ROOT)}. Commit it with your other changes, then push.")


if __name__ == "__main__":
    main()
