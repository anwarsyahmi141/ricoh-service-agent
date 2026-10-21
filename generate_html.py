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
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Ricoh SC Diagnostics | iOS Glass UI</title>

<!-- PWA Meta Tags -->
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#060810">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Ricoh SC">
<link rel="apple-touch-icon" href="icon.svg">
<link rel="icon" type="image/svg+xml" href="icon.svg">

<!-- Google Fonts: Plus Jakarta Sans, JetBrains Mono, & Icons -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />

<style>
  /* ================= Pure Coffee Color Scheme ================= */
  /* Palette: #6E4E36 (Coffee), #F0E3B4 (Cream), #724444 (Mocha), #603B39 (Roast), #482B29 (Dark Roast), #2C2323 (Espresso) */
  :root[data-theme="dark"] {{
    --bg-base: #1e1717;
    --text-primary: #F0E3B4;
    --text-secondary: rgba(240, 227, 180, 0.76);
    --text-tertiary: rgba(240, 227, 180, 0.48);
    
    --glass-bg: rgba(44, 35, 35, 0.58);
    --glass-bg-hover: rgba(72, 43, 41, 0.75);
    --glass-card: rgba(44, 35, 35, 0.68);
    --glass-border: rgba(240, 227, 180, 0.14);
    --glass-border-highlight: rgba(240, 227, 180, 0.32);
    --glass-specular: inset 0 1px 1px 0 rgba(240, 227, 180, 0.22);
    --glass-blur: blur(28px) saturate(190%);
    
    --ios-blue: #F0E3B4;
    --ios-blue-glass: rgba(240, 227, 180, 0.18);
    --ios-blue-border: rgba(240, 227, 180, 0.45);
    
    --ios-red: #e05353;
    --ios-red-glass: rgba(224, 83, 83, 0.22);
    --ios-red-border: rgba(224, 83, 83, 0.5);

    --ios-amber: #e8a355;
    --ios-amber-glass: rgba(232, 163, 85, 0.22);
    --ios-amber-border: rgba(232, 163, 85, 0.45);

    --ios-green: #59b87a;
    --segmented-bg: rgba(240, 227, 180, 0.08);
    --orb-1: radial-gradient(circle at 15% 20%, rgba(110, 78, 54, 0.4) 0%, transparent 45%);
    --orb-2: radial-gradient(circle at 85% 15%, rgba(114, 68, 68, 0.38) 0%, transparent 45%);
    --orb-3: radial-gradient(circle at 50% 80%, rgba(240, 227, 180, 0.16) 0%, transparent 50%);
  }}

  :root[data-theme="light"] {{
    --bg-base: #f9f6f0;
    --text-primary: #2C2323;
    --text-secondary: #603B39;
    --text-tertiary: #6E4E36;

    --glass-bg: rgba(240, 227, 180, 0.55);
    --glass-bg-hover: rgba(240, 227, 180, 0.85);
    --glass-card: rgba(255, 255, 255, 0.76);
    --glass-border: rgba(110, 78, 54, 0.18);
    --glass-border-highlight: rgba(110, 78, 54, 0.38);
    --glass-specular: inset 0 1px 1px 0 rgba(255, 255, 255, 0.95);
    --glass-blur: blur(28px) saturate(180%);

    --ios-blue: #6E4E36;
    --ios-blue-glass: rgba(110, 78, 54, 0.15);
    --ios-blue-border: rgba(110, 78, 54, 0.35);

    --ios-red: #c93434;
    --ios-red-glass: rgba(201, 52, 52, 0.14);
    --ios-red-border: rgba(201, 52, 52, 0.35);

    --ios-amber: #b86e1e;
    --ios-amber-glass: rgba(184, 110, 30, 0.14);
    --ios-amber-border: rgba(184, 110, 30, 0.35);

    --ios-green: #2d8a4e;
    --segmented-bg: rgba(44, 35, 35, 0.06);
    --orb-1: radial-gradient(circle at 10% 20%, rgba(240, 227, 180, 0.55) 0%, transparent 45%);
    --orb-2: radial-gradient(circle at 85% 20%, rgba(114, 68, 68, 0.18) 0%, transparent 45%);
    --orb-3: radial-gradient(circle at 50% 85%, rgba(110, 78, 54, 0.18) 0%, transparent 50%);
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
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 18px;
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
    padding: 14px 0;
    transition: all 0.3s ease;
  }}

  .header-content {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }}

  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .ios-app-icon {{
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: linear-gradient(145deg, #6E4E36, #482B29);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #F0E3B4;
    font-weight: 800;
    font-size: 1.15rem;
    box-shadow: 0 8px 16px rgba(44, 35, 35, 0.45), inset 0 1px 1px rgba(240, 227, 180, 0.5);
    letter-spacing: -0.05em;
  }}

  .brand-title h1 {{
    font-size: 1.2rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    color: var(--text-primary);
  }}

  .brand-title p {{
    font-size: 0.76rem;
    color: var(--text-secondary);
    font-weight: 500;
  }}

  .header-actions {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .ios-glass-btn {{
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    color: var(--text-primary);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-specular);
    border-radius: 9999px;
    padding: 7px 14px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .ios-glass-btn:hover {{
    background: var(--glass-bg-hover);
    border-color: var(--glass-border-highlight);
    transform: scale(1.02);
  }}

  /* iOS Search Bar (Glass Pill) */
  .search-area {{
    margin: 22px 0 12px 0;
  }}

  .ios-search-bar {{
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    box-shadow: 0 10px 30px rgba(0,0,0,0.12), var(--glass-specular);
    border-radius: 9999px;
    padding: 6px 16px 6px 18px;
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

  /* Filter Bars (Model Filter + Category Filter) */
  .filter-section-title {{
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-tertiary);
    margin: 12px 0 6px 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .segmented-scroll {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 2px 2px 10px 2px;
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
    padding: 7px 14px;
    border-radius: 9999px;
    font-size: 0.82rem;
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
    background: #6E4E36;
    color: #F0E3B4;
    border-color: rgba(240, 227, 180, 0.45);
    box-shadow: 0 4px 14px rgba(110, 78, 54, 0.45), inset 0 1px 1px rgba(240, 227, 180, 0.4);
  }}

  .ios-pill-model.active {{
    background: #724444;
    color: #F0E3B4;
    border-color: rgba(240, 227, 180, 0.45);
    box-shadow: 0 4px 14px rgba(114, 68, 68, 0.45), inset 0 1px 1px rgba(240, 227, 180, 0.4);
  }}

  .ios-pill-danger.active {{
    background: #603B39;
    color: #F0E3B4;
    border-color: rgba(240, 227, 180, 0.45);
    box-shadow: 0 4px 14px rgba(96, 59, 57, 0.45), inset 0 1px 1px rgba(240, 227, 180, 0.4);
  }}

  /* SP Mode Keypad Simulator Section */
  .sp-card-glass {{
    background: var(--glass-card);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12), var(--glass-specular);
    border-radius: 22px;
    margin: 14px 0 24px 0;
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
    gap: 20px;
  }}

  @media(min-width: 900px) {{
    .sp-grid {{ grid-template-columns: 1fr 1fr; }}
  }}

  .simulator-panel {{
    background: rgba(0, 0, 0, 0.28);
    border: 1px solid var(--glass-border);
    border-radius: 18px;
    padding: 16px;
  }}

  .sim-title {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }}

  .sim-title h3 {{
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-primary);
  }}

  .sim-screen {{
    background: #000;
    color: #30d158;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    padding: 10px 14px;
    border-radius: 10px;
    border: 1px solid #1c2b1e;
    margin-bottom: 14px;
    min-height: 44px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.8);
  }}

  .keypad-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    max-width: 240px;
    margin: 0 auto 12px auto;
  }}

  .kp-btn {{
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    color: var(--text-primary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.15rem;
    font-weight: 700;
    border-radius: 12px;
    padding: 12px 0;
    cursor: pointer;
    box-shadow: var(--glass-specular);
    transition: all 0.15s ease;
    user-select: none;
  }}

  .kp-btn:active, .kp-btn.active {{
    background: var(--ios-blue);
    color: white;
    transform: scale(0.94);
    box-shadow: 0 0 16px var(--ios-blue);
  }}

  .kp-btn-yellow {{
    background: rgba(234, 179, 8, 0.25);
    color: #fde047;
    border-color: rgba(234, 179, 8, 0.5);
    font-size: 0.82rem;
  }}
  .kp-btn-yellow.active {{
    background: #eab308 !important;
    color: black !important;
    box-shadow: 0 0 16px #eab308 !important;
  }}

  .kp-btn-red {{
    background: rgba(239, 68, 68, 0.25);
    color: #fca5a5;
    border-color: rgba(239, 68, 68, 0.5);
    font-size: 0.82rem;
  }}
  .kp-btn-red.active {{
    background: #ef4444 !important;
    color: white !important;
    box-shadow: 0 0 16px #ef4444 !important;
  }}

  .sim-controls {{
    display: flex;
    justify-content: center;
    gap: 10px;
  }}

  .sim-action-btn {{
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--glass-border);
    color: var(--text-primary);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.78rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }}

  .sim-action-btn:hover {{
    background: var(--glass-bg-hover);
    transform: scale(1.02);
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
    transform: translateY(-2px);
    border-color: var(--glass-border-highlight);
    box-shadow: 0 18px 48px rgba(0, 0, 0, 0.16), var(--glass-specular);
  }}

  .card-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 14px;
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
    font-weight: 800;
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

  .card-actions {{
    display: flex;
    gap: 6px;
    align-items: center;
    flex-wrap: wrap;
  }}

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
    color: var(--text-primary);
    border: 1px solid var(--ios-blue-border);
  }}

  .glass-badge-reset {{
    background: rgba(114, 68, 68, 0.4);
    color: #ffd4d4;
    border: 1px solid rgba(114, 68, 68, 0.7);
  }}

  .card-action-btn {{
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--glass-border);
    color: var(--text-primary);
    border-radius: 9999px;
    padding: 5px 12px;
    font-size: 0.76rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 5px;
    transition: all 0.2s;
  }}

  .card-action-btn:hover {{
    background: rgba(255, 255, 255, 0.18);
    transform: scale(1.03);
  }}

  .card-action-ticket {{
    background: rgba(110, 78, 54, 0.25);
    border-color: rgba(110, 78, 54, 0.5);
    color: var(--text-primary);
  }}

  .models-row {{
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-bottom: 12px;
  }}

  .section-label {{
    font-size: 0.74rem;
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

  /* iOS Dynamic Island Toast */
  .ios-toast {{
    position: fixed;
    top: 24px;
    left: 50%;
    transform: translateX(-50%) translateY(-30px) scale(0.9);
    background: rgba(20, 24, 38, 0.88);
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

  /* ================= Printable Service Ticket Modal ================= */
  .modal-backdrop {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(12px);
    z-index: 300;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}

  .modal-backdrop.open {{
    display: flex;
  }}

  .ticket-card {{
    background: #ffffff;
    color: #111827;
    width: 100%;
    max-width: 640px;
    max-height: 90vh;
    overflow-y: auto;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 24px 60px rgba(0,0,0,0.5);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}

  .ticket-header {{
    border-bottom: 2px solid #e5e7eb;
    padding-bottom: 14px;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .ticket-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: #111827;
  }}

  .ticket-badge {{
    background: #6E4E36;
    color: #F0E3B4;
    font-weight: 800;
    font-size: 0.75rem;
    padding: 4px 10px;
    border-radius: 6px;
  }}

  .ticket-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 16px;
    font-size: 0.85rem;
  }}

  .ticket-section-title {{
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
    color: #4b5563;
    margin: 12px 0 6px 0;
  }}

  .ticket-list {{
    margin-left: 20px;
    font-size: 0.88rem;
    color: #374151;
    line-height: 1.45;
  }}

  .ticket-list li {{
    margin-bottom: 4px;
  }}

  .ticket-sign-block {{
    margin-top: 24px;
    border-top: 1px dashed #9ca3af;
    padding-top: 16px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    font-size: 0.8rem;
    color: #4b5563;
  }}

  .sign-line {{
    border-bottom: 1px solid #000;
    height: 30px;
    margin-bottom: 4px;
  }}

  .ticket-actions {{
    margin-top: 20px;
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }}

  .btn-print {{
    background: #6E4E36;
    color: #F0E3B4;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 700;
    cursor: pointer;
  }}

  .btn-close {{
    background: #e5e7eb;
    color: #374151;
    border: none;
    border-radius: 10px;
    padding: 10px 16px;
    font-weight: 600;
    cursor: pointer;
  }}

  /* Print Stylesheet for Saving as Clean PDF */
  @media print {{
    body * {{
      visibility: hidden;
    }}
    .modal-backdrop, .modal-backdrop * {{
      visibility: visible;
    }}
    .modal-backdrop {{
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: auto;
      background: #fff !important;
      padding: 0 !important;
    }}
    .ticket-card {{
      box-shadow: none !important;
      border: none !important;
      width: 100% !important;
      max-width: 100% !important;
      padding: 0 !important;
    }}
    .ticket-actions {{
      display: none !important;
    }}
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
    <div class="header-actions">
      <button class="ios-glass-btn" id="installBtn" style="display: none;" onclick="installPWA()">
        <span class="material-symbols-rounded">download</span>
        <span>Install App</span>
      </button>
      <button class="ios-glass-btn" id="themeToggle" onclick="toggleTheme()">
        <span class="material-symbols-rounded" id="themeIcon">light_mode</span>
        <span id="themeText">Light Glass</span>
      </button>
    </div>
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

  <!-- Model Series Filter Bar (Option 3) -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin: 14px 4px 6px 4px;">
    <div class="filter-section-title" style="margin: 0;">
      <span class="material-symbols-rounded" style="font-size: 16px;">print</span> Filter by Ricoh Machine Series
    </div>
    <button class="ios-glass-btn" onclick="resetAllFilters()" style="padding: 4px 12px; font-size: 0.75rem; border-color: rgba(255,255,255,0.2);">
      <span class="material-symbols-rounded" style="font-size: 14px; color: var(--ios-amber);">restart_alt</span> Reset All Filters
    </button>
  </div>
  <div class="segmented-scroll" id="modelFilterBar">
    <button class="ios-pill ios-pill-model active" onclick="setModelFilter('ALL', event)">All Models</button>
    <button class="ios-pill ios-pill-model" onclick="setModelFilter('M', event)">M Series</button>
    <button class="ios-pill ios-pill-model" onclick="setModelFilter('MP', event)">MP Series (Mono)</button>
    <button class="ios-pill ios-pill-model" onclick="setModelFilter('MP_C', event)">MP C (Color)</button>
    <button class="ios-pill ios-pill-model" onclick="setModelFilter('IM', event)">IM Series (Smart Mono)</button>
    <button class="ios-pill ios-pill-model" onclick="setModelFilter('IM_C', event)">IM C (Smart Color)</button>
  </div>

  <!-- Subsystem Category Filter Bar -->
  <div class="filter-section-title">
    <span class="material-symbols-rounded" style="font-size: 16px;">category</span> Subsystem Category
  </div>
  <div class="segmented-scroll" id="categoryFilterBar">
    <button class="ios-pill active" onclick="setCategory('ALL', event)">All Categories</button>
    <button class="ios-pill ios-pill-danger" onclick="filterLevelA(event)">
      <span class="material-symbols-rounded" style="font-size: 16px;">lock_clock</span> Level A (Reset Required)
    </button>
    <button class="ios-pill" onclick="setCategory('SC100', event)">SC100 Optics</button>
    <button class="ios-pill" onclick="setCategory('SC200', event)">SC200 Laser</button>
    <button class="ios-pill" onclick="setCategory('SC300', event)">SC300 Drum & PCU</button>
    <button class="ios-pill" onclick="setCategory('SC400', event)">SC400 Transfer</button>
    <button class="ios-pill" onclick="setCategory('SC500', event)">SC500 Fuser</button>
    <button class="ios-pill" onclick="setCategory('SC600', event)">SC600 Comm & RFID</button>
    <button class="ios-pill" onclick="setCategory('SC700', event)">SC700 Finisher</button>
    <button class="ios-pill" onclick="setCategory('SC800', event)">SC800 Controller/HDD</button>
    <button class="ios-pill" onclick="setCategory('SC900', event)">SC900 Engine</button>
  </div>

  <!-- Visual SP Mode Keypad Simulator Section (Option 6) -->
  <section class="sp-card-glass">
    <div class="sp-header" onclick="toggleSPAccordion()">
      <h2>
        <span class="material-symbols-rounded">dialpad</span>
        Interactive SP Mode Keypad Simulator & Reset Cheatsheet
      </h2>
      <span class="material-symbols-rounded" id="spArrow" style="transition: transform 0.25s;">expand_more</span>
    </div>
    
    <div class="sp-grid" id="spContent" style="display: none;">
      <!-- Classic Keypad Simulator -->
      <div class="simulator-panel">
        <div class="sim-title">
          <h3>Classic Hardware Keypad (MP & M Series)</h3>
          <span style="font-size: 0.75rem; color: var(--ios-amber); font-weight: 600;">10-Key Sequence</span>
        </div>
        <div class="sim-screen" id="classicScreen">
          <span id="classicStatus">READY. PRESS YELLOW KEY</span>
          <span id="classicSeq" style="color: #60a5fa;">[ _ _ _ ]</span>
        </div>
        <div class="keypad-grid">
          <button class="kp-btn" onclick="pressClassicKey('1')">1</button>
          <button class="kp-btn" onclick="pressClassicKey('2')">2</button>
          <button class="kp-btn" onclick="pressClassicKey('3')">3</button>
          <button class="kp-btn" onclick="pressClassicKey('4')">4</button>
          <button class="kp-btn" onclick="pressClassicKey('5')">5</button>
          <button class="kp-btn" onclick="pressClassicKey('6')">6</button>
          <button class="kp-btn" onclick="pressClassicKey('7')">7</button>
          <button class="kp-btn" onclick="pressClassicKey('8')">8</button>
          <button class="kp-btn" onclick="pressClassicKey('9')">9</button>
          <button class="kp-btn kp-btn-yellow" id="btnYellow" onclick="pressClassicKey('CLEAR_MODES')">CLEAR</button>
          <button class="kp-btn" onclick="pressClassicKey('0')">0</button>
          <button class="kp-btn kp-btn-red" id="btnRed" onclick="pressClassicKey('HOLD_STOP')">STOP</button>
        </div>
        <div class="sim-controls">
          <button class="sim-action-btn" onclick="playClassicSequence()">
            <span class="material-symbols-rounded" style="font-size:16px;">play_arrow</span> Auto-Play Sequence
          </button>
          <button class="sim-action-btn" onclick="resetClassicKeypad()">
            <span class="material-symbols-rounded" style="font-size:16px;">refresh</span> Reset
          </button>
        </div>
      </div>

      <!-- Smart Operation Panel (SOP) Keypad Simulator -->
      <div class="simulator-panel">
        <div class="sim-title">
          <h3>Smart Operation Panel (IM & IM C Series)</h3>
          <span style="font-size: 0.75rem; color: var(--ios-blue); font-weight: 600;">SOP Virtual Keypad</span>
        </div>
        <div class="sim-screen" id="sopScreen">
          <span id="sopStatus">READY: TAP RESET</span>
          <span id="sopSeq" style="color: #a78bfa;">[ 806182 ]</span>
        </div>
        <div class="keypad-grid">
          <button class="kp-btn" onclick="pressSopKey('8')">8</button>
          <button class="kp-btn" onclick="pressSopKey('0')">0</button>
          <button class="kp-btn" onclick="pressSopKey('6')">6</button>
          <button class="kp-btn" onclick="pressSopKey('1')">1</button>
          <button class="kp-btn" onclick="pressSopKey('8')">8</button>
          <button class="kp-btn" onclick="pressSopKey('2')">2</button>
          <button class="kp-btn kp-btn-yellow" id="btnSopReset" onclick="pressSopKey('RESET')">RESET</button>
          <button class="kp-btn" onclick="pressSopKey('#')">#</button>
          <button class="kp-btn kp-btn-red" id="btnSopC" onclick="pressSopKey('HOLD_C')">HOLD C</button>
        </div>
        <div class="sim-controls">
          <button class="sim-action-btn" onclick="playSopSequence()">
            <span class="material-symbols-rounded" style="font-size:16px;">play_arrow</span> Auto-Play Sequence
          </button>
          <button class="sim-action-btn" onclick="resetSopKeypad()">
            <span class="material-symbols-rounded" style="font-size:16px;">refresh</span> Reset
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Status Bar -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; font-size: 0.85rem; color: var(--text-tertiary);">
    <span id="resultsCount">Loading error codes...</span>
    <span>iOS Glass Interface · PWA Ready</span>
  </div>

  <!-- Glass Cards Grid -->
  <div class="cards-grid" id="cardsGrid"></div>
</main>

<!-- Printable Service Ticket Modal (Option 5) -->
<div class="modal-backdrop" id="ticketModal" onclick="closeTicketOnBackdrop(event)">
  <div class="ticket-card" id="ticketCard">
    <div class="ticket-header">
      <div>
        <div class="ticket-badge">RICOH MFP SERVICE TICKET</div>
        <div class="ticket-title" id="tktCodeTitle" style="margin-top:6px;">SC542 - Warm-up Timeout</div>
      </div>
      <div style="text-align:right; font-size:0.75rem; color:#6b7280;">
        <div id="tktDate">Date: 2026-10-21</div>
        <div id="tktNum" style="font-family:'JetBrains Mono'; font-weight:700;">#RST-542-8821</div>
      </div>
    </div>

    <div class="ticket-grid">
      <div><strong>Severity Level:</strong> <span id="tktLevel">Level A (Reset Required)</span></div>
      <div><strong>Reset SP Code:</strong> <span id="tktSP">SP 5-810-001</span></div>
      <div style="grid-column: span 2;"><strong>Target Models:</strong> <span id="tktModels">M, MP, MP C, IM, IM C series</span></div>
    </div>

    <div class="ticket-section-title">Detected Symptom</div>
    <p id="tktSymptom" style="font-size:0.88rem; background:#f3f4f6; padding:8px 12px; border-radius:6px; margin-bottom:12px;"></p>

    <div class="ticket-section-title">Probable Root Causes</div>
    <ul class="ticket-list" id="tktCauses"></ul>

    <div class="ticket-section-title" style="margin-top:14px;">Technician Action Checklist</div>
    <ul class="ticket-list" id="tktSolutions"></ul>

    <div class="ticket-sign-block">
      <div>
        <div class="sign-line"></div>
        <div>Field Service Technician Signature</div>
      </div>
      <div>
        <div class="sign-line"></div>
        <div>Customer / Clerk Sign-Off</div>
      </div>
    </div>

    <div class="ticket-actions">
      <button class="btn-close" onclick="closeTicket()">Close</button>
      <button class="btn-print" onclick="window.print()">
        <span class="material-symbols-rounded" style="font-size:16px; vertical-align:middle; margin-right:4px;">print</span> Print / Save PDF
      </button>
    </div>
  </div>
</div>

<!-- Dynamic Island Toast -->
<div class="ios-toast" id="toast">
  <span class="material-symbols-rounded" style="color: #30d158; font-size: 20px;">check_circle</span>
  <span id="toastMsg">Copied to clipboard!</span>
</div>

<script>
const scData = {codes_json};
let currentCategory = 'ALL';
let currentModelFilter = 'ALL';
let filterOnlyLevelA = false;

// Self-clearing cache script: ensure browser never gets stuck on old Service Worker cache
if ('serviceWorker' in navigator) {{
  navigator.serviceWorker.getRegistrations().then(function(registrations) {{
    for (let registration of registrations) {{
      registration.unregister();
    }}
  }});
}}
if ('caches' in window) {{
  caches.keys().then(function(names) {{
    for (let name of names) {{
      caches.delete(name);
    }}
  }});
}}

// Handle PWA Install Prompt
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {{
  e.preventDefault();
  deferredPrompt = e;
  document.getElementById('installBtn').style.display = 'flex';
}});

function installPWA() {{
  if (deferredPrompt) {{
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choice) => {{
      if (choice.outcome === 'accepted') {{
        document.getElementById('installBtn').style.display = 'none';
      }}
      deferredPrompt = null;
    }});
  }} else {{
    showToast('Add to Home Screen from browser menu');
  }}
}}

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

// Service Ticket / PDF Modal (Option 5)
function openServiceTicket(item) {{
  document.getElementById('tktCodeTitle').textContent = `${{item.code}} - ${{item.title}}`;
  document.getElementById('tktLevel').textContent = `Level ${{item.level}} ${{item.sp_reset_required ? '(Reset Required)' : '(Auto Reset)'}}`;
  document.getElementById('tktSP').textContent = item.sp_reset_required ? 'SP 5-810-001' : 'None (Cycle Power)';
  document.getElementById('tktModels').textContent = item.models;
  document.getElementById('tktSymptom').textContent = item.symptom;
  
  const today = new Date().toISOString().slice(0, 10);
  const randNum = Math.floor(1000 + Math.random() * 9000);
  document.getElementById('tktDate').textContent = `Date: ${{today}}`;
  document.getElementById('tktNum').textContent = `#RST-${{item.code.replace('SC','')}}-${{randNum}}`;

  document.getElementById('tktCauses').innerHTML = item.causes.map(c => `<li>${{c}}</li>`).join('');
  document.getElementById('tktSolutions').innerHTML = item.solutions.map(s => `<li>[  ] ${{s}}</li>`).join('');

  document.getElementById('ticketModal').classList.add('open');
}}

function closeTicket() {{
  document.getElementById('ticketModal').classList.remove('open');
}}

function closeTicketOnBackdrop(e) {{
  if (e.target.id === 'ticketModal') {{
    closeTicket();
  }}
}}

// Keypad Simulator Logic (Option 6)
let classicStep = 0;
function pressClassicKey(key) {{
  const status = document.getElementById('classicStatus');
  const seq = document.getElementById('classicSeq');

  if (key === 'CLEAR_MODES') {{
    classicStep = 1;
    status.textContent = 'ENTER 1-0-7';
    seq.textContent = '[ C ]';
  }} else if (classicStep === 1 && key === '1') {{
    classicStep = 2;
    seq.textContent = '[ C 1 ]';
  }} else if (classicStep === 2 && key === '0') {{
    classicStep = 3;
    seq.textContent = '[ C 1 0 ]';
  }} else if (classicStep === 3 && key === '7') {{
    classicStep = 4;
    status.textContent = 'NOW HOLD STOP KEY (3s)';
    seq.textContent = '[ C 1 0 7 ]';
  }} else if (classicStep === 4 && key === 'HOLD_STOP') {{
    classicStep = 5;
    status.textContent = 'ACCESS GRANTED: SYSTEM SP';
    status.style.color = '#38bdf8';
    seq.textContent = 'SUCCESS: SP 5-810 UNLOCKED';
    showToast('SP Mode Unlocked!');
  }} else {{
    status.textContent = 'SEQUENCE MISMATCH. TAP CLEAR';
    seq.textContent = '[ ERROR ]';
    classicStep = 0;
  }}
}}

function resetClassicKeypad() {{
  classicStep = 0;
  const status = document.getElementById('classicStatus');
  status.textContent = 'READY. PRESS YELLOW KEY';
  status.style.color = '#30d158';
  document.getElementById('classicSeq').textContent = '[ _ _ _ ]';
}}

function playClassicSequence() {{
  resetClassicKeypad();
  const steps = [
    () => pressClassicKey('CLEAR_MODES'),
    () => pressClassicKey('1'),
    () => pressClassicKey('0'),
    () => pressClassicKey('7'),
    () => pressClassicKey('HOLD_STOP')
  ];
  steps.forEach((fn, idx) => {{
    setTimeout(fn, (idx + 1) * 600);
  }});
}}

// SOP Keypad Simulator
let sopStep = 0;
function pressSopKey(key) {{
  const status = document.getElementById('sopStatus');
  const seq = document.getElementById('sopSeq');

  if (key === 'RESET') {{
    sopStep = 1;
    status.textContent = 'ENTER 806182';
    seq.textContent = '[ RESET ]';
  }} else if (sopStep === 1 && key === '8') {{
    sopStep = 2;
    seq.textContent = '[ 8 ]';
  }} else if (sopStep === 2 && key === '0') {{
    sopStep = 3;
    seq.textContent = '[ 80 ]';
  }} else if (sopStep === 3 && key === '6') {{
    sopStep = 4;
    seq.textContent = '[ 806 ]';
  }} else if (sopStep === 4 && key === '1') {{
    sopStep = 5;
    seq.textContent = '[ 8061 ]';
  }} else if (sopStep === 5 && key === '8') {{
    sopStep = 6;
    seq.textContent = '[ 80618 ]';
  }} else if (sopStep === 6 && key === '2') {{
    sopStep = 7;
    status.textContent = 'NOW HOLD [C] KEY (3s)';
    seq.textContent = '[ 806182 ]';
  }} else if (sopStep === 7 && key === 'HOLD_C') {{
    sopStep = 8;
    status.textContent = 'ACCESS GRANTED: SYSTEM SP';
    status.style.color = '#38bdf8';
    seq.textContent = 'SOP UNLOCKED';
    showToast('SOP Mode Unlocked!');
  }}
}}

function resetSopKeypad() {{
  sopStep = 0;
  const status = document.getElementById('sopStatus');
  status.textContent = 'READY: TAP RESET';
  status.style.color = '#30d158';
  document.getElementById('sopSeq').textContent = '[ 806182 ]';
}}

function playSopSequence() {{
  resetSopKeypad();
  const steps = [
    () => pressSopKey('RESET'),
    () => pressSopKey('8'),
    () => pressSopKey('0'),
    () => pressSopKey('6'),
    () => pressSopKey('1'),
    () => pressSopKey('8'),
    () => pressSopKey('2'),
    () => pressSopKey('HOLD_C')
  ];
  steps.forEach((fn, idx) => {{
    setTimeout(fn, (idx + 1) * 500);
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
        <p style="margin-top: 4px;">Try adjusting the Model Filter or searching by keyword.</p>
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
        <div class="card-actions">
          <span class="glass-badge ${{badgeClass}}">Level ${{item.level}}</span>
          ${{item.sp_reset_required ? '<span class="glass-badge glass-badge-reset">SP 5-810 Reset</span>' : ''}}
          <button class="card-action-btn card-action-ticket" onclick='openServiceTicket(${{JSON.stringify(item)}})'>
            <span class="material-symbols-rounded" style="font-size:15px;">receipt_long</span> Ticket / PDF
          </button>
          <button class="card-action-btn" onclick='copyFix("${{item.code}}", "${{item.title.replace(/"/g, '&quot;')}}", ${{JSON.stringify(item.solutions)}})'>
            <span class="material-symbols-rounded" style="font-size:15px;">ios_share</span> Copy
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

      <div class="section-label">Troubleshooting & Repair Sequence</div>
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

function checkModelMatch(modelsStr, key) {{
  if (key === 'ALL') return true;
  const m = modelsStr.toUpperCase();
  if (key === 'M') return /\\bM\\b(?!\\s*P)/.test(m);
  if (key === 'MP') return /\\bMP\\b(?!\\s*C)/.test(m);
  if (key === 'MP_C') return m.includes('MP C');
  if (key === 'IM') return /\\bIM\\b(?!\\s*C)/.test(m);
  if (key === 'IM_C') return m.includes('IM C');
  return true;
}}

function applyFilter() {{
  const query = document.getElementById('searchInput').value.trim().toLowerCase();
  const clearBtn = document.getElementById('clearBtn');
  clearBtn.style.display = query.length > 0 ? 'flex' : 'none';

  const filtered = scData.filter(item => {{
    const matchesCategory = currentCategory === 'ALL' || item.category.startsWith(currentCategory);
    const matchesModel = checkModelMatch(item.models, currentModelFilter);
    const matchesLevel = !filterOnlyLevelA || item.sp_reset_required || item.level === 'A';
    
    if (!matchesCategory || !matchesModel || !matchesLevel) return false;
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

function setCategory(cat, ev) {{
  currentCategory = cat;
  filterOnlyLevelA = false;
  document.querySelectorAll('#categoryFilterBar .ios-pill').forEach(btn => btn.classList.remove('active'));
  if (ev && ev.currentTarget) {{
    ev.currentTarget.classList.add('active');
  }}
  applyFilter();
}}

function setModelFilter(model, ev) {{
  currentModelFilter = model;
  document.querySelectorAll('#modelFilterBar .ios-pill').forEach(btn => btn.classList.remove('active'));
  if (ev && ev.currentTarget) {{
    ev.currentTarget.classList.add('active');
  }}
  applyFilter();
}}

function filterLevelA(ev) {{
  filterOnlyLevelA = true;
  currentCategory = 'ALL';
  document.querySelectorAll('#categoryFilterBar .ios-pill').forEach(btn => btn.classList.remove('active'));
  if (ev && ev.currentTarget) {{
    ev.currentTarget.classList.add('active');
  }}
  applyFilter();
}}

function resetAllFilters() {{
  currentCategory = 'ALL';
  currentModelFilter = 'ALL';
  filterOnlyLevelA = false;
  document.getElementById('searchInput').value = '';
  document.getElementById('clearBtn').style.display = 'none';

  // Reset Model bar buttons
  document.querySelectorAll('#modelFilterBar .ios-pill').forEach(btn => btn.classList.remove('active'));
  const firstModelBtn = document.querySelector('#modelFilterBar .ios-pill');
  if (firstModelBtn) firstModelBtn.classList.add('active');

  // Reset Category bar buttons
  document.querySelectorAll('#categoryFilterBar .ios-pill').forEach(btn => btn.classList.remove('active'));
  const firstCatBtn = document.querySelector('#categoryFilterBar .ios-pill');
  if (firstCatBtn) firstCatBtn.classList.add('active');

  applyFilter();
  showToast('All filters reset: Showing all SC codes');
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
    print(f"Generated Enhanced iOS Glassy HTML guide at: {output_path}")

if __name__ == "__main__":
    generate_html_file()
