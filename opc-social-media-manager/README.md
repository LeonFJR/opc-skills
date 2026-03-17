# OPC Social Media Manager

**Social media growth operating system for solo entrepreneurs** — covers the full pipeline from brand positioning through content creation, calendar management, audience engagement, and performance optimization.

> **Important**: This is a content strategy and creation tool, not a social media scheduling or analytics platform. It generates content and strategy — you handle the actual posting and data collection.

## What It Does

### Brand Positioning → Content Strategy
- Brand voice profile (identity, tone, expertise, boundaries)
- Audience segmentation (customers, peers, investors, developers)
- Content pillar generation with weight allocation
- Platform-specific strategy (X, LinkedIn, Threads, Newsletter, etc.)
- Red lines and content boundary management

### Topic Strategy → Content Generation
- Topic backlog management with priority and pillar assignment
- Multi-platform content generation from a single topic
- Multiple hook options, CTA options, and alternative endings
- Platform-native formatting (X short + punchy, LinkedIn structured + professional)
- Bilingual output (English + Chinese) with cultural localization
- Risk scanning against brand safety rules
- Content series management (Weekly Build Log, Founder Lessons, etc.)

### Calendar → Publishing Cadence
- Weekly/monthly content calendar with platform distribution
- Pillar weight tracking (target vs actual content mix)
- Content density balance (heavy / medium / light)
- Pre-publish checklist for every content item
- Series scheduling and episode tracking

### Engagement → Growth
- Comment and DM reply generation
- Interaction classification (customer, investor, KOL, media, peer)
- Priority-based engagement queue
- Content opportunity mining from audience questions
- High-value contact tracking and follow-up suggestions

### Review → Optimization
- Performance analysis (best/worst content, patterns, platform breakdown)
- Hook pattern effectiveness analysis
- Pillar performance vs targets
- Inefficiency detection (too generic, too promotional, AI-smell)
- Next-week recommendations with specific topics
- High-performing content recycling candidates

## Installation

### Option 1: Clone the full repo

```bash
git clone https://github.com/LeonFJR/opc-skills.git ~/.claude/skills/opc-skills
```

### Option 2: Copy just this skill

```bash
cp -r opc-skills/opc-social-media-manager ~/.claude/skills/opc-social-media-manager
```

### Option 3: Add to Claude Code settings

```json
{
  "skills": ["path/to/opc-skills/opc-social-media-manager"]
}
```

## Usage Examples

### Set up brand and content strategy
> "I'm a solo founder building an AI invoice tool for freelancers. Set up my social media strategy."

### Generate content from a topic
> "Write a post about why I chose to build for freelancers instead of enterprises"

### Plan the week
> "Plan my content calendar for this week"

### Repurpose content across platforms
> "Turn this X thread into a LinkedIn post and a newsletter section"

### Handle engagement
> "Someone asked 'How is this different from FreshBooks?' — help me reply"

### Review performance
> "Here are my stats from last week: [paste metrics]. What worked?"

### Quick dashboard
> "Show me my social media dashboard"

## Archive Structure

```
social/
├── INDEX.json
├── my-brand/
│   ├── brand-profile.md        # Brand voice + strategy document
│   ├── metadata.json           # All structured data
│   └── content/
│       ├── 2026-03-17_postgres-choice.md
│       └── 2026-03-18_freelancer-market.md
```

## Skill Architecture

```
opc-social-media-manager/
├── SKILL.md                    # Core workflow (7 modes)
├── README.md                   # This file
├── LICENSE                     # MIT
├── references/
│   ├── platform-guide.md       # Platform rules, formats, repurposing matrix
│   ├── content-frameworks.md   # Pillars, hooks, CTAs, topic generation, series
│   └── brand-safety-guide.md   # Risk control, prohibited claims, compliance
├── templates/
│   ├── social-metadata-schema.json  # JSON schema for all data objects
│   ├── brand-profile.md        # Brand voice + strategy output
│   ├── content-calendar.md     # Weekly calendar template
│   ├── content-post.md         # Multi-platform post output
│   ├── engagement-queue.md     # Reply queue and follow-ups
│   └── content-review.md       # Weekly performance review
└── scripts/
    └── social_tracker.py       # CLI: index, status, calendar, backlog, review, engagement
```

## Requirements

- Claude Code CLI
- Python 3.8+ (stdlib only — no pip install needed)

## What This Skill Is NOT

- **Not a posting tool** — doesn't connect to social media APIs or schedule posts
- **Not an analytics platform** — doesn't pull metrics automatically (you input them)
- **Not a design tool** — doesn't create images, carousels, or videos
- **Not an ad manager** — doesn't manage paid campaigns or budgets
- **Not a bot** — doesn't auto-engage, auto-follow, or auto-like

## When to Involve a Human Expert

- **Crisis communication**: Public PR incidents, data breaches, viral negative coverage
- **Legal/compliance**: Advertising regulations, financial claims, health claims
- **Brand overhaul**: Major repositioning affecting all channels
- **Paid strategy**: Ad campaign design, budget allocation, audience targeting
- **Visual identity**: Logo, brand colors, design system decisions

## License

MIT
