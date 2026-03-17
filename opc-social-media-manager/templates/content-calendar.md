# Content Calendar: {{brand_name}}

> **Week**: {{calendar.current_week}} | **Generated**: {{date}}

---

## Weekly Schedule

| Day | Platform | Slot Type | Content | Status |
|-----|---------|-----------|---------|--------|
{{#each calendar.weekly_slots}}
| {{day}} | `{{platform}}` | {{slot_type}} | {{#if content_id}}[{{content_id}}]{{else}}— *empty* —{{/if}} | {{#if content_id}}assigned{{else}}open{{/if}} |
{{/each}}

---

## Platform Breakdown

{{#each platform_summary}}
### {{platform}} — {{frequency}}

Posts this week: {{planned_count}} / {{target_count}}

| # | Topic | Type | Status |
|---|-------|------|--------|
{{#each posts}}
| {{@index}} | {{topic}} | {{content_type}} | {{status}} |
{{/each}}

{{/each}}

---

## Content Mix This Week

| Pillar | Target | Planned | Gap |
|--------|--------|---------|-----|
{{#each pillar_allocation}}
| {{name}} | {{target}}% | {{planned}}% | {{gap}} |
{{/each}}

---

## Content Series

{{#each calendar.series}}
### {{name}}
- **Frequency**: {{frequency}}
- **Platform**: {{platform}}
- **Episodes so far**: {{episode_count}}
- **Next due**: {{next_due}}
{{/each}}

---

## Topic Backlog (Prioritized)

### High Priority
{{#each backlog_high}}
- [ ] **{{topic}}** — {{pillar_id}} / {{content_type}} / {{#each target_platforms}}`{{this}}` {{/each}}
{{/each}}

### Medium Priority
{{#each backlog_medium}}
- [ ] {{topic}} — {{pillar_id}} / {{content_type}}
{{/each}}

### Low Priority / Bank
{{#each backlog_low}}
- [ ] {{topic}} — {{pillar_id}}
{{/each}}

---

## Pre-Publish Checklist

For each content item before publishing:

- [ ] Goal is clear (awareness / engagement / leads / education)
- [ ] Fits a content pillar
- [ ] Hook stops the scroll
- [ ] Sounds like your voice (not generic)
- [ ] Has a CTA
- [ ] Platform format optimized (length, structure, hashtags)
- [ ] No prohibited claims or confidential data
- [ ] Not too similar to recent posts
