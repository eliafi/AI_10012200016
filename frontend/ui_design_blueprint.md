# Academic City RAG Chatbot — UI Design Blueprint

## 1. Exam Requirements Analysis

From the exam paper (CS4241), the UI **must** support these features:

| Feature | Exam Reference | Priority |
|:---|:---|:---|
| **Query input** | Part D, Final Deliverables | Critical |
| **Display retrieved chunks** | Part D, Final Deliverables | Critical |
| **Show similarity scores** | Part D | Critical |
| **Show final response** | Part D, Final Deliverables | Critical |
| **Display final prompt sent to LLM** | Part D | High |
| **Pipeline stage logging** | Part D | High |
| **Adversarial query testing** | Part E | Nice |
| **RAG vs Pure LLM comparison** | Part E | Nice |

### Backend API Response Shape (from `main.py`)
```json
{
  "run_id": "...",
  "query": "...",
  "retrieved_documents": [...],
  "context_selection": {...},
  "final_prompt_sent_to_llm": "...",
  "response": "...",
  "stage_times": {...},
  "run_log_path": "..."
}
```

---

## 2. Design Philosophy

### Theme: **"Ghana Civic Premium" — Black Star Dark Mode**

A premium dark interface rooted in **Ghanaian national identity**. The near-black background represents the **Black Star** — Ghana's symbol of freedom and African emancipation. Accent colors are desaturated, dark-mode-friendly renditions of the **Ghana national flag** (Red, Gold, Green). Surface elements use **"Transparent Ballot Box Glass"** — a glassmorphism metaphor inspired by Ghana's Electoral Commission, conveying transparency and civic trust.

### Core Principles
- **Civic authority**: The UI should feel like an official government/university portal
- **Focus-oriented**: Chat is the hero — everything else is secondary
- **Progressive disclosure**: Chunks, scores, and pipeline logs revealed on demand
- **Micro-animations**: Subtle feedback for every interaction
- **Mobile-first, fully responsive**: Designed for phone screens first — every feature must work perfectly on mobile. Desktop is an enhancement, not the baseline.

### UI Motifs
- **Black Star Motif**: A large, subtle, low-opacity (`0.03–0.05`) five-pointed star watermark on the page background or app header, evoking the Black Star of Africa
- **Transparent Ballot Box Glass**: All glassmorphism cards use frosted transparency as a metaphor for electoral/civic transparency — clear governance through clear data

---

## 3. Color Palette

### Black Star Backgrounds

| Token | Hex | Usage |
|:---|:---|:---|
| `--bg-deep` | `#0B0F1A` | Page background — "Black Star" near-black |
| `--bg-surface` | `#111827` | Card/panel backgrounds |
| `--bg-elevated` | `#1E293B` | Elevated surfaces, hover states |
| `--bg-glass` | `rgba(30, 41, 59, 0.55)` | Transparent Ballot Box Glass panels |
| `--border-subtle` | `rgba(148, 163, 184, 0.12)` | Subtle borders |
| `--border-glass` | `rgba(252, 209, 22, 0.08)` | Gold-tinted glass card borders |

### Ghana National Accents

| Token | Hex | Origin | Usage |
|:---|:---|:---|:---|
| `--ghana-gold` | `#FCD116` | Flag Gold | **Primary accent** — buttons, focus rings, hero gradient, active states |
| `--ghana-gold-muted` | `#D4A017` | Desaturated gold | Hover states, secondary gold uses |
| `--ghana-red` | `#CE1126` | Flag Red | Critical highlights, low similarity scores, errors, warnings |
| `--ghana-red-muted` | `#A30E1F` | Desaturated red | Hover/pressed states for destructive actions |
| `--ghana-green` | `#006B3F` | Flag Green | Success states, high similarity scores, positive feedback |
| `--ghana-green-bright` | `#00895A` | Brightened green | Text-on-dark legibility variant |
| `--accent-star` | `#F1F5F9` | Black Star (inverted) | Star watermark, premium icon highlights |

### Text Colors

| Token | Hex | Usage |
|:---|:---|:---|
| `--text-primary` | `#F1F5F9` | Primary text (off-white) |
| `--text-secondary` | `#94A3B8` | Secondary text, labels |
| `--text-muted` | `#64748B` | Muted text, timestamps |
| `--text-gold` | `#FCD116` | Links, interactive text, active nav items |

### Gradient Accents

```css
/* Hero gradient — Ghana tricolour sweep for header/branding areas */
--gradient-brand: linear-gradient(135deg, #CE1126 0%, #FCD116 50%, #006B3F 100%);

/* Subtle background glow — warm gold radiance from top */
--gradient-glow: radial-gradient(ellipse at top, rgba(252, 209, 22, 0.10), transparent 60%);

/* RAG similarity score bar — maps Red→Gold→Green (bad→ok→good) */
--gradient-score: linear-gradient(90deg, #CE1126, #FCD116, #006B3F);

/* Gold shimmer for premium elements */
--gradient-gold-shimmer: linear-gradient(90deg, #D4A017, #FCD116, #D4A017);
```

---

## 4. Typography

| Element | Font | Weight | Size (Desktop) | Size (Mobile) | Notes |
|:---|:---|:---|:---|:---|:---|
| App title | **Inter** | 800 | 24px | 18px | `letter-spacing: 0.08em; text-transform: uppercase;` |
| Section headers | **Inter** | 700 | 18px | 15px | |
| Body text | **Inter** | 400 | 15px | 14px | |
| Chat messages | **Inter** | 400 | 15px | 14px | |
| Code/prompt | **JetBrains Mono** | 400 | 13px | 12px | |
| Badges/labels | **Inter** | 600 | 11px | 10px | |
| Timestamps | **Inter** | 400 | 12px | 11px | |

Load via `next/font/google` (not CDN) for optimal performance with Next.js.

---

## 5. Responsive Layout Strategy

> **REQUIREMENT: Every layout, component, and feature MUST be fully functional and visually correct on all screen sizes. Mobile is not optional — it is the primary target.**

### Tailwind CSS Breakpoints (used throughout)

| Tailwind Prefix | Width | Layout |
|:---|:---|:---|
| *(default)* | `0px+` | **Mobile first** — single column, phone-app layout |
| `sm:` | `640px+` | Slightly wider single column, larger cards |
| `md:` | `768px+` | Tablet — single column, expanded padding |
| `lg:` | `1024px+` | **Two-panel split** layout unlocks |
| `xl:` | `1280px+` | Wider split, more padding |

All layout classes must be written **mobile-first**: base class = mobile style, `lg:` prefix = desktop override.

---

### Desktop Layout (`lg:` and above)

```
┌──────────────────────────────────────────────────────────┐
│  ★ GHANA CIVIC RAG | ACITY      ⚙ Settings              │
├────────────────────────┬─────────────────────────────────┤
│                        │                                 │
│    CHAT PANEL (55%)    │    INSPECTION PANEL (45%)       │
│                        │                                 │
│  ┌──────────────────┐  │  ┌───────────────────────────┐  │
│  │ User message     │  │  │ Retrieved Chunks          │  │
│  └──────────────────┘  │  │  ├─ Chunk 1  [0.92] Green │  │
│  ┌──────────────────┐  │  │  ├─ Chunk 2  [0.85] Green │  │
│  │ AI Response      │  │  │  └─ Chunk 3  [0.41] Red   │  │
│  │ with citations   │  │  ├───────────────────────────┤  │
│  └──────────────────┘  │  │ Prompt Sent to LLM        │  │
│                        │  │  (collapsible code block)  │  │
│                        │  ├───────────────────────────┤  │
│                        │  │ Pipeline Timing            │  │
│  ┌──────────────────┐  │  │  Retrieval: 120ms         │  │
│  │ Type message...  │  │  │  Context:   45ms          │  │
│  └──────────────────┘  │  │  LLM:       890ms         │  │
│                        │  └───────────────────────────┘  │
└────────────────────────┴─────────────────────────────────┘
```

**Desktop behavior:**
- Chat panel: `w-[55%]`, Inspection panel: `w-[45%]`
- Both panels scroll independently with `overflow-y-auto`
- Inspection panel updates in real-time as each response arrives

---

### Mobile Layout (default, below `lg:`)

```
┌─────────────────────────┐
│ ★ GH CIVIC RAG  ⚙  📋  │  ← Compact header (icon-only buttons)
├─────────────────────────┤
│                         │
│  ┌───────────────────┐  │
│  │ User message      │  │
│  └───────────────────┘  │
│  ┌───────────────────┐  │
│  │ AI Response       │  │
│  │ with inline       │  │
│  │ source badges     │  │
│  │                   │  │
│  │ ▼ View Sources(3) │  │  ← Expandable accordion
│  │ ▼ Pipeline Timing │  │  ← Expandable accordion
│  └───────────────────┘  │
│                         │
│  ┌───────────────────┐  │
│  │ Type message...   │  │  ← Fixed bottom input
│  │             ➤     │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

**Mobile behavior — ALL of these are REQUIRED, not optional:**
- **Full-screen chat** with no side panel
- Retrieved chunks and pipeline info are in **expandable accordions** under each AI response
- Input bar is **fixed to the bottom** (like iMessage/WhatsApp) using `fixed bottom-0`
- Header is **compact** with icon-only buttons to preserve vertical space
- **Bottom sheet** slides up from bottom for settings and pipeline details
- All text, padding, and touch targets scale correctly on small screens
- No horizontal scrolling at any viewport width
- Safe area insets respected for notched/dynamic-island phones

---

### Tablet Layout (`md:` to `lg:`)

```
┌──────────────────────────────────┐
│  ★ GHANA CIVIC RAG | ACITY  ⚙   │
├──────────────────────────────────┤
│                                  │
│   Full-width chat panel          │
│   (wider than mobile)            │
│                                  │
│   AI response with inline        │
│   expandable source cards        │
│                                  │
│  ┌────────────────────────────┐  │
│  │ Type message...         ➤  │  │  ← Bottom input
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

**Tablet behavior:**
- Single-column like mobile but with wider max-width cards (`max-w-2xl`)
- Expandable source/pipeline accordions same as mobile
- More generous padding (`px-6` vs `px-4` on mobile)
- Header shows abbreviated text label next to icon

---

## 6. Component Architecture (Next.js App Router)

```
src/
├── app/
│   ├── layout.tsx               # Root layout — font loading, global metadata, dark theme
│   ├── page.tsx                 # Home page — renders <AppShell />
│   ├── globals.css              # CSS custom properties (design tokens) + Tailwind base
│   └── api/
│       └── query/
│           └── route.ts         # API proxy to FastAPI backend (avoids CORS issues)
│
├── components/
│   ├── layout/
│   │   ├── AppShell.tsx         # Root responsive shell — single/split column logic
│   │   ├── CivicHeader.tsx      # Header — full on desktop, icon-only on mobile
│   │   ├── SplitPane.tsx        # lg: two-panel layout (chat 55% / inspection 45%)
│   │   ├── BottomSheet.tsx      # Mobile slide-up sheet (settings, pipeline details)
│   │   └── BlackStarBg.tsx      # SVG star watermark (opacity 0.03–0.05, aria-hidden)
│   │
│   ├── chat/
│   │   ├── ChatContainer.tsx    # Scrollable message list, auto-scroll on new message
│   │   ├── MessageBubble.tsx    # User (gold gradient) / Bot (glass) bubble
│   │   ├── ChatInput.tsx        # Input bar — fixed bottom on mobile, inline on desktop
│   │   ├── TypingIndicator.tsx  # Animated thinking dots (gold pulse)
│   │   └── WelcomeScreen.tsx    # Hero with Black Star + Ghana tricolour gradient
│   │
│   ├── rag/
│   │   ├── InspectionPanel.tsx  # Desktop right-hand panel container
│   │   ├── SourceCard.tsx       # Retrieved chunk card — Ballot Box Glass style
│   │   ├── SourceList.tsx       # List of source cards with score colour mapping
│   │   ├── SimilarityBadge.tsx  # Ghana-flag-coded score badge (Red / Gold / Green)
│   │   ├── PromptViewer.tsx     # Collapsible code block for final LLM prompt
│   │   ├── PipelineTimeline.tsx # Stage timing with gold timeline dots
│   │   ├── SourceAccordion.tsx  # Mobile accordion wrapping SourceList
│   │   └── DatasetTag.tsx       # Tag showing source dataset (Election / Budget)
│   │
│   ├── ui/
│   │   ├── BallotGlassCard.tsx  # Glassmorphism card — base component
│   │   ├── Badge.tsx            # Label badge (Ghana-colour variants)
│   │   ├── GoldButton.tsx       # Primary CTA — gold gradient, touch-friendly (min 44px)
│   │   ├── IconButton.tsx       # Icon-only button — min 44×44px touch target
│   │   ├── ScoreBar.tsx         # Red→Gold→Green animated progress bar
│   │   ├── CodeBlock.tsx        # Syntax-highlighted code display (react-syntax-highlighter)
│   │   ├── Accordion.tsx        # Expandable section — used heavily on mobile
│   │   ├── Tooltip.tsx          # Hover tooltip (desktop) / long-press (mobile)
│   │   └── Skeleton.tsx         # Loading skeleton — gold shimmer sweep
│   │
│   └── settings/
│       ├── SettingsPanel.tsx    # Config panel — sidebar on desktop, bottom sheet on mobile
│       ├── SliderInput.tsx      # Range slider (top_k, hybrid_alpha) — gold track
│       └── ModelSelector.tsx    # LLM model dropdown
│
├── hooks/
│   ├── useChat.ts               # Chat state, send message, streaming response logic
│   ├── useMediaQuery.ts         # Responsive hook — detect mobile/tablet/desktop
│   └── useBottomSheet.ts        # Bottom sheet open/close state
│
├── lib/
│   ├── api.ts                   # FastAPI client — fetch wrapper for /query and /health
│   └── types.ts                 # TypeScript types matching backend response shapes
│
└── styles/
    └── animations.css           # @keyframes definitions (slide-in, shimmer, pulse, bounce)
```

---

## 7. Key Component Designs

### 7.1 — Ballot Box Glass Card (Foundation Component)

```css
/* globals.css / Tailwind @layer components */
.ballot-glass {
  background: rgba(30, 41, 59, 0.55);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(252, 209, 22, 0.08);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.ballot-glass:hover {
  border-color: rgba(252, 209, 22, 0.18);
  box-shadow: 0 8px 32px rgba(252, 209, 22, 0.08);
}
```

Tailwind equivalent for JSX: `bg-slate-800/55 backdrop-blur-xl border border-yellow-400/[0.08] rounded-2xl shadow-lg`

### 7.2 — Message Bubble

```tsx
// User message — warm gold gradient, right-aligned
<div className="
  bg-gradient-to-br from-[#D4A017] to-[#FCD116]
  rounded-[20px_20px_4px_20px]
  text-[#0B0F1A] font-medium
  max-w-[75%] self-end
  px-4 py-3
  text-sm sm:text-[15px]
" />

// Bot message — Ballot Box Glass, left-aligned
<div className="
  bg-slate-800/70 backdrop-blur-md
  border border-yellow-400/[0.06]
  rounded-[20px_20px_20px_4px]
  text-slate-100
  max-w-[85%] self-start
  px-4 py-3
  text-sm sm:text-[15px]
" />
```

### 7.3 — Similarity Score Badge (Ghana Flag Spectrum)

```tsx
// Score thresholds
const badgeVariant = score >= 0.75 ? 'high' : score >= 0.5 ? 'medium' : 'low'

const variants = {
  high:   'bg-[#006B3F]/20 text-[#00895A]',   // Ghana Green — >= 0.75
  medium: 'bg-[#FCD116]/15 text-[#FCD116]',   // Ghana Gold  — 0.5–0.75
  low:    'bg-[#CE1126]/15 text-[#CE1126]',   // Ghana Red   — < 0.5
}

<span className={`
  inline-flex items-center gap-1
  px-2 py-0.5 rounded-full
  text-[10px] sm:text-[11px] font-semibold font-mono
  ${variants[badgeVariant]}
`}>
  {score.toFixed(2)}
</span>
```

### 7.4 — Pipeline Timeline

```tsx
<div className="border-l-2 border-[#FCD116] pl-4 space-y-3">
  {stages.map(stage => (
    <div key={stage.name} className="relative flex items-center gap-3 py-1">
      {/* Gold dot on the timeline line */}
      <span className="
        absolute -left-[21px]
        w-2.5 h-2.5 rounded-full
        bg-[#FCD116] shadow-[0_0_8px_rgba(252,209,22,0.4)]
      " />
      <span className="text-slate-400 text-xs sm:text-sm w-24 shrink-0">{stage.name}</span>
      <span className="text-[#FCD116] font-mono text-xs sm:text-sm">{stage.ms}ms</span>
    </div>
  ))}
</div>
```

### 7.5 — Responsive Chat Input

```tsx
// Fixed to bottom on mobile, inline at bottom of chat panel on desktop
<div className="
  fixed bottom-0 left-0 right-0 z-50
  lg:relative lg:bottom-auto lg:left-auto lg:right-auto
  px-4 pb-4 pt-2
  lg:px-0 lg:pb-0 lg:pt-4
  bg-[#0B0F1A]/90 backdrop-blur-md
  lg:bg-transparent lg:backdrop-blur-none
  safe-area-inset-bottom
">
  <div className="flex gap-2 items-end max-w-none lg:max-w-full">
    <textarea
      className="
        flex-1 resize-none
        bg-slate-800/70 backdrop-blur-md
        border border-yellow-400/10 rounded-2xl
        px-4 py-3 text-sm text-slate-100
        placeholder:text-slate-500
        focus:outline-none focus:border-[#FCD116]/40
        min-h-[48px] max-h-32
      "
      rows={1}
    />
    <button className="
      min-w-[48px] min-h-[48px]
      bg-gradient-to-br from-[#D4A017] to-[#FCD116]
      text-[#0B0F1A] rounded-xl
      flex items-center justify-center
      active:scale-95 transition-transform
    ">
      Send
    </button>
  </div>
</div>
```

---

## 8. Micro-Animations

| Animation | Trigger | Duration | Implementation |
|:---|:---|:---|:---|
| **Message slide-in** | New message | 300ms | `translateY(16px) → 0` + fade — CSS `@keyframes` |
| **Typing dots** | Waiting for response | Loop | 3 dots bouncing sequentially — `animate-bounce` with stagger |
| **Score badge pulse** | Score loads | 500ms | `scale(1) → scale(1.05) → scale(1)` |
| **Accordion expand** | Tap/click | 250ms | `max-height` transition + rotate chevron |
| **Glass card hover glow** | Mouse hover | 300ms | Border color shift + shadow bloom |
| **Send button pulse** | Input focus | 200ms | Scale up + accent glow |
| **Skeleton shimmer** | Loading state | Loop | Gradient sweep left-to-right |
| **Bottom sheet slide** | Mobile tap | 350ms | `translateY(100%) → 0` + backdrop fade |

Define all keyframes in `src/styles/animations.css` and apply via Tailwind `animate-*` utilities or inline `style` with CSS variable duration.

---

## 9. Mobile-Specific Requirements

> **These are non-negotiable requirements. The app MUST work perfectly on mobile screens (320px–767px).**

### Layout Rules
- Chat input **always fixed to bottom** (`fixed bottom-0`) on screens below `lg:`
- No horizontal overflow at any width — test at 320px minimum
- Header collapses to icon-only on mobile to maximise vertical space
- The inspection panel (sources, prompt, timing) **does not exist as a side panel on mobile** — it appears as accordions inside each bot message bubble
- Bottom sheet replaces modal/sidebar for settings on mobile

### Touch & Interaction
- All interactive elements: **minimum touch target 44×44px** (use `min-h-[44px] min-w-[44px]`)
- Tap states via `active:scale-95` or `active:opacity-80`
- No hover-only interactions — every hover behaviour needs a tap equivalent
- Accordion toggles must be easy to tap even with large fingers

### Viewport & iOS Handling
```css
/* In globals.css */
html {
  height: -webkit-fill-available;
}

body {
  min-height: 100svh; /* svh = small viewport height — handles iOS safari chrome */
}

/* Safe area padding for notched phones */
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom, 16px);
}
```

### Scroll Behavior
- Message list: `overflow-y-auto` with `-webkit-overflow-scrolling: touch`
- Auto-scroll to latest message on new content — use `useEffect` + `ref.scrollIntoView()`
- Prevent body scroll when bottom sheet is open (`overflow-hidden` on `<body>`)

### Performance on Mobile
- No layout shifts — use `min-h` placeholders for content that loads asynchronously
- Skeleton loaders shown immediately while API responds
- Images (logo, icons) use `next/image` with explicit `width`/`height` to prevent CLS

---

## 10. Technology Stack (Next.js)

| Aspect | Choice | Reason |
|:---|:---|:---|
| **Framework** | **Next.js 14+ (App Router)** | Exam mentions Next.js as a valid option; structured, production-grade, great DX |
| **Language** | **TypeScript** | Type-safe API response handling; catches shape mismatches at build time |
| **Styling** | **Tailwind CSS v3** | Mobile-first utility classes; built-in responsive prefixes (`sm:`, `md:`, `lg:`) |
| **Fonts** | **`next/font/google`** | Optimised font loading, zero layout shift, no external CDN request at runtime |
| **Icons** | **Lucide React** | `npm` package, tree-shakeable SVG icons |
| **Markdown** | **`react-markdown` + `remark-gfm`** | Render LLM responses with full markdown support |
| **Syntax highlighting** | **`react-syntax-highlighter`** | For prompt/code display in PromptViewer |
| **Animations** | **Tailwind `animate-*` + CSS `@keyframes`** | No animation library needed |
| **State management** | **React `useState` + `useReducer`** | Local state only — no Redux/Zustand needed at this scale |
| **HTTP client** | **Native `fetch`** | Built into Next.js; no extra dependency |

### Project Initialisation

```bash
npx create-next-app@latest frontend \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*"

cd frontend
npm install lucide-react react-markdown remark-gfm react-syntax-highlighter
npm install -D @types/react-syntax-highlighter
```

### Next.js Config Notes
- Set `NEXT_PUBLIC_API_URL=http://localhost:8000` in `.env.local` for the FastAPI backend URL
- Use `/app/api/query/route.ts` as a proxy to avoid browser CORS errors when calling FastAPI
- Enable `images.remotePatterns` in `next.config.ts` only if external images are needed

---

## 11. Implementation Phases

### Phase 1 — Project Setup
1. Run `create-next-app` with TypeScript + Tailwind (command above)
2. Define CSS custom properties (design tokens) in `globals.css`
3. Add `@keyframes` in `animations.css` and import in `globals.css`
4. Set up `lib/types.ts` with full TypeScript types for backend response
5. Set up `lib/api.ts` with the `postQuery()` fetch function
6. Set up `/app/api/query/route.ts` proxy

### Phase 2 — Core Chat
7. Build `AppShell` with responsive single-column / split-pane switching at `lg:`
8. Build `CivicHeader` — full text on desktop, icon-only on mobile
9. Build `ChatContainer` with auto-scroll
10. Build `MessageBubble` (user gold / bot glass variants)
11. Build `ChatInput` — fixed bottom on mobile, inline on desktop
12. Build `TypingIndicator` (gold bouncing dots)
13. Wire `useChat` hook to API — send query, receive and display response

### Phase 3 — RAG Inspection
14. Build `SimilarityBadge` with Ghana-flag colour thresholds
15. Build `SourceCard` and `SourceList`
16. Build `PipelineTimeline`
17. Build `PromptViewer` with collapsible code block
18. Desktop: assemble `InspectionPanel` as right-hand column
19. Mobile: wrap above in `SourceAccordion` inside each bot message

### Phase 4 — Settings & Polish
20. Build `SettingsPanel` — sidebar on desktop, `BottomSheet` on mobile
21. Build `SliderInput` (top_k, hybrid_alpha) and `ModelSelector`
22. Build `WelcomeScreen` hero with Black Star + Ghana gradient
23. Add `BlackStarBg` SVG watermark
24. Add `Skeleton` loaders for all async content
25. Implement all micro-animations

### Phase 5 — Responsive QA
26. Test at 320px, 375px, 414px, 768px, 1024px, 1280px, 1440px
27. Test on real iOS Safari and Android Chrome (keyboard push-up behaviour)
28. Verify touch targets ≥ 44px throughout
29. Verify no horizontal scroll at any width
30. Lighthouse audit — target ≥ 90 Performance, 100 Accessibility

---

## 12. Design Decision Summary

> **Why this design works for the exam:**
> - Shows **query input** prominently on all screen sizes
> - Displays **retrieved chunks** with colour-coded similarity scores
> - Shows the **final prompt sent to LLM** in a collapsible code viewer
> - Displays the **AI response** with full markdown rendering
> - Shows **pipeline stage timing** (logging at each stage)
> - **Fully responsive** — identical feature coverage on mobile and desktop
> - Premium dark look with Ghanaian national identity demonstrates real design effort
> - Next.js + TypeScript = production-grade architecture that matches exam expectations

---

## Open Questions

1. **Do you want a welcome/landing screen** with the Black Star hero, or jump straight into the chat?
2. **Should settings (top_k, model, alpha) be in a sidebar, modal, or within the header?**
3. **Preferred app title?** — `GHANA CIVIC RAG | ACITY` vs `ELECTORAL & ECONOMIC EXPLORER`?
4. **Do you want a light mode toggle**, or dark-only?
5. **Streaming responses?** — FastAPI can stream tokens; should the UI render them word-by-word?
