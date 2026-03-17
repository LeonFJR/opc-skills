# Content: {{topic}}

> **Topic ID**: {{topic_id}} | **Pillar**: {{pillar}} | **Persona**: {{persona}} | **Date**: {{date}}

---

{{#each platform_versions}}
## {{platform}} Version

**Format**: {{content_format}} | **Language**: {{language}} | **Chars**: {{char_count}}

### Hook Options

{{#each hook_options}}
{{@index}}. {{this}}
{{/each}}

**Selected hook**: {{selected_hook}}

### Body

```
{{body}}
```

### CTA Options

{{#each cta_options}}
{{@index}}. [{{cta_type}}] {{this}}
{{/each}}

**Selected CTA**: {{selected_cta}}

### Alternative Endings

{{#each alt_endings}}
{{@index}}. {{this}}
{{/each}}

{{#if risk_warnings}}
### ⚠️ Risk Warnings

{{#each risk_warnings}}
- {{this}}
{{/each}}
{{/if}}

{{#if hashtags}}
### Hashtags
{{#each hashtags}}`#{{this}}` {{/each}}
{{/if}}

---

{{/each}}

## Content Metadata

| Field | Value |
|-------|-------|
| Topic | {{topic}} |
| Pillar | {{pillar}} |
| Content type | {{content_type}} |
| Density | {{density}} |
| Persona | {{persona}} |
| Platforms | {{#each platforms}}`{{this}}` {{/each}} |
| Status | {{status}} |
| Scheduled | {{scheduled_date}} |

{{#if bilingual}}
---

## 中文版本 / Chinese Version

### {{primary_platform}} 版本

**格式**: {{zh_format}} | **字数**: {{zh_char_count}}

#### 开头选项

{{#each zh_hook_options}}
{{@index}}. {{this}}
{{/each}}

#### 正文

```
{{zh_body}}
```

#### CTA 选项

{{#each zh_cta_options}}
{{@index}}. {{this}}
{{/each}}

{{#if zh_risk_warnings}}
#### ⚠️ 风险提示

{{#each zh_risk_warnings}}
- {{this}}
{{/each}}
{{/if}}
{{/if}}
