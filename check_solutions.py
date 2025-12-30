#!/usr/bin/env python3
import os
from pathlib import Path

solutions_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Recursion/solutions/python")

for file in sorted(solutions_dir.glob("REC-*.py")):
    with open(file) as f:
        content = f.read()

    has_todo = "TODO" in content
    has_main = "def main" in content
    has_print = "print(" in content
    has_stdin = "sys.stdin" in content

    status = "✓ OK" if (has_main and has_stdin and has_print and not has_todo) else "✗ NEEDS FIX"

    print(f"{file.name}: {status}")
    if has_todo:
        print(f"  - Has TODO comment")
    if not has_main:
        print(f"  - Missing main function")
    if not has_stdin:
        print(f"  - Missing stdin reading")
    if not has_print:
        print(f"  - Missing print statement")
