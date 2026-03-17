# Content Review: Week {{week}}

> **Brand**: {{brand_name}} | **Period**: {{period_start}} — {{period_end}}

---

## Summary

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Posts published | {{posts_published}} | {{prev_posts_published}} | {{posts_change}} |
| Total impressions | {{total_impressions}} | {{prev_impressions}} | {{impressions_change}} |
| Total engagements | {{total_engagements}} | {{prev_engagements}} | {{engagements_change}} |
| Avg engagement rate | {{avg_engagement_rate}}% | {{prev_engagement_rate}}% | {{rate_change}} |
| Leads generated | {{leads}} | {{prev_leads}} | {{leads_change}} |
| DMs received | {{dms}} | {{prev_dms}} | {{dms_change}} |

---

## Best Performing Content

{{#each best_performing}}
### #{{@index}} — {{platform}}

**Post**: "{{hook_preview}}..."
**Metrics**: {{impressions}} impressions, {{engagements}} engagements, {{engagement_rate}}% rate
**Why it worked**: {{why}}

{{/each}}

---

## Worst Performing Content

{{#each worst_performing}}
### #{{@index}} — {{platform}}

**Post**: "{{hook_preview}}..."
**Metrics**: {{impressions}} impressions, {{engagements}} engagements, {{engagement_rate}}% rate
**Why it underperformed**: {{why}}

{{/each}}

---

## Effective Patterns

What worked this week:

{{#each effective_patterns}}
- ✅ {{this}}
{{/each}}

---

## Ineffective Patterns

What didn't work:

{{#each ineffective_patterns}}
- ❌ {{this}}
{{/each}}

---

## Platform Breakdown

{{#each platform_breakdown}}
### {{platform}}

| Metric | Value |
|--------|-------|
| Posts | {{posts}} |
| Impressions | {{impressions}} |
| Engagements | {{engagements}} |
| Engagement rate | {{engagement_rate}}% |
| Best content type | {{best_type}} |

{{/each}}

---

## Pillar Performance

| Pillar | Posts | Avg Engagement Rate | Target Weight | Actual Weight |
|--------|-------|--------------------|----|------|
{{#each pillar_performance}}
| {{name}} | {{posts}} | {{avg_rate}}% | {{target_weight}}% | {{actual_weight}}% |
{{/each}}

---

## Hook Analysis

| Hook Pattern | Uses | Avg Engagement Rate | Verdict |
|-------------|------|--------------------|----|
{{#each hook_analysis}}
| {{pattern}} | {{uses}} | {{avg_rate}}% | {{verdict}} |
{{/each}}

---

## Next Week Recommendations

{{#each next_week_recommendations}}
{{@index}}. **{{this}}**
{{/each}}

### Suggested Topics for Next Week

{{#each suggested_topics}}
- [ ] **{{topic}}** — {{pillar}} / {{platform}} / {{content_type}} — {{rationale}}
{{/each}}

### Recycling Candidates

Posts from 4+ weeks ago worth revisiting:

{{#each recycle_candidates}}
- **"{{hook_preview}}"** ({{original_date}}, {{platform}}) — {{original_engagement_rate}}% engagement. Suggest: {{new_angle}}
{{/each}}
