# Brand & Social Strategy Profile: {{brand_name}}

> **Created**: {{created_at}} | **Version**: {{version}} | **Status**: {{status}}

---

## 1. Brand Voice

**Identity**: {{brand_voice.identity}}

**Persona**: {{brand_voice.persona}}

**Expertise areas**:
{{#each brand_voice.expertise}}
- {{this}}
{{/each}}

**Tone attributes**: {{#each brand_voice.tone_attributes}}`{{this}}` {{/each}}

**Voice examples**:
{{#each brand_voice.voice_examples}}
> "{{this}}"
{{/each}}

**Never say / never do**:
{{#each brand_voice.never_say}}
- ❌ {{this}}
{{/each}}

---

## 2. Target Audiences

{{#each audiences}}
### {{label}} ({{priority}})

{{description}}

**Platforms**: {{#each platforms}}`{{this}}` {{/each}}

{{/each}}

---

## 3. Content Pillars

| Pillar | Weight | Content Types | Description |
|--------|--------|--------------|-------------|
{{#each content_pillars}}
| **{{name}}** | {{weight}}% | {{#each content_types}}`{{this}}` {{/each}} | {{description}} |
{{/each}}

### Example Topics Per Pillar

{{#each content_pillars}}
**{{name}}**:
{{#each example_topics}}
- {{this}}
{{/each}}

{{/each}}

---

## 4. Platform Strategy

{{#each platform_strategy.platforms}}
### {{platform}} {{#if active}}✅{{else}}⏸️{{/if}}

- **Goal**: {{goal}}
- **Frequency**: {{frequency}}
- **Handle**: {{handle}}
{{#if tone_override}}- **Tone note**: {{tone_override}}{{/if}}

{{/each}}

---

## 5. Red Lines & Content Boundaries

### Prohibited Topics
{{#each red_lines.prohibited_topics}}
- 🚫 {{this}}
{{/each}}

### Prohibited Claims
{{#each red_lines.prohibited_claims}}
- ⚠️ {{this}}
{{/each}}

### Confidential Entities (Never Mention)
{{#each red_lines.confidential_entities}}
- 🔒 {{this}}
{{/each}}

### Competitor Policy
{{red_lines.competitor_rules}}

{{#if red_lines.legal_disclaimers}}
### Required Disclaimers
{{#each red_lines.legal_disclaimers}}
- {{this}}
{{/each}}
{{/if}}

---

## 6. Cross-Skill Links

{{#if product_id}}- **Product Spec**: `{{product_id}}` (opc-product-manager){{/if}}
{{#if landing_page_project_id}}- **Landing Page**: `{{landing_page_project_id}}` (opc-landing-page-manager){{/if}}
{{#if landscape_id}}- **Competitive Intelligence**: `{{landscape_id}}` (opc-competitive-intelligence){{/if}}
