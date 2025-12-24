#!/usr/bin/env python3
"""Test AGR-016 Java compilation"""
import subprocess
import tempfile
import re
import os

editorial = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs/editorials/AGR-016-offline-lca-with-mods.md'

with open(editorial, 'r') as f:
    content = f.read()

pattern = r'### Java\n\n```java\n(.*?)\n```'
match = re.search(pattern, content, re.DOTALL)

if match:
    code = match.group(1)
    print(f"Extracted {len(code)} characters of Java code")
    
    # Write to file
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, 'Main.java')
    
    with open(temp_file, 'w') as f:
        f.write(code)
    
    print(f"\nCompiling...")
    result = subprocess.run(
        ['javac', temp_file],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    if result.returncode != 0:
        print("❌ COMPILATION FAILED:")
        print(result.stderr)
    else:
        print("✅ COMPILATION SUCCESSFUL")
else:
    print("❌ Could not extract Java code")
