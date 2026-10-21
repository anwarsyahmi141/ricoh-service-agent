import json
import os
from ricoh_database import SC_CODES, SP_MODE_PROCEDURES

def generate_html_file(output_path="C:\\Users\\kaze\\ricoh-service-agent\\ricoh_sc_guide.html"):
    codes_json = json.dumps(SC_CODES)
    sp_json = json.dumps(SP_MODE_PROCEDURES)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ricoh MFP SC Error Code Master Guide & Troubleshooting Assistant</title>
<style>
  :root {{
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-card: #1e293b;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --accent: #38bdf8;
    --accent-hover: #0284c7;
    --border: #334155;
    --danger: #ef4444;
    --warning: #f59e0b;
    --success: #10b981;
    --code-bg: #090d16;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.5;
    padding-bottom: 40px;
  }}
  header {{
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border-bottom: 1px solid var(--border);
    padding: 24px 20px;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(8px);
  }}
  .container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 16px;
  }}
  .header-content {{
    display: flex;
    flex-direction: column;
    gap: 16px;
  }}
  .header-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }}
  h1 {{
    font-size: 1.5rem;
    font-weight: 700;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .badge-ricoh {{
    background-color: #e11d48;
    color: white;
    font-size: 0.75rem;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 800;
    letter-spacing: 0.5px;
  }}
  .model-tags {{
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }}
  .model-tag {{
    background: #334155;
    color: #e2e8f0;
    font-size: 0.75rem;
    padding: 2px 8px;
    border-radius: 12px;
  }}
  .search-bar {{
    display: flex;
    gap: 10px;
  }}
  .search-input {{
    flex: 1;
    background: #0b1120;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 1rem;
    color: white;
    outline: none;
    transition: border-color 0.2s;
  }}
  .search-input:focus {{
    border-color: var(--accent);
    box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
  }}
  .filter-bar {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding-bottom: 4px;
  }}
  .filter-btn {{
    background: #1e293b;
    border: 1px solid var(--border);
    color: var(--text-secondary);
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 0.85rem;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s;
  }}
  .filter-btn:hover, .filter-btn.active {{
    background: var(--accent);
    color: #0f172a;
    font-weight: 600;
    border-color: var(--accent);
  }}
  .stats-bar {{
    margin: 16px 0;
    font-size: 0.85rem;
    color: var(--text-secondary);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .cards-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
  }}
  .sc-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    transition: transform 0.15s, border-color 0.15s;
  }}
  .sc-card:hover {{
    border-color: #475569;
  }}
  .sc-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  .sc-code-title {{
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }}
  .sc-code {{
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: var(--accent);
  }}
  .sc-title {{
    font-size: 1.1rem;
    font-weight: 600;
    color: #f1f5f9;
  }}
  .badge {{
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
  }}
  .badge-level-a {{
    background-color: rgba(239, 68, 68, 0.2);
    color: #fca5a5;
    border: 1px solid rgba(239, 68, 68, 0.4);
  }}
  .badge-level-b {{
    background-color: rgba(245, 158, 11, 0.2);
    color: #fcd34d;
    border: 1px solid rgba(245, 158, 11, 0.4);
  }}
  .badge-level-d {{
    background-color: rgba(56, 189, 248, 0.2);
    color: #7dd3fc;
    border: 1px solid rgba(56, 189, 248, 0.4);
  }}
  .badge-reset {{
    background-color: rgba(225, 29, 72, 0.2);
    color: #fda4af;
    border: 1px solid rgba(225, 29, 72, 0.4);
    font-size: 0.7rem;
  }}
  .section-label {{
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-secondary);
    margin-top: 12px;
    margin-bottom: 6px;
  }}
  .symptom-text {{
    color: #cbd5e1;
    font-size: 0.95rem;
    margin-bottom: 12px;
    background: rgba(0,0,0,0.25);
    padding: 8px 12px;
    border-radius: 6px;
    border-left: 3px solid var(--accent);
  }}
  ul.causes-list, ol.solutions-list {{
    margin-left: 20px;
    margin-bottom: 12px;
    font-size: 0.92rem;
    color: #cbd5e1;
  }}
  li {{
    margin-bottom: 4px;
  }}
  ol.solutions-list li {{
    color: #e2e8f0;
  }}
  .reset-box {{
    background: rgba(225, 29, 72, 0.12);
    border: 1px solid rgba(225, 29, 72, 0.3);
    border-radius: 6px;
    padding: 10px 14px;
    margin-top: 10px;
    font-size: 0.88rem;
    color: #fecdd3;
  }}
  .reset-box strong {{
    color: #ffe4e6;
  }}
  .sp-card-section {{
    background: #172554;
    border: 1px solid #1e40af;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 24px;
  }}
  .sp-card-section h2 {{
    font-size: 1.25rem;
    margin-bottom: 12px;
    color: #93c5fd;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .sp-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
  }}
  @media(min-width: 768px) {{
    .sp-grid {{ grid-template-columns: 1fr 1fr; }}
  }}
  .sp-box {{
    background: #0f172a;
    border: 1px solid #1e3a8a;
    border-radius: 8px;
    padding: 14px;
  }}
  .sp-box h3 {{
    font-size: 1rem;
    color: #bfdbfe;
    margin-bottom: 8px;
  }}
  .sp-box pre {{
    white-space: pre-wrap;
    font-family: inherit;
    font-size: 0.85rem;
    color: #cbd5e1;
    line-height: 1.45;
  }}
  .empty-state {{
    text-align: center;
    padding: 60px 20px;
    color: var(--text-secondary);
  }}
</style>
</head>
<body>

<header>
  <div class="container header-content">
    <div class="header-title-row">
      <h1>
        <span class="badge-ricoh">RICOH</span> Service Call (SC) Error Code Diagnostics
      </h1>
      <div class="model-tags">
        <span class="model-tag">M Series</span>
        <span class="model-tag">MP Series</span>
        <span class="model-tag">MP C Series</span>
        <span class="model-tag">IM Series</span>
        <span class="model-tag">IM C Series</span>
      </div>
    </div>
    <div class="search-bar">
      <input type="text" id="searchInput" class="search-input" placeholder="Type SC code (e.g., SC542, 672, 899) or keyword (fuser, laser, motor, chip, hdd)..." autofocus />
    </div>
    <div class="filter-bar">
      <button class="filter-btn active" onclick="setCategory('ALL')">All Categories</button>
      <button class="filter-btn" onclick="setCategory('SC100')">SC100 Scanning</button>
      <button class="filter-btn" onclick="setCategory('SC200')">SC200 Laser</button>
      <button class="filter-btn" onclick="setCategory('SC300')">SC300 Drum & PCU</button>
      <button class="filter-btn" onclick="setCategory('SC400')">SC400 Transfer</button>
      <button class="filter-btn" onclick="setCategory('SC500')">SC500 Fuser</button>
      <button class="filter-btn" onclick="setCategory('SC600')">SC600 Comms</button>
      <button class="filter-btn" onclick="setCategory('SC700')">SC700 Finisher</button>
      <button class="filter-btn" onclick="setCategory('SC800')">SC800 Controller/HDD</button>
      <button class="filter-btn" onclick="setCategory('SC900')">SC900 System</button>
      <button class="filter-btn" onclick="filterLevelA()">Level A (Reset Required)</button>
    </div>
  </div>
</header>

<main class="container" style="margin-top: 20px;">
  <!-- Service Program (SP) Mode Guide -->
  <section class="sp-card-section">
    <h2>🛠️ Service Program (SP) Mode Quick Entry & Fuser Reset Cheat Sheet</h2>
    <div class="sp-grid">
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
        <pre>Method 1 (Touch Keypad):
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

  <div class="stats-bar">
    <span id="resultsCount">Loading error codes...</span>
    <span>Click any code to inspect full troubleshooting details</span>
  </div>

  <div class="cards-grid" id="cardsGrid"></div>
</main>

<script>
const scData = {codes_json};
let currentCategory = 'ALL';
let filterOnlyLevelA = false;

function getBadgeClass(level) {{
  if (level === 'A') return 'badge-level-a';
  if (level === 'B') return 'badge-level-b';
  return 'badge-level-d';
}}

function renderCards(items) {{
  const grid = document.getElementById('cardsGrid');
  const count = document.getElementById('resultsCount');
  grid.innerHTML = '';
  count.textContent = `Showing ${{items.length}} error codes`;

  if (items.length === 0) {{
    grid.innerHTML = '<div class="empty-state"><h3>No matching SC codes found</h3><p>Try searching by code number (e.g. 542, 672) or component keyword (e.g. fuser, laser, toner).</p></div>';
    return;
  }}

  items.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'sc-card';
    card.id = item.code.toLowerCase();

    const causesHtml = item.causes.map(c => `<li>${{c}}</li>`).join('');
    const solutionsHtml = item.solutions.map(s => `<li>${{s}}</li>`).join('');

    card.innerHTML = `
      <div class="sc-header">
        <div class="sc-code-title">
          <span class="sc-code">${{item.code}}</span>
          <span class="sc-title">${{item.title}}</span>
        </div>
        <div style="display:flex; gap:6px; align-items:center;">
          <span class="badge ${{getBadgeClass(item.level)}}">Level ${{item.level}}</span>
          ${{item.sp_reset_required ? '<span class="badge badge-reset">SP 5-810 Reset</span>' : ''}}
        </div>
      </div>
      <div>
        <div class="section-label">Applicable Series: <span style="color:#94a3b8; font-weight:normal;">${{item.models}}</span></div>
        <div class="section-label">Symptom</div>
        <div class="symptom-text">${{item.symptom}}</div>
        
        <div class="section-label">Probable Causes</div>
        <ul class="causes-list">${{causesHtml}}</ul>

        <div class="section-label">Troubleshooting & Repair Steps</div>
        <ol class="solutions-list">${{solutionsHtml}}</ol>

        ${{item.sp_reset_required ? `<div class="reset-box"><strong>⚠️ Reset Notice:</strong> ${{item.sp_reset_guide}}</div>` : ''}}
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function applyFilter() {{
  const query = document.getElementById('searchInput').value.trim().toLowerCase();
  
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

function setCategory(cat) {{
  currentCategory = cat;
  filterOnlyLevelA = false;
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  applyFilter();
}}

function filterLevelA() {{
  filterOnlyLevelA = true;
  currentCategory = 'ALL';
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
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
    print(f"Generated HTML guide at: {output_path}")

if __name__ == "__main__":
    generate_html_file()
