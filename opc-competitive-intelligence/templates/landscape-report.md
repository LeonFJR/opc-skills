# Competitive Landscape: {{landscape_name}}

> **Product**: {{product_description}}
> **Market**: {{market.category}} {{#if market.subcategory}}→ {{market.subcategory}}{{/if}}
> **Date**: {{created_at}} | **Version**: {{version}} | **Status**: {{status}}

---

## 1. Market Definition

**Category**: {{market.category}}
**Subcategory**: {{market.subcategory}}
**Market Stage**: {{market.market_stage}}
**Buyer Type**: {{market.buyer_type}}
**Switching Cost**: {{market.switching_cost}}
**Winner-Take-All Dynamics**: {{market.winner_take_all}}

**Adjacent Markets**:
{{#each market.adjacent_categories}}
- {{this}}
{{/each}}

**Key Trends**:
{{#each market.key_trends}}
- {{this}}
{{/each}}

---

## 2. Competitive Map

### Direct Competitors (Same problem, same audience, similar approach)

| Competitor | Positioning | Pricing | Overlap | Threat | Moat |
|-----------|-------------|---------|---------|--------|------|
{{#each competitors_direct}}
| **{{name}}** | {{positioning}} | {{pricing_model}} {{pricing_range}} | {{overlap_score}}/100 | {{threat_level}} | {{moat_type}} |
{{/each}}

### Indirect Competitors (Same problem, different approach)

| Competitor | Positioning | How They Differ | Overlap | Threat |
|-----------|-------------|-----------------|---------|--------|
{{#each competitors_indirect}}
| **{{name}}** | {{positioning}} | {{notes}} | {{overlap_score}}/100 | {{threat_level}} |
{{/each}}

### Potential Competitors (Could enter your space)

| Company | Why They Might Enter | When | Threat |
|---------|---------------------|------|--------|
{{#each competitors_potential}}
| **{{name}}** | {{notes}} | {{stage}} | {{threat_level}} |
{{/each}}

### Substitutes (What users do without any product)

| Alternative | How Users Solve It Today | Why They Switch (or Don't) |
|------------|-------------------------|---------------------------|
{{#each competitors_substitute}}
| **{{name}}** | {{positioning}} | {{notes}} |
{{/each}}

---

## 3. Not Competitors

These companies look similar but are **NOT** real competitors:

{{#each not_competitors}}
- **{{name}}**: {{reason}}
{{/each}}

---

## 4. Top 3 Deep Dives

{{#each top_3_competitors}}
### {{name}} — Threat Level: {{threat_level}}

**What they do**: {{positioning}}
**Who they serve**: {{target_audience}}
**Pricing**: {{pricing_model}} — {{pricing_range}}
**Stage**: {{stage}}

**Strengths**:
{{#each strengths}}
- {{this}}
{{/each}}

**Weaknesses**:
{{#each weaknesses}}
- {{this}}
{{/each}}

**Their moat**: {{moat_type}}
**Overlap with you**: {{overlap_score}}/100

**How to compete against them**:
{{compete_strategy}}

{{/each}}

---

## 5. Market Forces (Porter's Five Forces — Solo Founder Edition)

| Force | Level | What It Means For You |
|-------|-------|----------------------|
| **Buyer Power** | {{market_forces.buyer_power}} | {{buyer_power_explanation}} |
| **Supplier Power** | {{market_forces.supplier_power}} | {{supplier_power_explanation}} |
| **New Entrant Threat** | {{market_forces.new_entrant_threat}} | {{new_entrant_explanation}} |
| **Substitute Threat** | {{market_forces.substitute_threat}} | {{substitute_explanation}} |
| **Competitive Intensity** | {{market_forces.competitive_intensity}} | {{intensity_explanation}} |

**Summary**: {{market_forces.summary}}

---

## 6. Positioning Recommendation

**Your positioning**: {{positioning.recommended_position}}

**Differentiation axis**: {{positioning.differentiation_axis}} ({{positioning.differentiation_type}})

**Target gap**: {{positioning.target_gap}}

**Wedge strategy**: {{positioning.wedge_strategy}}

**Messaging angle**: {{positioning.messaging_angle}}

### Battles to Avoid

{{#each positioning.avoid_battles}}
- {{this}}
{{/each}}

---

## 7. Comparison Handling Guide

When users compare you to competitors, use these responses:

{{#each positioning.comparison_handling}}
### "How are you different from {{competitor_name}}?"

> {{response}}

{{/each}}

---

## 8. Action Items

### Immediate (This Week)
{{#each action_items_immediate}}
- [ ] **{{action}}** — {{rationale}}
{{/each}}

### Short Term (This Month)
{{#each action_items_short_term}}
- [ ] **{{action}}** — {{rationale}}
{{/each}}

### Medium Term (This Quarter)
{{#each action_items_medium_term}}
- [ ] **{{action}}** — {{rationale}}
{{/each}}
