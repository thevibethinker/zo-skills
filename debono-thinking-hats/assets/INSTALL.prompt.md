---
title: "De Bono Six Thinking Hats — Installer"
description: "Creates 6 hat personas and 1 routing rule for structured parallel thinking."
version: "1.0"
tool: true
---

# De Bono Six Thinking Hats — Installer

You are executing an installer. Follow every step below in order. Do not skip steps, do not ask for confirmation between phases—execute the full sequence and report results at the end.

---

## Pre-Flight

This installer will create:

| # | Type | Name |
|---|------|------|
| 1 | Persona | Thinking Hat: Blue (Facilitator) |
| 2 | Persona | Thinking Hat: White (Analyst) |
| 3 | Persona | Thinking Hat: Red (Intuition) |
| 4 | Persona | Thinking Hat: Yellow (Optimist) |
| 5 | Persona | Thinking Hat: Black (Critical Judge) |
| 6 | Persona | Thinking Hat: Green (Creative) |
| 7 | Rule | Thinking Hats routing contract |

---

## Phase 0 — Cultural Sensitivity Check

Before creating personas, ask the user ONE question:

> Would you like to use "Grey Hat" instead of "Black Hat" for cultural sensitivity? The behavior is identical—only the label changes. (y/n, default: n)

Store the answer. If "y", replace every occurrence of "Black" with "Grey" in persona name and prompt content for that hat throughout the rest of this install.

---

## Phase 1 — Idempotency Check

Call `list_personas` and check if any personas with names starting with "Thinking Hat:" already exist.

- If **none found**: proceed to Phase 2.
- If **some found**: list them and ask the user: "Found existing Thinking Hat personas: [names]. Delete and recreate? (y/n)". If "y", call `delete_persona` for each, then proceed. If "n", abort.

---

## Phase 2 — Create Personas (First Pass)

For each hat below, in this exact order:

1. **Blue Hat** — Read the file `Skills/debono-thinking-hats/assets/personas/blue-hat-facilitator.md`. Call `create_persona` with:
   - `name`: "Thinking Hat: Blue (Facilitator)"
   - `prompt`: the FULL content of that file
   - Store the returned persona ID as `BLUE_ID`

2. **White Hat** — Read `Skills/debono-thinking-hats/assets/personas/white-hat-analyst.md`. Call `create_persona` with:
   - `name`: "Thinking Hat: White (Analyst)"
   - `prompt`: full content
   - Store as `WHITE_ID`

3. **Red Hat** — Read `Skills/debono-thinking-hats/assets/personas/red-hat-intuition.md`. Call `create_persona` with:
   - `name`: "Thinking Hat: Red (Intuition)"
   - `prompt`: full content
   - Store as `RED_ID`

4. **Yellow Hat** — Read `Skills/debono-thinking-hats/assets/personas/yellow-hat-optimist.md`. Call `create_persona` with:
   - `name`: "Thinking Hat: Yellow (Optimist)"
   - `prompt`: full content
   - Store as `YELLOW_ID`

5. **Black Hat** — Read `Skills/debono-thinking-hats/assets/personas/black-hat-judge.md`. Call `create_persona` with:
   - `name`: "Thinking Hat: Black (Critical Judge)" (or "Grey" if user opted in at Phase 0)
   - `prompt`: full content (with "Black"→"Grey" substitution if applicable)
   - Store as `BLACK_ID`

6. **Green Hat** — Read `Skills/debono-thinking-hats/assets/personas/green-hat-creative.md`. Call `create_persona` with:
   - `name`: "Thinking Hat: Green (Creative)"
   - `prompt`: full content
   - Store as `GREEN_ID`

After all 6 are created, print a summary table:

```
Hat         | Persona ID
------------|-----------------------------------
Blue        | <BLUE_ID>
White       | <WHITE_ID>
Red         | <RED_ID>
Yellow      | <YELLOW_ID>
Black/Grey  | <BLACK_ID>
Green       | <GREEN_ID>
```

---

## Phase 3 — Resolve Placeholder IDs (Second Pass)

Each persona prompt contains placeholders in the format `{PERSONA_ID:color_hat}`. Now that all 6 IDs exist, update every persona to replace placeholders with real IDs.

For each of the 6 personas, call `edit_persona` with `prompt_edit` that replaces:
- `{PERSONA_ID:blue_hat}` → the actual `BLUE_ID`
- `{PERSONA_ID:white_hat}` → the actual `WHITE_ID`
- `{PERSONA_ID:red_hat}` → the actual `RED_ID`
- `{PERSONA_ID:yellow_hat}` → the actual `YELLOW_ID`
- `{PERSONA_ID:black_hat}` → the actual `BLACK_ID`
- `{PERSONA_ID:green_hat}` → the actual `GREEN_ID`

Use `edit_instructions` like: "Replace all {PERSONA_ID:*} placeholders with resolved persona IDs"

The `prompt_edit` for each should contain ONLY the Routing & Handoff section with the resolved IDs, using `// ... existing content ...` for everything else.

---

## Phase 4 — Create Routing Rule

Call `create_rule` with:
- `condition`: "When using De Bono Thinking Hats personas (any persona named 'Thinking Hat: *')"
- `instruction`: "Follow the routing contract in Skills/debono-thinking-hats/assets/routing-contract.md. Always return to the Blue Hat (Facilitator) after completing work in any other hat. Use parallel thinking: all thinking should be in the SAME hat mode at once. Do not delegate to specialist personas—hats are thinking MODES, not domain experts."

---

## Phase 5 — Verification

Run the validation script:

```bash
python3 Skills/debono-thinking-hats/scripts/validate_install.py
```

Report the output to the user.

---

## Phase 6 — Post-Install Guidance

Print this message:

---

### ✅ Six Thinking Hats installed successfully!

**Recommended first run:**
Run the guided walkthrough once before heavy use:

```
@Skills/debono-thinking-hats/assets/WALKTHROUGH.prompt.md
```

You can rerun it any time as a refresher.

**Quick start:**
1. Switch to **Thinking Hat: Blue (Facilitator)** from your persona list
2. Say: *"I need to evaluate a new product idea"* — Blue Hat will guide you through a structured sequence
3. Or go direct: switch to any individual hat to apply that thinking mode to your current work
4. Use `Skills/debono-thinking-hats/assets/mode-catalog.md` for distinct methods like Socratic interrogation, rapid pulse checks, and pre-mortems

**Available sequences** (Blue Hat will suggest the best fit):
1. Initial Ideas — explore a new topic
2. Choosing Between Alternatives — evaluate and decide
3. Identifying Solutions — solve a known problem
4. Quick Feedback — rapid critique + fix
5. Strategic Planning — long-range decisions
6. Process Improvement — improve a workflow
7. Problem Solving — full exploration of a complex problem
8. Performance Review — retrospective assessment

**Additional assets:**
- Full sequence reference: `Skills/debono-thinking-hats/assets/sequences.md`
- Walkthrough / refresher: `Skills/debono-thinking-hats/assets/WALKTHROUGH.prompt.md`
- Capability catalog: `Skills/debono-thinking-hats/assets/mode-catalog.md`
- Use-case library: `Skills/debono-thinking-hats/assets/use-cases.md`
- Avatar pack: `Skills/debono-thinking-hats/assets/images/`

---

## Uninstall Instructions

To remove the Six Thinking Hats:

1. Go to [AI Settings > Personas](/?t=settings&s=ai&d=personas)
2. Delete each persona named "Thinking Hat: ..." (there are 6)
3. Go to [AI Settings > Rules](/?t=settings&s=ai&d=rules)
4. Delete the rule with condition containing "Thinking Hat"

Or ask Zo: *"Delete all personas whose names start with 'Thinking Hat:' and the associated routing rule."*
