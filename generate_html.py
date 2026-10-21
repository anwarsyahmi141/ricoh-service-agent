import json
import os
from ricoh_database import SC_CODES, SP_MODE_PROCEDURES

def generate_html_file(output_path="C:\\Users\\kaze\\ricoh-service-agent\\ricoh_sc_guide.html"):
    codes_json = json.dumps(SC_CODES)
    sp_json = json.dumps(SP_MODE_PROCEDURES)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="matte-black">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Ricoh SC Diagnostics | Omarchy Matte Black</title>

<!-- PWA Meta Tags -->
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#0d0d0d">
<meta name="color-scheme" content="dark">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Ricoh SC">
<link rel="apple-touch-icon" href="icon.svg">
<link rel="icon" type="image/svg+xml" href="icon.svg">

<!-- Omarchy OS Fonts: Geist & JetBrains Mono -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />

<style>
  /* ================= Omarchy OS Matte Black Theme ================= */
  :root, [data-theme="matte-black"] {{
    --t-bg-deep: #0d0d0d;
    --t-bg: #121212;
    --t-surface: #181818;
    --t-surface-2: #1e1e1e;
    --t-border-subtle: #1e1e1e;
    --t-border-strong: #333333;
    --t-text: #eaeaea;
    --t-text-secondary: #bebebe;
    --t-text-muted: #8a8a8a;
    --t-brand: #e68e0d;
    --t-brand-soft: rgba(230, 142, 13, 0.12);
    --t-brand-ink: #0c0e10;
    --t-elevation: 0 0 0 1px rgba(255, 255, 255, 0.07);
    --t-elevation-hover: 0 0 0 1px rgba(255, 255, 255, 0.13), 0 8px 24px rgba(0, 0, 0, 0.6);
    --t-selection: #2a2a2a;
    --t-field-bg: #090909;
    --t-field-dim: #4b310a;
    --t-field-mid: #925b0b;
    --t-field-lit: #e68e0d;
    --t-field-hover: #eeb056;
    --t-field-crest: #f6d4a3;
    --t-hdr-text: #f3f3f3;
    --t-hdr-text-2: #c7c7c7;
    --t-hdr-brand: #ef9716;
    --t-hdr-surface: #181818;
    --t-hdr-surface-2: #212121;
    
    --t-danger: #ef4444;
    --t-danger-soft: rgba(239, 68, 68, 0.15);
    --t-danger-border: rgba(239, 68, 68, 0.35);

    --default-font-family: "Geist", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    --default-mono-font-family: "JetBrains Mono", monospace;
    color-scheme: dark;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: var(--default-font-family);
    background-color: var(--t-bg-deep);
    color: var(--t-text);
    line-height: 1.5;
    padding-bottom: 80px;
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    letter-spacing: -0.01em;
  }}

  ::selection {{
    background: var(--t-selection);
    color: var(--t-brand);
  }}

  .container {{
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 18px;
    position: relative;
    z-index: 1;
  }}

  /* Omarchy Matte Header */
  .omarchy-header {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--t-bg);
    border-bottom: 1px solid var(--t-border-subtle);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
    padding: 14px 0;
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

  .brand-icon {{
    width: 38px;
    height: 38px;
    border-radius: 8px;
    background: var(--t-surface-2);
    border: 1px solid var(--t-border-strong);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--t-brand);
    font-weight: 800;
    font-size: 1.15rem;
    font-family: var(--default-mono-font-family);
    box-shadow: var(--t-elevation);
  }}

  .brand-title h1 {{
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--t-hdr-text);
  }}

  .brand-title p {{
    font-size: 0.75rem;
    color: var(--t-text-muted);
    font-weight: 400;
  }}

  .header-actions {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .omarchy-badge {{
    background: var(--t-surface-2);
    border: 1px solid var(--t-border-subtle);
    color: var(--t-text-secondary);
    font-size: 0.75rem;
    font-family: var(--default-mono-font-family);
    padding: 4px 10px;
    border-radius: 6px;
  }}

  .omarchy-btn {{
    background: var(--t-surface-2);
    color: var(--t-text);
    border: 1px solid var(--t-border-strong);
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.15s ease;
  }}

  .omarchy-btn:hover {{
    background: var(--t-surface);
    border-color: var(--t-brand);
    color: var(--t-brand);
  }}

  /* Omarchy Matte Search Box */
  .search-area {{
    margin: 24px 0 16px 0;
  }}

  .omarchy-search-bar {{
    background: var(--t-field-bg);
    border: 1px solid var(--t-border-strong);
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
    border-radius: 8px;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    transition: border-color 0.2s, box-shadow 0.2s;
  }}

  .omarchy-search-bar:focus-within {{
    border-color: var(--t-brand);
    box-shadow: 0 0 0 1px var(--t-brand), inset 0 2px 4px rgba(0,0,0,0.5);
  }}

  .search-icon {{
    color: var(--t-brand);
    font-size: 22px;
    margin-right: 12px;
  }}

  .omarchy-search-input {{
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    font-size: 0.95rem;
    font-family: var(--default-font-family);
    color: var(--t-text);
  }}

  .omarchy-search-input::placeholder {{
    color: var(--t-text-muted);
  }}

  .clear-btn {{
    background: var(--t-surface-2);
    border: 1px solid var(--t-border-subtle);
    color: var(--t-text-muted);
    border-radius: 4px;
    width: 22px;
    height: 22px;
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 14px;
  }}

  .clear-btn:hover {{
    color: var(--t-text);
    border-color: var(--t-border-strong);
  }}

  /* Filter Bars */
  .filter-section-title {{
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--t-text-muted);
    font-family: var(--default-mono-font-family);
    margin: 14px 0 6px 2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .segmented-scroll {{
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding: 2px 2px 10px 2px;
    scrollbar-width: thin;
    scrollbar-color: var(--t-border-strong) transparent;
  }}

  .omarchy-pill {{
    background: var(--t-surface);
    border: 1px solid var(--t-border-subtle);
    color: var(--t-text-secondary);
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 500;
    white-space: nowrap;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.15s ease;
    user-select: none;
  }}

  .omarchy-pill:hover {{
    color: var(--t-text);
    background: var(--t-surface-2);
    border-color: var(--t-border-strong);
  }}

  .omarchy-pill.active {{
    background: var(--t-brand);
    color: var(--t-brand-ink);
    border-color: var(--t-brand);
    font-weight: 700;
    box-shadow: 0 0 12px rgba(230, 142, 13, 0.3);
  }}

  .omarchy-pill-model.active {{
    background: #ffaa33;
    color: #0d0d0d;
    border-color: #ffaa33;
    font-weight: 700;
  }}

  .omarchy-pill-danger.active {{
    background: var(--t-danger);
    color: #ffffff;
    border-color: var(--t-danger);
    font-weight: 700;
  }}

  /* SP Mode Keypad Simulator Section */
  .sp-card-omarchy {{
    background: var(--t-surface);
    border: 1px solid var(--t-border-subtle);
    box-shadow: var(--t-elevation);
    border-radius: 10px;
    margin: 14px 0 24px 0;
    overflow: hidden;
  }}

  .sp-header {{
    padding: 14px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    user-select: none;
    background: var(--t-bg);
    border-bottom: 1px solid var(--t-border-subtle);
  }}

  .sp-header h2 {{
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--t-brand);
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .sp-grid {{
    padding: 18px;
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
  }}

  @media(min-width: 900px) {{
    .sp-grid {{ grid-template-columns: 1fr 1fr; }}
  }}

  .simulator-panel {{
    background: var(--t-bg-deep);
    border: 1px solid var(--t-border-subtle);
    border-radius: 8px;
    padding: 14px;
  }}

  .sim-title {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }}

  .sim-title h3 {{
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--t-text);
  }}

  .sim-screen {{
    background: #050505;
    color: var(--t-brand);
    font-family: var(--default-mono-font-family);
    font-size: 0.82rem;
    padding: 10px 14px;
    border-radius: 6px;
    border: 1px solid var(--t-border-strong);
    margin-bottom: 14px;
    min-height: 42px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}

  .keypad-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    max-width: 230px;
    margin: 0 auto 12px auto;
  }}

  .kp-btn {{
    background: var(--t-surface);
    border: 1px solid var(--t-border-subtle);
    color: var(--t-text);
    font-family: var(--default-mono-font-family);
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 6px;
    padding: 10px 0;
    cursor: pointer;
    transition: all 0.1s ease;
    user-select: none;
  }}

  .kp-btn:active, .kp-btn.active {{
    background: var(--t-brand);
    color: var(--t-brand-ink);
    border-color: var(--t-brand);
    transform: scale(0.96);
  }}

  .kp-btn-yellow {{
    background: rgba(230, 142, 13, 0.15);
    color: var(--t-brand);
    border-color: rgba(230, 142, 13, 0.4);
    font-size: 0.75rem;
  }}

  .kp-btn-red {{
    background: var(--t-danger-soft);
    color: var(--t-danger);
    border-color: var(--t-danger-border);
    font-size: 0.75rem;
  }}

  .sim-controls {{
    display: flex;
    justify-content: center;
    gap: 8px;
  }}

  .sim-action-btn {{
    background: var(--t-surface);
    border: 1px solid var(--t-border-subtle);
    color: var(--t-text-secondary);
    padding: 5px 12px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-family: var(--default-mono-font-family);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: all 0.15s;
  }}

  .sim-action-btn:hover {{
    background: var(--t-surface-2);
    border-color: var(--t-border-strong);
    color: var(--t-text);
  }}

  /* Cards Grid */
  .cards-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
  }}

  .omarchy-card {{
    background: var(--t-surface);
    border: 1px solid var(--t-border-subtle);
    border-radius: 10px;
    padding: 22px;
    box-shadow: var(--t-elevation);
    transition: border-color 0.15s, box-shadow 0.15s;
  }}

  .omarchy-card:hover {{
    border-color: var(--t-border-strong);
    box-shadow: var(--t-elevation-hover);
  }}

  .card-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 12px;
    flex-wrap: wrap;
  }}

  .code-title-group {{
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}

  .sc-code-badge {{
    font-family: var(--default-mono-font-family);
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--t-brand);
    background: var(--t-bg-deep);
    border: 1px solid var(--t-border-strong);
    padding: 3px 12px;
    border-radius: 6px;
  }}

  .sc-title {{
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--t-text);
  }}

  .card-actions {{
    display: flex;
    gap: 6px;
    align-items: center;
    flex-wrap: wrap;
  }}

  .matte-badge {{
    font-size: 0.72rem;
    font-family: var(--default-mono-font-family);
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}

  .matte-badge-a {{
    background: var(--t-danger-soft);
    color: #f87171;
    border: 1px solid var(--t-danger-border);
  }}

  .matte-badge-b {{
    background: rgba(230, 142, 13, 0.12);
    color: var(--t-brand);
    border: 1px solid rgba(230, 142, 13, 0.3);
  }}

  .matte-badge-d {{
    background: var(--t-surface-2);
    color: var(--t-text-secondary);
    border: 1px solid var(--t-border-subtle);
  }}

  .matte-badge-reset {{
    background: rgba(239, 68, 68, 0.2);
    color: #fca5a5;
    border: 1px solid rgba(239, 68, 68, 0.5);
  }}

  .card-action-btn {{
    background: var(--t-surface-2);
    border: 1px solid var(--t-border-subtle);
    color: var(--t-text-secondary);
    border-radius: 4px;
    padding: 4px 10px;
    font-size: 0.75rem;
    font-family: var(--default-font-family);
    font-weight: 500;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: all 0.15s;
  }}

  .card-action-btn:hover {{
    color: var(--t-text);
    border-color: var(--t-border-strong);
    background: var(--t-bg-deep);
  }}

  .card-action-ticket {{
    color: var(--t-brand);
    border-color: rgba(230, 142, 13, 0.4);
    background: var(--t-brand-soft);
  }}

  .card-action-ticket:hover {{
    border-color: var(--t-brand);
    background: rgba(230, 142, 13, 0.2);
  }}

  .models-row {{
    font-size: 0.8rem;
    color: var(--t-text-muted);
    margin-bottom: 12px;
  }}

  .section-label {{
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--t-text-muted);
    font-family: var(--default-mono-font-family);
    margin: 14px 0 6px 0;
  }}

  .symptom-box {{
    background: var(--t-bg-deep);
    border: 1px solid var(--t-border-subtle);
    border-left: 3px solid var(--t-brand);
    border-radius: 4px;
    padding: 10px 14px;
    font-size: 0.9rem;
    color: var(--t-text);
  }}

  ul.omarchy-list, ol.omarchy-list {{
    margin-left: 20px;
    font-size: 0.9rem;
    color: var(--t-text-secondary);
  }}

  ul.omarchy-list li, ol.omarchy-list li {{
    margin-bottom: 4px;
  }}

  .reset-alert-box {{
    margin-top: 14px;
    background: var(--t-danger-soft);
    border: 1px solid var(--t-danger-border);
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    gap: 8px;
    color: #fca5a5;
  }}

  /* Toast */
  .omarchy-toast {{
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%) translateY(-30px);
    background: var(--t-bg);
    border: 1px solid var(--t-brand);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
    color: var(--t-text);
    border-radius: 6px;
    padding: 8px 18px;
    font-size: 0.85rem;
    font-family: var(--default-mono-font-family);
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s ease;
    z-index: 200;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .omarchy-toast.show {{
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }}

  .empty-state {{
    text-align: center;
    padding: 80px 20px;
    color: var(--t-text-muted);
  }}

  .empty-state span {{
    font-size: 48px;
    color: var(--t-brand);
  }}

  /* Printable Service Ticket Modal */
  .modal-backdrop {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.85);
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
    border-radius: 12px;
    padding: 28px;
    box-shadow: 0 24px 60px rgba(0,0,0,0.8);
    font-family: var(--default-font-family);
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
    background: #e68e0d;
    color: #0c0e10;
    font-weight: 800;
    font-size: 0.75rem;
    font-family: var(--default-mono-font-family);
    padding: 4px 10px;
    border-radius: 4px;
  }}

  .ticket-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    padding: 12px;
    border-radius: 6px;
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
    background: #e68e0d;
    color: #0c0e10;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: 700;
    font-family: var(--default-font-family);
    cursor: pointer;
  }}

  .btn-close {{
    background: #e5e7eb;
    color: #374151;
    border: none;
    border-radius: 6px;
    padding: 10px 16px;
    font-weight: 600;
    cursor: pointer;
  }}

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

<!-- Omarchy Matte Header -->
<header class="omarchy-header">
  <div class="container header-content">
    <div class="brand">
      <div class="brand-icon">R</div>
      <div class="brand-title">
        <h1>Ricoh Diagnostics</h1>
        <p>M · MP · MP C · IM · IM C Series</p>
      </div>
    </div>
    <div class="header-actions">
      <span class="omarchy-badge">OMARCHY MATTE-BLACK</span>
      <button class="omarchy-btn" id="installBtn" style="display: none;" onclick="installPWA()">
        <span class="material-symbols-rounded" style="font-size: 16px;">download</span> Install App
      </button>
    </div>
  </div>
</header>

<main class="container">
  <!-- Search Bar -->
  <div class="search-area">
    <div class="omarchy-search-bar">
      <span class="material-symbols-rounded search-icon">search</span>
      <input type="text" id="searchInput" class="omarchy-search-input" placeholder="Search error code (e.g. 542, 672, 899) or component (fuser, laser, motor)..." autofocus autocomplete="off" />
      <button class="clear-btn" id="clearBtn" onclick="clearSearch()">
        <span class="material-symbols-rounded" style="font-size: 14px;">close</span>
      </button>
    </div>
  </div>

  <!-- Model Series Filter Bar -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin: 14px 2px 6px 2px;">
    <div class="filter-section-title" style="margin: 0;">
      <span class="material-symbols-rounded" style="font-size: 14px; color: var(--t-brand);">print</span> Machine Series
    </div>
    <button class="omarchy-btn" onclick="resetAllFilters()" style="padding: 3px 10px; font-size: 0.72rem;">
      <span class="material-symbols-rounded" style="font-size: 14px; color: var(--t-brand);">restart_alt</span> Reset Filters
    </button>
  </div>
  <div class="segmented-scroll" id="modelFilterBar">
    <button class="omarchy-pill omarchy-pill-model active" onclick="setModelFilter('ALL', event)">All Models</button>
    <button class="omarchy-pill omarchy-pill-model" onclick="setModelFilter('M', event)">M Series</button>
    <button class="omarchy-pill omarchy-pill-model" onclick="setModelFilter('MP', event)">MP Series (Mono)</button>
    <button class="omarchy-pill omarchy-pill-model" onclick="setModelFilter('MP_C', event)">MP C (Color)</button>
    <button class="omarchy-pill omarchy-pill-model" onclick="setModelFilter('IM', event)">IM Series (Smart Mono)</button>
    <button class="omarchy-pill omarchy-pill-model" onclick="setModelFilter('IM_C', event)">IM C (Smart Color)</button>
  </div>

  <!-- Subsystem Category Filter Bar -->
  <div class="filter-section-title">
    <span class="material-symbols-rounded" style="font-size: 14px; color: var(--t-brand);">category</span> Subsystem Category
  </div>
  <div class="segmented-scroll" id="categoryFilterBar">
    <button class="omarchy-pill active" onclick="setCategory('ALL', event)">All Categories</button>
    <button class="omarchy-pill omarchy-pill-danger" onclick="filterLevelA(event)">
      <span class="material-symbols-rounded" style="font-size: 15px;">lock_clock</span> Level A (Reset Required)
    </button>
    <button class="omarchy-pill" onclick="setCategory('SC100', event)">SC100 Optics</button>
    <button class="omarchy-pill" onclick="setCategory('SC200', event)">SC200 Laser</button>
    <button class="omarchy-pill" onclick="setCategory('SC300', event)">SC300 Drum & PCU</button>
    <button class="omarchy-pill" onclick="setCategory('SC400', event)">SC400 Transfer</button>
    <button class="omarchy-pill" onclick="setCategory('SC500', event)">SC500 Fuser</button>
    <button class="omarchy-pill" onclick="setCategory('SC600', event)">SC600 Comm & RFID</button>
    <button class="omarchy-pill" onclick="setCategory('SC700', event)">SC700 Finisher</button>
    <button class="omarchy-pill" onclick="setCategory('SC800', event)">SC800 Controller/HDD</button>
    <button class="omarchy-pill" onclick="setCategory('SC900', event)">SC900 Engine</button>
  </div>

  <!-- SP Mode Keypad Simulator Section -->
  <section class="sp-card-omarchy">
    <div class="sp-header" onclick="toggleSPAccordion()">
      <h2>
        <span class="material-symbols-rounded">dialpad</span>
        SP Mode Keypad Simulator & Reset Cheatsheet
      </h2>
      <span class="material-symbols-rounded" id="spArrow" style="transition: transform 0.2s; color: var(--t-text-muted);">expand_more</span>
    </div>
    
    <div class="sp-grid" id="spContent" style="display: none;">
      <!-- Classic Keypad Simulator -->
      <div class="simulator-panel">
        <div class="sim-title">
          <h3>Classic Keypad (MP & M Series)</h3>
          <span style="font-size: 0.72rem; color: var(--t-brand); font-family: var(--default-mono-font-family);">10-Key Sequence</span>
        </div>
        <div class="sim-screen" id="classicScreen">
          <span id="classicStatus">READY. PRESS YELLOW KEY</span>
          <span id="classicSeq" style="color: var(--t-brand);">[ _ _ _ ]</span>
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
            <span class="material-symbols-rounded" style="font-size:14px;">play_arrow</span> Auto-Play
          </button>
          <button class="sim-action-btn" onclick="resetClassicKeypad()">
            <span class="material-symbols-rounded" style="font-size:14px;">refresh</span> Reset
          </button>
        </div>
      </div>

      <!-- Smart Operation Panel (SOP) Keypad Simulator -->
      <div class="simulator-panel">
        <div class="sim-title">
          <h3>Smart Operation Panel (IM & IM C Series)</h3>
          <span style="font-size: 0.72rem; color: var(--t-brand); font-family: var(--default-mono-font-family);">SOP Virtual Keypad</span>
        </div>
        <div class="sim-screen" id="sopScreen">
          <span id="sopStatus">READY: TAP RESET</span>
          <span id="sopSeq" style="color: var(--t-brand);">[ 806182 ]</span>
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
            <span class="material-symbols-rounded" style="font-size:14px;">play_arrow</span> Auto-Play
          </button>
          <button class="sim-action-btn" onclick="resetSopKeypad()">
            <span class="material-symbols-rounded" style="font-size:14px;">refresh</span> Reset
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Status Bar -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; font-size: 0.8rem; color: var(--t-text-muted); font-family: var(--default-mono-font-family);">
    <span id="resultsCount">Loading error codes...</span>
    <span>OMARCHY OS THEME · GEIST FONT</span>
  </div>

  <!-- Cards Grid -->
  <div class="cards-grid" id="cardsGrid"></div>
</main>

<!-- Printable Service Ticket Modal -->
<div class="modal-backdrop" id="ticketModal" onclick="closeTicketOnBackdrop(event)">
  <div class="ticket-card" id="ticketCard">
    <div class="ticket-header">
      <div>
        <div class="ticket-badge">RICOH MFP SERVICE TICKET</div>
        <div class="ticket-title" id="tktCodeTitle" style="margin-top:6px;">SC542 - Warm-up Timeout</div>
      </div>
      <div style="text-align:right; font-size:0.75rem; color:#6b7280;">
        <div id="tktDate">Date: 2026-10-21</div>
        <div id="tktNum" style="font-family:var(--default-mono-font-family); font-weight:700;">#RST-542-8821</div>
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

<!-- Omarchy Toast -->
<div class="omarchy-toast" id="toast">
  <span class="material-symbols-rounded" style="color: var(--t-brand); font-size: 18px;">check_circle</span>
  <span id="toastMsg">Copied to clipboard!</span>
</div>

<script>
const scData = {codes_json};
let currentCategory = 'ALL';
let currentModelFilter = 'ALL';
let filterOnlyLevelA = false;

// Auto-purge any stale Service Worker cache so updates appear instantly
if ('serviceWorker' in navigator) {{
  navigator.serviceWorker.getRegistrations().then((registrations) => {{
    for (let reg of registrations) {{
      reg.unregister();
    }}
  }});
}}
if ('caches' in window) {{
  caches.keys().then((names) => {{
    for (let name of names) {{
      caches.delete(name);
    }}
  }});
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
  setTimeout(() => toast.classList.remove('show'), 2000);
}}

function copyFix(code, title, solutions) {{
  const text = `Ricoh SC Error: ${{code}} - ${{title}}\\n\\nTroubleshooting:\\n${{solutions.map((s, i) => `${{i+1}}. ${{s}}`).join('\\n')}}`;
  navigator.clipboard.writeText(text).then(() => {{
    showToast(`Copied fix for ${{code}}`);
  }});
}}

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

// Keypad Simulator Logic
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
    status.style.color = 'var(--t-brand)';
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
  status.style.color = 'var(--t-brand)';
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
    status.style.color = 'var(--t-brand)';
    seq.textContent = 'SOP UNLOCKED';
    showToast('SOP Mode Unlocked!');
  }}
}}

function resetSopKeypad() {{
  sopStep = 0;
  const status = document.getElementById('sopStatus');
  status.textContent = 'READY: TAP RESET';
  status.style.color = 'var(--t-brand)';
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

function renderCards(items) {{
  const grid = document.getElementById('cardsGrid');
  const count = document.getElementById('resultsCount');
  grid.innerHTML = '';
  count.textContent = `Showing ${{items.length}} error codes`;

  if (items.length === 0) {{
    grid.innerHTML = `
      <div class="empty-state">
        <span class="material-symbols-rounded">search_off</span>
        <h3 style="margin-top: 12px; color: var(--t-text);">No matching SC codes found</h3>
        <p style="margin-top: 4px;">Try searching by keyword or clicking Reset Filters.</p>
      </div>
    `;
    return;
  }}

  items.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'omarchy-card';
    card.id = item.code.toLowerCase();

    const causesHtml = item.causes.map(c => `<li>${{c}}</li>`).join('');
    const solutionsHtml = item.solutions.map(s => `<li>${{s}}</li>`).join('');

    let badgeClass = 'matte-badge-d';
    if (item.level === 'A') badgeClass = 'matte-badge-a';
    else if (item.level === 'B') badgeClass = 'matte-badge-b';

    card.innerHTML = `
      <div class="card-top">
        <div class="code-title-group">
          <span class="sc-code-badge">${{item.code}}</span>
          <span class="sc-title">${{item.title}}</span>
        </div>
        <div class="card-actions">
          <span class="matte-badge ${{badgeClass}}">Level ${{item.level}}</span>
          ${{item.sp_reset_required ? '<span class="matte-badge matte-badge-reset">SP 5-810 Reset</span>' : ''}}
          <button class="card-action-btn card-action-ticket" onclick='openServiceTicket(${{JSON.stringify(item)}})'>
            <span class="material-symbols-rounded" style="font-size:14px;">receipt_long</span> Ticket / PDF
          </button>
          <button class="card-action-btn" onclick='copyFix("${{item.code}}", "${{item.title.replace(/"/g, '&quot;')}}", ${{JSON.stringify(item.solutions)}})'>
            <span class="material-symbols-rounded" style="font-size:14px;">content_copy</span> Copy
          </button>
        </div>
      </div>

      <div class="models-row">
        <strong>Supported Models:</strong> ${{item.models}}
      </div>

      <div class="section-label">Symptom</div>
      <div class="symptom-box">${{item.symptom}}</div>

      <div class="section-label">Probable Causes</div>
      <ul class="omarchy-list">${{causesHtml}}</ul>

      <div class="section-label">Troubleshooting & Repair Sequence</div>
      <ol class="omarchy-list">${{solutionsHtml}}</ol>

      ${{item.sp_reset_required ? `
        <div class="reset-alert-box">
          <span class="material-symbols-rounded" style="font-size: 18px;">restart_alt</span>
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
  document.querySelectorAll('#categoryFilterBar .omarchy-pill').forEach(btn => btn.classList.remove('active'));
  if (ev && ev.currentTarget) {{
    ev.currentTarget.classList.add('active');
  }}
  applyFilter();
}}

function setModelFilter(model, ev) {{
  currentModelFilter = model;
  document.querySelectorAll('#modelFilterBar .omarchy-pill').forEach(btn => btn.classList.remove('active'));
  if (ev && ev.currentTarget) {{
    ev.currentTarget.classList.add('active');
  }}
  applyFilter();
}}

function filterLevelA(ev) {{
  filterOnlyLevelA = true;
  currentCategory = 'ALL';
  document.querySelectorAll('#categoryFilterBar .omarchy-pill').forEach(btn => btn.classList.remove('active'));
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

  document.querySelectorAll('#modelFilterBar .omarchy-pill').forEach(btn => btn.classList.remove('active'));
  const firstModelBtn = document.querySelector('#modelFilterBar .omarchy-pill');
  if (firstModelBtn) firstModelBtn.classList.add('active');

  document.querySelectorAll('#categoryFilterBar .omarchy-pill').forEach(btn => btn.classList.remove('active'));
  const firstCatBtn = document.querySelector('#categoryFilterBar .omarchy-pill');
  if (firstCatBtn) firstCatBtn.classList.add('active');

  applyFilter();
  showToast('Filters Reset');
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
    print(f"Generated Omarchy Matte Black HTML guide at: {output_path}")

if __name__ == "__main__":
    generate_html_file()
