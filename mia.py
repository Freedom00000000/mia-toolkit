#!/usr/bin/env python3
"""
Mia Toolkit — CLI entrypoint
Built by Agent Mia

Usage:
  python mia.py sysinfo
  python mia.py scan <directory>
  python mia.py hash <file>
  python mia.py weather <city>
  python mia.py timer <seconds>
"""

import sys
from tools import sysinfo, scanner, hasher, weather, timer

COMMANDS = {
    "sysinfo":  (sysinfo.run,  "Show system information"),
    "scan":     (scanner.run,  "Scan a directory and list files"),
    "hash":     (hasher.run,   "Hash a file (SHA-256)"),
    "weather":  (weather.run,  "Get weather for a city"),
    "timer":    (timer.run,    "Run a countdown timer"),
}

def usage():
    print("\n\033[1;36m  MIA TOOLKIT\033[0m")
    print("  " + "-" * 30)
    for cmd, (_, desc) in COMMANDS.items():
        print(f"  \033[1;32m{cmd:<12}\033[0m {desc}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        usage()
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]
    fn, _ = COMMANDS[cmd]
    fn(args)
