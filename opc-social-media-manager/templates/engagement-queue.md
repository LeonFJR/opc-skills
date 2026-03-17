# Engagement Queue: {{brand_name}}

> **Date**: {{date}} | **Pending**: {{pending_count}} | **High-Value**: {{high_value_count}}

---

## Priority Replies

{{#each urgent_replies}}
### {{@index}}. [{{type}}] from {{from}} ({{from_tier}}) on {{platform}}

**Context**: {{context}}

**Suggested Reply**:
> {{suggested_reply}}

**Priority**: {{priority}} | **Status**: {{status}}

{{#if content_opportunity}}
💡 **Content opportunity**: {{content_opportunity}}
{{/if}}

---

{{/each}}

## Standard Replies

| # | Type | From | Tier | Platform | Priority | Status |
|---|------|------|------|----------|----------|--------|
{{#each standard_replies}}
| {{@index}} | {{type}} | {{from}} | {{from_tier}} | {{platform}} | {{priority}} | {{status}} |
{{/each}}

{{#each standard_replies}}
### {{from}} — {{type}}

**Context**: {{context}}
**Suggested reply**: {{suggested_reply}}

---

{{/each}}

## High-Value Contacts

People worth proactively engaging with:

| Name | Tier | Platform | Handle | Last Interaction | Notes |
|------|------|----------|--------|-----------------|-------|
{{#each high_value_contacts}}
| {{name}} | {{tier}} | {{platform}} | {{handle}} | {{last_interaction}} | {{notes}} |
{{/each}}

### Follow-Up Suggestions

{{#each follow_up_suggestions}}
- **{{contact_name}}** ({{tier}}): {{suggestion}}
{{/each}}

---

## Content Opportunities from Engagement

Topics extracted from audience interactions:

{{#each content_opportunities}}
- **From**: {{source}} | **Topic idea**: {{topic}} | **Why**: {{rationale}}
{{/each}}
