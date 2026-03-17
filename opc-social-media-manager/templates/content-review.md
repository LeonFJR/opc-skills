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

## Section 1: What Worked (Required)

Top 3 posts and why they performed. Be specific — cite hook pattern, topic, format, timing, platform.

{{#each best_performing}}
### #{{@index}} — {{platform}}

**Post**: "{{hook_preview}}..."
**Metrics**: {{impressions}} impressions, {{engagements}} engagements, {{engagement_rate}}% rate
**Review Verdict**: {{review_verdict}}
**Why it worked**: {{why}}

{{/each}}

---

## Section 2: What Flopped (Required)

Bottom 3 posts and why. Specific diagnosis: too generic, wrong platform, bad hook, AI-smell, wrong timing.

{{#each worst_performing}}
### #{{@index}} — {{platform}}

**Post**: "{{hook_preview}}..."
**Metrics**: {{impressions}} impressions, {{engagements}} engagements, {{engagement_rate}}% rate
**Review Verdict**: {{review_verdict}}
**Why it underperformed**: {{why}}

{{/each}}

---

## Section 3: AI-Smell / Overly Polished (Required)

Content that sounded too corporate, generic, or AI-generated. Quote the problematic phrases and suggest rewrites.

{{#each ai_smell_flags}}
- **Content**: "{{phrase}}"
  **Problem**: {{diagnosis}}
  **Rewrite**: "{{suggested_fix}}"
{{/each}}

{{#if no_ai_smell}}
_No AI-smell detected this week._
{{/if}}

---

## Section 4: Recycle Candidates (Required)

Posts with review_verdict = "strong" + published on ≤ 2 platforms + still on-brand. Each with a suggested new angle/platform.

{{#each recycle_candidates}}
- **"{{hook_preview}}"** ({{original_date}}, {{platform}})
  Engagement: {{engagement_rate}}% | Verdict: {{review_verdict}}
  **Suggested recycling**: {{new_angle}} on {{new_platform}} as {{new_format}}
{{/each}}

{{#if no_recycle_candidates}}
_No recycle candidates this week._
{{/if}}

---

## Section 5: Pillar Imbalance (Required)

Target vs actual content weight per pillar. Flag deviations above threshold.

| Pillar | Posts | Target Weight | Actual Weight | Deviation | Status |
|--------|-------|--------------|---------------|-----------|--------|
{{#each pillar_imbalance}}
| {{name}} | {{posts}} | {{target_weight}}% | {{actual_weight}}% | {{deviation}}% | {{#if over_threshold}}⚠️ OFF TARGET{{else}}OK{{/if}} |
{{/each}}

**Recommendation**: {{pillar_recommendation}}

---

## Section 6: Next-Week Experiments (Required)

3 specific experiments to try. Each must be concrete and actionable.

{{#each experiments_next_week}}
{{@index}}. **{{experiment}}**
   What to test: {{what_to_test}}
   Success metric: {{success_metric}}
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

## Hook Analysis

| Hook Pattern | Uses | Avg Engagement Rate | Verdict |
|-------------|------|--------------------|----|
{{#each hook_analysis}}
| {{pattern}} | {{uses}} | {{avg_rate}}% | {{verdict}} |
{{/each}}
