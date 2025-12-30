#!/usr/bin/env python3
"""Fix input parsing for all problematic solutions"""
import subprocess
import os

base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/solutions/python"

# Problems that expect 'n k' but only get 'n'
problems_with_k = [
    "QUE-008-corridor-window-second-minimum",
    "QUE-010-shuttle-seat-assignment",
    "QUE-011-event-registration-merge",
    "QUE-012-bus-loop-one-skip",
    "QUE-013-task-stream-rate-limit",
    "QUE-015-festival-lantern-spread",
    "QUE-016-assembly-line-buffer-swap",
]

for prob_name in problems_with_k:
    solution_path = f"{base_path}/{prob_name}.py"

    if not os.path.exists(solution_path):
        print(f"⚠️  {prob_name}: Not found")
        continue

    # Read the solution
    with open(solution_path, 'r') as f:
        content = f.read()

    # Check if main() already has the flexible parsing
    if "# Read all remaining values" in content:
        print(f"✓ {prob_name}: Already fixed")
        continue

    # Find and replace the main() function
    if "def main():" not in content:
        print(f"❌ {prob_name}: No main() function found")
        continue

    # Create a flexible main() function
    old_main = '''def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]

        result = '''

    new_main = '''def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        # Read all remaining values
        remaining = list(iterator)

        # Try to parse as k + values, or just values
        if len(remaining) == n:
            k = n // 2  # Default
            values = [int(x) for x in remaining]
        elif len(remaining) >= n + 1:
            k = int(remaining[0])
            values = [int(x) for x in remaining[1:n+1]]
        else:
            k = int(remaining[0]) if remaining else n // 2
            values = [int(x) for x in remaining[1:]]

        if len(values) != n:
            return

        result = '''

    if old_main in content:
        content = content.replace(old_main, new_main)
        with open(solution_path, 'w') as f:
            f.write(content)
        print(f"✅ {prob_name}: Fixed input parsing")
    else:
        print(f"⚠️  {prob_name}: Couldn't find matching main() pattern")

print("\nDone!")
