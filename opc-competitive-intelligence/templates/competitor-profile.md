# Competitor Deep Dive: {{name}}

> **Landscape**: {{landscape_name}}
> **Date**: {{date}} | **Tier**: {{tier}} | **Threat Level**: {{threat_level}}

---

## Company Overview

- **Name**: {{name}}
- **URL**: {{url}}
- **Stage**: {{stage}}
- **Founded**: {{founded}}
- **Funding**: {{funding}}
- **Team size**: {{team_size}}

## Product Analysis

**One-liner**: {{positioning}}

**Target audience**: {{target_audience}}

**Core features**:
{{#each core_features}}
- {{this}}
{{/each}}

**What they do well**:
{{#each strengths}}
- {{this}}
{{/each}}

**Where they fall short**:
{{#each weaknesses}}
- {{this}}
{{/each}}

## Pricing Deep Dive

- **Model**: {{pricing_model}}
- **Range**: {{pricing_range}}
- **Free tier**: {{free_tier}}
- **Key pricing insight**: {{pricing_insight}}

## Moat Assessment

**Primary moat**: {{moat_type}}

**Moat strength**: {{moat_strength}}

**Can you replicate it?**: {{moat_replicable}}

## Overlap Analysis

**Overlap score**: {{overlap_score}}/100

| Dimension | Score | Details |
|-----------|-------|---------|
| Audience overlap | {{audience_overlap}}/100 | {{audience_overlap_detail}} |
| Feature overlap | {{feature_overlap}}/100 | {{feature_overlap_detail}} |
| Pricing overlap | {{pricing_overlap}}/100 | {{pricing_overlap_detail}} |

## Threat Assessment

| Dimension | Threat | Evidence | Your Counter |
|-----------|--------|----------|-------------|
{{#each threat_dimensions}}
| {{dimension}} | {{threat_level}} | {{evidence}} | {{your_counter}} |
{{/each}}

## How to Compete Against {{name}}

### Where you can win
{{#each win_areas}}
- {{this}}
{{/each}}

### Where you should NOT compete
{{#each avoid_areas}}
- {{this}}
{{/each}}

### Comparison handling
> When users say "How are you different from {{name}}?"
>
> {{comparison_response}}

## Signals to Watch

Monitor these for changes in threat level:
{{#each watch_signals}}
- {{this}}
{{/each}}
