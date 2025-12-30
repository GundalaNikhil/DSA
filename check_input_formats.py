#!/usr/bin/env python3
"""Check input formats from problem statements"""
from pathlib import Path

problems = [10, 11, 12, 13, 15, 16]
base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/problems"

for num in problems:
    prob_files = list(Path(base_path).glob(f"QUE-{num:03d}-*.md"))
    if not prob_files:
        print(f"QUE-{num:03d}: Not found")
        continue

    with open(prob_files[0], 'r') as f:
        content = f.read()

    # Extract Input Format section
    if "## Input Format" in content:
        section = content.split("## Input Format")[1].split("## ")[0]
        lines = section.strip().split('\n')[:5]
        print(f"\nQUE-{num:03d}:")
        for line in lines:
            if line.strip():
                print(f"  {line}")
