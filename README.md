# opc-skills

Claude Code skills for solo entrepreneurs and one-person company CEOs.

Build, run, and grow your business with AI-powered operational tools — designed for founders who wear every hat.

## Available Skills

| Skill | Description | Status |
|-------|-------------|--------|
| [opc-contract-manager](./opc-contract-manager/) | Review, archive, and manage contracts. Pre-signing risk analysis, negotiation prep, deadline tracking, and portfolio insights. | Available |
| [opc-invoice-manager](./opc-invoice-manager/) | AR light system — invoice generation, collections follow-up, payment reconciliation, aging analysis, and cash flow visibility. | Available |
| [opc-landing-page-manager](./opc-landing-page-manager/) | Landing page strategy, copywriting, design, and code generation — from product idea to a complete, conversion-optimized HTML page. | Available |
| [opc-product-manager](./opc-product-manager/) | Product spec generation — turn a one-sentence idea into a build-ready spec for Claude Code. MVP scoping, tech stack recommendations, complexity assessment. | Available |
| [opc-cash-flow-manager](./opc-cash-flow-manager/) | Cash flow decision system — probability-weighted forecasting, runway calculation, burn rate analysis, survival alerts, and cost-cut recommendations. | Available |

## Installation

### Option 1: Clone to Claude Code skills directory

```bash
git clone https://github.com/LeonFJR/opc-skills.git ~/.claude/skills/opc-skills
```

### Option 2: Copy a specific skill

```bash
# Copy only the skill you need
cp -r opc-skills/opc-contract-manager ~/.claude/skills/opc-contract-manager
```

### Option 3: Add as a project skill

Reference the skill directory in your project's `.claude/settings.json`:

```json
{
  "skills": ["path/to/opc-skills/opc-contract-manager"]
}
```

## Philosophy

These skills are built for **one-person companies** — founders who need to move fast without a legal team, finance department, or ops staff. Each skill:

- **Reduces friction** — auto-infers context instead of asking 20 questions
- **Produces actionable output** — not reports that sit in a folder, but decisions you can act on today
- **Stays in its lane** — clearly tells you when to escalate to a professional
- **Works locally** — no external services, no databases, just files you own

## License

MIT
