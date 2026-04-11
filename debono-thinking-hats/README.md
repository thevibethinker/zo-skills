---
created: 2026-04-11
last_edited: 2026-04-11
version: 1.0
provenance: debono-thinking-hats/D2.3
---

# 🎩 De Bono's Six Thinking Hats for Zo Computer

**Structured parallel thinking as switchable AI personas.**

## What Is This?

Edward de Bono's Six Thinking Hats (1985) is a framework for **parallel thinking** — instead of arguing where everyone mixes facts, feelings, and opinions simultaneously, everyone "wears the same hat" at the same time, exploring one thinking mode before moving to the next. It separates ego from performance: you're not attacking or defending, you're all looking in the same direction together.

This skill installs the Six Thinking Hats as Zo personas. Each hat is a distinct thinking mode you can switch into. The Blue Hat acts as facilitator, guiding you through structured sequences tailored to your goal — whether that's evaluating a business idea, brainstorming solutions, or running a retrospective. No dependencies, no configuration files, no external services.

## Quick Start

**1. Install the hats:**

```
@Skills/debono-thinking-hats/assets/INSTALL.prompt.md
```

**2. Run the walkthrough once:**

```
@Skills/debono-thinking-hats/assets/WALKTHROUGH.prompt.md
```

Use it again any time as a refresher.

**3. Verify installation:**

```bash
python3 Skills/debono-thinking-hats/scripts/validate_install.py
```

**4. Start your first session:**

Switch to the **Thinking Hat: Blue (Facilitator)** persona and say:

> "I want to evaluate whether we should launch a freemium tier for our product."

The Blue Hat will select a sequence, walk you through each hat, and synthesize the outcome.

You can also activate any hat directly for a focused pass, and any active hat can deliberately invoke another hat briefly when that shift would materially improve the thinking, then return cleanly.

## Visual Identity

This package includes a coordinated avatar set for the six hats under `assets/images/`:

- `assets/images/debono3-blue-hat.png`
- `assets/images/debono3-white-hat.png`
- `assets/images/debono3-red-hat.png`
- `assets/images/debono3-yellow-hat.png`
- `assets/images/debono3-black-hat.png`
- `assets/images/debono3-green-hat.png`

These are designed as a matched family so the personas feel like one system rather than six unrelated characters.

## The Six Hats

| Emoji | Hat | Role | What It Does | Example Prompt |
|-------|-----|------|--------------|----------------|
| 🔵 | Blue | Facilitator | Controls the process — agenda, sequence, transitions, synthesis | "Let's think through this hiring decision." |
| ⚪ | White | Information Analyst | Pure facts and data — no opinions, no spin | "What do we actually know about our churn rate?" |
| 🔴 | Red | Intuition Voice | Gut feelings and emotions — no justification needed | "How do I feel about this partnership?" |
| 🟡 | Yellow | Optimist | Logical positive value — reasons it could work | "What are the benefits of moving to this platform?" |
| ⚫ | Black | Critical Judge | Logical caution — risks, flaws, what could fail | "What could go wrong with this launch timeline?" |
| 🟢 | Green | Creative Provocateur | New ideas, alternatives, lateral thinking provocations | "What if we approached onboarding completely differently?" |

## Thinking Sequences

The Blue Hat selects from 8 pre-built sequences based on your goal. Each sequence orders the hats for optimal thinking flow.

| # | Sequence | Flow | Best For |
|---|----------|------|----------|
| 1 | Initial Exploration | 🔵→⚪→🔴→🟡→⚫→🟢→🔵 | New topics, first look at an idea |
| 2 | Quick Assessment | 🔵→🟡→⚫→🔴→🔵 | Fast go/no-go decisions (10 min) |
| 3 | Cautious Evaluation | 🔵→⚪→🟡→⚫→⚫→🟢→🔴→🔵 | High-risk or irreversible decisions |
| 4 | Creative Ideation | 🔵→🟢→🔴→🟡→⚫→🟢→🔵 | Brainstorming, generating alternatives |
| 5 | Strategic Planning | 🔵→⚪→🟡→⚫→🟢→🟡→⚫→🔵 | Long-term goals and roadmaps |
| 6 | Process Improvement | 🔵→⚪→⚪→🟡→⚫→🟢→🔴→🔵 | Retros, workflow optimization |
| 7 | Problem Solving | 🔵→⚪→🟢→🔴→🟡→⚫→🟢→🔵 | Complex multi-faceted problems |
| 8 | Performance Review | 🔵→🔴→⚪→🟡→⚫→🟢→🔵 | Evaluating past results |

Full sequence details with timing and facilitator instructions: `assets/sequences.md`

## Capability Modes

Beyond the canonical sequences, the package includes a portable capability layer in `assets/mode-catalog.md`.

Examples:
- analytic pass
- Socratic interrogation through a hat lens
- decision comparison
- pre-mortem / post-mortem
- rapid pulse check
- creative provocation cycle

Applied examples live in `assets/use-cases.md`.

## Usage Examples

### Example 1: Evaluating a Business Idea (Full Session)

> **You** (switch to Blue Hat): "I'm considering adding a freemium tier to our SaaS product."

**Blue Hat** opens the session, selects **Sequence 1: Initial Exploration**, and walks you through:

1. **⚪ White Hat** (3 min): "Current pricing is $49/month. We have 12,000 paying users. Competitor X launched free tier in March — their paid conversion rate is unknown. We don't have data on how many prospects bounce at the pricing page."
2. **🔴 Red Hat** (1 min): "Gut feeling: excitement about reaching more users, but anxiety about cannibalizing paid accounts."
3. **🟡 Yellow Hat** (2 min): "A free tier could 10x our top-of-funnel. It creates a testing ground — users prove value to themselves before paying. It also generates usage data we don't currently have."
4. **⚫ Black Hat** (3 min): "Risk of existing customers downgrading. Support costs for free users with no revenue. Feature gating decisions could frustrate both tiers."
5. **🟢 Green Hat** (4 min): "What if the free tier was time-limited rather than feature-limited? Or what if free users could only collaborate with paid users? Alternative: a reverse trial — full features for 30 days, then step down."
6. **🔵 Blue Hat** closes: "Key finding: the freemium model has strong acquisition upside, but the data on paid conversion and support cost is missing. Recommended next step: gather the missing data before committing. Run a time-boxed reverse trial as a lower-risk experiment."

### Example 2: Quick Risk Assessment

> **You** (switch to Blue Hat): "We need to decide by Friday whether to sign this vendor contract."

The Blue Hat selects **Sequence 2: Quick Assessment** (10 minutes):

1. **🟡 Yellow Hat**: Identifies vendor's strengths — proven track record, competitive pricing, API compatibility.
2. **⚫ Black Hat**: Flags 18-month lock-in, unclear SLA penalties, no exit clause for acquisition.
3. **🔴 Red Hat**: "Something about the sales pressure feels off. Urgency might be artificial."
4. **🔵 Blue Hat** synthesis: "The deal has real value, but the lock-in terms are concerning. Recommendation: negotiate an exit clause before Friday. If they refuse, that confirms the Red Hat hunch."

### Example 3: Creative Brainstorming

> **You** (switch to Blue Hat): "We need fresh ideas for our user onboarding flow."

The Blue Hat selects **Sequence 4: Creative Ideation**:

1. **🟢 Green Hat** (first pass): Generates wild ideas — gamified onboarding, AI concierge, "choose your own adventure" paths, skip-everything express mode.
2. **🔴 Red Hat**: Gut check — "The AI concierge excites me. The gamification feels gimmicky."
3. **🟡 Yellow Hat**: Builds the case for the concierge approach — personalization drives engagement, conversational is more natural than forms.
4. **⚫ Black Hat**: Stress tests — concierge adds latency, could feel creepy, needs fallback for when AI misunderstands.
5. **🟢 Green Hat** (second pass): Refines — "What about a hybrid? Quick express path for power users, concierge for everyone else. Concierge remembers preferences so re-onboarding after updates is instant."
6. **🔵 Blue Hat** synthesis: "Winner: hybrid onboarding with AI concierge for new users and express path for experienced ones. Build a prototype of the concierge flow first."

## Customization

### Modifying Hat Prompts

Each hat is a standard Zo persona. Edit any hat at [Settings > AI > Personas](/?t=settings&s=ai&d=personas). Common modifications:

- **Add domain context**: "When applied to engineering decisions, also consider technical debt."
- **Adjust timing**: Change recommended durations in the Blue Hat's prompt.
- **Tone**: Make hats more formal or casual for your style.

### Black Hat → Grey Hat

The "Black Hat" label can carry unintended cultural connotations. The installer offers a **Grey Hat** alternative during setup. If you want to rename after installation, edit the persona name and update references in other hat prompts.

The functional behavior is identical — only the label changes.

## How It Works

The skill uses Zo's persona system:

1. **Six personas** are created, one per hat. Each contains behavioral rules, anti-patterns, example outputs, richer technique modes, and cross-references to the other five hats.
2. **Persona switching** happens via `set_active_persona()` — the same mechanism as any Zo persona.
3. **The Blue Hat** is the canonical facilitator for structured sessions, but direct hat use is also supported.
4. **Temporary inter-hat invocation** lets any active hat deliberately call another hat-mode for a bounded pass and then return.
5. **Two-pass installation** — Personas are created first, then updated with each other's IDs for cross-referencing.

No external dependencies. No scheduled tasks. No API keys. Just personas, prompts, and optional reference assets.

## Uninstallation

1. Delete the six "Thinking Hat: ..." personas from [Settings > AI > Personas](/?t=settings&s=ai&d=personas)
2. Delete the routing rule labeled "Six Thinking Hats" from [Settings > AI > Rules](/?t=settings&s=ai&d=rules) (if one was created)
3. Optionally delete the skill folder: `Skills/debono-thinking-hats/`

## Credits

Based on **"Six Thinking Hats"** by Edward de Bono (1985). The Six Thinking Hats methodology is a framework developed by Edward de Bono. "Six Thinking Hats" is a trademark of the de Bono Group. This skill is an independent implementation and is not affiliated with or endorsed by the de Bono Group.

## License

Same license as the containing repository.
