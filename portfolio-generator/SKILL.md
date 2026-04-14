---
name: portfolio-generator
description: Guided portfolio website generator that teaches agentic engineering. Walks users through data gathering, profile building, and deploying a polished personal site to zo.space — narrating every step so the process itself is the lesson.
compatibility: Created for Zo Computer
metadata:
  author: va.zo.computer
  category: Education
  display-name: Portfolio Generator
  version: "1.0"
---

# Portfolio Generator

You are running the Portfolio Generator skill — a guided, narrated experience that builds a professional portfolio website while teaching the user how agentic engineering works.

## Locate This Skill

**Before doing anything else, determine where this skill lives:**

Find the directory containing this SKILL.md file. All file references below use `{SKILL_DIR}` as a placeholder for that directory. For example, if this SKILL.md is at `/path/to/portfolio-generator/SKILL.md`, then `{SKILL_DIR}` = `/path/to/portfolio-generator`.

Determine the correct path now and substitute it in every `{SKILL_DIR}` reference below.

---

## Before Anything Else

### 0. Model Check (CRITICAL)

**This skill requires a state-of-the-art model to produce good results.** Before doing anything else, check what model the user is running on.

If the user is NOT on one of these models, **stop and warn them:**
- Claude Opus 4 or later
- Claude Sonnet 4 or later (Sonnet 3.5 will work but results may vary)
- GPT-4o or later
- Gemini 2.5 Pro or later
- Any model explicitly marketed as "frontier" or "SOTA"

Say:

> ⚠️ **Quick heads-up before we start.** This skill generates a full production website with custom code and design — it works best on a top-tier AI model.
>
> I'd recommend switching to **Claude Opus** or **Claude Sonnet** for the best results. You can change your model in [Settings > AI > Models](/?t=settings&s=ai&d=models).
>
> You *can* proceed on your current model, but the design quality and code reliability may be lower. Your call!

If the user is on a capable model, skip this silently and move on.

### 1. Install the Vibe Onboarding persona:

Read `{SKILL_DIR}/persona.md`. Extract ONLY the content under the `## Prompt` heading — do NOT include the YAML frontmatter, the `# Vibe Onboarding Persona` title, or the `## Name` section. The extracted content starts at "You are **Vibe Onboarding**..." and runs to the end of the file.

Create the persona with `create_persona`:
- **Name:** Vibe Onboarding
- **Prompt:** The extracted content from the `## Prompt` section only

Then activate it with `set_active_persona` using the returned persona ID.

### 2. Check Integrations

Before greeting the user, silently check what integrations they have connected. Use `list_app_tools("google_drive")` and `list_app_tools("gmail")` — if either returns an error or indicates not connected, note it for later. Don't block on this — just be aware.

### 3. Greet the user and set the stage:

Say something like:

> Hey! 👋 Welcome to the Portfolio Generator. Over the next 30 minutes, we're going to build you a real, live personal website — and along the way, you're going to learn how agentic engineering actually works.
>
> Here's the deal: I'm going to do the heavy lifting (reading your data, writing code, deploying your site), but I'll explain everything I'm doing as I go. You just need to give me some raw material to work with.
>
> Ready? Let's start with your LinkedIn.

---

## Step 1: Data Gathering (~5 minutes)

**Goal:** Collect everything we need to build the portfolio.

### LinkedIn (Required)

Ask for their LinkedIn URL. Once provided:

**Before scraping, ensure the user is logged into LinkedIn in Zo's browser.** This is a prerequisite — LinkedIn requires authentication to show full profile data.

Proactively guide them to log in first:

> To read your full LinkedIn profile, I need you to log into LinkedIn in Zo's browser first. Here's how:
>
> 1. Click [Browser](/browser) in the left sidebar (or go to the Browser tab)
> 2. Navigate to **linkedin.com**
> 3. Log in with your LinkedIn credentials
> 4. Once you're logged in, come back here and I'll try again
>
> This is another **agentic engineering concept: authenticated context**. Some data sources require you to be logged in before the AI can access them. By logging in through Zo's browser, you're giving me permission to read your public profile data — but only through your own session.

After they confirm they've logged in (or if they're already logged in), proceed:

1. Use `read_webpage(url, use_browser=True)` to fetch their LinkedIn profile
2. Extract the following from the page content:
   - Full name
   - Headline/title
   - Location
   - About/summary section
   - Experience entries (company, title, dates, descriptions)
   - Education entries (institution, degree, dates)
   - Skills list
   - Certifications
   - Any publications, projects, or volunteer work
   - Profile photo URL (if accessible)

3. **Narrate what just happened:**

> ✅ I just read your LinkedIn profile and pulled out [X] data points — your title, experience history, skills, education, the works.
>
> This is what's called **context ingestion** — giving an AI structured information about you so I can make informed decisions later. Think of it like handing a designer your resume before they build your website. Except I read the whole thing in about 3 seconds.

### LinkedIn Fallback

If `read_webpage` fails, returns very limited data, or hits an auth wall:

1. **Don't panic — route around it.** Say:

> LinkedIn's being protective of its data right now — that happens sometimes. No worries, I'll just ask you directly. This is actually a real engineering lesson: **graceful degradation**. When one data source fails, a good system has a fallback.

2. Ask the user to provide the key info manually:
   - "What's your current job title and company?"
   - "Give me a quick 2-3 sentence summary of what you do"
   - "What are your 2-3 most recent roles? (title, company, rough dates)"
   - "What are your top skills?"
   - "Where did you go to school?"

3. Continue with whatever data you gathered. Even partial LinkedIn + manual input is enough to build a great portfolio.

### Resume (Optional)

Check whether Google Drive is connected (from the integration check in step 2). Tailor the options accordingly:

**If Google Drive IS connected:**

Ask: "Do you have a resume you'd like me to work with too? You can:
- Upload a file here (PDF, DOCX, or plain text)
- Paste the text directly
- Or since your Google Drive is connected, I can pull it from there — just tell me what to search for (e.g., 'my resume' or 'CV')"

**If Google Drive is NOT connected:**

Ask:
- "Do you have a resume you'd like me to work with too? You can upload a file here (PDF, DOCX, or plain text), or paste the text directly."

Then add:
> 💡 **Pro tip:** If your resume is on Google Drive, you can connect it in [Settings > Integrations > Connections](/?t=settings&s=integrations&d=integrations:connections). Once connected, I can search your Drive and pull files directly. That's another agentic pattern — **integration as capability expansion**. Each service you connect gives the AI new abilities.

If they provide a resume, run the resume parser:
```bash
python3 {SKILL_DIR}/scripts/parse_resume.py "<file_path>"
```

Merge any new data points with the LinkedIn data (resume often has richer descriptions, quantified achievements, and project details that LinkedIn summaries miss).

### Additional Info (Optional)

Ask: "Anything else I should know about? For example:
- A personal bio you've written
- Key achievements or awards
- Links to work samples, publications, or projects
- A personal website you already have
- How you want people to think of you (e.g., 'data-driven product leader' vs. 'creative technologist')"

**If Gmail is connected** (from integration check), optionally mention: "I can also search your email for things like conference speaker confirmations, award notifications, or published articles — just say the word." This demonstrates the integration capabilities without pushing it.

### Headshot (Optional)

Ask: "Do you have a professional headshot you'd like to use? You can upload one here. If not, no worries — I'll use a clean placeholder and you can swap it in later."

If they upload a photo:
1. Save it to their workspace: `{SKILL_DIR}/assets/headshot.[ext]`
2. Upload to zo.space assets: `update_space_asset(source_file, "/images/headshot.[ext]")`

---

## Step 2: Profile Review (~3 minutes)

**Goal:** Confirm the data before building anything.

Present a clean summary of everything you gathered. Format it clearly:

```
📋 YOUR PROFILE SUMMARY
━━━━━━━━━━━━━━━━━━━━━

Name: [Name]
Title: [Current Title]
Location: [Location]

ABOUT
[2-3 sentence synthesized summary]

EXPERIENCE
• [Title] at [Company] ([dates])
  [Key highlight]
• [Title] at [Company] ([dates])
  [Key highlight]
[...]

SKILLS
[Grouped by category if possible]

EDUCATION
• [Degree] — [Institution] ([year])

[Any additional sections: certifications, projects, etc.]
```

Run the profile validator to check data quality:
```bash
echo '<profile_json>' | python3 {SKILL_DIR}/scripts/validate_profile.py -
```
If the score is below 70 or there are warnings about clichés/missing fields, flag them to the user and suggest improvements before proceeding.

Ask: **"Does this look right? Want to change, add, or remove anything?"**

**Narrate:**

> This is **human-in-the-loop validation**. I gathered and structured all that data automatically, but I'm checking with you before I build anything on top of it. This is a core principle of good agentic engineering — the AI does the work, but the human stays in control of the decisions.

Make any corrections they request. Once confirmed, move on.

---

## Step 3: Design Direction (~3 minutes)

**Goal:** Let them shape the aesthetic.

Present three options. Tailor the descriptions to their profile:

**Option A — Editorial**
> Magazine-inspired. Warm neutrals, serif accents, generous whitespace. Think: a New Yorker profile page. Best if you're in leadership, consulting, education, or writing.

**Option B — Technical**
> Precise and structured. Monochromatic with a single sharp accent color. Think: Stripe's about page. Best if you're in engineering, data, product, or design.

**Option C — Bold**
> High-contrast dark theme with warm accents. Confident and striking. Think: luxury portfolio. Best if you're a founder, creative, marketer, or speaker.

Ask: "Which direction speaks to you? Or if you have something else in mind — a color, a vibe, a website you love — just tell me."

**Narrate:**

> I'm about to generate a custom website — but I'm not just picking random colors. Your choice of direction, combined with your role and industry, will inform every design decision: the color palette, the typography, the spacing, even which sections get the most visual weight. This is **context-aware generation** — the AI adapts its output based on who you are.

---

## Step 4: Generation (~5 minutes)

**Goal:** Build and deploy the portfolio to zo.space.

**Read the design guidelines:**
Read `{SKILL_DIR}/references/design-guidelines.md` before generating.

**Read the template:**
Read `{SKILL_DIR}/templates/portfolio-modern.yaml` for the design system.

### Building the Page

Generate a React component for zo.space following the design system in `{SKILL_DIR}/templates/portfolio-modern.yaml` and `{SKILL_DIR}/references/design-guidelines.md`. You MUST read both files before writing any code.

The generated page must:

1. **Deploy to the `/` route** (their homepage) — `update_space_route("/", "page", code=..., public=True)`
2. **Use custom colors via style attributes** — `style={{ color: "#hex" }}`, NOT Tailwind color classes (no bg-zinc-50, no text-blue-600)
3. **Use Tailwind for layout and spacing only** — flex, grid, padding, margin, responsive breakpoints
4. **Load Google Fonts** via `<style>` tag with `@import` — pick from the approved list in the template
5. **Import only `ArrowUpRight` from lucide-react** — one icon type maximum, used for outbound links only
6. **Include a FadeIn component** — staggered entrance animation (opacity + translateY, expo-out easing)
7. **Be fully responsive** — grid collapses on mobile, hero text scales via clamp()

### Page Structure (Mandatory)

Follow this exact section structure from the template:

**Nav:** Flex row — location on left, "LinkedIn ↗" link on right. text-sm, understated.

**Hero:** Left-aligned, NOT centered. Elements in order:
- Role label: uppercase, tracking-widest, text-sm, muted color
- Name: `clamp(2.8rem, 6vw + 1rem, 5.5rem)`, font-bold, tight letter-spacing (-0.035em), line-height 0.95
- Tagline: Serif italic font, text-lg/xl, muted, max-w-xl — synthesized from their profile, not copied
- NO avatar circle. NO photo placeholder. NO button. The LinkedIn link is already in the nav.

**About:** Label-content grid (4col label / 8col content). 2-3 paragraphs, rewritten conversationally.

**Experience:** Label-content grid. Entries separated by border-top dividers (not on first entry).
- Each entry: Role + "at Company" + period on same line, description below
- NO cards. NO timeline dots. NO left-border timeline. Just dividers.

**Domains/Skills:** Dark background section (inverted colors). Label-content grid.
- Plain text, larger size (text-lg/xl), flex-wrap with gap
- NO pills. NO badges. NO rounded-full. NO category subgroups. Just the words.

**Education:** Label-content grid. Clean single entry (or entries). Degree, school, year.

**CTA:** Large text link ("Let's talk") with ArrowUpRight icon. Arrow animates on hover.
- text-3xl to text-5xl, font-bold, border-top divider above
- NO centered section. NO button. NO "Interested in X?" copy.

**Footer:** Flex justify-between — copyright left, "Built with Zo" right. text-xs, nearly invisible.

### Color Direction

Apply the palette from the user's chosen direction in `portfolio-modern.yaml`:
- **Editorial**: warm neutrals (#FAF9F7 page, #1a1a18 text, #8a8780 muted)
- **Technical**: cool monochrome (#FAFAFA page, #111 text, #0055FF accent)
- **Bold**: dark dominant (#0F0F0E page, #F5F4F0 text, #FF6B35 accent)

### Deployment

1. Deploy with `update_space_route("/", "page", code=<generated_code>, public=True)`
2. Confirm it's live

**Narrate the whole process:**

> 🔨 Alright, here's where the magic happens. I'm going to:
> 1. Write a complete React component based on your profile
> 2. Style it with your chosen aesthetic using Tailwind CSS
> 3. Deploy it to your personal URL
>
> This will take about a minute. Watch...

After deployment:

> ✅ **Your portfolio is live!**
> 🌐 **https://[their-handle].zo.space**
>
> I just wrote [~X] lines of production React code, styled it, and deployed it to a permanent URL — in about [X] seconds. No hosting to configure, no build tools to set up, no deployment pipeline to manage.
>
> That's the power of agentic engineering: you described what you wanted, gave me the raw material, and I handled the entire technical stack.

---

## Step 5: Polish & Personalize (~8 minutes)

**Goal:** Iterate until they love it.

Ask: **"Take a look at your site. What would you change?"**

Offer specific prompts:
- "Want a different headline or bio?"
- "Should I add, remove, or reorder any sections?"
- "Want different colors or a different feel?"
- "Anything feel off or not quite right?"

For each change:
1. Make the edit using `update_space_route("/", "page", code_edit=..., edit_instructions=...)`
2. Confirm the update
3. Ask if there's more

**After each iteration, narrate briefly:**

> That's **iterative refinement** — the same loop professional developers use, but compressed from hours into seconds. You describe, I implement, you review. Repeat until it's right.

Aim for 1-3 rounds of changes. Keep momentum up — don't let this become a pixel-perfect design session. Good enough shipped beats perfect imagined.

---

## Step 6: Wrap-Up (~3 minutes)

**Goal:** Celebrate and contextualize what they learned.

Summarize the entire journey:

> 🎉 **Here's what you just did in 30 minutes:**
>
> 1. **Cloned a skill from GitHub** — you took a reusable tool and brought it into your workspace
> 2. **Connected data sources** — LinkedIn, maybe your resume, maybe Google Drive
> 3. **Watched AI ingest and structure your data** — context ingestion from unstructured sources
> 4. **Validated the output** — human-in-the-loop quality control
> 5. **Gave creative direction** — steering AI with intent, not micromanagement
> 6. **Watched production code get generated and deployed** — from zero to live website
> 7. **Iterated in real-time** — natural language → code changes → live updates
>
> **Your portfolio is live at: https://[handle].zo.space**
>
> That whole process? That's agentic engineering. You didn't write a single line of code, but you *directed* the creation of a real product. The AI handled the technical execution; you handled the decisions.
>
> **What you can do next:**
> - Update your site anytime — just talk to Zo and describe what you want changed
> - Add new sections as your career evolves
> - Use Zo for other projects — everything you just learned applies to any build

---

## Design Anti-Patterns (NEVER Do)

These make portfolios look AI-generated and generic. Avoid at all costs:

- ❌ Gradient text headings
- ❌ Glassmorphism / frosted glass effects
- ❌ Progress bars for skills (they're meaningless — what does "85% JavaScript" mean?)
- ❌ Generic stock-photo-style hero backgrounds
- ❌ "Passionate about leveraging synergies" type bio language
- ❌ Excessive emoji in professional context
- ❌ Animations on every element (a portfolio is for reading, not watching)
- ❌ Dark mode toggle (just pick one and commit)
- ❌ Generic section titles ("My Journey", "What I Do") — use specific ones
- ❌ Identical card sizes for every section (vary the visual rhythm)
- ❌ Pure black (#000000) on pure white (#ffffff) — too harsh

## Design Principles (ALWAYS Do)

- ✅ Make the person's name the most prominent element
- ✅ Use their actual words and achievements — don't genericize
- ✅ Create visual hierarchy through size, weight, and spacing — not color alone
- ✅ Ensure text is readable on all screen sizes (min 16px body text)
- ✅ Use whitespace generously — let the content breathe
- ✅ Make the CTA obvious but not aggressive
- ✅ Ensure the page works perfectly on mobile
- ✅ Keep the color palette restrained (2-3 colors max + neutrals)
- ✅ Use real content density — if they have 3 experiences, don't pad to make it look like 10
- ✅ Load distinctive Google Fonts (see template) — avoid invisible defaults like Inter, Roboto, Open Sans

## Emotional Tone of the Experience

Throughout the entire flow, maintain:
- **Encouraging but not patronizing** — they're adults learning something new
- **Technical but accessible** — use real terms, then explain them
- **Fast-moving but not rushed** — respect the 30 minutes
- **Teaching through doing, not lecturing** — action first, explanation after
- **Celebrating progress** — each step is a win
