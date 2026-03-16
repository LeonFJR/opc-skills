# Quick Competitive Brief: {{landscape_name}}

> {{product_description}} | {{market.category}} | {{market.market_stage}} market | {{created_at}}

## Market

**Category**: {{market.category}} ({{market.market_stage}})
**Buyer**: {{market.buyer_type}} | **Switching cost**: {{market.switching_cost}}
**Key trend**: {{primary_trend}}

## Top 5 Competitors

| # | Competitor | Tier | Threat | Overlap | Key Insight |
|---|-----------|------|--------|---------|-------------|
{{#each top_5}}
| {{@index}} | **{{name}}** | {{tier}} | {{threat_level}} | {{overlap_score}}/100 | {{key_insight}} |
{{/each}}

## Not Competitors (Don't Waste Time On)

{{#each not_competitors}}
- ~~{{name}}~~ — {{reason}}
{{/each}}

## Your Position

**Differentiate on**: {{positioning.differentiation_axis}} ({{positioning.differentiation_type}})
**Target gap**: {{positioning.target_gap}}
**Entry strategy**: {{positioning.wedge_strategy}}
**Avoid**: {{avoid_summary}}

## 3 Actions Now

1. **{{action_1}}**
2. **{{action_2}}**
3. **{{action_3}}**
