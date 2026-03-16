# OPC Competitive Intelligence

**Competitive intelligence and strategic positioning for solo entrepreneurs** — turns a one-sentence product description into an actionable competitive map with market analysis, threat assessment, positioning recommendations, and comparison handling.

> **Important**: This is a competitive intelligence tool, not a market research firm. It provides structured analysis based on available information. For market sizing with primary data, patent analysis, or M&A due diligence, consult a domain expert.

## What It Does

### Product Description → Competitive Map
- Market classification (category, stage, buyer type)
- Four-tier competitor discovery (direct, indirect, potential, substitute)
- Non-competitor identification (who to ignore and why)
- Overlap scoring (0-100) per competitor

### Strategic Analysis
- Porter's Five Forces adapted for solo founders
- Threat assessment with evidence-based scoring
- Positioning gap identification
- Market entry strategy recommendation

### Positioning & Differentiation
- 7 differentiation axes (price, niche, experience, tech, integration, speed, simplicity)
- Wedge strategy selection with first-100-users plan
- Battles-to-avoid list
- Comparison handling templates ("When users ask how you differ from X, say...")

### Ongoing Intelligence
- Signal tracking (funding, launches, pricing changes, acquisitions)
- Threat matrix monitoring
- Competitor comparison tool
- Dashboard across all tracked landscapes

## Installation

### Option 1: Clone the full repo

```bash
git clone https://github.com/LeonFJR/opc-skills.git ~/.claude/skills/opc-skills
```

### Option 2: Copy just this skill

```bash
cp -r opc-skills/opc-competitive-intelligence ~/.claude/skills/opc-competitive-intelligence
```

### Option 3: Add to Claude Code settings

```json
{
  "skills": ["path/to/opc-skills/opc-competitive-intelligence"]
}
```

## Usage Examples

### Full competitive landscape from a product idea
> "I'm building an AI-powered invoice generator for freelancers"

### Quick competitive brief
> "Quick brief on the project management tools market"

### Deep dive a specific competitor
> "Deep dive on Notion — how do they compare to my product?"

### Get positioning strategy
> "How should I position my freelancer invoicing tool against FreshBooks and Wave?"

### Threat assessment
> "Who should I worry about most in the AI writing assistant space?"

### Track competitive signals
> "Notion just launched an AI writing feature — what does this mean for me?"

### Dashboard
> "Show me all the competitive landscapes I'm tracking"

## Archive Structure

```
intelligence/
├── INDEX.json
├── ai-invoice-generator/
│   ├── landscape.md              # Full competitive landscape report
│   ├── metadata.json             # Structured metadata
│   └── competitors/
│       └── freshbooks.md         # Individual competitor deep dive
└── project-management-tools/
    ├── landscape.md
    └── metadata.json
```

## Skill Architecture

```
opc-competitive-intelligence/
├── SKILL.md                      # Core workflow (7 modes, phased analysis)
├── README.md                     # This file
├── LICENSE                       # MIT
├── references/
│   ├── analysis-frameworks.md    # 4-tier model, Porter's, overlap scoring, threat classification
│   ├── positioning-playbook.md   # Positioning canvas, 7 axes, wedge strategies, messaging
│   └── entry-strategy-guide.md   # 5 entry patterns, decision matrix, first 100 users, pivot signals
├── templates/
│   ├── intelligence-metadata-schema.json  # JSON schema for all metadata
│   ├── landscape-report.md       # Full competitive landscape (8 sections)
│   ├── competitor-profile.md     # Individual competitor deep dive
│   ├── positioning-brief.md      # Positioning strategy output
│   └── quick-brief.md            # 1-page quick competitive brief
└── scripts/
    └── intel_tracker.py          # CLI: index, status, threats, signals, compare
```

## Requirements

- Claude Code CLI
- Python 3.8+ (stdlib only — no pip install needed)

## What This Skill Is NOT

- **Not a market research firm** — doesn't access proprietary databases or conduct surveys
- **Not a patent analyzer** — doesn't assess IP landscape or freedom-to-operate
- **Not M&A due diligence** — doesn't value companies or assess acquisition targets
- **Not a sales strategy tool** — doesn't design enterprise sales motions
- **Not financial modeling** — doesn't forecast market size or revenue with primary data

## When to Involve a Human Expert

- **Regulated industries**: Healthcare, finance, insurance — regulatory dynamics require domain expertise
- **Patent/IP questions**: Freedom-to-operate, infringement risk, IP strategy
- **International entry**: Country-specific regulatory requirements, localization strategy
- **Market sizing**: When precise TAM/SAM/SOM numbers are needed for investors or planning
- **M&A/acquisition**: Due diligence on targets or competitive acqui-hire situations

## License

MIT
