#!/usr/bin/env python3
"""
Ricoh MFP SC (Service Call) Error Code Diagnostic Agent
Covers Ricoh M Series, MP Series, MP C Series, IM Series, and IM C Series.
"""

import sys
import os
import argparse

# Ensure standard output handles UTF-8 / Windows CP gracefully
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from ricoh_database import SC_CODES, SP_MODE_PROCEDURES
from generate_html import generate_html_file

class RicohAgent:
    def __init__(self):
        self.codes = SC_CODES
        self.code_map = {}
        for entry in self.codes:
            clean_code = entry["code"].upper().replace("SC", "").strip()
            self.code_map[entry["code"].upper()] = entry
            self.code_map[clean_code] = entry

    def print_banner(self):
        banner = """
========================================================================
   RICOH MFP SERVICE CALL (SC) ERROR CODE DIAGNOSTIC AGENT
   Applicable to: M Series, MP Series, MP C Series, IM & IM C Series
========================================================================
Type an SC code (e.g. 542, SC672, 899) or keyword (fuser, laser, chip)
Commands:
  'sp' or 'reset'   : Show SP Mode access & SC reset instructions
  'categories'      : List all SC error code ranges
  'export'          : Generate offline interactive HTML reference guide
  'exit' or 'quit'  : Exit agent
========================================================================
"""
        print(banner)

    def format_entry(self, item):
        lines = []
        lines.append("=" * 72)
        lines.append(f"  ERROR CODE : {item['code']} - {item['title']}")
        lines.append(f"  CATEGORY   : {item['category']}")
        lines.append(f"  SEVERITY   : Level {item['level']} {'[SP 5-810 RESET REQUIRED]' if item['sp_reset_required'] else '[Auto-Reset on Power Cycle]'}")
        lines.append(f"  MODELS     : {item['models']}")
        lines.append("-" * 72)
        lines.append("SYMPTOM:")
        lines.append(f"  {item['symptom']}")
        lines.append("")
        lines.append("PROBABLE CAUSES:")
        for idx, cause in enumerate(item['causes'], 1):
            lines.append(f"  {idx}. {cause}")
        lines.append("")
        lines.append("STEP-BY-STEP FIX / TROUBLESHOOTING:")
        for idx, sol in enumerate(item['solutions'], 1):
            lines.append(f"  {idx}) {sol}")
        
        if item.get("sp_reset_required"):
            lines.append("")
            lines.append("[!] SP RESET PROCEDURE:")
            lines.append(f"  {item['sp_reset_guide']}")
        lines.append("=" * 72)
        return "\n".join(lines)

    def lookup(self, query):
        clean_q = query.strip().upper()
        # Direct match
        if clean_q in self.code_map:
            return [self.code_map[clean_q]]
        
        if not clean_q.startswith("SC") and f"SC{clean_q}" in self.code_map:
            return [self.code_map[f"SC{clean_q}"]]

        # Search across code, title, causes, and symptoms
        q_lower = query.strip().lower()
        results = []
        for item in self.codes:
            full_text = " ".join([
                item["code"].lower(),
                item["title"].lower(),
                item["category"].lower(),
                item["symptom"].lower(),
                " ".join(item["causes"]).lower(),
                " ".join(item["solutions"]).lower()
            ])
            if q_lower in full_text:
                results.append(item)
        return results

    def display_sp_guide(self):
        print("\n" + "#" * 72)
        print("  RICOH SERVICE PROGRAM (SP) MODE & SC RESET REFERENCE")
        print("#" * 72)
        for key, guide in SP_MODE_PROCEDURES.items():
            print(f"\n--- {guide['title']} ---")
            print(f"Target Models: {guide['models']}")
            print("\n" + "\n".join(guide['steps']))
        print("\n" + "#" * 72 + "\n")

    def display_categories(self):
        cats = [
            ("SC100 - SC199", "Scanning, Optics, Exposure, Standard White Plate, ADF/CIS"),
            ("SC200 - SC299", "Laser Diode (LD), Polygon Mirror Motor, Sync Detection, MUSIC"),
            ("SC300 - SC399", "Charge Roller/Corona, OPC Drum, Developer Bias, TD Sensors"),
            ("SC400 - SC499", "Transfer Belt (ITB), Paper Transfer, Cleaning Unit, Waste Toner"),
            ("SC500 - SC599", "Fusing Unit (Lamps, Thermistors, Thermostats, Paper Jams, IH)"),
            ("SC600 - SC699", "Communication (Engine-Controller, Operation Panel, RFID Toner Chips)"),
            ("SC700 - SC799", "Peripherals (Finisher, Stapler, Shift Tray, Punch, Bridge Unit)"),
            ("SC800 - SC899", "Controller, OS Kernel, RAM, Hard Disk (HDD), Network, Corrupt Jobs"),
            ("SC900 - SC999", "Engine Software, Firmware Anomalies, Destination / NVRAM Mismatch")
        ]
        print("\n=== RICOH SC CODE CATEGORIES ===")
        for code_range, desc in cats:
            print(f"  {code_range:<16} : {desc}")
        print("================================\n")

    def interactive_shell(self):
        self.print_banner()
        while True:
            try:
                user_input = input("\n[Ricoh-Agent] Enter SC Code or Query > ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting Ricoh Diagnostic Agent. Goodbye!")
                break

            if not user_input:
                continue

            cmd = user_input.lower()
            if cmd in ['exit', 'quit', 'q']:
                print("Exiting Ricoh Diagnostic Agent. Goodbye!")
                break
            elif cmd in ['sp', 'reset', 'spmode', 'sp mode']:
                self.display_sp_guide()
            elif cmd in ['categories', 'cat', 'list']:
                self.display_categories()
            elif cmd in ['export', 'html', 'web']:
                out_path = os.path.join(os.path.dirname(__file__), "ricoh_sc_guide.html")
                generate_html_file(out_path)
                print(f"--> Successfully generated HTML guide: {out_path}")
            else:
                matches = self.lookup(user_input)
                if not matches:
                    print(f"\n[!] No exact SC code or keyword matching '{user_input}'.")
                    print("    Tips: Type the number (e.g. '542'), 'SC672', or keywords like 'fuser', 'laser', 'toner'.")
                    print("    Type 'categories' to see code families.")
                elif len(matches) == 1:
                    print(self.format_entry(matches[0]))
                else:
                    print(f"\nFound {len(matches)} matching codes for '{user_input}':")
                    for idx, item in enumerate(matches, 1):
                        print(f"  {idx}. {item['code']:<8} : {item['title']} ({item['category']})")
                    print("\nTip: Type specific code (e.g. SC" + matches[0]['code'].replace("SC", "") + ") for full troubleshooting details.")

def main():
    parser = argparse.ArgumentParser(description="Ricoh MFP SC Error Code Diagnostic Tool")
    parser.add_argument("code", nargs="?", help="Specific SC Code (e.g. 542, SC672, SC899) to look up immediately")
    parser.add_argument("-s", "--search", help="Search by keyword across all symptoms and causes")
    parser.add_argument("--sp", action="store_true", help="Display Service Program (SP) Mode & SC Reset instructions")
    parser.add_argument("--categories", action="store_true", help="List all SC error code ranges")
    parser.add_argument("--export-html", action="store_true", help="Generate standalone interactive HTML dashboard")

    args = parser.parse_args()
    agent = RicohAgent()

    if args.export_html:
        out_path = os.path.join(os.path.dirname(__file__), "ricoh_sc_guide.html")
        generate_html_file(out_path)
        return

    if args.sp:
        agent.display_sp_guide()
        return

    if args.categories:
        agent.display_categories()
        return

    if args.code:
        matches = agent.lookup(args.code)
        if matches:
            for item in matches:
                print(agent.format_entry(item))
        else:
            print(f"Error: No SC code found matching '{args.code}'")
        return

    if args.search:
        matches = agent.lookup(args.search)
        if matches:
            print(f"Found {len(matches)} results for '{args.search}':\n")
            for item in matches:
                print(agent.format_entry(item))
        else:
            print(f"No results found for keyword '{args.search}'")
        return

    # Default to interactive shell
    agent.interactive_shell()

if __name__ == "__main__":
    main()
