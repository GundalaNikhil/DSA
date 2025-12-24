#!/usr/bin/env python3
import subprocess
import sys

# Test a simple Python program
code = """
n, m = map(int, input().split())
print(f"Got {n} and {m}")
"""

test_input = "4 4"

result = subprocess.run(
    ['python3', '-c', code],
    input=test_input,
    capture_output=True,
    text=True,
    timeout=5
)

print(f"Return code: {result.returncode}")
print(f"Output: {result.stdout}")
print(f"Error: {result.stderr}")
