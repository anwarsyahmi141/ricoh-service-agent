import json
import os
from ricoh_database import SC_CODES, SP_MODE_PROCEDURES

def generate_html_file(output_path="C:\\Users\\kaze\\ricoh-service-agent\\ricoh_sc_guide.html"):
    codes_json = json.dumps(SC_CODES)
    sp_json = json.dumps(SP_MODE_PROCEDURES)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ricoh SC Diagnostics | Material You</title>
<!-- Google Fonts: Roboto Flex & Material Symbols Outlined -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Roboto+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />

<style>
  /* ================= Material You (M3) Design Tokens ================= */
  :root[data-theme="dark"] {{
    --md-sys-color-background: #0f141c;
    --md-sys-color-on-background: #e1e2e9;
    --md-sys-color-surface: #121824;
    --md-sys-color-surface-dim: #0a0e17;
    --md-sys-color-surface-container-lowest: #0b1019;
    --md-sys-color-surface-container-low: #151d2c;
    --md-sys-color-surface-container: #1b2436;
    --md-sys-color-surface-container-high: #222d42;
    --md-sys-color-surface-container-highest: #2b3850;
    
    --md-sys-color-primary: #a8c7fa;
    --md-sys-color-on-primary: #062e6f;
    --md-sys-color-primary-container: #1b437e;
    --md-sys-color-on-primary-container: #d3e3fd;

    --md-sys-color-secondary: #c2e7ff;
    --md-sys-color-on-secondary: #003353;
    --md-sys-color-secondary-container: #004a75;
    --md-sys-color-on-secondary-container: #c2e7ff;

    --md-sys-color-tertiary: #d0bcff;
    --md-sys-color-on-tertiary: #381e72;
    --md-sys-color-tertiary-container: #4f378b;
    --md-sys-color-on-tertiary-container: #eaddff;

    --md-sys-color-error: #ffb4ab;
    --md-sys-color-on-error: #690005;
    --md-sys-color-error-container: #93000a;
    --md-sys-color-on-error-container: #ffdad6;

    --md-sys-color-warning: #ffb74d;
    --md-sys-color-warning-container: #4e2c00;
    --md-sys-color-on-warning-container: #ffe0b2;

    --md-sys-color-outline: #8c919d;
    --md-sys-color-outline-variant: #434751;
    --md-sys-color-shadow: rgba(0, 0, 0, 0.4);
    --card-border: rgba(255, 255, 255, 0.06);
  }}

  :root[data-theme="light"] {{
    --md-sys-color-background: #fdfcff;
    --md-sys-color-on-background: #1a1c1e;
    --md-sys-color-surface: #f8f9ff;
    --md-sys-color-surface-dim: #dedfe5;
    --md-sys-color-surface-container-lowest: #ffffff;
    --md-sys-color-surface-container-low: #f3f3fa;
    --md-sys-color-surface-container: #ededf4;
    --md-sys-color-surface-container-high: #e7e8ef;
    --md-sys-color-surface-container-highest: #e1e2e9;

    --md-sys-color-primary: #0b57d0;
    --md-sys-color-on-primary: #ffffff;
    --md-sys-color-primary-container: #d3e3fd;
    --md-sys-color-on-primary-container: #041e49;

    --md-sys-color-secondary: #00639b;
    --md-sys-color-on-secondary: #ffffff;
    --md-sys-color-secondary-container: #c2e7ff;
    --md-sys-color-on-secondary-container: #001d32;

    --md-sys-color-tertiary: #6750a4;
    --md-sys-color-on-tertiary: #ffffff;
    --md-sys-color-tertiary-container: #eaddff;
    --md-sys-color-on-tertiary-container: #21005d;

    --md-sys-color-error: #ba1a1a;
    --md-sys-color-on-error: #ffffff;
    --md-sys-color-error-container: #ffdad6;
    --md-sys-color-on-error-container: #410002;

    --md-sys-color-warning: #b26a00;
    --md-sys-color-warning-container: #ffe0b2;
    --md-sys-color-on-warning-container: #331c00;

    --md-sys-color-outline: #73777f;
    --md-sys-color-outline-variant: #c3c7d0;
    --md-sys-color-shadow: rgba(0, 0, 0, 0.08);
    --card-border: rgba(0, 0, 0, 0.08);
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    background-color: var(--md-sys-color-background);
    color: var(--md-sys-color-on-background);
    line-height: 1.5;
    padding-bottom: 60px;
    transition: background-color 0.25s, color 0.25s;
    -webkit-font-smoothing: antialiased;
  }}

  .container {{
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 20px;
  }}

  /* Top App Bar */
  .m3-top-bar {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--md-sys-color-surface-container);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--card-border);
    padding: 16px 0;
    transition: background 0.25s;
  }}

  .top-bar-inner {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
  }}

  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .brand-logo {{
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: linear-gradient(135deg, #e11d48, #be123c);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1.15rem;
    box-shadow: 0 4px 12px rgba(225, 29, 72, 0.35);
  }}

  .brand-text h1 {{
    font-size: 1.25rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--md-sys-color-on-background);
  }}

  .brand-text p {{
    font-size: 0.78rem;
    color: var(--md-sys-color-outline);
    font-weight: 500;
  }}

  .theme-toggle-btn {{
    background: var(--md-sys-color-surface-container-high);
    color: var(--md-sys-color-on-background);
    border: none;
    border-radius: 20px;
    padding: 8px 16px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
  }}

  .theme-toggle-btn:hover {{
    background: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
  }}

  /* Material You Floating Search Bar */
  .search-wrapper {{
    margin: 24px 0 16px 0;
  }}

  .m3-search-bar {{
    background: var(--md-sys-color-surface-container-high);
    border-radius: 28px;
    display: flex;
    align-items: center;
    padding: 6px 14px 6px 20px;
    box-shadow: 0 6px 20px var(--md-sys-color-shadow);
    transition: all 0.25s cubic-bezier(0.2, 0, 0, 1);
    border: 2px solid transparent;
  }}

  .m3-search-bar:focus-within {{
    background: var(--md-sys-color-surface-container-highest);
    border-color: var(--md-sys-color-primary);
    box-shadow: 0 8px 28px rgba(168, 199, 250, 0.25);
  }}

  .search-icon {{
    color: var(--md-sys-color-primary);
    margin-right: 12px;
    font-size: 26px;
  }}

  .m3-search-input {{
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1.05rem;
    font-family: inherit;
    color: var(--md-sys-color-on-background);
  }}

  .m3-search-input::placeholder {{
    color: var(--md-sys-color-outline);
    font-size: 0.95rem;
  }}

  .clear-btn {{
    background: transparent;
    border: none;
    color: var(--md-sys-color-outline);
    cursor: pointer;
    display: none;
    padding: 6px;
    border-radius: 50%;
  }}

  .clear-btn:hover {{
    color: var(--md-sys-color-on-background);
  }}

  /* M3 Filter Chips */
  .chips-container {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 4px 2px 14px 2px;
    scrollbar-width: thin;
  }}

  .m3-chip {{
    background: var(--md-sys-color-surface-container-low);
    color: var(--md-sys-color-on-background);
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 8px 16px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s cubic-bezier(0.2, 0, 0, 1);
  }}

  .m3-chip:hover {{
    background: var(--md-sys-color-surface-container-high);
  }}

  .m3-chip.active {{
    background: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
    border-color: var(--md-sys-color-primary);
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }}

  .m3-chip-danger.active {{
    background: var(--md-sys-color-error-container);
    color: var(--md-sys-color-on-error-container);
    border-color: var(--md-sys-color-error);
  }}

  /* Model Badges Bar */
  .model-pill-row {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    align-items: center;
    margin-bottom: 20px;
  }}

  .model-pill {{
    background: var(--md-sys-color-surface-container-highest);
    color: var(--md-sys-color-on-background);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    letter-spacing: 0.02em;
  }}

  /* SP Mode Banner Accordion */
  .sp-card-m3 {{
    background: var(--md-sys-color-surface-container-low);
    border-radius: 24px;
    border: 1px solid var(--card-border);
    margin-bottom: 28px;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.2, 0, 0, 1);
  }}

  .sp-card-header {{
    padding: 18px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    user-select: none;
    background: var(--md-sys-color-surface-container);
  }}

  .sp-card-header h2 {{
    font-size: 1.05rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--md-sys-color-primary);
  }}

  .sp-content {{
    padding: 20px 24px;
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
  }}

  @media(min-width: 768px) {{
    .sp-content {{ grid-template-columns: 1fr 1fr; }}
  }}

  .sp-box {{
    background: var(--md-sys-color-surface-container-highest);
    border-radius: 16px;
    padding: 16px;
  }}

  .sp-box h3 {{
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--md-sys-color-secondary);
    margin-bottom: 8px;
  }}

  .sp-box pre {{
    font-family: 'Roboto Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.5;
    white-space: pre-wrap;
    color: var(--md-sys-color-on-background);
  }}

  /* Error Cards Grid */
  .cards-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
  }}

  .m3-card {{
    background: var(--md-sys-color-surface-container);
    border-radius: 24px;
    border: 1px solid var(--card-border);
    padding: 24px;
    box-shadow: 0 4px 16px var(--md-sys-color-shadow);
    transition: transform 0.2s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.2s;
  }}

  .m3-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px var(--md-sys-color-shadow);
  }}

  .card-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }}

  .code-group {{
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }}

  .sc-badge-code {{
    font-family: 'Roboto Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--md-sys-color-primary);
    background: var(--md-sys-color-surface-container-high);
    padding: 4px 14px;
    border-radius: 14px;
  }}

  .sc-title {{
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--md-sys-color-on-background);
  }}

  .badge-tag {{
    font-size: 0.72rem;
    font-weight: 800;
    padding: 6px 12px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}

  .badge-level-a {{
    background: var(--md-sys-color-error-container);
    color: var(--md-sys-color-on-error-container);
  }}

  .badge-level-b {{
    background: var(--md-sys-color-warning-container);
    color: var(--md-sys-color-on-warning-container);
  }}

  .badge-level-d {{
    background: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
  }}

  .badge-reset-needed {{
    background: #e11d48;
    color: white;
  }}

  /* Card Inner Sections */
  .section-title {{
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--md-sys-color-outline);
    margin: 14px 0 6px 0;
  }}

  .symptom-box {{
    background: var(--md-sys-color-surface-container-high);
    border-left: 4px solid var(--md-sys-color-primary);
    border-radius: 0 12px 12px 0;
    padding: 10px 14px;
    font-size: 0.92rem;
    color: var(--md-sys-color-on-background);
  }}

  ul.m3-list, ol.m3-list {{
    margin-left: 20px;
    font-size: 0.92rem;
    color: var(--md-sys-color-on-background);
  }}

  ul.m3-list li, ol.m3-list li {{
    margin-bottom: 6px;
  }}

  .reset-alert-box {{
    margin-top: 16px;
    background: var(--md-sys-color-error-container);
    color: var(--md-sys-color-on-error-container);
    border-radius: 14px;
    padding: 12px 16px;
    font-size: 0.88rem;
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 500;
  }}

  .copy-card-btn {{
    background: var(--md-sys-color-surface-container-highest);
    color: var(--md-sys-color-on-background);
    border: none;
    border-radius: 12px;
    padding: 6px 12px;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background 0.2s;
  }}

  .copy-card-btn:hover {{
    background: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
  }}

  /* Toast Notification */
  .m3-toast {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--md-sys-color-on-background);
    color: var(--md-sys-color-background);
    border-radius: 28px;
    padding: 12px 24px;
    font-size: 0.9rem;
    font-weight: 600;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.25s cubic-bezier(0.2, 0, 0, 1);
    pointer-events: none;
    z-index: 1000;
  }}

  .m3-toast.show {{
    opacity: 1;
    transform: translateY(0);
  }}

  .empty-state {{
    text-align: center;
    padding: 80px 20px;
    color: var(--md-sys-color-outline);
  }}

  .empty-state span {{
    font-size: 48px;
    color: var(--md-sys-color-primary);
  }}
</style>
</head>
<body>

<!-- Material 3 Top App Bar -->
<header class="m3-top-bar">
  <div class="container top-bar-inner">
    <div class="brand">
      <div class="brand-logo">R</div>
      <div class="brand-text">
        <h1>Ricoh Service Call (SC) Diagnostics</h1>
        <p>M · MP · MP C · IM · IM C Series</p>
      </div>
    </div>
    <button class="theme-toggle-btn" id="themeToggle" onclick="toggleTheme()">
      <span class="material-symbols-outlined" id="themeIcon">light_mode</span>
      <span id="themeText">Light Mode</span>
    </button>
  </div>
</header>

<main class="container">
  <!-- Material You Floating Search Bar -->
  <div class="search-wrapper">
    <div class="m3-search-bar">
      <span class="material-symbols-outlined search-icon">search</span>
      <input type="text" id="searchInput" class="m3-search-input" placeholder="Search SC code (542, 672, 899) or component (fuser, laser, motor, chip)..." autofocus autocomplete="off" />
      <button class="clear-btn" id="clearBtn" onclick="clearSearch()">
        <span class="material-symbols-outlined">close</span>
      </button>
    </div>
  </div>

  <!-- Material 3 Filter Chips -->
  <div class="chips-container">
    <button class="m3-chip active" onclick="setCategory('ALL')">All Codes</button>
    <button class="m3-chip m3-chip-danger" onclick="filterLevelA()">
      <span class="material-symbols-outlined" style="font-size: 18px;">warning</span> Level A (Reset Required)
    </button>
    <button class="m3-chip" onclick="setCategory('SC100')">SC100 Optics</button>
    <button class="m3-chip" onclick="setCategory('SC200')">SC200 Laser</button>
    <button class="m3-chip" onclick="setCategory('SC300')">SC300 Drum & PCU</button>
    <button class="m3-chip" onclick="setCategory('SC400')">SC400 Transfer</button>
    <button class="m3-chip" onclick="setCategory('SC500')">SC500 Fuser</button>
    <button class="m3-chip" onclick="setCategory('SC600')">SC600 Comm & RFID</button>
    <button class="m3-chip" onclick="setCategory('SC700')">SC700 Finisher</button>
    <button class="m3-chip" onclick="setCategory('SC800')">SC800 Controller/HDD</button>
    <button class="m3-chip" onclick="setCategory('SC900')">SC900 Engine</button>
  </div>

  <!-- SP Mode Accordion -->
  <section class="sp-card-m3">
    <div class="sp-card-header" onclick="toggleSPAccordion()">
      <h2>
        <span class="material-symbols-outlined">build</span>
        Service Program (SP) Mode Entry & Fuser Reset Cheatsheet
      </h2>
      <span class="material-symbols-outlined" id="spArrow" style="transition: transform 0.25s;">expand_more</span>
    </div>
    <div class="sp-content" id="spContent" style="display: none;">
      <div class="sp-box">
        <h3>Classic MP & M Series (Physical Keypad)</h3>
        <pre>1. Press Yellow [Clear Modes / Reset] button.
2. Type 1 - 0 - 7 on numeric keypad.
3. Press and HOLD Red [Clear/Stop] button (3-5 sec).
4. Tap [System SP] on screen.
5. To clear Fuser SC codes:
   - Type 5810 then press [#].
   - Select SP 5-810-001 (SC Code Reset).
   - Press [Execute].
6. Switch Main Power OFF for 15 sec, then turn ON.</pre>
      </div>
      <div class="sp-box">
        <h3>Smart Operation Panel (SOP) - MP Cxx04 & IM / IM C Series</h3>
        <pre>Method 1 (Keypad Code):
1. Go to Home -> open [Copier] application.
2. Open on-screen virtual keypad -> press [Reset].
3. Type 8 - 0 - 6 - 1 - 8 - 2.
4. Press and HOLD the [C] (Clear) key for 3-5 sec.
5. Tap [System SP].

Method 2 (Check Status):
1. Press [Check Status] -> touch blank area in title.
2. Press Stop -> 0 -> 0 -> 1 -> 0 -> 7 -> Start.
3. Select [System SP] -> SP 5-810-001 -> [Execute] -> Reboot.</pre>
      </div>
    </div>
  </section>

  <!-- Counter & Status -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; font-size: 0.85rem; color: var(--md-sys-color-outline);">
    <span id="resultsCount">Loading error codes...</span>
    <span>Material 3 Diagnostic Guide</span>
  </div>

  <!-- Cards Grid -->
  <div class="cards-grid" id="cardsGrid"></div>
</main>

<!-- Material 3 Toast -->
<div class="m3-toast" id="toast">Copied to clipboard!</div>

<script>
const scData = {codes_json};
let currentCategory = 'ALL';
let filterOnlyLevelA = false;

function toggleTheme() {{
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') === 'dark';
  const newTheme = isDark ? 'light' : 'dark';
  html.setAttribute('data-theme', newTheme);
  
  document.getElementById('themeIcon').textContent = isDark ? 'dark_mode' : 'light_mode';
  document.getElementById('themeText').textContent = isDark ? 'Dark Mode' : 'Light Mode';
}}

function toggleSPAccordion() {{
  const content = document.getElementById('spContent');
  const arrow = document.getElementById('spArrow');
  const isOpen = content.style.display === 'grid';
  content.style.display = isOpen ? 'none' : 'grid';
  arrow.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
}}

function showToast(msg) {{
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2200);
}}

function copyFix(code, title, solutions) {{
  const text = `Ricoh SC Error: ${{code}} - ${{title}}\\n\\nSolutions:\\n${{solutions.map((s, i) => `${{i+1}}. ${{s}}`).join('\\n')}}`;
  navigator.clipboard.writeText(text).then(() => {{
    showToast(`Copied fix for ${{code}}!`);
  }});
}}

function renderCards(items) {{
  const grid = document.getElementById('cardsGrid');
  const count = document.getElementById('resultsCount');
  grid.innerHTML = '';
  count.textContent = `Showing ${{items.length}} error codes`;

  if (items.length === 0) {{
    grid.innerHTML = `
      <div class="empty-state">
        <span class="material-symbols-outlined">search_off</span>
        <h3 style="margin-top: 12px; color: var(--md-sys-color-on-background);">No matching SC codes found</h3>
        <p style="margin-top: 4px;">Try searching by code number (e.g. 542, 672) or component (fuser, laser, toner).</p>
      </div>
    `;
    return;
  }}

  items.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'm3-card';
    card.id = item.code.toLowerCase();

    const causesHtml = item.causes.map(c => `<li>${{c}}</li>`).join('');
    const solutionsHtml = item.solutions.map(s => `<li>${{s}}</li>`).join('');

    let levelBadgeClass = 'badge-level-d';
    if (item.level === 'A') levelBadgeClass = 'badge-level-a';
    else if (item.level === 'B') levelBadgeClass = 'badge-level-b';

    card.innerHTML = `
      <div class="card-top">
        <div class="code-group">
          <span class="sc-badge-code">${{item.code}}</span>
          <span class="sc-title">${{item.title}}</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="badge-tag ${{levelBadgeClass}}">Level ${{item.level}}</span>
          ${{item.sp_reset_required ? '<span class="badge-tag badge-reset-needed">SP 5-810 Reset</span>' : ''}}
          <button class="copy-card-btn" onclick='copyFix("${{item.code}}", "${{item.title.replace(/"/g, '&quot;')}}", ${{JSON.stringify(item.solutions)}})'>
            <span class="material-symbols-outlined" style="font-size:16px;">content_copy</span> Copy
          </button>
        </div>
      </div>

      <div style="font-size:0.8rem; color:var(--md-sys-color-outline); margin-bottom:12px;">
        <strong>Models:</strong> ${{item.models}}
      </div>

      <div class="section-title">Symptom</div>
      <div class="symptom-box">${{item.symptom}}</div>

      <div class="section-title">Probable Causes</div>
      <ul class="m3-list">${{causesHtml}}</ul>

      <div class="section-title">Step-by-Step Fix / Troubleshooting</div>
      <ol class="m3-list">${{solutionsHtml}}</ol>

      ${{item.sp_reset_required ? `
        <div class="reset-alert-box">
          <span class="material-symbols-outlined">restart_alt</span>
          <div><strong>Reset Required:</strong> ${{item.sp_reset_guide}}</div>
        </div>
      ` : ''}}
    `;
    grid.appendChild(card);
  }});
}}

function applyFilter() {{
  const query = document.getElementById('searchInput').value.trim().toLowerCase();
  const clearBtn = document.getElementById('clearBtn');
  clearBtn.style.display = query.length > 0 ? 'inline-block' : 'none';

  const filtered = scData.filter(item => {{
    const matchesCategory = currentCategory === 'ALL' || item.category.startsWith(currentCategory);
    const matchesLevel = !filterOnlyLevelA || item.sp_reset_required || item.level === 'A';
    
    if (!matchesCategory || !matchesLevel) return false;
    if (!query) return true;

    const haystack = [
      item.code,
      item.title,
      item.category,
      item.symptom,
      item.causes.join(' '),
      item.solutions.join(' ')
    ].join(' ').toLowerCase();

    return haystack.includes(query);
  }});

  renderCards(filtered);
}}

function clearSearch() {{
  document.getElementById('searchInput').value = '';
  applyFilter();
  document.getElementById('searchInput').focus();
}}

function setCategory(cat) {{
  currentCategory = cat;
  filterOnlyLevelA = false;
  document.querySelectorAll('.m3-chip').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  applyFilter();
}}

function filterLevelA() {{
  filterOnlyLevelA = true;
  currentCategory = 'ALL';
  document.querySelectorAll('.m3-chip').forEach(btn => btn.classList.remove('active'));
  event.currentTarget.classList.add('active');
  applyFilter();
}}

document.getElementById('searchInput').addEventListener('input', applyFilter);

// Initial render
renderCards(scData);
</script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated Material You HTML guide at: {output_path}")

if __name__ == "__main__":
    generate_html_file()
