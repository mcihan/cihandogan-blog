# 🌐 PERSONAL WEBSITE SPEC DOCUMENT
## AI-Friendly Specification for Static Website Generation

---

## 1. PROJECT OVERVIEW

### Purpose
Personal portfolio and technical blog website for a Senior Software Engineer applying for UK Global Talent Visa (Exceptional Talent). The website will showcase technical articles, professional background, and thought leadership in payment systems, fintech, and AI integration.

### Target Audience
- Tech Nation assessors (primary)
- Industry professionals
- Potential employers/collaborators

### Hosting
- **Platform:** GitHub Pages (free static hosting)
- **Domain:** `<DOMAIN>.co.uk` (custom domain via GoDaddy)
- **SSL:** GitHub Pages auto-SSL (HTTPS enforced)

### Constraints
- Pure static site (NO backend, NO database, NO server-side code)
- No JavaScript frameworks (no React, Vue, Angular)
- Minimal vanilla JavaScript only (mobile menu toggle, theme)
- Must work without JavaScript enabled
- Must score 90+ on Google Lighthouse (Performance, Accessibility, SEO)

---

## 2. TECH STACK

| Layer | Technology |
|-------|------------|
| **Markup** | HTML5 (semantic) |
| **Styling** | CSS3 (custom, no frameworks) |
| **JavaScript** | Vanilla JS (minimal, optional enhancements only) |
| **Hosting** | GitHub Pages |
| **Domain** | GoDaddy DNS → GitHub Pages A Record |
| **SSL** | GitHub Pages auto-SSL |
| **Images** | WebP/PNG (optimized, max 200KB each) |
| **Fonts** | System fonts stack (no external font loading) |

### Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; /* code blocks */
```

---

## 3. SITE MAP & FILE STRUCTURE

```
<DOMAIN>.github.io/
│
├── index.html                  (Home / Landing Page)
├── about.html                  (Professional Biography)
├── blog.html                   (Articles Listing Page)
├── contact.html                (Contact Information)
│
├── articles/
│   ├── building-payment-systems-with-ai-agents.html  (Article 1)
│   └── (future articles)
│
├── assets/
│   ├── css/
│   │   └── style.css           (All styles - single file)
│   ├── images/
│   │   ├── profile.jpg          (Professional headshot)
│   │   ├── article-1-hero.png   (Article 1 hero image)
│   │   └── diagrams/
│   │       ├── architecture.png
│   │       └── flow-diagram.png
│   └── js/
│       └── main.js              (Minimal JS - mobile menu only)
│
├── favicon.ico
├── robots.txt
├── sitemap.xml
├── CNAME                        (GitHub Pages custom domain)
└── README.md
```

---

## 4. PAGE SPECIFICATIONS

---

### 4.1 HOME PAGE (index.html)

**Purpose:** First impression. Show expertise, credibility, and link to articles.

**Sections (in order):**

#### Section 1: Navigation Bar (shared across all pages)
```
[Logo: "FirstName LastName"]     [Home] [About] [Articles] [Contact]
```
- Fixed/sticky on scroll
- Mobile: hamburger menu (CSS-only or minimal JS)
- Active page highlighted
- Background: semi-transparent with blur effect

#### Section 2: Hero Section
```
┌──────────────────────────────────────────────┐
│                                              │
│   Senior Software Engineer                   │
│                                              │
│   10+ years building payment systems,        │
│   fintech solutions, and AI-powered          │
│   backend architectures                      │
│                                              │
│   📍 United Kingdom                          │
│                                              │
│   [Read Articles]  [About Me]                │
│                                              │
└──────────────────────────────────────────────┘
```
- Full-width section
- Subtle gradient background (dark blue → dark navy)
- White text
- Two CTA buttons (primary: filled, secondary: outlined)

#### Section 3: Expertise Grid
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ 🏦          │ │ 🔧          │ │ 🤖          │ │ 🌍          │
│ Payment     │ │ Backend     │ │ AI          │ │ Multi-      │
│ Systems     │ │ Engineering │ │ Integration │ │ Regional    │
│             │ │             │ │             │ │             │
│ Description │ │ Description │ │ Description │ │ Description │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```
- 4 cards in a row (desktop)
- 2 cards per row (tablet)
- 1 card per row (mobile)
- Each card: icon + title + short description
- Card content:
  1. Payment Systems: "10+ years designing payment gateways, merchant integrations, and financial infrastructure across multiple countries"
  2. Backend Engineering: "Leading 12-20 microservices architectures, system optimization, and high-performance backend solutions"
  3. AI Integration: "Production implementation of AI agents (Claude), workflow automation (n8n), and intelligent processing systems"
  4. Multi-Regional Experience: "Delivering solutions across Turkey, Middle East, Eastern Europe, and United Kingdom"

#### Section 4: Impact Statistics
```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│   10+    │ │   £1M+   │ │    3     │ │    4     │
│  Years   │ │   Cost   │ │ Regions  │ │  Years   │
│  Exp.    │ │ Savings  │ │  Served  │ │  in UK   │
└──────────┘ └──────────┘ └──────────┘ └──────────┘
```
- Centered section
- Large bold numbers
- Subtle descriptions below
- Light background color for contrast

#### Section 5: Featured Article Preview
```
┌──────────────────────────────────────────────┐
│  Latest Article                              │
│                                              │
│  ┌──────┐  Building Payment Systems with     │
│  │ IMG  │  AI Agents: A Production Case Study│
│  │      │                                    │
│  └──────┘  Brief excerpt of the article...   │
│                                              │
│            [AI] [Payments] [Backend]          │
│                                              │
│            Read Full Article →                │
└──────────────────────────────────────────────┘
```
- Article card with hero image thumbnail
- Title, date, excerpt, tags
- "Read Full Article →" link

#### Section 6: Footer (shared across all pages)
```
┌──────────────────────────────────────────────┐
│  © 2026 FirstName LastName                   │
│  Email | LinkedIn | GitHub                   │
└──────────────────────────────────────────────┘
```
- Dark background
- Social links (LinkedIn, GitHub, Email)
- Copyright notice

---

### 4.2 ABOUT PAGE (about.html)

**Purpose:** Professional biography showing career trajectory, expertise, and credibility.

**Sections:**

#### Section 1: About Header
```
┌──────────────────────────────────────────────┐
│                                              │
│  ┌──────────┐                                │
│  │ PROFILE  │  FirstName LastName            │
│  │  PHOTO   │  Senior Software Engineer      │
│  │          │  📍 United Kingdom              │
│  └──────────┘  ✉️ hello@<DOMAIN>.co.uk       │
│                                              │
└──────────────────────────────────────────────┘
```
- Profile photo (professional headshot, 200x200px, rounded)
- Name, title, location, email

#### Section 2: Professional Summary
- 2-3 paragraphs about career focus
- Key themes: payment systems, backend engineering, AI integration
- Mention UK-based, international experience

#### Section 3: Career Timeline
```
┌─ 2022-Present ──────────────────────────────┐
│  Senior Software Engineer | UK Fintech      │
│  • Led DB2→MySQL migration (£1M savings)    │
│  • 12-20 microservices leadership           │
│  • AI agent integration (Claude, n8n)       │
│  • PCI compliance & payment systems         │
└─────────────────────────────────────────────┘
        │
┌─ 2021-2022 ─────────────────────────────────┐
│  Senior Software Engineer | Siemens, Turkey │
│  • Enterprise-scale software development    │
└─────────────────────────────────────────────┘
        │
┌─ 2018-2021 ─────────────────────────────────┐
│  Senior Engineer | Fintech Company, Turkey  │
│  • Payment gateway architecture             │
│  • Multi-region deployment (3+ regions)     │
│  • 3DS/ACS, UnionPay, PayPal integration    │
└─────────────────────────────────────────────┘
        │
┌─ 2015-2018 ─────────────────────────────────┐
│  Backend Engineer | StartUp, Turkey         │
│  • Mobile payment app for banking sector    │
└─────────────────────────────────────────────┘
```
- Vertical timeline layout
- Left-aligned with connector lines
- Each entry: date range, company, role, bullet points
- Most recent at top

#### Section 4: Technical Skills
```
┌─────────────────┐ ┌─────────────────┐
│ Languages &     │ │ Domains         │
│ Frameworks      │ │                 │
│ • Java          │ │ • Payment       │
│ • Spring Boot   │ │   Systems       │
│ • Spring Cloud  │ │ • Fintech       │
│ • Microservices │ │ • PCI DSS       │
│ • REST & gRPC   │ │ • Fraud         │
│ • SQL           │ │   Detection     │
└─────────────────┘ └─────────────────┘
┌─────────────────┐ ┌─────────────────┐
│ AI & Modern     │ │ Leadership      │
│ Tech            │ │                 │
│ • Claude AI     │ │ • Architecture  │
│ • n8n           │ │   Design        │
│ • LLM           │ │ • Team          │
│   Integration   │ │   Leadership    │
│ • Workflow      │ │ • Mentoring     │
│   Automation    │ │ • Technical     │
│                 │ │   Decisions     │
└─────────────────┘ └─────────────────┘
```
- 4 skill category cards (2x2 grid)
- Clean list format

#### Section 5: Education & Certifications
```
🎓 Education:
  • Bachelor's Degree: Computer Science
  • Master's Degree: Management Information Systems

📜 Certifications:
  • Oracle Java 11 Professional
  • Scrum Master 1 & 2
  • Product Owner 1
```
- Simple list format
- Icons for visual distinction

---

### 4.3 BLOG PAGE (blog.html)

**Purpose:** List all published articles with preview cards.

**Sections:**

#### Section 1: Page Header
```
┌──────────────────────────────────────────────┐
│  Technical Articles                          │
│  In-depth articles on payment systems,       │
│  backend engineering, and AI integration     │
│  based on real-world production experience   │
└──────────────────────────────────────────────┘
```

#### Section 2: Articles List
```
┌──────────────────────────────────────────────┐
│  ┌──────┐                                    │
│  │ IMG  │  Building Payment Systems with     │
│  │      │  AI Agents: A Production Case Study│
│  │      │                                    │
│  └──────┘  📅 May 1, 2026 | ⏱️ 8 min read   │
│                                              │
│            Real-world case study on          │
│            integrating Claude AI agents      │
│            and n8n into a fintech payment    │
│            system. Achieved 70% automation   │
│            and £1M annual cost savings...    │
│                                              │
│            [AI Agents] [Payments] [Backend]  │
│                                              │
│            Read Full Article →               │
└──────────────────────────────────────────────┘
```
- Each article: horizontal card (image left, content right)
- Mobile: stack vertically (image top, content bottom)
- Tags as colored badges
- Reading time estimate

---

### 4.4 ARTICLE PAGE (articles/building-payment-systems-with-ai-agents.html)

**Purpose:** Full technical article showcasing thought leadership.

**Layout:**
```
┌──────────────────────────────────────────────┐
│  Building Payment Systems with AI Agents:    │
│  A Production Case Study                     │
│                                              │
│  📅 May 1, 2026 | ⏱️ 8 min read             │
│  Tags: [AI Agents] [Payment Systems]         │
│         [Backend] [n8n] [Claude AI]          │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │         HERO IMAGE                   │    │
│  │    (Architecture Diagram)            │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  ## Introduction                             │
│  <article text>                              │
│                                              │
│  ## The Challenge                            │
│  <article text>                              │
│                                              │
│  ## Architecture Overview                    │
│  <article text + diagram image>              │
│                                              │
│  ## Implementation                           │
│  <article text + code blocks>                │
│                                              │
│  ## Results & Metrics                        │
│  <article text + metrics table>              │
│                                              │
│  ## Lessons Learned                          │
│  <article text>                              │
│                                              │
│  ## Conclusion                               │
│  <article text>                              │
│                                              │
│  ─────────────────────────────────           │
│  About the Author                            │
│  [Profile pic] FirstName LastName            │
│  Senior Software Engineer | UK              │
│  [LinkedIn] [GitHub]                         │
└──────────────────────────────────────────────┘
```

**Article Content Structure:**
- Max width: 720px (optimal reading width)
- Typography: 18px base, 1.8 line-height
- Code blocks: syntax highlighted (CSS-only, dark theme)
- Images: full-width within content area
- Tables: clean bordered style
- Blockquotes: left-bordered, italic

**Article Placeholder Content:**
```
Title: "Building Payment Systems with AI Agents: A Production Case Study"
Date: May 1, 2026
Reading Time: 8 minutes
Tags: AI Agents, Payment Systems, Backend Architecture, n8n, Claude AI

Sections:
1. Introduction (250 words)
   - Context: Why AI in payment systems?
   - Problem statement
   - What this article covers

2. The Challenge (300 words)
   - Legacy system limitations
   - Manual workflow bottlenecks
   - Scale requirements
   - PCI compliance constraints

3. Architecture Overview (400 words)
   - System design diagram
   - Microservices topology
   - AI agent placement
   - n8n workflow design
   - Data flow explanation

4. Implementation Details (600 words)
   - Claude agent configuration
   - n8n workflow setup
   - Integration patterns
   - Error handling strategy
   - Testing approach
   - Code examples (anonymized)

5. Database Migration: DB2 to MySQL (400 words)
   - Migration strategy
   - Custom tooling built
   - PCI compliance during migration
   - Zero-downtime approach
   - Validation methodology

6. Results & Metrics (300 words)
   - £1M annual cost savings
   - 70% workflow automation
   - Performance improvements (before/after)
   - Reliability metrics
   - Team adoption rate
   - Company-wide methodology spread

7. Lessons Learned (250 words)
   - What worked well
   - What we'd do differently
   - Best practices for AI in fintech
   - Recommendations

8. Conclusion (150 words)
   - Summary
   - Future outlook
   - Call to action

Total: ~2,650 words
```

---

### 4.5 CONTACT PAGE (contact.html)

**Purpose:** Simple contact information.

**Layout:**
```
┌──────────────────────────────────────────────┐
│  Get In Touch                                │
│                                              │
│  ✉️  hello@<DOMAIN>.co.uk                    │
│  🔗  linkedin.com/in/<USERNAME>              │
│  🐙  github.com/<USERNAME>                   │
│  📍  United Kingdom                          │
│                                              │
│  I'm always open to discussing payment      │
│  systems, backend architecture, and AI       │
│  integration opportunities.                  │
└──────────────────────────────────────────────┘
```
- No contact form needed (static site)
- Direct email link (mailto:)
- Social media links
- Brief message

---

## 5. DESIGN SPECIFICATIONS

### 5.1 Color Palette

```css
:root {
    /* Primary Colors */
    --color-primary: #2563EB;        /* Blue - links, buttons, accents */
    --color-primary-dark: #1D4ED8;   /* Darker blue - hover states */
    --color-primary-light: #DBEAFE;  /* Light blue - backgrounds */

    /* Neutral Colors */
    --color-bg: #FFFFFF;             /* White - main background */
    --color-bg-alt: #F8FAFC;         /* Off-white - alternate sections */
    --color-bg-dark: #1E293B;        /* Dark slate - header/footer */
    --color-text: #334155;           /* Dark gray - body text */
    --color-text-light: #64748B;     /* Medium gray - secondary text */
    --color-text-dark: #0F172A;      /* Near black - headings */
    --color-border: #E2E8F0;         /* Light gray - borders */

    /* Accent Colors */
    --color-success: #10B981;        /* Green - stats, highlights */
    --color-warning: #F59E0B;        /* Amber - tags */
    --color-code-bg: #1E293B;        /* Dark - code blocks */
    --color-code-text: #E2E8F0;      /* Light - code text */
}
```

### 5.2 Typography

```css
/* Headings */
h1 { font-size: 2.5rem; font-weight: 800; line-height: 1.2; color: var(--color-text-dark); }
h2 { font-size: 2rem; font-weight: 700; line-height: 1.3; color: var(--color-text-dark); }
h3 { font-size: 1.5rem; font-weight: 600; line-height: 1.4; color: var(--color-text-dark); }
h4 { font-size: 1.25rem; font-weight: 600; line-height: 1.4; color: var(--color-text-dark); }

/* Body */
p { font-size: 1.125rem; line-height: 1.8; color: var(--color-text); }

/* Article body - slightly larger for readability */
.blog-post p { font-size: 1.175rem; line-height: 1.9; }

/* Code blocks */
pre, code { font-size: 0.9rem; line-height: 1.6; }
```

### 5.3 Spacing System

```css
/* Spacing scale */
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
--space-4xl: 6rem;     /* 96px */

/* Container */
--container-max: 1200px;     /* Main container */
--article-max: 720px;        /* Article content width */
--container-padding: 1.5rem; /* Side padding */
```

### 5.4 Responsive Breakpoints

```css
/* Mobile first approach */
/* Base: 0-767px (mobile) */
@media (min-width: 768px)  { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Large desktop */ }
```

### 5.5 Component Styles

#### Buttons
```css
.btn-primary {
    background: var(--color-primary);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    font-weight: 600;
    transition: background 0.2s;
}
.btn-primary:hover {
    background: var(--color-primary-dark);
}

.btn-secondary {
    background: transparent;
    color: var(--color-primary);
    border: 2px solid var(--color-primary);
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    font-weight: 600;
    transition: all 0.2s;
}
.btn-secondary:hover {
    background: var(--color-primary);
    color: white;
}
```

#### Cards
```css
.card {
    background: var(--color-bg);
    border: 1px solid var(--color-border);
    border-radius: 0.75rem;
    padding: 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    transition: box-shadow 0.2s;
}
.card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
```

#### Tags/Badges
```css
.tag {
    display: inline-block;
    background: var(--color-primary-light);
    color: var(--color-primary);
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.875rem;
    font-weight: 500;
}
```

#### Code Blocks
```css
pre {
    background: var(--color-code-bg);
    color: var(--color-code-text);
    padding: 1.5rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

code {
    font-family: var(--font-mono);
}

/* Inline code */
p code {
    background: var(--color-bg-alt);
    color: var(--color-primary-dark);
    padding: 0.15rem 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.9em;
}
```

---

## 6. SEO & META TAGS

### 6.1 Meta Tags (every page)

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[PAGE_SPECIFIC_DESCRIPTION]">
    <meta name="author" content="FirstName LastName">
    <meta name="keywords" content="software engineer, payment systems, fintech, AI, backend, UK">
    
    <!-- Open Graph (Social sharing) -->
    <meta property="og:title" content="[PAGE_TITLE]">
    <meta property="og:description" content="[PAGE_DESCRIPTION]">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://<DOMAIN>.co.uk/[PAGE_PATH]">
    <meta property="og:image" content="https://<DOMAIN>.co.uk/assets/images/og-image.png">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="[PAGE_TITLE]">
    <meta name="twitter:description" content="[PAGE_DESCRIPTION]">
    
    <title>[PAGE_TITLE] | FirstName LastName</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="icon" href="favicon.ico">
</head>
```

### 6.2 Page-Specific Meta Descriptions

| Page | Title | Description |
|------|-------|-------------|
| Home | "FirstName LastName - Senior Software Engineer" | "Senior Software Engineer specializing in payment systems, fintech, and AI integration. 10+ years experience. Based in the United Kingdom." |
| About | "About - FirstName LastName" | "Professional background, career trajectory, and technical expertise of FirstName LastName. 10+ years in payment systems and backend engineering." |
| Blog | "Technical Articles - FirstName LastName" | "In-depth technical articles on payment systems, backend engineering, AI integration, and fintech solutions." |
| Article 1 | "Building Payment Systems with AI Agents" | "Real-world case study on integrating AI agents into fintech payment systems. Production implementation with Claude AI and n8n." |
| Contact | "Contact - FirstName LastName" | "Get in touch with FirstName LastName for discussions on payment systems, backend architecture, and AI integration." |

### 6.3 robots.txt

```
User-agent: *
Allow: /
Sitemap: https://<DOMAIN>.co.uk/sitemap.xml
```

### 6.4 sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://<DOMAIN>.co.uk/</loc>
    <lastmod>2026-05-01</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://<DOMAIN>.co.uk/about.html</loc>
    <lastmod>2026-05-01</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://<DOMAIN>.co.uk/blog.html</loc>
    <lastmod>2026-05-01</lastmod>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://<DOMAIN>.co.uk/articles/building-payment-systems-with-ai-agents.html</loc>
    <lastmod>2026-05-01</lastmod>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://<DOMAIN>.co.uk/contact.html</loc>
    <lastmod>2026-05-01</lastmod>
    <priority>0.5</priority>
  </url>
</urlset>
```

### 6.5 CNAME File

```
<DOMAIN>.co.uk
```

---

## 7. JAVASCRIPT SPECIFICATIONS

### 7.1 main.js (Minimal)

**Only these features:**

```javascript
// 1. Mobile hamburger menu toggle
// 2. Smooth scroll for anchor links (optional)
// 3. Active nav link highlighting based on current page

// NO: Analytics, tracking, frameworks, libraries, CDN dependencies
// Site MUST work fully without JavaScript enabled
```

---

## 8. PLACEHOLDER VALUES TO REPLACE

**Before publishing, replace these placeholders:**

| Placeholder | Replace With |
|-------------|-------------|
| `FirstName LastName` | Your full name |
| `<DOMAIN>` | Your domain name (without .co.uk) |
| `<USERNAME>` | Your LinkedIn/GitHub username |
| `hello@<DOMAIN>.co.uk` | Your contact email |
| `profile.jpg` | Your professional headshot |
| `article-1-hero.png` | Your article hero image |
| `architecture.png` | Your architecture diagram |
| `flow-diagram.png` | Your flow diagram |
| Career dates | Your actual career dates |
| Company names | Your actual company names (or anonymized) |
| Article content | Your actual article text |

---

## 9. PERFORMANCE REQUIREMENTS

### 9.1 Google Lighthouse Targets

| Metric | Target |
|--------|--------|
| Performance | 90+ |
| Accessibility | 95+ |
| Best Practices | 95+ |
| SEO | 95+ |

### 9.2 Performance Rules

- Total page size: < 500KB (including images)
- Images: Optimized WebP/PNG, max 200KB each
- CSS: Single file, minified for production
- JS: Single file, < 5KB
- No external CDN dependencies
- No external font loading (system fonts only)
- No third-party scripts (no analytics, no tracking)
- Lazy loading for below-fold images

### 9.3 Accessibility Rules

- All images: `alt` text required
- Color contrast: WCAG AA minimum
- Keyboard navigation: Full support
- Semantic HTML: `<nav>`, `<main>`, `<article>`, `<section>`, `<header>`, `<footer>`
- ARIA labels where needed
- Skip to main content link
- Focus styles visible

---

## 10. OUTPUT FILES

**AI should generate these exact files:**

```
Files to create:
1.  index.html
2.  about.html
3.  blog.html
4.  contact.html
5.  articles/building-payment-systems-with-ai-agents.html
6.  assets/css/style.css
7.  assets/js/main.js
8.  robots.txt
9.  sitemap.xml
10. CNAME
11. README.md
```

**Total: 11 files**

---

## 11. VISUAL REFERENCE (Wireframes)

### Desktop Layout (1200px)
```
┌────────────────────────────────────────────────────────┐
│  [Logo]              [Home] [About] [Articles] [Contact]│
├────────────────────────────────────────────────────────┤
│                                                        │
│              Senior Software Engineer                  │
│     10+ years building payment systems...              │
│         [Read Articles]  [About Me]                    │
│                                                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐              │
│  │Pay-  │  │Back- │  │AI    │  │Multi-│              │
│  │ment  │  │end   │  │Integ.│  │Region│              │
│  │Sys.  │  │Eng.  │  │      │  │      │              │
│  └──────┘  └──────┘  └──────┘  └──────┘              │
│                                                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│     10+        £1M+         3           4              │
│    Years     Savings     Regions     UK Years          │
│                                                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Latest Article                                        │
│  ┌────┐ Building Payment Systems with AI Agents...     │
│  │IMG │ Brief excerpt...                               │
│  └────┘ [AI] [Payments] → Read More                    │
│                                                        │
├────────────────────────────────────────────────────────┤
│  © 2026 FirstName LastName | Email | LinkedIn | GitHub │
└────────────────────────────────────────────────────────┘
```

### Mobile Layout (375px)
```
┌──────────────────┐
│ [Logo]      [☰]  │
├──────────────────┤
│                  │
│  Senior Software │
│    Engineer      │
│                  │
│  10+ years...    │
│                  │
│ [Read Articles]  │
│ [About Me]       │
│                  │
├──────────────────┤
│ ┌──────────────┐ │
│ │Payment Sys.  │ │
│ └──────────────┘ │
│ ┌──────────────┐ │
│ │Backend Eng.  │ │
│ └──────────────┘ │
│ ┌──────────────┐ │
│ │AI Integr.    │ │
│ └──────────────┘ │
│ ┌──────────────┐ │
│ │Multi-Region  │ │
│ └──────────────┘ │
├──────────────────┤
│  10+     £1M+    │
│  Years   Savings │
│                  │
│   3        4     │
│ Regions  UK Yrs  │
├──────────────────┤
│ Latest Article   │
│ ┌──────────────┐ │
│ │     IMG      │ │
│ └──────────────┘ │
│ Title...         │
│ Excerpt...       │
│ Read More →      │
├──────────────────┤
│ © 2026 FN LN    │
│ Email|LI|GH     │
└──────────────────┘
```

---

## 12. QUALITY CHECKLIST

**Before deployment, verify:**

### HTML
- [ ] All pages valid HTML5
- [ ] Semantic tags used correctly
- [ ] All links working
- [ ] All images have alt text
- [ ] Meta tags on every page
- [ ] Open Graph tags on every page
- [ ] Favicon linked
- [ ] Mobile viewport meta tag

### CSS
- [ ] Mobile-first responsive design
- [ ] All breakpoints working (mobile, tablet, desktop)
- [ ] Consistent spacing and typography
- [ ] Color contrast WCAG AA compliant
- [ ] No horizontal scrolling on any viewport
- [ ] Print styles (optional)
- [ ] Dark mode support (optional, bonus)

### Content
- [ ] All placeholder text replaced
- [ ] No lorem ipsum
- [ ] All links point to correct pages
- [ ] Contact email correct
- [ ] Social links correct
- [ ] Copyright year correct

### Performance
- [ ] Total page < 500KB
- [ ] Images optimized
- [ ] Single CSS file
- [ ] Minimal JS
- [ ] No external dependencies
- [ ] Lazy loading for images

### SEO
- [ ] sitemap.xml valid
- [ ] robots.txt correct
- [ ] CNAME file present
- [ ] Meta descriptions unique per page
- [ ] Page titles unique per page

### Accessibility
- [ ] Keyboard navigation works
- [ ] Focus styles visible
- [ ] Skip to main content link
- [ ] ARIA labels where needed
- [ ] Screen reader friendly

---

## 13. DEPLOYMENT STEPS

```
1. Create GitHub repository: <USERNAME>.github.io
2. Push all files to main branch
3. GitHub Settings → Pages → Source: main branch
4. GitHub Settings → Pages → Custom domain: <DOMAIN>.co.uk
5. GoDaddy DNS → A Record: @ → 185.199.108.153 (TTL: 3600)
6. Wait 5-30 minutes for DNS propagation
7. GitHub Settings → Pages → Enforce HTTPS ✅
8. Test: https://<DOMAIN>.co.uk
9. Run Google Lighthouse audit
10. Verify all pages and links
```

---

## 14. FUTURE EXPANSION (OPTIONAL)

**If time permits, add these pages/features:**

1. **Article 2:** "REST to gRPC Migration: Performance Gains in Payment Systems"
2. **Article 3:** "PCI-Compliant Database Migration: A Step-by-Step Guide"
3. **Projects page:** Showcase key projects with case studies
4. **Dark mode toggle:** CSS custom properties + JS toggle
5. **Reading progress bar:** For article pages
6. **Print stylesheet:** Clean print layout for articles

---

**END OF SPECIFICATION**

*This document is designed to be AI-friendly. Copy the entire content and provide it to any AI code generator (Claude, ChatGPT, Copilot) with the instruction: "Generate all files according to this specification."*
