# Conversion Optimization

> Reference for maximizing landing page conversion rates.
> Load with `read_file("references/conversion-optimization.md")` during Strategy and Review phases.

---

## Conversion Goal Types

| Goal | Metric | Typical CTA |
|------|--------|-------------|
| **Email capture** | Signups | "Get early access" / "Join the waitlist" |
| **Free trial** | Trial starts | "Start your free trial" |
| **Purchase** | Transactions | "Buy now" / "Get started" |
| **Demo request** | Demo bookings | "Book a demo" / "Schedule a call" |
| **Download** | Downloads | "Download free" / "Get the guide" |
| **Contact** | Inquiry submissions | "Get in touch" / "Request a quote" |

**For solo entrepreneurs launching new products**: Email capture or free trial. Don't ask for money from cold traffic on a brand-new product.

---

## Conversion Principles

### 1. One Page, One Goal

- A landing page has **one** conversion goal
- Every section should move the visitor toward that goal
- Remove anything that doesn't serve the goal (nav links to blog, multiple offers, etc.)
- If you need multiple goals, create multiple pages

### 2. Reduce Friction

| Friction Source | Fix |
|----------------|-----|
| Too many form fields | Name + email only. Ask the rest later. |
| Unclear CTA | Use action-specific text: "Start my trial" not "Submit" |
| No trust signals | Add testimonials, security badges, guarantee |
| Price shock | Anchor with annual pricing, show per-day cost |
| Decision fatigue | Reduce choices to 2-3 options maximum |
| Slow loading | Optimize images, minimize scripts |

### 3. Social Proof Hierarchy

From strongest to weakest:

1. **Specific results** — "Increased revenue by 40% in 3 months"
2. **Named testimonials with photos** — Real people, real roles
3. **User count** — "Join 10,000+ founders"
4. **Client logos** — Recognizable brand names
5. **Ratings** — "4.9/5 on G2" or star ratings
6. **Media mentions** — "As seen in TechCrunch"
7. **Generic praise** — "Great product!" (weakest — avoid)

**If you have no social proof yet**: Use a "beta" or "early access" frame. Don't fabricate testimonials.

### 4. Risk Reversal

Reduce the perceived risk of taking action:

| Risk | Reversal |
|------|----------|
| "What if I don't like it?" | Money-back guarantee |
| "What if it's too complex?" | "Set up in 5 minutes" |
| "Will I get locked in?" | "Cancel anytime, no questions asked" |
| "Is my data safe?" | Security badges, privacy statement |
| "Is this legit?" | Testimonials, company info, founder story |
| "What if I need help?" | "Free support included" |

### 5. Urgency and Scarcity (Use Honestly)

**Legitimate urgency**:
- Limited-time launch pricing
- Cohort-based enrollment with real deadlines
- Genuinely limited spots (small group coaching)
- Seasonal relevance (tax tools before tax season)

**Never fabricate**:
- Fake countdown timers that reset
- "Only 3 left!" when supply is unlimited
- Artificial "limited time" on evergreen products

---

## Above-the-Fold Optimization

### The 5-Second Test

A visitor decides to stay or leave within 5 seconds. Above the fold must pass:

1. **Clarity test** — Can I tell what this product does?
2. **Relevance test** — Is this for me?
3. **Value test** — Why should I care?
4. **Action test** — What do I do next?

### Headline Optimization

| Weak | Strong | Why |
|------|--------|-----|
| "Welcome to our platform" | "Send invoices that get paid 2x faster" | Specific outcome |
| "The best project management tool" | "Finish projects on time without the chaos" | Benefit, not claim |
| "Next-generation AI solution" | "Write your marketing copy in 5 minutes" | Concrete result |
| "We help businesses grow" | "10,000 founders use this to get their first 100 customers" | Social proof + specificity |

### CTA Button Optimization

| Element | Best Practice |
|---------|--------------|
| Color | High contrast against background. Not the same color as other elements. |
| Size | Large enough to be obvious, not so large it looks desperate |
| Text | Action verb + benefit: "Start my free trial" |
| Position | Visible without scrolling |
| Surrounding space | Whitespace around the button — don't crowd it |
| Sub-CTA text | Risk reversal: "No credit card required" directly below button |

---

## Form Optimization

### Field Reduction

Every additional field reduces conversion by ~10%. Minimum viable form:

| Goal | Fields Needed |
|------|---------------|
| Email capture | Email only |
| Free trial | Email + password (or just email with magic link) |
| Demo booking | Name + email + company |
| Purchase | Email + payment (use Stripe/payment processor) |

### Form Placement

- **Above the fold** for email captures
- **After value demonstration** for trials/purchases
- **Inline with the CTA section** — don't link to a separate page

---

## Page Speed Impact

| Load Time | Bounce Rate Increase |
|-----------|---------------------|
| 1-3 seconds | Baseline |
| 3-5 seconds | +32% |
| 5-6 seconds | +90% |
| 6-10 seconds | +106% |
| 10+ seconds | +123% |

### Speed Optimization for Self-Contained Pages

- **Inline CSS** — no external stylesheets to fetch
- **Minimize images** — use CSS gradients, SVG icons where possible
- **Lazy load below-fold images** — `loading="lazy"` attribute
- **System fonts first** — use web fonts only if brand requires it
- **No external JS** unless essential (analytics, payment processor)
- **Compress images** — use appropriate format (WebP where supported)

---

## Mobile Optimization Checklist

- [ ] Touch targets ≥ 44×44px
- [ ] Body text ≥ 16px
- [ ] Headlines scale down appropriately
- [ ] Single-column layout below 768px
- [ ] CTA buttons full-width on mobile
- [ ] No horizontal scrolling
- [ ] Forms are usable with mobile keyboard
- [ ] Images don't break layout on small screens
- [ ] Sticky CTA or floating action button on mobile
- [ ] Navigation is minimal (logo + CTA, or hamburger)

---

## Pre-Launch Page Optimization

For products not yet ready — optimize the waitlist/early access page:

### Waitlist Page Must-Haves

1. **Clear value proposition** — what will this be?
2. **Email capture form** — just email, no other fields
3. **Expected timeline** — "Launching Q2 2026" or "Join 500 others waiting"
4. **Social proof if available** — beta user count, advisor logos
5. **Teaser** — screenshot mockup, feature preview, or demo video

### Waitlist Optimization

- Offer incentive: "Early access members get 50% off"
- Show momentum: "432 people on the waitlist"
- Set expectations: "We'll email you once, when we launch"
- Shareable: "Share with a friend" referral after signup

---

## Post-Build Checklist

Before considering the landing page "done", verify:

### Content
- [ ] Headline passes the 5-second clarity test
- [ ] Subheadline adds specificity (who it's for, what outcome)
- [ ] Every section serves the one conversion goal
- [ ] No jargon — a non-technical friend would understand this
- [ ] CTA text is action-specific (not "Submit" or "Click here")
- [ ] Social proof is specific and credible (or absent if none available)
- [ ] FAQ addresses top 3-5 objections

### Design
- [ ] Visual hierarchy guides the eye: headline → subheadline → CTA
- [ ] One dominant CTA color — no competing visual weights
- [ ] Adequate whitespace — sections breathe
- [ ] Consistent typography (max 2 font families)
- [ ] Images are relevant and high-quality (or omitted)

### Technical
- [ ] Loads in < 3 seconds
- [ ] Responsive on mobile, tablet, desktop
- [ ] CTA links/forms work correctly
- [ ] Open Graph / social sharing meta tags are set
- [ ] Page title and meta description are set for SEO
- [ ] Favicon is set
- [ ] Analytics tracking is in place (or placeholder ready)

### Legal (For Solo Entrepreneurs)
- [ ] Privacy policy link (if collecting data)
- [ ] Terms of service link (if selling something)
- [ ] Cookie notice (if applicable to jurisdiction)
- [ ] No false claims or fabricated testimonials

---

## A/B Testing Priorities

When iterating, test these elements in order of impact:

1. **Headline** — biggest impact on above-fold conversion
2. **CTA text** — directly affects click-through
3. **Social proof placement** — where and what type
4. **Hero image vs. no image** — sometimes less is more
5. **Form fields** — fewer almost always wins
6. **Pricing display** — monthly vs annual, price anchoring
7. **Page length** — long-form vs. short-form

**For solo entrepreneurs without traffic for real A/B testing**: Generate 2-3 copy variants and test manually with your target audience. The skill can generate variants in Iterate mode.

---

*Reference for opc-landing-page-manager.*
