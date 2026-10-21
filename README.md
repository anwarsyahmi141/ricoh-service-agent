# Ricoh MFP Service Call (SC) Diagnostics & Guide

Interactive diagnostics tool and searchable web dashboard for Ricoh multifunction printers (MFP) across:
- **M Series**
- **MP Series** (Monochrome)
- **MP C Series** (Color)
- **IM Series** (Smart Monochrome)
- **IM C Series** (Smart Color)

## 🌐 Live Web Dashboard
Visit the live interactive troubleshooting dashboard directly in your browser:
👉 **[https://anwarsyahmi141.github.io/ricoh-service-agent/](https://anwarsyahmi141.github.io/ricoh-service-agent/)**

---

## 🛠 Features
- **Real-time Search:** Filter SC codes by number (`542`, `672`, `899`) or symptom (`fuser`, `laser`, `toner`, `rfid`, `hdd`).
- **Level A Safety Codes:** Clear warnings and step-by-step instructions for `SP 5-810-001` reset procedures.
- **Service Program (SP) Mode Cheatsheet:** Step-by-step entry sequences for both Classic keypad models (MP/M) and Smart Operation Panel (SOP) models (MP Cxx04, IM, IM C).
- **CLI Assistant:** Python interactive diagnostic agent.

---

## 💻 CLI Usage

```bash
# Run interactive assistant
python ricoh_agent.py

# Instant SC lookup
python ricoh_agent.py 542
python ricoh_agent.py SC672

# Keyword search
python ricoh_agent.py -s "fuser"

# SP Mode reset guide
python ricoh_agent.py --sp
```
