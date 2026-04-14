---
created: 2026-03-20
last_edited: 2026-03-20
version: "2.0"
provenance: portfolio-generator
source: Adapted from Skills/frontend-design and Skills/landing-page-generator, refined via audit
---

# Portfolio Design Guidelines v2

Rules for generating portfolio pages that look professionally designed — not AI-generated.

## The AI Slop Test

Before deploying, ask: "If I told someone AI made this, would they believe me immediately?" If yes, it fails.

**AI tells to eliminate:**
- Default Tailwind color palette (zinc-50, blue-600, etc.)
- Centered-everything layouts
- Rounded pill skill badges
- Circle avatar placeholders with initials
- Card-wrapped experience entries
- Identical section padding throughout
- Generic "Let's Connect" CTAs with buttons
- Inter, Roboto, system sans-serif only

## Architecture: Label-Content Grid

Every content section uses the same skeleton:

```
┌──────────────────────────────────────────────┐
│ SECTION LABEL (4 cols)  │  Content (8 cols)  │
│ text-xs uppercase       │  Body text, lists   │
│ tracking-widest         │  or data entries    │
│ muted color             │                     │
└──────────────────────────────────────────────┘
```

This creates a consistent left-rail navigation pattern. Section labels act as wayfinding, not decoration.

## Typography

### Font Strategy
Load from Google Fonts with `font-display: swap`. Always pair:
- **Heading font**: Geometric sans (Instrument Sans, Plus Jakarta Sans, Outfit, Onest)
- **Accent font**: Editorial serif for taglines/quotes (Newsreader, Source Serif 4)

### Banned Fonts
Inter, Roboto, Open Sans, Arial, Lato, Montserrat — these are invisible defaults that scream template.

### Scale
| Element | Size | Weight | Extra |
|---------|------|--------|-------|
| Hero name | clamp(2.8rem, 6vw + 1rem, 5.5rem) | bold | letter-spacing: -0.035em, line-height: 0.95 |
| Hero label | text-sm | medium | uppercase, tracking-widest |
| Tagline | text-lg md:text-xl | 400 | serif italic, max-w-xl |
| Section label | text-xs | semibold | uppercase, tracking: 0.2em |
| Section body | text-base md:text-lg | 400 | leading-relaxed |
| Experience title | text-xl md:text-2xl | semibold | tracking: -0.02em |
| CTA | text-3xl md:text-5xl | bold | tracking: -0.03em |
| Nav / footer | text-sm / text-xs | medium / 400 | — |

## Color

### Custom Palettes Only
NEVER use raw Tailwind color classes (bg-zinc-50, text-blue-600). Always use `style={{ color: "#hex" }}` or `style={{ backgroundColor: "#hex" }}`.

### Neutral Tinting
All neutrals must be tinted toward the page's warmth/coolness. Pure gray (#888) is dead — use warm (#8a8780) or cool (#888890) tints.

### Contrast Section
Every portfolio MUST have one section with an inverted background (dark section on light pages, light section on dark pages). This is the domains/skills section. It breaks visual monotony.

### Required Color Roles
| Role | Purpose | Example (editorial) |
|------|---------|---------------------|
| page | Main background | #FAF9F7 |
| surface | Section variant bg | #F3F2EF |
| dark_section_bg | Contrast section | #1a1a18 |
| text_primary | Headlines, name | #1a1a18 |
| text_secondary | Body text | #52514d |
| text_muted | Labels, metadata | #8a8780 |
| text_faint | Footer, deemphasis | #b0afa9 |
| border | Dividers | #e5e4e0 |

## Layout

### Hero
- Left-aligned, NEVER centered
- No avatar/photo placeholder — just typography
- Label above name (role + company)
- Tagline below name in serif italic
- No button — the LinkedIn link is in the nav

### Spacing Rhythm
Vary section padding intentionally:
- Hero: `pt-16 md:pt-28 pb-20 md:pb-36` (most generous)
- Content sections: `py-16 md:py-24` (standard)
- CTA: `pt-12 pb-20 md:pb-32` (asymmetric)
- Nav/footer: `py-6` (tight)

### Responsive
- Grid collapses from 12-col to single column on mobile
- Hero name scales via clamp() — no breakpoint jumps
- Horizontal padding: `px-6 md:px-12 lg:px-20`

## Motion

### FadeIn Component
Wrap every visible element in a FadeIn component:
- Initial: `opacity: 0, translateY: 12px`
- Final: `opacity: 1, translateY: 0`
- Duration: `0.6s`
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` — expo out
- Stagger: 60-120ms between siblings

### Rules
- One orchestrated page load animation, nothing else
- No scroll-triggered animations
- No bounce or elastic easing
- CTA arrow animates on hover (gap widens + slight translate)

## Components

### Experience Entry
```
┌──────────────────────────────────┐
│ Role at Company        2021 –    │  ← flex, items-baseline, justify-between
│                                  │
│ Description text here.           │  ← text-base, text-secondary
│──────────────────────────────────│  ← border-t divider (not on first)
│ Next Role at Company   2017–21   │
└──────────────────────────────────┘
```
NO cards. NO timeline dots. NO left border. Just clean dividers.

### Domains/Skills
Plain text, larger size, comma-separated or flex-wrap with gap. In the dark contrast section.
NO pills. NO badges. NO categories with subgroups. Just the words.

### CTA
Large text link with ArrowUpRight icon. Arrow animates on hover (gap widens, arrow shifts up-right).
NO button. NO centered layout. NO "Interested in X? Let's connect!" copy.

### Footer
Two items, flex justify-between: copyright and "Built with Zo". text-xs, nearly invisible.

## Icons

Use only `ArrowUpRight` from lucide-react. One icon type maximum. Icons are functional (outbound link indicator), not decorative.

## What Makes This Work

The design looks professional because:
1. **Asymmetry** — left-aligned hero, label-content grid, nothing centered
2. **Typography does the heavy lifting** — big name, serif tagline, strict hierarchy
3. **Color restraint** — warm neutrals, no accent color needed (except in technical direction)
4. **Whitespace as design** — generous spacing signals confidence
5. **One dark section** — breaks monotony without being gimmicky
6. **Motion adds polish** — staggered entrance makes the page feel alive
7. **No decoration** — no icons, badges, cards, circles, gradients — just text and space
