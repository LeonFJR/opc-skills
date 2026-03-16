# Competitive Analysis Frameworks

Reference guide for structured competitive intelligence. Load on demand during Landscape and Threat Check modes.

---

## 1. Four-Tier Competitive Classification

Every competitor must be placed into exactly one tier. This is non-negotiable — an undifferentiated list is useless.

### Tier 1: Direct Competitors

**Definition**: Same problem, same audience, similar solution approach.

**Detection signals**:
- Users mention them in the same breath as your product
- They show up in the same search queries
- Feature sets overlap >60%
- Target audience is nearly identical
- Pricing is in the same range

**Example**: Notion vs Coda (both are all-in-one workspace tools for teams)

### Tier 2: Indirect Competitors

**Definition**: Same problem, different approach or different primary audience.

**Detection signals**:
- Solves the same underlying need but with a different method
- Different product category but overlapping use cases
- Users might choose them instead, but for different reasons
- Feature overlap is 20-60%

**Example**: Notion (workspace) vs Google Docs + Sheets (separate tools solving same needs)

### Tier 3: Potential Competitors

**Definition**: Adjacent players who don't compete today but could enter your space.

**Detection signals**:
- Large platform that could add your feature as a module
- Well-funded startup in adjacent space
- Company with overlapping audience but different product today
- Announced roadmap items that move toward your space

**Example**: Shopify adding email marketing (entering Mailchimp's space)

### Tier 4: Substitutes

**Definition**: What users do today without any product — the "do nothing" or "manual process" option.

**Detection signals**:
- Spreadsheets, email, pen-and-paper, hiring someone
- "We just use [basic tool] for that"
- Internal custom scripts or workflows
- Outsourcing to agencies or freelancers

**Example**: For a proposal generator tool, the substitute is "copy-paste from last proposal in Google Docs"

---

## 2. Overlap Scoring (0-100)

Calculate overlap across three dimensions, then average:

| Dimension | Weight | Scoring |
|-----------|--------|---------|
| **Audience overlap** | 40% | 0 = completely different users, 100 = identical target user |
| **Feature overlap** | 35% | 0 = no shared features, 100 = identical feature set |
| **Pricing overlap** | 25% | 0 = different price tier entirely, 100 = same price range and model |

**Overlap score** = (audience × 0.4) + (feature × 0.35) + (pricing × 0.25)

**Interpretation**:
- **80-100**: Near-identical competitor — head-on battle, must differentiate clearly
- **60-79**: Strong competitor — significant overlap, need strategic positioning
- **40-59**: Moderate competitor — partial overlap, can coexist with clear niche
- **20-39**: Weak competitor — limited overlap, mostly different markets
- **0-19**: Not really a competitor — surface similarity only

---

## 3. Threat Level Classification

Every threat_level assignment MUST cite specific evidence. No vibes.

### Critical

Assign when ANY of these are true:
- Direct competitor with >80% overlap AND dominant market position
- Well-funded competitor ($10M+) actively targeting your exact niche
- Platform risk: your product depends on their platform and they're building competing features
- Competitor with strong network effects in your target market

**Evidence required**: Specific funding amounts, market share data, product announcements, platform policies.

### High

Assign when ANY of these are true:
- Direct competitor with 60-80% overlap AND growing fast
- Indirect competitor with strong distribution that could pivot
- Competitor with significantly lower pricing for similar features
- Competitor with established brand trust in your target audience

**Evidence required**: Growth signals (hiring, feature launches), pricing pages, brand recognition indicators.

### Medium

Assign when:
- Direct competitor with 40-60% overlap OR different target segment
- Potential competitor that hasn't signaled entry yet
- Competitor with higher pricing (you can undercut)
- Competitor with weaker product but stronger distribution

**Evidence required**: Product comparison, pricing analysis, distribution channel assessment.

### Low

Assign when:
- Overlap <40%
- Competitor focused on different market segment
- Declining or stagnant competitor
- Substitute that users are accustomed to but could be disrupted

### None

Assign when:
- Surface similarity only — actually serves different need
- Different market entirely despite similar technology
- Shut down or pivoted away from your space

---

## 4. Porter's Five Forces (Solo Founder Adaptation)

Simplified to actionable questions. Score each as Low / Medium / High.

### Buyer Power (Can customers easily leave?)

| Signal | Score |
|--------|-------|
| No switching cost, data is portable | High |
| Some learning curve, data export exists | Medium |
| Deep integration, data lock-in, workflow dependency | Low (good for you) |

**Solo founder implication**: High buyer power → you need to earn loyalty daily. Low → focus on acquisition, retention is built-in.

### Supplier Power (Are you dependent on platforms?)

| Signal | Score |
|--------|-------|
| Built on a single platform API (Shopify, Slack, etc.) | High |
| Uses commodity infrastructure (AWS, Stripe) | Medium |
| Fully self-contained, no critical dependencies | Low |

**Solo founder implication**: High supplier power → platform risk. Build abstraction layers or diversify.

### New Entrant Threat (How easy to copy you?)

| Signal | Score |
|--------|-------|
| Simple CRUD app, no data moat, weekend buildable | High |
| Requires domain expertise or proprietary data | Medium |
| Network effects, regulatory barriers, deep integration | Low |

**Solo founder implication**: High new entrant threat → speed to market matters more than perfection. Ship fast, build switching costs.

### Substitute Threat (Can users just NOT use any product?)

| Signal | Score |
|--------|-------|
| Users currently solve this with spreadsheets/email successfully | High |
| Manual process exists but is painful | Medium |
| No viable manual alternative | Low |

**Solo founder implication**: High substitute threat → your product must be 10x better than the manual process, not 2x.

### Competitive Intensity (How crowded and aggressive?)

| Signal | Score |
|--------|-------|
| 10+ direct competitors, frequent price wars, high marketing spend | High |
| 3-10 competitors, some differentiation | Medium |
| <3 direct competitors, clear segmentation | Low |

**Solo founder implication**: High intensity → niche down aggressively. Don't compete on all fronts.

---

## 5. Moat Types

Assess which moats competitors have, and which you can realistically build.

| Moat Type | Description | Solo-Buildable? |
|-----------|-------------|-----------------|
| **Network effects** | Product gets better as more people use it | Hard — requires critical mass |
| **Data** | Proprietary data that improves the product | Possible — if you collect unique data over time |
| **Brand** | Trust and recognition in the market | Slow — but personal brand can substitute |
| **Switching cost** | Users are locked in by integrations/data/workflow | Yes — deep integrations create this |
| **Distribution** | Privileged access to customers | Possible — via niche communities, SEO, partnerships |
| **Tech** | Proprietary technology that's hard to replicate | Possible — if you have deep domain expertise |
| **Regulatory** | Licenses, certifications, compliance barriers | Unlikely — expensive for solo founders |
| **None** | No sustainable competitive advantage | Common — compete on speed and focus |

---

## 6. Market Stage Detection

| Stage | Signals | Solo Founder Strategy |
|-------|---------|----------------------|
| **Emerging** | Few competitors, undefined category, users don't know they need this yet | Educate market, establish category, move fast |
| **Growing** | New entrants weekly, VC money flowing in, "hot" space | Niche down, avoid head-on with funded players, find underserved segment |
| **Mature** | Established leaders, consolidation happening, growth slowing | Differentiate sharply, target neglected segments, innovate on experience |
| **Declining** | Leaders pivoting away, users migrating to alternatives | Don't enter unless you see a counter-trend others miss |

---

## 7. "Not a Competitor" Framework

It's equally important to identify who is NOT a competitor. This prevents wasted energy.

**Not a competitor when**:
- **Different primary audience**: Even if the product looks similar, they serve enterprise and you serve indie creators
- **Different core problem**: Similar technology but solving fundamentally different jobs-to-be-done
- **Different geography**: They're dominant in Asia, you're targeting US/EU
- **Different price tier**: They charge $500/mo enterprise, you charge $9/mo solo — different buyers entirely
- **Complementary, not competitive**: Their product integrates with or feeds into yours
- **Abandoned/pivoted**: Product exists but is no longer actively developed in your space

**Always explicitly state**: "These companies may look like competitors but aren't, because [specific reason]."
