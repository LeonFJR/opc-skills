# Engagement Queue: {{brand_name}}

> **Date**: {{date}} | **Pending**: {{pending_count}} | **Overdue Follow-Ups**: {{overdue_count}}

---

## Group 1: Urgent Replies

Items with priority = urgent OR overdue follow-ups (follow_up_due < today AND follow_up_status = "pending").

{{#each urgent_replies}}
### {{@index}}. [{{type}}] from {{from}} ({{from_tier}}) on {{platform}}

**Context**: {{context}}
**Reply Goal**: {{reply_goal}}
**Follow-Up Due**: {{follow_up_due}} {{#if days_overdue}}({{days_overdue}} days overdue){{/if}}

**Suggested Reply**:
> {{suggested_reply}}

---

{{/each}}

{{#if no_urgent}}
_No urgent items._
{{/if}}

---

## Group 2: High-Value Relationship Follow-Ups

From tier: investor, existing_customer, potential_customer, kol, media — with pending follow-ups.

{{#each high_value_followups}}
### {{from}} ({{from_tier}}) — {{platform}}

**Reply Goal**: {{reply_goal}}
**Follow-Up Due**: {{follow_up_due}}
**Follow-Up Reason**: {{follow_up_reason}}
**Follow-Up Status**: {{follow_up_status}}

**Context**: {{context}}
**Suggested Reply**:
> {{suggested_reply}}

---

{{/each}}

{{#if no_high_value}}
_No high-value follow-ups pending._
{{/if}}

---

## Group 3: Community & Low-Priority

All other pending replies — peers, general audience, non-urgent interactions.

| # | Type | From | Tier | Platform | Reply Goal | Priority |
|---|------|------|------|----------|------------|----------|
{{#each community_replies}}
| {{@index}} | {{type}} | {{from}} | {{from_tier}} | {{platform}} | {{reply_goal}} | {{priority}} |
{{/each}}

{{#each community_replies}}
### {{from}} — {{type}}

**Context**: {{context}}
**Reply Goal**: {{reply_goal}}
**Suggested reply**: {{suggested_reply}}

---

{{/each}}

---

## High-Value Contacts

People worth proactively engaging with:

| Name | Tier | Platform | Handle | Last Interaction | Follow-Up Status |
|------|------|----------|--------|-----------------|-----------------|
{{#each high_value_contacts}}
| {{name}} | {{tier}} | {{platform}} | {{handle}} | {{last_interaction}} | {{follow_up_status}} |
{{/each}}

---

## Content Opportunities from Engagement

Topics extracted from audience interactions:

{{#each content_opportunities}}
- **From**: {{source}} | **Topic idea**: {{topic}} | **Why**: {{rationale}}
{{/each}}
