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
<title>Ricoh SC Diagnostics | iOS Glass UI</title>
<!-- Google Fonts: SF Pro / Inter & Icons -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />

<style>
  /* ================= iOS Glassmorphism Design Tokens ================= */
  :root[data-theme="dark"] {{
    --bg-base: #060810;
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.68);
    --text-tertiary: rgba(255, 255, 255, 0.45);
    
    /* Apple Vision / iOS Glass Tokens */
    --glass-bg: rgba(25, 30, 48, 0.42);
    --glass-bg-hover: rgba(35, 42, 66, 0.55);
    --glass-card: rgba(20, 25, 40, 0.48);
    --glass-card-hover: rgba(28, 35, 56, 0.62);
    --glass-border: rgba(255, 255, 255, 0.12);
    --glass-border-highlight: rgba(255, 255, 255, 0.22);
    --glass-specular: inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
    --glass-blur: blur(28px) saturate(190%);
    
    --ios-blue: #0a84ff;
    --ios-blue-glass: rgba(10, 132, 255, 0.22);
    --ios-blue-border: rgba(10, 132, 255, 0.4);
    
    --ios-red: #ff453a;
    --ios-red-glass: rgba(255, 69, 58, 0.22);
    --ios-red-border: rgba(255, 69, 58, 0.45);

    --ios-amber: #ff9f0a;
    --ios-amber-glass: rgba(255, 159, 10, 0.22);
    --ios-amber-border: rgba(255, 159, 10, 0.4);

    --ios-green: #30d158;
    --segmented-bg: rgba(255, 255, 255, 0.08);
    --orb-1: radial-gradient(circle at 15% 20%, rgba(10, 132, 255, 0.25) 0%, transparent 45%);
    --orb-2: radial-gradient(circle at 85% 15%, rgba(191, 90, 242, 0.22) 0%, transparent 45%);
    --orb-3: radial-gradient(circle at 50% 80%, rgba(48, 209, 88, 0.15) 0%, transparent 50%);
  }}

  :root[data-theme="light"] {{
    --bg-base: #f2f4f8;
    --text-primary: #1c1c1e;
    --text-secondary: rgba(60, 60, 67, 0.75);
    --text-tertiary: rgba(60, 60, 67, 0.45);

    --glass-bg: rgba(255, 255, 255, 0.72);
    --glass-bg-hover: rgba(255, 255, 255, 0.85);
    --glass-card: rgba(255, 255, 255, 0.75);
    --glass-card-hover: rgba(255, 255, 255, 0.9);
    --glass-border: rgba(255, 255, 255, 0.65);
    --glass-border-highlight: rgba(255, 255, 255, 0.9);
    --glass-specular: inset 0 1px 1px 0 rgba(255, 255, 255, 0.8);
    --glass-blur: blur(28px) saturate(180%);

    --ios-blue: #007aff;
    --ios-blue-glass: rgba(0, 122, 255, 0.15);
    --ios-blue-border: rgba(0, 122, 255, 0.3);

    --ios-red: #ff3b30;
    --ios-red-glass: rgba(255, 59, 48, 0.15);
    --ios-red-border: rgba(255, 59, 48, 0.3);

    --ios-amber: #ff9500;
    --ios-amber-glass: rgba(255, 149, 0, 0.15);
    --ios-amber-border: rgba(255, 149, 0, 0.3);

    --ios-green: #34c759;
    --segmented-bg: rgba(0, 0, 0, 0.06);
    --orb-1: radial-gradient(circle at 10% 20%, rgba(0, 122, 255, 0.2) 0%, transparent 45%);
    --orb-2: radial-gradient(circle at 85% 20%, rgba(175, 82, 222, 0.18) 0%, transparent 45%);
    --orb-3: radial-gradient(circle at 50% 85%, rgba(52, 199, 89, 0.15) 0%, transparent 50%);
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", 'Plus Jakarta Sans', "Helvetica Neue", sans-serif;
    background-color: var(--bg-base);
    color: var(--text-primary);
    line-height: 1.45;
    padding-bottom: 80px;
    position: relative;
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    transition: background-color 0.3s ease;
  }}

  /* Ambient Glass Lighting Mesh */
  .ambient-glow {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 0;
    background-image: var(--orb-1), var(--orb-2), var(--orb-3);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    filter: blur(40px);
    transition: all 0.4s ease;
  }}

  .container {{
    max-width: 1120px;
    margin: 0 auto;
    padding: 0 20px;
    position: relative;
    z-index: 1;
  }}

  /* iOS Frosted Header */
  .ios-header {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border-bottom: 1px solid var(--glass-border);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1), var(--glass-specular);
    padding: 16px 0;
    transition: all 0.3s ease;
  }}

  .header-content {{
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

  .ios-app-icon {{
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(145deg, #e11d48, #be123c);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-weight: 800;
    font-size: 1.2rem;
    box-shadow: 0 8px 16px rgba(225, 29, 72, 0.35), inset 0 1px 1px rgba(255, 255, 255, 0.5);
    letter-spacing: -0.05em;
  }}

  .brand-title h1 {{
    font-size: 1.25rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    color: var(--text-primary);
  }}

  .brand-title p {{
    font-size: 0.78rem;
    color: var(--text-secondary);
    font-weight: 500;
  }}

  .ios-glass-btn {{
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    color: var(--text-primary);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-specular);
    border-radius: 9999px;
    padding: 8px 16px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .ios-glass-btn:hover {{
    background: var(--glass-bg-hover);
    border-color: var(--glass-border-highlight);
    transform: scale(1.02);
  }}

  /* iOS Search Bar (Glass Pill) */
  .search-area {{
    margin: 28px 0 16px 0;
  }}

  .ios-search-bar {{
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    box-shadow: 0 10px 30px rgba(0,0,0,0.15), var(--glass-specular);
    border-radius: 9999px;
    padding: 6px 16px 6px 20px;
    display: flex;
    align-items: center;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .ios-search-bar:focus-within {{
    border-color: var(--ios-blue);
    background: var(--glass-bg-hover);
    box-shadow: 0 12px 36px rgba(10, 132, 255, 0.25), var(--glass-specular);
    transform: translateY(-1px);
  }}

  .search-icon {{
    color: var(--ios-blue);
    font-size: 24px;
    margin-right: 12px;
  }}

  .ios-search-input {{
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1.05rem;
    font-family: inherit;
    color: var(--text-primary);
  }}

  .ios-search-input::placeholder {{
    color: var(--text-tertiary);
    font-weight: 400;
  }}

  .clear-btn {{
    background: var(--segmented-bg);
    border: none;
    color: var(--text-secondary);
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 16px;
    transition: background 0.2s;
  }}

  .clear-btn:hover {{
    color: var(--text-primary);
  }}

  /* iOS Segmented / Pill Filter Control */
  .segmented-scroll {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 6px 4px 18px 4px;
    scrollbar-width: none;
  }}

  .segmented-scroll::-webkit-scrollbar {{
    display: none;
  }}

  .ios-pill {{
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-specular);
    color: var(--text-secondary);
    padding: 8px 16px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 600;
    white-space: nowrap;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .ios-pill:hover {{
    color: var(--text-primary);
    background: var(--glass-bg-hover);
    border-color: var(--glass-border-highlight);
  }}

  .ios-pill.active {{
    background: var(--ios-blue);
    color: #ffffff;
    border-color: rgba(255, 255, 255, 0.4);
    box-shadow: 0 4px 16px rgba(10, 132, 255, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.4);
  }}

  .ios-pill-danger.active {{
    background: var(--ios-red);
    color: #ffffff;
    border-color: rgba(255, 255, 255, 0.4);
    box-shadow: 0 4px 16px rgba(255, 69, 58, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.4);
  }}

  /* SP Mode Collapsible Frosted Glass Card */
  .sp-card-glass {{
    background: var(--glass-card);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12), var(--glass-specular);
    border-radius: 22px;
    margin-bottom: 24px;
    overflow: hidden;
    transition: all 0.3s ease;
  }}

  .sp-header {{
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    user-select: none;
    background: rgba(255, 255, 255, 0.04);
  }}

  .sp-header h2 {{
    font-size: 1rem;
    font-weight: 700;
    color: var(--ios-blue);
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .sp-grid {{
    padding: 20px;
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
  }}

  @media(min-width: 768px) {{
    .sp-grid {{ grid-template-columns: 1fr 1fr; }}
  }}

  .sp-inner-box {{
    background: rgba(0, 0, 0, 0.2);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 16px;
  }}

  .sp-inner-box h3 {{
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 8px;
  }}

  .sp-inner-box pre {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.5;
    white-space: pre-wrap;
    color: var(--text-secondary);
  }}

  /* Glass Cards Grid */
  .cards-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
  }}

  .ios-glass-card {{
    background: var(--glass-card);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.1), var(--glass-specular);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s, border-color 0.25s;
    position: relative;
  }}

  .ios-glass-card:hover {{
    transform: translateY(-3px);
    border-color: var(--glass-border-highlight);
    box-shadow: 0 18px 48px rgba(0, 0, 0, 0.18), var(--glass-specular);
  }}

  .card-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 14px;
    flex-wrap: wrap;
  }}

  .code-title-group {{
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }}

  .sc-code-badge {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--text-primary);
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--glass-border);
    padding: 4px 14px;
    border-radius: 12px;
    letter-spacing: -0.02em;
  }}

  .sc-title {{
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--text-primary);
  }}

  /* Translucent Glass Badges */
  .glass-badge {{
    font-size: 0.72rem;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 9999px;
    letter-spacing: 0.03em;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    backdrop-filter: blur(10px);
  }}

  .glass-badge-a {{
    background: var(--ios-red-glass);
    color: #ff6b62;
    border: 1px solid var(--ios-red-border);
  }}

  .glass-badge-b {{
    background: var(--ios-amber-glass);
    color: #ffb84d;
    border: 1px solid var(--ios-amber-border);
  }}

  .glass-badge-d {{
    background: var(--ios-blue-glass);
    color: #5ac8fa;
    border: 1px solid var(--ios-blue-border);
  }}

  .glass-badge-reset {{
    background: rgba(225, 29, 72, 0.25);
    color: #ff7597;
    border: 1px solid rgba(225, 29, 72, 0.5);
  }}

  .card-copy-btn {{
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--glass-border);
    color: var(--text-primary);
    border-radius: 9999px;
    padding: 5px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 5px;
    transition: all 0.2s;
  }}

  .card-copy-btn:hover {{
    background: rgba(255, 255, 255, 0.18);
    transform: scale(1.03);
  }}

  .models-row {{
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-bottom: 12px;
  }}

  .section-label {{
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-tertiary);
    margin: 14px 0 6px 0;
  }}

  .glass-symptom-box {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--glass-border);
    border-left: 3px solid var(--ios-blue);
    border-radius: 12px;
    padding: 10px 14px;
    font-size: 0.92rem;
    color: var(--text-primary);
  }}

  ul.glass-list, ol.glass-list {{
    margin-left: 20px;
    font-size: 0.92rem;
    color: var(--text-primary);
  }}

  ul.glass-list li, ol.glass-list li {{
    margin-bottom: 5px;
  }}

  .reset-glass-callout {{
    margin-top: 16px;
    background: var(--ios-red-glass);
    border: 1px solid var(--ios-red-border);
    border-radius: 14px;
    padding: 12px 16px;
    font-size: 0.88rem;
    display: flex;
    align-items: center;
    gap: 10px;
    color: #ffd2cf;
  }}

  /* iOS Floating Dynamic Island Toast */
  .ios-toast {{
    position: fixed;
    top: 24px;
    left: 50%;
    transform: translateX(-50%) translateY(-30px) scale(0.9);
    background: rgba(20, 24, 38, 0.85);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.35), inset 0 1px 1px rgba(255, 255, 255, 0.4);
    color: #ffffff;
    border-radius: 9999px;
    padding: 10px 24px;
    font-size: 0.88rem;
    font-weight: 600;
    opacity: 0;
    pointer-events: none;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 200;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .ios-toast.show {{
    opacity: 1;
    transform: translateX(-50%) translateY(0) scale(1);
  }}

  .empty-state {{
    text-align: center;
    padding: 80px 20px;
    color: var(--text-tertiary);
  }}

  .empty-state span {{
    font-size: 48px;
    color: var(--ios-blue);
  }}
</style>
</head>
<body>

<!-- Ambient Lighting Orbs for Specular Reflection -->
<div class="ambient-glow"></div>

<!-- iOS Frosted Header -->
<header class="ios-header">
  <div class="container header-content">
    <div class="brand">
      <div class="ios-app-icon">R</div>
      <div class="brand-title">
        <h1>Ricoh Diagnostics</h1>
        <p>M · MP · MP C · IM · IM C Series</p>
      </div>
    </div>
    <button class="ios-glass-btn" id="themeToggle" onclick="toggleTheme()">
      <span class="material-symbols-rounded" id="themeIcon">light_mode</span>
      <span id="themeText">Light Glass</span>
    </button>
  </div>
</header>

<main class="container">
  <!-- iOS Search Bar (Glass Capsule) -->
  <div class="search-area">
    <div class="ios-search-bar">
      <span class="material-symbols-rounded search-icon">search</span>
      <input type="text" id="searchInput" class="ios-search-input" placeholder="Search error code (e.g. 542, 672, 899) or component..." autofocus autocomplete="off" />
      <button class="clear-btn" id="clearBtn" onclick="clearSearch()">
        <span class="material-symbols-rounded" style="font-size: 16px;">close</span>
      </button>
    </div>
  </div>

  <!-- iOS Segmented Filter Pills -->
  <div class="segmented-scroll">
    <button class="ios-pill active" onclick="setCategory('ALL')">All Codes</button>
    <button class="ios-pill ios-pill-danger" onclick="filterLevelA()">
      <span class="material-symbols-rounded" style="font-size: 16px;">lock_clock</span> Level A (Reset Required)
    </button>
    <button class="ios-pill" onclick="setCategory('SC100')">SC100 Optics</button>
    <button class="ios-pill" onclick="setCategory('SC200')">SC200 Laser</button>
    <button class="ios-pill" onclick="setCategory('SC300')">SC300 Drum & PCU</button>
    <button class="ios-pill" onclick="setCategory('SC400')">SC400 Transfer</button>
    <button class="ios-pill" onclick="setCategory('SC500')">SC500 Fuser</button>
    <button class="ios-pill" onclick="setCategory('SC600')">SC600 Comm & RFID</button>
    <button class="ios-pill" onclick="setCategory('SC700')">SC700 Finisher</button>
    <button class="ios-pill" onclick="setCategory('SC800')">SC800 Controller/HDD</button>
    <button class="ios-pill" onclick="setCategory('SC900')">SC900 Engine</button>
  </div>

  <!-- SP Mode Frosted Glass Accordion -->
  <section class="sp-card-glass">
    <div class="sp-header" onclick="toggleSPAccordion()">
      <h2>
        <span class="material-symbols-rounded">build</span>
        Service Program (SP) Mode Entry & Fuser Reset Guide
      </h2>
      <span class="material-symbols-rounded" id="spArrow" style="transition: transform 0.25s;">expand_more</span>
    </div>
    <div class="sp-grid" id="spContent" style="display: none;">
      <div class="sp-inner-box">
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
      <div class="sp-inner-box">
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

  <!-- Status Row -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; font-size: 0.85rem; color: var(--text-tertiary);">
    <span id="resultsCount">Loading error codes...</span>
    <span>iOS Glassmorphism Interface</span>
  </div>

  <!-- Glass Cards Grid -->
  <div class="cards-grid" id="cardsGrid"></div>
</main>

<!-- Dynamic Island Toast -->
<div class="ios-toast" id="toast">
  <span class="material-symbols-rounded" style="color: #30d158; font-size: 20px;">check_circle</span>
  <span id="toastMsg">Copied to clipboard!</span>
</div>

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
  document.getElementById('themeText').textContent = isDark ? 'Dark Glass' : 'Light Glass';
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
  document.getElementById('toastMsg').textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2200);
}}

function copyFix(code, title, solutions) {{
  const text = `Ricoh SC Error: ${{code}} - ${{title}}\\n\\nTroubleshooting:\\n${{solutions.map((s, i) => `${{i+1}}. ${{s}}`).join('\\n')}}`;
  navigator.clipboard.writeText(text).then(() => {{
    showToast(`Copied fix for ${{code}}`);
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
        <span class="material-symbols-rounded">search_off</span>
        <h3 style="margin-top: 12px; color: var(--text-primary);">No matching SC codes found</h3>
        <p style="margin-top: 4px;">Search by number (542, 672) or keyword (fuser, laser, motor).</p>
      </div>
    `;
    return;
  }}

  items.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'ios-glass-card';
    card.id = item.code.toLowerCase();

    const causesHtml = item.causes.map(c => `<li>${{c}}</li>`).join('');
    const solutionsHtml = item.solutions.map(s => `<li>${{s}}</li>`).join('');

    let badgeClass = 'glass-badge-d';
    if (item.level === 'A') badgeClass = 'glass-badge-a';
    else if (item.level === 'B') badgeClass = 'glass-badge-b';

    card.innerHTML = `
      <div class="card-top">
        <div class="code-title-group">
          <span class="sc-code-badge">${{item.code}}</span>
          <span class="sc-title">${{item.title}}</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="glass-badge ${{badgeClass}}">Level ${{item.level}}</span>
          ${{item.sp_reset_required ? '<span class="glass-badge glass-badge-reset">SP 5-810 Reset</span>' : ''}}
          <button class="card-copy-btn" onclick='copyFix("${{item.code}}", "${{item.title.replace(/"/g, '&quot;')}}", ${{JSON.stringify(item.solutions)}})'>
            <span class="material-symbols-rounded" style="font-size:16px;">ios_share</span> Copy
          </button>
        </div>
      </div>

      <div class="models-row">
        <strong>Supported Models:</strong> ${{item.models}}
      </div>

      <div class="section-label">Symptom</div>
      <div class="glass-symptom-box">${{item.symptom}}</div>

      <div class="section-label">Probable Causes</div>
      <ul class="glass-list">${{causesHtml}}</ul>

      <div class="section-label">Troubleshooting & Repair</div>
      <ol class="glass-list">${{solutionsHtml}}</ol>

      ${{item.sp_reset_required ? `
        <div class="reset-glass-callout">
          <span class="material-symbols-rounded" style="font-size: 20px;">restart_alt</span>
          <div><strong>SP Mode Reset Required:</strong> ${{item.sp_reset_guide}}</div>
        </div>
      ` : ''}}
    `;
    grid.appendChild(card);
  }});
}}

function applyFilter() {{
  const query = document.getElementById('searchInput').value.trim().toLowerCase();
  const clearBtn = document.getElementById('clearBtn');
  clearBtn.style.display = query.length > 0 ? 'flex' : 'none';

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
  document.querySelectorAll('.ios-pill').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  applyFilter();
}}

function filterLevelA() {{
  filterOnlyLevelA = true;
  currentCategory = 'ALL';
  document.querySelectorAll('.ios-pill').forEach(btn => btn.classList.remove('active'));
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
    print(f"Generated iOS Glassy HTML guide at: {output_path}")

if __name__ == "__main__":
    generate_html_file()
