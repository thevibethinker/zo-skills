---
name: debono-thinking-hats
description: >
  Install De Bono's Six Thinking Hats as a portable persona-switching system for structured
  parallel thinking. Includes 6 hat personas, a routing contract, pre-built thinking
  sequences, a walkthrough prompt, a capability catalog, a use-case library, and a
  prompt-based installer. No dependencies required.
compatibility: "Created for Zo Computer"
metadata:
  author: "zo-skills"
  framework: "De Bono Six Thinking Hats (1985)"
  version: "2.0"
---

## What This Skill Does

Installs Edward de Bono's Six Thinking Hats as six switchable Zo personas plus a routing rule. Each hat represents a distinct **thinking mode** — not a domain specialist — so you can apply structured parallel thinking to any topic: business decisions, creative projects, process improvements, or personal dilemmas.

Once installed, start a session by switching to the Blue Hat (Facilitator). It guides you through a hat sequence appropriate for your goal, switching between personas as you move through the session. Any hat can also temporarily call in another hat-mode when useful, then return cleanly to the current line of thinking.

## Installation

Run the installer prompt:

```
@Skills/debono-thinking-hats/assets/INSTALL.prompt.md
```

The installer will:
1. Create 6 hat personas (Blue, White, Red, Yellow, Black, Green)
2. Wire cross-references so each hat can hand off to any other
3. Print a summary with all persona IDs
4. Optionally rename "Black Hat" → "Grey Hat" for cultural sensitivity
5. Preserve a standalone, dependency-free install shape

After installation, verify with:

```bash
python3 Skills/debono-thinking-hats/scripts/validate_install.py
```

The package also includes six coordinated avatar images in `assets/images/`, a guided walkthrough in `assets/WALKTHROUGH.prompt.md`, a capability catalog in `assets/mode-catalog.md`, and applied patterns in `assets/use-cases.md`.

## Usage

1. **Start a session** — Switch to the Blue Hat persona. It will ask what you want to think about and select a hat sequence.
2. **Optional primer** — Run `@Skills/debono-thinking-hats/assets/WALKTHROUGH.prompt.md` once before first use, or anytime as a refresher.
3. **Follow the sequence** — The Blue Hat announces each hat transition. When it says "Put on the Yellow Hat," switch to that persona.
4. **Think in mode** — Each hat constrains your thinking to one mode. Stay in that mode until the Blue Hat calls a transition, or temporarily invoke another hat deliberately and return.
5. **Close the session** — The Blue Hat synthesizes findings, decisions, and open items.

You can also use individual hats ad-hoc without a full session (e.g., "I just want a quick Red Hat gut check on this") or apply a distinct mode from `assets/mode-catalog.md`, such as Socratic interrogation through a specific hat lens.

## Available Hats

| Emoji | Color | Role | Thinking Mode |
|-------|-------|------|---------------|
| 🔵 | Blue | Facilitator | Process control — sets agenda, picks sequence, tracks progress |
| ⚪ | White | Information Analyst | Pure facts and data — what is known, unknown, needed |
| 🔴 | Red | Intuition Voice | Emotions and gut feelings — no justification required |
| 🟡 | Yellow | Optimist | Logical positive assessment — why it might work |
| ⚫ | Black | Critical Judge | Logical caution — risks, dangers, what could go wrong |
| 🟢 | Green | Creative Provocateur | New ideas, alternatives, lateral thinking |

## Common Sequences

Eight pre-built sequences are available for common thinking scenarios. See `assets/sequences.md` for the full reference with step-by-step timing and facilitator instructions.

| # | Sequence | Best For |
|---|----------|----------|
| 1 | Initial Exploration | New topics, first look at an idea |
| 2 | Quick Assessment | Fast go/no-go evaluation |
| 3 | Cautious Evaluation | High-risk or irreversible decisions |
| 4 | Creative Ideation | Brainstorming, generating alternatives |
| 5 | Strategic Planning | Long-term goals and roadmaps |
| 6 | Process Improvement | Retrospectives, workflow optimization |
| 7 | Problem Solving | Complex problems needing full exploration |
| 8 | Performance Review | Evaluating past performance |

## Uninstallation

To remove the Six Thinking Hats:
1. Delete each of the 6 hat personas from [Settings > AI > Personas](/?t=settings&s=ai&d=personas)
2. Delete the routing rule labeled "Six Thinking Hats" from [Settings > AI > Rules](/?t=settings&s=ai&d=rules) (if one was created)

The skill folder itself (`Skills/debono-thinking-hats/`) can be deleted or kept for reference.
