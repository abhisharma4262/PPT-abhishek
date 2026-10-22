---
name: "myridius-slide-decks"
description: "Create or revise Myridius and Evoq slide decks (client proposals, client discussion decks, offering and POV decks) in the Myridius 2026 template, story-led, research-backed and agency quality."
---
<!-- Shared copy for the myridius-slide-decks plugin. Generated from the root SKILL.md by scripts/sync_plugin_skill.py: edit the root SKILL.md, then run the script. -->

# Myridius slide decks

Use this skill whenever the user asks for slides, a deck, a proposal, a pitch, an offering or solution presentation, or changes to any of these. It encodes how this user wants decks thought through, written, designed and delivered. Read all of it before starting; most rework in past projects came from skipping one of these rules. This is the shared copy of the skill, installed as a plugin, and each update replaces it, so do not edit it. When the user says "remember this", apply it for the rest of the session and suggest they send it to the skill's owner (Abhishek Sharma) so it can be added for everyone.

Myridius is an IT services company that builds and runs agentic and AI-driven software for enterprise clients. Evoq is the brand of Myridius' AI accelerators, including Evoq AEO (Agentic Engineering Orchestrator) and Code to Clarity.

The user is a Myridius leader who sells Evoq to enterprise clients. The user also works on client proposals that may not involve Evoq at all; build those decks in exactly the same way. Past examples: a client proposal (Disney DCL GRATS migration), an offering and point-of-view deck (Agent Assurance), a client discussion deck for a COO-type executive (Fiserv, "Agentic Customer Service Operations", Oct 2026), and an Evoq AEO harness deck for Disney Signature Experiences leadership (Oct 2026; final file "Myridius_DSE_Evoq_AEO.pptx" in the "Evoq_Claude slides" folder). The first two are in the reference folder (see Assets).

**Everything in this skill that comes from past decks (story arcs, diagrams, components, titles) is a reference, not a template.** The message of each slide decides its visual, and the purpose, audience and content of each deck decide its structure. Claude, as the deck builder, makes those calls and is expected to design new structures, diagrams and components whenever they serve the message better.

---

## 1. Philosophy

1. **The deck is a story.** Top to bottom it reads as one argument, shaped by the deck's purpose and audience (section 3). Every slide answers the question the previous slide raised.
2. **Thought leader first, seller second.** Write as a trusted advisor to the client's leadership while wearing the Myridius hat. Consultative, not salesy: frame the client's decision, show the honest options, then show why our approach wins for this case.
3. **The diagram is the message.** Each content slide has one visual idea that carries the point on its own. Text supports the visual, never the other way round. Imagine the visual from the message first, then see whether the kit already has it (section 6); a new diagram is welcome whenever it says the point better.
4. **Agency polish, product-brochure richness.** Clean grids, generous white space, consistent spacing, icons on every list item or tile, nothing cramped or busy. Where a slide explains how something works, aim for the look AI product companies use in their brochures (section 6), not a plain box diagram.
5. **Research-backed and true.** Facts come from the user's documents or from current, verified research. Never invent facts, numbers, client details, product features or quotes. When unsure, say so and ask.
6. **Realistic.** Show trade-offs, including the costs of our own recommendation (set-up time, SME time, platform to run). A deck that makes everything look good is not credible.
7. **Executive tone.** Plain, confident, specific. No arrogance, no hype, no AI-sounding phrasing.
8. **Nothing templated.** Every element on a slide is there because this slide needs it. Furniture that appears on every slide by habit (eyebrows, subtitles, pills, tags) makes a deck look generated.

---

## 2. Workflow

### Step 0. Understand the brief
- Identify: deck type (client proposal, client discussion, offering/POV, internal), audience (CXO, IT leadership, procurement), the decision the deck must drive, length, must-have content, reference documents, whether research is wanted.
- Read every reference document fully before writing (RFPs, solution strategies, walkthrough decks, screenshots, process notes, case studies). Use the client's own words and names (for example "Disney RA stack").
- The user dictates by voice. Fix likely transcription slips from context (for example "Go to Clarity" means "Code to Clarity", "Evo AEO" means "Evoq AEO") and mention any you were unsure of.
- If something core is missing (audience, purpose, scope), ask once, in one round of questions. Otherwise make a sensible assumption, state it, and proceed.
- When the user points to material "in the knowledge base" or "the HTML I gave you" and it is not in the session, look for it in their connected folders (Evoq material lives in their EVOQ offering folder, for example the AEO explainer "one machine, three assemblies" and the Agentic Engineering Playbook) and ask for folder access if needed. Do not redesign without it.
- When the user asks "what do you suggest" or says "let's have a conversation first", reply in chat with a recommendation and two wording options at most, and build only after they agree.

### Step 1. Research (when asked, or when the deck makes claims about the market, competitors, the client or technology)
- Search before stating anything about the present-day world: competitor products and their real capabilities, market shifts, adoption data, standards, the client's stated goals and announcements. Use primary sources (vendor docs, analyst and survey publishers, investor material, regulators).
- Go deep enough to be current. Do not present an approach the market has moved past (for example, hand-written "traditional rewrite" as a modernization option).
- Verify the client's own names: business units, org names and acronyms (Fiserv "FS" is Financial Solutions, not Financial Services). When the user's draft has an org name wrong, correct it with a one-line reason.
- **Sources on the slide are hyperlinks.** Every cited source appears on the slide as a small source line in which each label is a working link to the source page (`sources_line()` / `link()` in mkit). The label is the source name only, no dates: "Gartner predictions", "Gartner customer survey", "Fiserv Investor Day", "Fiserv second-quarter results"; the link carries the detail. When a slide cites several sources, number the claims with superscripts (¹ ² ³) that match the source line. Put the full source list in the reply as well.
- Points that are not public (the executive's scope, internal initiatives, priorities we heard) are marked on the slide with an asterisk and "our understanding, to validate with you".
- Statistics: in client proposals, default to point-of-view statements, not percentages, unless the user specifically wants statistics on a slide. In offering, market and client discussion decks, third-party statistics are fine when sourced on the slide. Ask if unsure. Never put numbers about the client's own situation (attrition, savings targets) on a slide unless asked. Check each figure against the publisher's own release. A stat band with large Pulse numbers on a dark strip works well.
- Enrich with specifics the reader recognises: named tools and platforms, standards, the client's systems, epics and stories, real screens. Richness comes from specifics, not from more words.

### Step 2. Storyline before visuals
Write the spine first: for each slide, the message title, the visual idea in one line (imagined from the content, section 6), and whether it needs an eyebrow or subtitle (section 4). For a new deck of five or more slides, show the spine in chat and get a go-ahead before building (if the user is away, proceed and put the spine at the top of the reply). The visual line is part of that same chat message; it does not add a review step. Check the threading and naming rules in section 3 against the spine.

### Step 3. Build
Design each slide's visual from its message (section 6), then build it in HTML with the mkit kit, preview, export to editable PPTX, then merge into the Myridius template (section 8). Every shape, text box and icon must stay editable in PowerPoint with no loss of quality.

### Step 4. QA
Run the linter and render every slide of the exported PPTX (not only the HTML preview: an arrow hidden behind a shape once looked fine in HTML and was invisible in PowerPoint). Look at every image. Fix and re-render until the checklist in section 9 passes. LibreOffice renders show only the final state of animated slides; describe the animation order in the reply so the user can check it in PowerPoint.

### Step 5. Deliver
- Save the PPTX into the user's project folder with a version suffix (`Client_Topic_v3.pptx`), one new version per round of feedback. Never overwrite a file the user has edited.
- The user may rename a version to share it with colleagues (for example `Myridius_DSE_Evoq_AEO.pptx`). Before every new round, list the folder and work from the newest file, renamed or not.
- "Update in the same version" means overwrite that file, but first check whether the user has changed it since your last save (size or date): if so, patch their copy with `insert_slides.py` or python-pptx instead of rebuilding.
- If the file is open in PowerPoint (locked, the commit is rejected), save it beside the original as `<name>_updated.pptx`, also send it in the chat, and offer to replace the original once the user closes it. Do not wait idle for the lock.
- Reply in a few lines: what changed, any judgement calls, anything the user must confirm (commercial or ownership claims, facts you could not verify, animation order), and a Sources list when research was used.
- When asked for a single slide, deliver only that slide.

---

## 3. Story architecture

The structure comes from the deck's purpose, audience and content, not from a fixed list. Build it this way:
1. Name the decision or belief the audience should leave with.
2. List the three to six messages they must accept to get there, in the order they would ask for them.
3. Give each message a slide (or a short sequence) and pick the opening: context first for a proposal, point of view first for an offering, discussion or thought-leadership deck, recommendation first for a decision-ready leadership audience.
4. Add only the slide types the content calls for. A demo slide belongs only when there is a product to show; credentials only when they help the argument; an appendix or deep-dive section only when depth would interrupt the story.

The arcs below are how past decks were structured. Borrow from them, combine them or ignore them.

### Example: client proposal arc (Disney deck)
1. Cover: "Discussion with <Client>" / "Myridius <Programme name>" / month and year.
2. Background and the bigger picture: current vs target state, how we see the opportunity, how it extends beyond the first project, and "What this presentation covers" (three or four numbered chapters).
3. What it takes: the considerations that matter to the client (icon tiles), plus the three ways to do it.
4. Our POV: the options, each with a mini-illustration of how it works, where certainty comes from, when it is strongest, and what it means for this client. Recommended option in the dark card.
5. Comparison: options as columns, decision dimensions as rows (efficiency and speed, quality and traceability, repeatability and scale, cost of ownership, reusability after go-live).
6. Build approach: how we build it with the client and hand it over (assets we bring with approvals, built together, replicated, owned by the client) next to what the solution is made of.
7. The solution: how it works (people, the line, the learning loop, always-on controls).
8. Applied to the client (eyebrow "... (CLIENT - Illustrative example)"): the governed path on the client's own system, with what it drives for them.
9. Demo: product screenshots, brochure style, with "Demo available".
10. Trust: how quality is assured (guardrails, evals, human gates, audit).
11. Appendix divider, then depth: evals, testing including UAT, execution and hosting options.
12. End slide.

### Example: offering and POV arc (Agent Assurance deck)
Market shift (where it is happening) → why tools alone fail → our credentials (client examples) → section divider "Our point of view" → urgency (sourced statistics) → the mandate (2x2) → old world vs new world (comparison table with mini-diagrams) → failure modes (hub diagram, then cards) → what it requires → our framework (dimensions) → platform partner and what Myridius brings → workflow loops → demos → appendix: maturity curve, engagement models, tool landscape → end.

### Example: client discussion arc (Fiserv deck, first meeting with an SVP of operations; the version the user signed off)
The user adds the Myridius intro slides. The deck's anchor term is on the cover and used throughout: "Agentic Customer Service Operations". Three themes (A Equip the front line, B Automate behind the conversation, C Run it as a service) are introduced on the hook slide and every later slide reuses them.
1. Cover: "Discussion with Fiserv" / "Agentic Customer|Service Operations" / month and year.
2. OUR POV, the hook: "Agentic AI is moving customer service from answering to resolving". Three shifts as from/to lanes, one per theme; a market signals band with linked sources.
3. OUR POV: "Resolution is decided behind the AI front door". Front-door strip, one broad arrow down, the conditions grouped under the three themes.
4. OUR POV: "Fiserv is already moving on all three shifts". The client's stated goals on top, then per theme what they have said or started (numbered to linked sources) and what it will need next.
5. Bridge slide, eyebrow "Illustrative example | FINANCIAL SOLUTIONS OPERATIONS": "Your customer service operations are where the shifts land first". The executive's area (scope, what is in motion, stated priority), marked "our understanding, to validate with you". This is the one slide that connects the anchor term to the client's org name.
6. Divider "How Myridius can help".
7. Where we fit: "Myridius adds the layers that turn AI answers into resolution". Equation: platforms the client chooses + layers Myridius adds = "What Fiserv gets" as business outcomes (never labelled "Theme A/B/C").
8. Services anchor (section 6): "What we can do for your customer service operations". Advise, Build, Run as rows across the three themes as columns, the proposition codes in the cells, a "Click here for use case deep dive" link to the deep-dive section, and a "Built on Myridius engineering" line.
9. to 10. Client stories (caselet template), each with a "Related:" line naming the propositions it proves.
11. How we engage: advise, build or run, each can start on its own; a band of how-we-work items.
12. "Where to focus first, and how we could start": three discussion questions, then three proposed next steps, each with "You bring" and "You get" (advisory working session; rapid prototype or proof of concept on one use case with real data; MVP with one team, measured).
13. Divider "Use Cases - Deep Dive", then one slide per proposition (A1, A2, B1, B2, B3, C1, C2) in a shared frame: What we see | the brochure visual | What it moves (↑/↓ metric list) | How Myridius helps. Eyebrow names the theme and code ("EQUIP THE FRONT LINE (A1)").
14. End slide.
The user moved the deep dives from the middle of the story to this end section: the main story stays short for the meeting, and the services anchor links into the depth.

### Example: Evoq AEO harness arc (Disney Signature Experiences, Oct 2026; the version the user shared with colleagues)
Generic Evoq AEO slides that work for any client, plus one opportunity slide in the appendix.
1. Cover: "Discussion with Disney" / "Evoq AEO harness | Agentic engineering" / month and year.
2. OUR POV, the concept: "AI coding agents need an engineering harness to work at scale". Concentric rings around the AI coding agent (Context, Conventions, Workflow, Checks, Record) and a table: Layer | The agent on its own | At scale, teams also need. No product names on this slide; a band at the bottom says Evoq AEO brings this engineering harness.
3. THE EVOQ AEO HARNESS, the bridge: "Every layer of the harness is built into Evoq AEO". The same rings with an "Evoq AEO harness" badge, and the Evoq components for each layer.
4. INSIDE THE EVOQ AEO HARNESS: "The Evoq AEO harness runs engineering end to end in five modules" (Ingestion, Context Engine, I2D engine, Trust and flexibility, Audit spine, with a conventions band on top). No subtitle.
5. ARCHETYPES: "The same harness assembles differently for each archetype". Four families (build new, evolve what exists, modernize and migrate, run and sustain) as assembly lines of steps, with "E.g.," notes. No subtitle.
6. Appendix divider, then ILLUSTRATIVE EXAMPLE | <OPPORTUNITY>: "The club management system would draw on three archetypes", based on "our current understanding, to validate with you".
7. End slide.
Lessons from building it: explain the concept before the product, then reuse the same diagram to map the concept to Evoq; keep the opportunity slide conditional and in the appendix (we do not know yet whether we will win the work); keep the other slides client-neutral so they can be reused.

### Threading rules
- **One thread from the hook to the end.** Open with a hook that introduces the deck's organising idea (themes, shifts, buckets), then double-click on it slide by slide. Every slide should visibly reuse the same terms: theme letters, column names, proposition codes. The user rejected a v1 where each slide was "a standalone story" with its own new terms; "we may lose the audience".
- **Naming thread.** Pick one anchor term for the subject on the cover (for example "customer service operations") and use exactly that term on every slide. Introduce the client's own org name for it (for example "Financial Solutions Operations") on one explicit bridge slide that connects the two, and never switch between terms silently. The user found "AI-led customer service" on one slide and "FS operations" on another confusing.
- **Zoom in: industry, then client, then their area.** For a first meeting, never open on the executive's own unit as if we already know each other. Start with our industry point of view, then look at the client through that lens, then the executive's area on the bridge slide. The user prefers "Our POV" to "Our understanding".
- **State the point of view early, then drill down.** Make the thesis clear in the first few slides, then prove it slide by slide.
- **Introduced once, reused everywhere.** Themes or dimensions or buckets introduced early must be the same buckets used later. Never add a bucket on slide 4 that slide 1 did not introduce.
- **No duplication** across slides or within a slide. If two sections say the same thing, merge them.
- **Each slide earns its place.** If a slide re-explains what the previous one said, cut or merge it.
- **Anticipate the reader's practical question.** Example: "How do the accelerators get into the client's AWS? Do we rebuild them or bring them?" Answer it on the slide (installed, not rebuilt).
- **Depth goes to the end**, behind a divider (appendix, or a "Use Cases - Deep Dive" section), linked from the slide that introduces it.
- **Offer a non-controversial alternative** when a slide scores or judges options (for example scored comparison vs "what the client would need to add").

### Positioning rules for client discussion decks
- **A services anchor slide in every client deck.** One slide a salesperson can present on its own: "this is all we can do for you from the services perspective", in service language (advise, build, run across the themes, with proposition codes), linked to the deep dives.
- **Outcomes are business outcomes for the client** (lower cost to serve, faster cycle time, revenue sooner, clients kept), headed "What <Client> gets". Never label outcomes with internal constructs such as "Theme A".
- **Stay tool-agnostic.** Name the client's platforms only as examples inside categories ("AI agents, e.g., Sierra"; "Contact center platform and AI assistants, e.g., Dynamics 365, Copilot"). Never tie a proposition to one product; the client may have more tools or change them, and our approach must hold either way.
- **Neutral comparisons; never imply the client is doing it wrong.** When contrasting the tools a client uses today with what we bring, describe what the tool does on its own as plain fact ("Runs the tests it is asked to run") and frame our side as what scale needs ("At scale, teams also need"). Avoid "without", minus or cross icons and deficit words for the client's current state.
- **Concept before product.** A point-of-view slide explains the idea in plain terms with no product component names; the next slide reuses the same diagram and maps each part to the Myridius offering.
- **Inputs and outputs in business language.** Not "what goes in / what comes out"; use phrases such as "business intent and enterprise context" and "governed, release-ready software", or a "The result" band.
- **Opportunity-specific slides are illustrative.** Put them in the appendix, mark them "Illustrative example", base them on "our current understanding, to validate with you", and use conditional titles ("would draw on"). Never write as if the deal is won or the start date is ours.
- **Say what we do, not what we do not do.** Position around our strengths so gaps are implicit; never write "not in our scope" or "we do not build X".
- **How we engage stays high level** for CXO, CIO and COO audiences: advise, build, run, with a light "how we work" band. No sprint lengths, durations or delivery mechanics. Use "Managed by Myridius" style wording for run services.
- **Next steps are few and action-oriented.** Two or three concrete steps, each with "You bring / You get": an advisory working session to pick and size use cases; a rapid prototype or POC on one use case with real data; an MVP with one team. No vague steps such as "agree the way forward". Three discussion questions at most.
- **No numbers about the client's own situation** (attrition, savings targets, KPIs) unless the user asks; describe their priorities in words with a linked source. Our own case-study outcomes may carry numbers.
- **Sensitive context stays off the slides.** Leadership changes, litigation and investor pressure go in the reply as briefing for the user, not on slides.
- **Mask client names in credentials** unless the user confirms they can be named ("two leading American insurance software providers", "Leading American insurtech").
- **Plain language for regulation.** Do not lean on acronyms the audience may not know (the user, a BA by background, did not know Reg E or Reg Z). Say what the rule does ("US consumer protection rules set deadlines to acknowledge, investigate, credit and close every dispute") and link the rule in the source line.

---

## 4. Headers and titles

The header elements sit at fixed template positions (`header()` in mkit). Only the title is always there.
- **Title**: the message of the slide, written for a CXO. One line (about 65 characters at 28pt bold; the user's titles run 63 to 66). Sentence case. Two lines only when the user asks.
- **Teal accent: use it generously.** Highlight the phrase that carries the message on most titles (for example "...moving customer service **from answering to resolving**"); the user removes what is not wanted. Do not ration it to one or two slides.
- **Eyebrow: only when it orients the reader.** 1 to 3 words, caps, teal. Keep it for chapter markers the audience needs: OUR POV on point-of-view slides, the theme and code on deep dives ("EQUIP THE FRONT LINE (A1)"), "CLIENT STORIES (1/2)", the client's org name on the bridge slide ("Illustrative example | FINANCIAL SOLUTIONS OPERATIONS"), DEMO, APPENDIX topics. Drop it on slides where it only repeats the title. `header(None, title, ...)` leaves it out.
- **Subtitle: only when it adds context the title needs.** One line, for example the scope of a claim or the supporting proof, or the definition of a new term ("An engineering harness is the context, standards, process and controls a team puts around its AI coding agents"). When the title is descriptive, the subtitle carries the message ("When AI writes the code, the method decides the outcome"). Never write a subtitle just to fill the slot. The user deletes subtitles that only explain mechanics the visual already shows (they removed them from the five-modules and archetypes slides), so leave those out.

Titles the user accepted: "Agentic AI is moving customer service from answering to resolving"; "Resolution is decided behind the AI front door"; "Fiserv is already moving on all three shifts"; "Your customer service operations are where the shifts land first"; "Myridius adds the layers that turn AI answers into resolution"; "What we can do for your customer service operations"; "Where to focus first, and how we could start"; "Disputes close on time when AI does the legwork"; "Build the harness once and run every migration after GRATS on it"; "AI-generated code earns trust through guardrails, evals and people"; "Adoption is racing ahead of assurance"; "AI coding agents need an engineering harness to work at scale"; "Every layer of the harness is built into Evoq AEO"; "The Evoq AEO harness runs engineering end to end in five modules"; "The same harness assembles differently for each archetype"; "The club management system would draw on three archetypes".

When fixing wording elsewhere, leave accepted titles alone: the user reverted "Five modules cover the full engineering lifecycle" and "The same harness adapts its steps to each archetype" to the originals above.

Titles the user rejected, and why:
- "The AI is the same in every option, the harness around it is not": childish, not CXO messaging.
- "We run modernization as an AI factory, not a one-off project": arrogant.
- Titles that explain the slide ("Overview of approaches") instead of stating its message.
- "A fast pick-up in November, then AI-led delivery to September": childish, sounds AI-written, and assumes we have won the work.

---

## 5. Writing rules

**Never use em dashes.** Not in titles, body, labels, notes or replies. Rewrite with a semicolon, comma, colon or two sentences. The user has removed hundreds by hand. Also no en dash used as a dash, no double hyphens. The linter checks this. If a semicolon or colon does not make sense in a sentence, make sure it is grammatically correct and uses business language.

**No dot or bullet separators inside text.** Never join items with a middle dot or bullet ("Advise · Build · Run", "Fast · Governed"); the user calls it AI slop. Use separate items with icons and thin divider lines (`band_items()`), or the user's own " | " style in eyebrows. The linter checks this.

**Write like a person, not a model.** The user reads these patterns as AI writing and rejects them:
- Cute metaphors and personification in explanations: "the rest stay home", "remembers it all", "telemetry feeds the same return lane", "always on, never a stage". Short descriptive taglines under a component name are fine ("brings the work in, as it is", "records every hop"; the user kept these).
- Long lines built as clause; clause with an abstract second half, and stacked participles: "Inside the harness, the I2D engine deploys only the components each piece of work needs; the rest stay home"; "our detailed instructions, best practices and coding conventions, plus your own, loaded once and applied on every run".
- Repeated "every step, every change, every run" cadence and lists of three by habit.
Write what a consultant would say out loud: a subject, a verb, a concrete point ("The I2D engine picks the components each piece of work needs, so a small fix does not go through every step"). The user's own rewrite of the conventions line shows the tone: "Your coding conventions added at the start of the project combined with the industry best practices". Lead with the client's own standards and describe ours as industry best practices rather than branding everything as Myridius.
When asked to remove AI language across a deck, change only the sentences with these patterns. Keep accepted titles and keep component and step labels that come from the source material (the user reverted "Blueprint", "Build ×n", "Safety-net tests" and "Ready" after they were renamed). Expect the user to adopt rewrites selectively.

No AI markers or slop: no hype words (unleash, robust, cutting-edge, game-changer, transformative, elevate, empower, synergy, best-in-class, world-class, next-gen), no "in today's fast-paced", no "it's not just X, it's Y", no "not only... but also", no moreover / furthermore / in conclusion, no filler intensifiers (genuinely, honestly, truly, really, very), no emojis, no exclamation marks, no rhetorical questions as titles.

Style:
- Short phrases, not paragraphs. A tile has a 2 to 4 word heading and one line beneath. Bullets stay under about 15 words and two lines. Groups of three are ideal; four or five at most.
- Low text density. If a slide feels heavy, cut words; never shrink fonts below the floor (section 6).
- Specific beats generic: "Payouts must match to the cent" beats "ensure accuracy".
- No arrogance or absolutes ("only we", "guaranteed", "unmatched").
- Plain labels over invented jargon: "What Fiserv gets", "What it moves", "You bring / You get", "Related:".
- Use client-provided facts verbatim; when given a slide or screenshot to polish, do not reinvent its facts or assumptions, only improve wording and layout.
- Explain jargon the first time, or avoid it (the user asked "what is RA standards?").
- Prefer neutral, descriptive comparisons to judgement labels. Labels such as "Included / Partly" can read as controversial; describe what each option does or what the client must add.
- Harvey balls or scores only when the user wants scoring, and label them as Myridius' assessment.
- Trade-offs: state the real cost of each option, including ours.
- People are "the Myridius team"; Evoq is the accelerator brand. Use product names exactly: Myridius, Evoq, Evoq AEO (Agentic Engineering Orchestrator), Code to Clarity, Context Engine, Intent2Delivery (I2D) engine, Agentic QE.
- The user often uses ";" as a joiner in short lines ("Fast to start; but..."). That is fine in a short line, but do not make "clause; clause" the default shape of every sentence (see "Write like a person" above).
- Notes that describe one example of a general case start with "E.g.," ("E.g., a migration. Parity tests check that the new system gives the same results as the old one."). Do not add notes that only list what is not used.
- Evoq AEO terms (Oct 2026): say "AI coding agents" (for example Claude Code, Codex, Cursor CLI, GitHub Copilot), never just "coding agents". Call the idea an "engineering harness" and our version the "Evoq AEO harness"; "core harness" and "outer harness" are for the presenter to say, not for slides. Use the word "archetype" for types of engineering work, grouped into families when there are more than five. Say "inherited or partly built app", not "takeover".

---

## 6. Visual design system

### Template and canvas
- Always the Myridius 2026 template (from the "Myridius_Disney_GRATS Migration_Oct2026" pack). 16:9, 13.333 x 7.5 in. White content slides.
- The template's content layout draws the Myridius logo (bottom left) and the page number (bottom right), plus the copyright line where the layout has one. Never draw your own logo, footer, brand mark or page number, and keep the bottom 0.75 in clear.
- Cover: beige layout with the large M graphic. Section dividers ("Our point of view", "How Myridius can help", "Use Cases - Deep Dive", "Appendix"): dark layout with the teal M. End slide: beige "Learn more at myridius.com".

### Colour (only these)
| Token | Hex | Use |
|---|---|---|
| Carbon Moss | 0C2226 | dark panels, primary dark text, recommended card |
| Quantum Leaf | 194247 | titles, body text, secondary dark panels |
| Ocean Slate | 337077 | secondary text and labels; sparingly |
| Myridius Teal | 09A78D | eyebrows, title accents, small accents |
| Infinite Mint | D2F0C6 | light fills, icon tiles, highlighted cells; text on dark |
| Pulse Green | 52E081 | highlights on dark; sparingly |
| White | FFFFFF | background, text on dark |
| Beige | F6F3F0 | soft panels behind brochure visuals, output card rows |

Light surfaces use Moss, Leaf or Slate text. Dark surfaces use White or Mint text. Avoid other theme colours (lime, extra greens) unless the user asks. Keep box colours uniform within a group; the user rejected progressive or rainbow fills ("make them transparent like the first box").

### Typography
- Segoe UI only (Semibold allowed; no Light or thin weights). Template sizes: eyebrow 10pt bold caps, teal, tracking 2.1pt; title 28pt bold Leaf; subtitle 12pt Leaf.
- **Floor: nothing below 9pt (18 px on the canvas)**, including small-caps section labels, chips, tags, badges, legends, captions and source lines. The user found 7.5pt section labels too small and raised them to 9pt. Card body text 10.5pt (21 px); key outcomes and "what it moves" lines about 12pt (24 px); card headings 11 to 13pt bold. If text does not fit, cut words or enlarge the box. The linter warns on any run below 9pt.
- Left-aligned text. Titles and subtitles left-aligned at the template positions.

### Components
These are defaults that keep decks consistent, not a limit. The content decides what a slide needs: tables, timelines, maps, charts, screenshots, illustrations, quotes, org charts, or something new. Keep whatever you use inside the palette, typography and polish rules above.
- Cards: white with a thin border (Moss at 16%) or very light fill; radius about 0.1 in. One dark card (Moss) marks the recommendation or the hero element.
- Icons (the user corrected these by hand): line icons with round caps, glyph about 70 to 75% of its round tile, thin stroke of about 1/2 to 3/4 pt whatever the size, dark teal (Leaf) on mint tiles and Pulse on dark tiles. Tile size follows the need (40 to 76 px on the canvas is typical). Never small glyphs with thick strokes. mkit's `icon()`, `ico()` and `gicon()` default to this; pass `sw` only for a deliberate exception. Every list item and tile gets an icon. Use icons, not big letters or numbers, as the visual anchor of a tile.
- Bands: a dark Leaf or Moss strip for a takeaway or a set of always-on items. Order inside a band is always icon, then label, then message (`banner()`), or icon, label, then separate items with their own icons and thin dividers (`band_items()`). Never put the icon between the label and the message.
- **Lists are one text box with native bullets** (the user's rule, Oct 2026). Every set of bullets that belongs together is a single text box whose paragraphs carry real PowerPoint bullets, so the user can move, align and edit the list as one block. Never draw a separate dot shape per bullet or one text box per item; the user found those impossible to realign. The chosen style is a teal dot (Pulse on dark panels), Arial "●" at about 86% of the text size, with a hanging indent and a little space between items; sign-off and outcome lines use the Wingdings check in teal. Bold key phrases stay as bold runs inside the bullet text. mkit's `dot_list()` and `tick_list()` export this way automatically (section 8).
- Fewer pills. Avoid status pills, tags and chips that make a slide busy. Theme references are a small badge plus text (`badge()`); "What it moves" is a ↑/↓ metric list (`metric_list()`); caselets end with a plain "Related: A1 Knowledge foundation, B1 Disputes" line. Mint chips are for named assets only (Code to Clarity, Eval suites).
- Numbered steps and chevrons for sequences; connectors with arrowheads, always labelled (an unlabelled dotted line confused the user). Connectors sit in the foreground and must be visible in the exported PPTX; draw arrows inside a flex row or on an overlay SVG layer, never under a filled shape. When a whole group feeds a whole group, use one broad arrow, not several dotted lines that look like links to specific boxes, and never let a label sit on a line.
- When one element of a diagram differs in kind (for example a "Run" layer across a stack), give it the same visual weight as its peers and frame the diagram (dotted container, ownership legend: dark = Myridius, light = client and partners) so it does not look bolted on.
- Mark worked examples and mock-ups "Illustrative example" (in the eyebrow or a small caption).
- No unexplained badges or numbers. Everything on the slide must be readable without a presenter.

### Services anchor slide
A matrix the sales team can present alone: Advise, Build, Run as rows (icon and one line each) across the deck's themes as columns; each cell names the propositions (code and short name) that live there, and cells holding a deep-dive proposition are tinted mint. Add a link button ("Click here for use case deep dive") that jumps to the deep-dive divider (`add_slide_link.py`), and a closing line on the engineering base ("Built on Myridius engineering: data and integration, AI and agent engineering, quality engineering for AI, cloud and platform migration"). Title in the client's language: "What we can do for your <anchor term>".

### Client stories (caselet template)
All case studies and caselets use this layout (from the user's "Client stories | Data & AI" slides):
- Eyebrow "Client stories (1/2)"; the title states what the set proves ("We have built AI knowledge and case automation at scale"); no subtitle.
- Three columns separated by thin vertical rules; row labels on the left in small caps: CLIENT SITUATION, OUR SOLUTION, OUTCOMES.
- Top of each column: the anonymised client descriptor in italic slate ("Multinational financial services company").
- Client situation: two or three lines with key phrases in bold.
- Our solution: light card with an icon tile and the solution name in bold, then three short points (teal dot bullets, bold key phrases).
- Outcomes: dark Moss card with three check lines in white; numbers allowed when they come from the user's material.
- Under each column: a plain "Related:" line naming the propositions it proves ("Related: A1 Knowledge foundation").
- Use only facts from the user's case-study material. When a story has no outcomes or situation, write only what the solution implies and flag it for the user to complete.

### Designing the visual: content first, then the repository
The visual is imagined from the content, then looked up in the repository; never the other way round. The repository makes a good idea faster and better built; it is not where ideas come from.
1. Write the slide's message in one sentence.
2. Name the relationship it is about: a sequence, a choice, a comparison, layers, a cycle, a hierarchy, before and after, cause and effect, convergence (many inputs to one result), volume splitting across routes, ownership moving from one party to another, a conversation or interaction, maturity over time, parts of a whole.
3. Imagine two or three visual ideas from the content alone, before opening any library. Ask what the audience should see to believe the message (the real thing: a screen, a queue, a conversation, a trace, money or volume moving) and how a product company or a top agency would draw it. New and unusual forms are welcome when they are clearer.
4. Then check the repository for each idea: the building blocks and patterns in `tools/patterns.py`, the visual style catalogue, the reference diagrams below and past decks. If the idea already exists, reuse its code and adapt it to the content; if parts exist, build from the blocks; if nothing exists, build it new and add it to the repository once the user likes it. Never start from the library and fit the content to a pattern.
5. Pick the idea where the picture alone carries the message. Test it: hide the text; the shape should still suggest the point. Then add only the words it needs.
6. Within one deck, do not repeat a pattern by habit (the user asked not to repeat the knowledge-foundation pattern everywhere). Across decks, repetition is fine: each deck goes to a different client, so reuse whatever fits the content. There is no log of past decks to check.

### What makes a visual look polished
These qualities come from the visual style catalogue and the slides the user liked. Apply them to every visual, new or reused:
- **Show the real thing.** A realistic mock-up (a chat, a queue, an agent trace, a summary card, a product window) with plausible specifics beats boxes that describe it. Label it "Illustrative example".
- **One focal element.** A hero card, a dark panel or a highlighted row draws the eye first; everything else supports it.
- **Depth through layers.** Cards on soft panels, a window frame, a highlighted row inside a list, isometric plates, soft shadows. No gradients.
- **A clear path for the eye.** Left to right or top to bottom, arrows that show direction, numbered or timed steps.
- **Notes outside the picture.** Explanations sit in a side panel, a legend or beside lines, never on top of the visual.
- **One colour logic per slide.** For example dark for the AI or Myridius, mint for people or highlights, white for the client's systems; add a legend when colour carries meaning.
- **True proportions or an honest label.** Sized shapes (a waffle, bar heights, bubble sizes) follow real numbers; otherwise mark them "illustrative".
- **No dead space inside shapes.** If a card or block has room left, give it a small meaningful element (a mini visual, a status row) rather than leaving it empty or shrinking type.
- **Motion only when it carries meaning.**

### Brochure visuals and animation
The user wants explanatory slides to look like product-company brochures (the reference the user shared: messy inputs, struck-through noise, a hub, one clean output card), built as editable shapes rather than images.
- `tools/patterns.py` holds the repository in code. Patterns: `scatter_hub_card()` (scattered, slightly rotated input chips with noise struck through, converging on a hub, one clean output card; used and liked for "knowledge sources to one trusted answer" and "support tickets to a triaged queue"); `out_card()` (the clean product-style result card); `ui_window()` (a product window framing panes so a process reads as one tool); `flow_ribbons()` (Sankey-style split of volume; tried for L1/L2 support and the user preferred the scatter view, so use it only when proportions are the message). Building blocks for new pictures: `text_box`, `anim`, `chat_bubble`, `avatar`, `node`, `port`, `edge`, `mini_row`, `bento_cell`, `steps_track`, `iso_plate`, `ring_points`, `orbit_pill`, `loop_arcs`, `waffle`.
- The visual style catalogue ("Myridius_Visual_Style_Catalogue_v1.pptx" in the kit's "Claude outputs" folder; source `examples/style_catalogue.py`) shows twelve styles built on customer service examples. They are references for the quality bar and a head start in code, not a menu:

| Style | Use it for | Motion |
|---|---|---|
| Bento grid | Many parts of one offer or platform in one view | Static |
| Conversation and actions | What AI does during one interaction (chat on one side, system actions on the other) | Builds message by message |
| Agent trace | Each AI step with its evidence and the point where a person approved; auditability and control | Steps appear in order |
| Workflow canvas | Branching logic, routing, where people step in | Builds left to right |
| Swimlane handoffs | Work moving between customer, AI agent and teams, with context passed at each handoff | Builds along the path |
| Before and after | The change a solution makes to a task | The after side wipes in |
| Layered stack (isometric) | Architecture, what sits on what, who runs each layer | Optional, bottom up |
| Orbit | One core connected to channels and platforms | Static |
| Horizon staircase | Maturity and phases over time, with the condition to move on | Static |
| Bubble matrix | Options compared on two criteria, with where to start | Static |
| Flywheel | A cycle that improves with each turn; operating models | Static |
| Stat hero | One or two sourced numbers that frame the issue (big number, waffle, linked source) | Static |

- When a message needs a new picture, build it from the blocks, and add it to `patterns.py` (or the catalogue) once the user likes it.
- Inside output cards and mock-ups, write realistic content (a real-looking question, answer and cited source; a queue with priorities), labelled "Illustrative example".
- **Animation only when motion carries meaning**: inputs converging, a flow building up, a before turning into an after. Structural pictures (windows, grids, tables, stacks, matrices) stay static. The user called an animation on a static window slide "force fit". Use entrance animations that play automatically (After Previous, fade or wipe), a few steps per slide, never flying or bouncing effects.
- Rotation (`data-rot`) only on small elements that should look scattered; keep it within about 3 degrees.

### Offering options and redesigns
- When the user dislikes a slide, give three genuinely different visual ideas, not restyles: for example an equation (platforms + layers = outcome), a ring around a core, and swimlanes across a sequence. Keep the same title so only the visual differs, label the eyebrows "(Option 1/2/3)", insert them right after the original, and recommend one in a line. For a first executive meeting the user chose the simplest to read in five seconds (the equation).
- When the user likes one option, make two or three variants of that same design (for the harness slide the user picked the concentric rings, then asked for ring variants that also showed how work runs with and without the harness), keep the same title, and expect the user to delete the variants they do not want. Drop option sets the user rejects instead of carrying them forward.
- A redesign must be an upgrade, not a downgrade. The user rejected two rounds of experimental redesigns that stripped content or went abstract (big letters, light weights, sparse minimal layouts). Keep the slide's structure and content, and raise the richness: better visual, icons, realistic detail.

### Reference diagrams from past decks (inspiration, not a menu; checked after the idea, step 4 above)
- Options cards with mini-illustrations (people with agents; a platform with managed paths; a harness ring), recommended option dark.
- Columns x rows comparison: options as columns, decision dimensions as row bands with icons on the left; row labels once on the left, never repeated in cells.
- Harness ring: segmented donut (Understand, Govern, Prove, Scale) around an engine core, curved labels, callouts with leader lines and asset chips.
- Harness rings (Evoq AEO deck, liked): the AI coding agent as a dark core inside five concentric mint rings with curved labels (Context, Conventions, Workflow, Checks, Record), a small dark badge on the outer ring naming the harness, and a table on the right (Layer | The agent on its own | At scale, teams also need). The rings build ring by ring with the matching table row. The next slide reuses the same rings with a product badge and the components for each layer.
- Assembly lines for archetypes: one row per family, the family and its archetypes on the left, then the steps as round nodes on a line, coloured by type (context, engineering step, human gate, quality or security check, starting point, release), with an "E.g.," note under each row; rows wipe in one after another.
- Concentric layers of control (guardrails, evals, human gates, audit trail) with an exit path to "accepted".
- Governed path: chevron stages with human sign-off gates, an always-on band below, "what it drives" outcomes.
- Factory line: people row, migration line, learning loop, always-on controls.
- Staircase for layered testing ending in UAT and go-live sign-off.
- Hub and spoke for failure modes; 2x2 for mandates; maturity curve with three stages; stacked dimension layers with tool examples.
- Current to target state mapping (from, arrow, to) on a dark background card.
- From/to lanes for shifts: one lane per theme with the theme badge, a muted "from" card, a teal-bordered "to" card, and "what it opens up" with an icon.
- Equation: client's platforms (light) + Myridius layers by theme (dark) = what the client gets, as business outcomes (teal-bordered), with round + and = operators.
- Deadline-bound process: a deadline card on top, stages from intake to closure with the AI work in each, a line where people decide, and an always-on band below (deadline tracking, letters on time, audit trail).
- Brochure screenshots: real product screens, cropped tight, rounded corners and soft shadow, no window dots or browser chrome, captions and numbered callouts outside the screen, never covering it; only screens relevant to the story.

---

## 7. Collaboration rules (learned from interventions)

- When the user has modified a slide or the deck, work from their latest file and keep their layout and wording. Change only what was asked. If you cannot access their file, rebuild their version exactly from the screenshot and say so.
- After each round, diff the user's newest file against the version you delivered: the user often copies only some of your changes into the file they share and edits the rest themselves. Treat what they reverted as a preference, keep what they wrote in their own words, and record the lessons here.
- Read the user's final file after sign-off and record what they changed (restored views, moved sections, re-added eyebrows, renamed dividers) as lessons here. Example: in the signed-off Fiserv deck the user restored "OUR POV" eyebrows that had been stripped, restored the scatter view on C1 over a new Sankey, and moved the deep dives into an end section.
- When a change on one slide affects others, tell the user which slides and give the replacement text; do not regenerate those slides unless asked.
- "Take a judgement call" or "use your judgment" means decide, do it, and explain the decision in one or two lines.
- When unsure of visual direction, offer two or three options of the same slide.
- Keep content changes minimal when the user says "do not make major tweaks".
- Remove anything the user flags as busy, repeated or confusing rather than restyling it.
- When the user says "be generous" with a style (accents, highlights), apply it widely; the user prefers removing extras by hand to asking for more.
- Validate the user's own draft content: keep what is right, correct what is not (with a reason and a source), and add what is missing.
- Answer side questions (for example "what is RA standards?") directly before continuing.
- When the user gives feedback on the spine, apply it across the whole deck, not just the slide named (for example, tool-agnostic wording everywhere once asked for one slide).
- When the user edits a slide to show a preference (for example duplicating a slide and resizing its icons), read their edit from the file (sizes, stroke widths, colours), apply it deck-wide and record it in this skill. Example: the user merged one list's bullets into a single text box by hand to show they want lists editable as one block; the kit now does that for every list.
- Do not invent missing case-study facts (outcomes, situations). Write only what the material supports and flag the gaps; the user confirmed this is right.
- When the user asks you to remember a preference, do not edit this shared copy: apply it for the rest of the session and suggest they send it to the skill's owner (Abhishek Sharma) so it can be added for everyone.

---

## 8. Building: the mkit kit

### Assets
Kit folder: the kit ships with this plugin. Its root is the plugin folder two levels above this file (this file sits in `skills/myridius-slide-decks/`; the same folder as `${CLAUDE_PLUGIN_ROOT}` when that is set), with `template/`, `tools/`, `examples/` and `Claude outputs/` in it. The installed copy may be read-only, so copy the whole kit folder to a scratch folder and run the pipeline there; if node cannot find pptxgenjs or sharp, run `npm install pptxgenjs sharp` in the copy's `tools` folder. If the user has connected their own copy of the kit, use that instead. If the kit cannot be used at all, build directly on the template with python-pptx (use the layout of the template's content sample slide, with header text boxes at the template positions) and still follow every rule here.
- `template/Myridius_Template_2026.pptx`: four sample slides in this order: cover, content sample, divider, end slide. The merge tool uses whatever layout the content sample uses, so the user can change the template in PowerPoint as long as that order stays.
- `tools/mkit.py`: HTML kit: palette, `header()` at template positions, icons, `banner()`, `band_items()`, `link()`, `sources_line()`, `metric_list()`, `badge()`, `dot_list()`, `tick_list()`, `legend()`, ring and arc helpers.
- `tools/patterns.py`: brochure patterns (`scatter_hub_card`, `out_card`, `ui_window`, `flow_ribbons`), the building blocks listed in section 6, and `PATTERN_CSS` (include it whenever you use them).
- `tools/html2pptx.py` with `extract.js`, `build.js`, `postproc.py`, `round_pics.py`: HTML deck to editable PPTX.
- `tools/merge_into_template.py`: cover, dividers, end slide, logo and page numbers.
- `tools/group_anim.py`: turns tagged shapes into groups, applies rotation and adds entrance animations.
- `tools/add_slide_link.py`: makes a text box (and its button shape) jump to another slide.
- `tools/native_bullets.py`: turns each list into one text box with native bullets. `html2pptx.py` runs it for every list built with `dot_list()` / `tick_list()`; run it with `--cards N` on an existing or hand-edited slide to merge its dot shapes and per-item text boxes card by card.
- `tools/insert_slides.py`, `tools/lint_text.py`, `tools/render_qa.py`, `tools/icons.py`, `tools/fonts.conf`.
- `examples/example_deck.py` (options, comparison grid, governed path with `band_items`, client stories caselet), `examples/patterns_demo.py` (scatter to hub to card with animation and linked sources, UI window with metric list, flow ribbons) and `examples/style_catalogue.py` (the twelve catalogue styles, built from the building blocks).
- "Claude outputs/Myridius_Visual_Style_Catalogue_v1.pptx": the rendered catalogue, with an index that links to each style.
- Reference decks (kept by the skill's owner and not bundled with this plugin; use them only if the user has them, otherwise use the style catalogue above as the reference): "Myridius_Disney_GRATS Migration_Oct2026.pptx" (proposal) and "Agent Assurance_June2026.pptx" (offering). Render and look at them when starting a new deck type. The signed-off Fiserv deck ("Myridius_Fiserv_FS_Operations_v3_updated.pptx", in the Fiserv project folder) is the reference for client discussion decks, the services anchor and brochure visuals.

### Pipeline
Work from your scratch copy of the kit (it needs Chromium, node and LibreOffice), then:
```
python3 slides.py                                    # your mkit script writes deck.html
python3 tools/html2pptx.py deck.html raw.pptx "Deck title"
python3 tools/merge_into_template.py raw.pptx merged.pptx \
   --kicker "Discussion with <Client>" --title "<Line one>|<Line two>" --date "<Month Year>" \
   --divider "Our point of view@1" --divider "Appendix@9"
python3 tools/group_anim.py merged.pptx Client_Topic_v1.pptx          # groups, rotation, animation
python3 tools/add_slide_link.py Client_Topic_v1.pptx Client_Topic_v1.pptx --on 8 --text "deep dive" --to 13   # optional
python3 tools/lint_text.py Client_Topic_v1.pptx --no-stats
python3 tools/render_qa.py Client_Topic_v1.pptx qa
```
Run `group_anim.py` on every deck (it is harmless when nothing is tagged). `html2pptx.py` already merges each list into one text box with native bullets, inside the right animation group. Commit the final PPTX to the user's project folder.
To fix lists on slides that were built earlier or edited by hand: `python3 tools/native_bullets.py deck.pptx deck_v2.pptx --cards 2,3` (keeps the slide's spacing; check the render).

### Kit rules
- Canvas 1920 x 1080 px; 144 px = 1 in; 1 pt = 2 px, so the 9pt floor is 18 px. Content zone x 59 to 1860, y 190 to 958 (160 when there is no subtitle). Use `header(eyebrow or None, title, sub or None, accent=...)`; never move it.
- The kit is a toolbox, not a set of slide templates: any layout built from positioned HTML and SVG within these rules converts to editable shapes, so new diagrams cost nothing extra.
- Everything absolutely positioned (`.slide > *`). Flex is fine inside a positioned element (use a `.flow` wrapper so children are static).
- SVG layers: `svg(...)`; paths with M, L, Q, C, Z only (use `arc_c` / `seg_path` for arcs). Put a background SVG layer before the HTML it sits under (`o.insert(1, svg(...))`), and an overlay after.
- Curved text with `curved_label` (exports as rotated letters). No CSS gradients, transforms or filters on exported elements; box shadows are fine. For rotation use `data-rot`, not CSS transforms.
- Export features (tags in the HTML):
  - `<a href="...">` becomes a PowerPoint hyperlink (underlined, colour kept); use `link()` and `sources_line()`.
  - `class="strike"` (or `text-decoration: line-through`) becomes strikethrough, for struck-out noise.
  - `data-grp="name"` groups all shapes inside an element; add `data-rot="-2"` to rotate the group.
  - `data-anim="1"`, `"2w"`, `"u"`: entrance step 1, 2 (w = wipe from the left, u = wipe up), default fade; steps play After Previous. Keep each animated block contiguous in paint order.
- Animation wrappers: wrap each step's elements with `anim(step, html)`. Cards and bands inside a wrapper stay positioned (PATTERN_CSS); any other element inside one needs its own absolute position (`text_box`, `node`, `chat_bubble` already have it). A card left static inside a wrapper once jumped to the top-left corner of the slide.
- In a flex row, wrap every text run in its own `<span>`; bare text next to swatches or icons merges into one text box on export (a legend once read "Run by MyridiusYour platforms").
- Arrowheads: `ah` (Moss), `ahl` (Leaf), `ahm` (Mint), `aht` (Teal), `ahs` (Slate). Use HTML text for labels; SVG `<text>` exports as separate letters (only for curved labels).
- Icons: `icon()`, `ico()` (tile), `gicon()` (inside SVG). They export as native SVG pictures with PNG fallback, with the house stroke and size by default (`STROKE_PT`, `ICON_RATIO` in mkit).
- Build every list with `dot_list()` or `tick_list()` (pass `dot=PULSE` and `color='#fff'` on dark panels; bold a phrase with `<b>`, coloured if needed). They tag the list so the export makes one text box with native bullets. Never hand-build bullets from dot spans or one text box per item, and do not use HTML `<ul>`/`<li>` (their markers are lost in the export). Wrap each list in a `text_box()` sized to the column, because the list box takes that width.
- Curved labels: use single spaces (`extract.js` collapses whitespace).
- Screenshots: `<img>` with border-radius; exported as pictures with rounded corners.
- Preview furniture (`.tpl`) shows where the logo and footer will sit and is not exported.
- Inter stands in for Segoe UI when rendering in the cloud; it is wider, so if a line fits in the render it fits in PowerPoint.
- Small edits to an existing PPTX (text, a word in a title, an eyebrow) are better done directly with python-pptx on the user's file than by rebuilding.
- To add, replace or patch slides in a deck the user has edited, build only the new slides with mkit and html2pptx (then `group_anim.py` if they animate), then use `tools/insert_slides.py` (`--after N --take 1,2`, `--replace N:k`, `--region N:k:y0:y1`, `--delete`). It keeps the user's other slides untouched and gives new slides the template layout, logo and page number.

---

## 9. QA checklist (all must pass before delivery)

Story
- [ ] Each slide's title states its message; read only the titles and the story still holds.
- [ ] The hook introduces the organising idea and every later slide reuses its terms; a first-meeting deck zooms in from industry to client to the executive's area.
- [ ] One anchor term from the cover onwards; the client's org name is introduced on one bridge slide; org names verified.
- [ ] Buckets and terms are introduced before they are used and stay consistent; nothing is duplicated.
- [ ] Client decks have a services anchor slide; outcomes are business outcomes; next steps are few, concrete, with "You bring / You get".
- [ ] Every fact is from the user's documents or a cited, current source; nothing invented; non-public points marked "our understanding, to validate with you".
- [ ] Trade-offs are shown honestly, including for our recommendation.

Writing
- [ ] `lint_text.py` reports 0 errors (no em dashes, dot or bullet separators, emojis, exclamation marks); warnings reviewed, including any text below 9pt.
- [ ] Sources on slides are working links, labelled by name without dates, numbered when several.
- [ ] No percentages in client proposals unless the user asked; any statistic has a linked source.
- [ ] No arrogant, absolute or hype phrasing; product names spelled exactly; no unexplained regulatory or industry acronyms; client names in credentials masked unless confirmed.
- [ ] Read every line aloud: no metaphors or cute phrasing in explanations, no habitual "clause; clause" sentences, no stacked lists of three; it sounds like a consultant wrote it.
- [ ] Comparisons are neutral; nothing implies the client is doing it wrong; opportunity slides are illustrative and conditional.

Design
- [ ] Titles on one line in the render, at template positions, with teal accents used generously; eyebrows and subtitles only where they orient or add context.
- [ ] Nothing below 9pt; card body about 10.5pt; key outcomes about 12pt.
- [ ] Only palette colours; Segoe UI only; uniform box colours within a group; one dark emphasis; few pills.
- [ ] Each visual was imagined from the content first, then matched to the repository; no pattern repeated within the deck by habit.
- [ ] The polish qualities hold: real-looking content, one focal element, depth, a clear path for the eye, notes outside the picture, one colour logic, no dead space inside shapes.
- [ ] Icons on list items and tiles, large glyphs with thin strokes; bands read icon, label, message; connectors labelled, in the foreground and visible in the exported render.
- [ ] Every list is one text box with native teal dot bullets (or checks); no separate dot shapes or one-box-per-bullet lists left in the PPTX.
- [ ] Animation only where motion carries meaning; order described in the reply.
- [ ] No overflow, collisions or text touching edges; bottom 0.75 in clear for logo and footer.
- [ ] Opened render of every slide looked at, not just the contact sheet.
- [ ] Output is editable PPTX in the Myridius template, versioned, saved to the user's folder (or `_updated` beside a locked file).