# Brand Safety & Risk Control Guide

Reference guide for content risk management, brand consistency, and compliance. Load on demand during Create mode and Review mode.

---

## 1. Mandatory Risk Scan

Every generated content item MUST be scanned against these rules before output. Violations produce warnings in `risk_warnings[]`.

### Category A: Prohibited Claims (Always Flag)

| Pattern | Why It's Risky | Flag As |
|---------|---------------|---------|
| "Industry first" / "World's first" / "Only solution" | Unverifiable superlative — legal risk, credibility risk | ⚠️ **UNVERIFIABLE CLAIM**: Cannot prove "[claim]" — rephrase with specifics |
| "Guaranteed results" / "You will [outcome]" | Promise without evidence — misleading | ⚠️ **UNSUBSTANTIATED PROMISE**: Remove guarantee language |
| "Used by thousands" / "Loved by hundreds" (without data) | Fabricated social proof | ⚠️ **UNVERIFIED SOCIAL PROOF**: Replace with specific, verifiable number or remove |
| "[X]% faster/better/cheaper" (without source) | Unverified comparative claim | ⚠️ **UNSOURCED STATISTIC**: Add source or remove |
| "AI-powered" as primary differentiator | Overused, unspecific, quickly dated | ⚠️ **GENERIC CLAIM**: "AI-powered" is not differentiation — specify what AI enables |
| Revenue/growth numbers not explicitly approved | May violate confidentiality | ⚠️ **CONFIDENTIAL DATA**: Verify this number is approved for public sharing |

### Category B: Confidentiality Violations (Always Block)

These MUST be caught before content is finalized:

- Client names not explicitly approved for public mention
- Revenue or financial figures not approved for sharing
- Contract terms, deal sizes, or pricing details
- Internal metrics not designated as public
- Investor names or fundraising details (unless publicly announced)
- Employee/contractor names without consent
- Product roadmap specifics not publicly announced

**Output format when detected**:
```
🚫 **CONFIDENTIALITY RISK**: This content mentions [entity/data] which may be confidential.
Verify this is approved for public sharing before publishing.
```

### Category C: Platform Compliance Risks

| Platform | Risk Area | Rule |
|---------|-----------|------|
| **All** | Fake engagement bait | Never write "Like if you agree" / "Share for good luck" / "Comment [word] to get [thing]" |
| **LinkedIn** | Manipulation tactics | Avoid "I'm humbled to announce" / engagement farming / fake vulnerability |
| **X** | Rage bait | Avoid deliberately inflammatory posts designed only for angry engagement |
| **All** | Misleading content | Never present speculation as fact, or others' results as your own |
| **All** | Impersonation | Never write in a way that suggests authority you don't have |

---

## 2. Brand Voice Consistency Checks

### Voice Drift Detection

Run these checks against the brand_voice profile:

| Check | How to Detect | Action |
|-------|--------------|--------|
| **Tone drift** | Content uses adjectives/style not in `tone_attributes` | Flag: "This sounds [detected tone] — your brand voice is [expected tone]" |
| **Persona mismatch** | "Researcher" voice in a "builder" branded post | Flag: "Persona mismatch — this reads as [detected] but you write as [expected]" |
| **Never-say violation** | Content contains phrases from `never_say` list | Flag: "Contains prohibited phrasing: [phrase]" |
| **Formality mismatch** | Too corporate for a casual brand, or too casual for professional | Flag: "Formality level doesn't match your brand voice" |
| **Generic voice** | Content could be written by anyone — no personality | Flag: "This lacks your unique voice — add a personal angle or specific experience" |

### Consistency Rules
1. **Same person across platforms**: Tone can adapt (more casual on X, more structured on LinkedIn) but the personality must feel like the same human.
2. **Opinions must be consistent**: Don't contradict a position you took last week unless explicitly framing it as "I changed my mind."
3. **Expertise claims must be real**: Only claim expertise in topics listed in `brand_voice.expertise`.
4. **No AI voice tells**: Remove phrases that scream AI-generated: "In today's landscape", "It's worth noting", "Let's dive in", "Here's the thing", "Buckle up."

---

## 3. Content-Type Specific Rules

### Product Updates
- ✅ Share features, milestones, behind-the-scenes
- ❌ Don't overpromise on roadmap ("coming soon" is fine, "launching next week" requires certainty)
- ❌ Don't disparage competitors while promoting your product
- ⚠️ If sharing metrics, only share what you'd be comfortable with investors or competitors seeing

### Case Studies / Customer Results
- ✅ Use real data with permission
- ✅ "One user reported..." with attribution or anonymized
- ❌ Don't fabricate case studies or composite "typical results"
- ❌ Don't present outlier results as typical
- ⚠️ Flag: "Have you confirmed this customer is OK being mentioned?"

### Industry Commentary
- ✅ Strong opinions based on personal experience
- ✅ Respectful disagreement with named companies
- ❌ Don't make accusations without evidence
- ❌ Don't share insider information from private conversations
- ⚠️ Flag when naming specific people (not companies) negatively

### Personal Narrative
- ✅ Be vulnerable and specific
- ✅ Share failures and lessons
- ❌ Don't share others' personal stories without permission
- ❌ Don't perform vulnerability for engagement (fake struggles)
- ⚠️ Flag content that might embarrass you in a future fundraise or partnership

---

## 4. Competitor Mention Rules

### Default Policy (Unless Overridden)

| Action | Rule |
|--------|------|
| **Name competitors directly?** | Yes, but respectfully. Never trash-talk. |
| **Compare features?** | Yes, with accurate data. "We do X differently" > "They're bad at X." |
| **React to competitor launches?** | Yes — congratulate or analyze objectively. |
| **Screenshot competitor UI?** | Check platform terms. Usually OK for commentary but risky. |
| **Poach competitor customers?** | Never target-shame. "If [tool] isn't working for you" > "Leave [tool]." |

### Competitor Mention Templates

**Respectful comparison**:
> "[Competitor] does [X] really well. We took a different approach for [audience] who need [Y] — here's why:"

**Reacting to their launch**:
> "Interesting move by [Competitor] launching [feature]. Here's what it means for [market]:"

**When asked "Why not [Competitor]?"**:
> "[Competitor] is great for [their audience]. We're built specifically for [your audience] who need [your differentiator]."

---

## 5. Escalation Triggers

Format: `📢 **COMMS EXPERT RECOMMENDED**: [reason].`

Flag and continue when ANY of these apply:

- Content references ongoing legal proceedings or disputes
- Content discusses regulatory compliance in specific jurisdictions
- Content involves crisis communication (public PR incident, data breach, controversy)
- Content names specific individuals negatively
- Content discusses financial performance in fundraising context
- Content could be interpreted as financial advice or investment recommendation
- Content involves health claims or medical advice
- Content references political topics or controversial social issues

---

## 6. Pre-Publish Checklist

Run before every piece of content is finalized:

| Check | Question |
|-------|----------|
| **Goal** | Does this post have a clear goal (awareness, engagement, leads, education)? |
| **Pillar** | Does it fit one of your content pillars? |
| **Audience** | Is it clear who this is for? |
| **Hook** | Would you stop scrolling to read this? |
| **Voice** | Does it sound like you (not generic AI)? |
| **CTA** | Is there a call to action (even if subtle)? |
| **Platform** | Is the format optimized for the target platform? |
| **Risk** | Any prohibited claims, confidential data, or risky phrasing? |
| **Overlap** | Have you posted something too similar in the past 4 weeks? |
| **Length** | Is it within the platform's optimal length range? |

If 2+ checks fail → revise before publishing.

---

## 7. Crisis Response Templates

### When You Made a Mistake Publicly

```
I got this wrong. [What you said] → [What's actually true].

Here's what I'm doing about it: [action].

Appreciate those who pointed it out. Will do better.
```

### When Someone Attacks Your Product

**Do NOT**:
- Respond emotionally
- Get into a public argument
- Delete their comment (unless abusive)

**Do**:
- Acknowledge the feedback
- Respond factually
- Take detailed discussion to DM

```
Thanks for the feedback. You're right that [acknowledged issue].
We're [working on X / aware of Y / this is by design because Z].
Happy to discuss more in DM.
```

### When a Competitor Calls You Out

```
Appreciate the mention. We see [topic] differently —
[your perspective in 1-2 sentences].
Always good for the market to have diverse approaches.
```
