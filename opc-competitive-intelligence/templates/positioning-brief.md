# Positioning Strategy: {{landscape_name}}

> **Product**: {{product_description}}
> **Market**: {{market.category}}
> **Date**: {{date}}

---

## Positioning Canvas

| Element | Your Position |
|---------|--------------|
| **Audience** | {{audience}} |
| **Problem** | {{problem}} |
| **Solution** | {{solution}} |
| **Differentiation** | {{differentiation}} |
| **Proof** | {{proof}} |

**Positioning statement**:
> For {{audience}} who {{problem}}, {{product_name}} is the {{category}} that {{differentiation}}. Unlike {{primary_competitor}}, we {{key_difference}}.

---

## Differentiation Strategy

**Primary axis**: {{positioning.differentiation_axis}}
**Type**: {{positioning.differentiation_type}}

**Why this axis**:
{{differentiation_rationale}}

**The specific gap you fill**:
{{positioning.target_gap}}

---

## Wedge Strategy

**Recommended entry pattern**: {{positioning.wedge_strategy}}

**Step-by-step**:
{{#each wedge_steps}}
{{@index}}. {{this}}
{{/each}}

**First 100 users**:
{{#each first_100_users}}
- {{this}}
{{/each}}

---

## Battles to Avoid

{{#each positioning.avoid_battles}}
### {{this}}
**Why**: {{reason}}
**Instead**: {{alternative}}

{{/each}}

---

## Messaging Framework

### Headline
{{headline}}

### Subheadline
{{subheadline}}

### Three Proof Points
{{#each proof_points}}
{{@index}}. {{this}}
{{/each}}

### CTA
{{cta}}

---

## Comparison Handling Guide

{{#each positioning.comparison_handling}}
### vs {{competitor_name}}
> {{response}}

{{/each}}

---

## Action Items

{{#each action_items}}
- [ ] **[{{priority}}]** {{action}}
{{/each}}
