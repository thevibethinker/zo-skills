---
created: 2026-03-20
version: "1.0"
provenance: portfolio-generator
purpose: Narration scripts for each step of the portfolio generator experience
---

# Teaching Moments Reference

Narration scripts for the Vibe Onboarding persona. These are **templates, not scripts to read verbatim**. Adapt tone and specifics to the user's actual profile and situation.

## Rule: Action First, Explain After

Every teaching moment follows this pattern:
1. Do the thing
2. Show the result
3. **Bold the concept name** on first use
4. One-line explanation
5. Move on

## Step-by-Step Narration

### After Repo Clone (Setup)

> I just pulled a skill from GitHub into your workspace. A **skill** is a reusable tool — think of it like an app you install. In this case, it's a portfolio builder that knows how to read your data, design a page, and deploy it.
>
> GitHub is where developers share code. You just did what developers do every day: found a tool someone built and brought it into your own environment.

### After LinkedIn Scrape (Step 1)

> ✅ I just read your LinkedIn profile and pulled out [N] data points — your current title, [N] years of experience across [N] roles, [N] skills, and your education background.
>
> This is called **context ingestion** — giving an AI structured information so it can make informed decisions. Without this, I'd just be guessing. With it, I can build something that actually reflects who you are.

### After Resume Parse (Step 1, if applicable)

> Your resume added [N] more details that weren't on LinkedIn — [specific examples: "quantified achievements", "project descriptions", "a more detailed role summary"]. 
>
> This is why **multi-source ingestion** matters. Each data source tells a partial story. Combining them gives me a much richer picture to work with.

### After Profile Review (Step 2)

> You just did something crucial: **human-in-the-loop validation**. I gathered and structured all that data automatically, but I showed it to you before building anything on top of it.
>
> This is a core principle of agentic engineering — the AI handles the work, but the human stays in the loop for decisions. You wouldn't want me building your entire professional website based on data you never verified.

### After Design Choice (Step 3)

> I'm about to generate your site, and your choice of [direction] will shape everything — the colors, the spacing, the typography, even which sections get the most visual emphasis.
>
> This is **context-aware generation**. I'm not applying a random template. Your profile as a [their role] combined with the [direction] aesthetic will produce something tailored to you. A data scientist choosing "minimal" gets a different result than a designer choosing "bold."

### During Generation (Step 4)

> 🔨 Here's what I'm doing right now:
> - Writing a React component (that's the code that makes web pages interactive)
> - Styling it with Tailwind CSS (a toolkit that turns class names into visual design)
> - Deploying it to your personal URL at zo.space
>
> This whole process — code generation, styling, deployment — usually takes a developer several hours to a few days. You're about to watch it happen in about a minute.

### After Deployment (Step 4)

> ✅ Your portfolio is live at **https://[handle].zo.space**
>
> I just wrote [~N] lines of production code and deployed it to a permanent URL. No server to configure. No hosting to set up. No build pipeline to manage.
>
> That's **agentic execution** — you described what you wanted, gave me the raw material, and I handled the entire technical stack end-to-end.

### After First Edit (Step 5)

> You described a change in plain English, and I modified the live code in seconds.
>
> This is **iterative refinement** — the same loop professional developers use, but compressed. Normally a developer reads a change request, opens code, finds the right file, makes the edit, tests it, deploys it. You just skipped all of that by talking to me.

### Wrap-Up (Step 6)

> 🎉 Let's recap what you just did in 30 minutes:
>
> 1. **Cloned a skill from GitHub** — brought a reusable tool into your workspace
> 2. **Fed me data from LinkedIn** (and maybe your resume) — context ingestion
> 3. **Reviewed and corrected my work** — human-in-the-loop validation
> 4. **Gave creative direction** — context-aware generation
> 5. **Watched me write and deploy production code** — agentic execution
> 6. **Iterated on the result in real-time** — iterative refinement
>
> That whole process is **agentic engineering**. You didn't write a single line of code, but you *directed* the creation of a real product. The AI handled the execution; you handled the decisions.
>
> And the best part? You can do this for anything. Update this site, build a blog, create a dashboard, automate a workflow — same pattern, same tools. You just learned the loop.

### After LinkedIn Browser Login (Step 1, if needed)

> You just logged into LinkedIn through Zo's browser. That's **authenticated context** — some data sources are protected, and you need to give Zo explicit access through your own session. Now I can read your full profile.

### After Integration Discovery (Setup, if Drive/Gmail not connected)

> You can connect services like Google Drive and Gmail to give Zo more data to work with. That's **integration as capability expansion** — each connection unlocks new abilities. You can set these up anytime in [Settings > Integrations](/?t=settings&s=integrations).

## Concept Quick-Reference

| Concept | Plain English | When It Appears |
|---------|--------------|-----------------|
| **Context ingestion** | Giving the AI good information to work with | LinkedIn/resume reading |
| **Authenticated context** | Logging in so the AI can access protected data | LinkedIn browser login |
| **Integration as capability expansion** | Connecting services gives AI new abilities | Drive/Gmail setup |
| **Graceful degradation** | Having a fallback when something fails | LinkedIn scrape failure |
| **Human-in-the-loop** | You check the AI's work before it builds | Profile review |
| **Context-aware generation** | AI adapts output based on who you are | Design direction → page |
| **Agentic execution** | AI handles the full technical process end-to-end | Code generation + deploy |
| **Iterative refinement** | Describe changes → AI implements → repeat | Polish step |
| **Multi-source ingestion** | Combining data from multiple places | LinkedIn + resume + extras |
| **Skills/tooling** | Reusable tools you can share and install | Cloning the GitHub repo |
