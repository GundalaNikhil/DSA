#!/usr/bin/env python3
"""
Script to find and fix all potentially plagiarized examples across DSA problems
"""

import os
import re
from pathlib import Path

# Known LeetCode examples to replace
LEETCODE_PATTERNS = {
    # Fruit basket (LeetCode #904)
    r'fruits = \[1,2,1\]': 'fruits = [3,1,3]',
    r'fruits = \[0,1,2,2\]': 'fruits = [5,2,4,4]',
    r'fruits = \[1,2,3,2,2\]': 'fruits = [2,4,3,4,4]',
    r'fruits = \[3,3,3,1,2,1,1,2,3,3,4\]': 'fruits = [5,5,5,2,3,2,2,3,5,5,6]',

    # Permutations (LeetCode #46)
    r'nums = \[1,2,3\]': 'nums = [2,5,7]',
    r'nums = \[0,1\]': 'nums = [3,6]',
    r'nums = \[1\](\s|$)': 'nums = [8]\\1',
    r'nums = \[1,2,3,4\]': 'nums = [3,5,7,9]',

    # Minimum Size Subarray (LeetCode #209)
    r'target = 7.*consumption = \[2,3,1,2,4,3\]': 'target = 8, consumption = [3,2,4,1,5,2]',
    r'consumption = \[1,2,3,4,5\]': 'consumption = [2,3,4,5,6]',
    r'target = 4.*consumption = \[1,4,4\]': 'target = 5, consumption = [2,3,3]',
    r'target = 11.*consumption = \[1,1,1,1,1,1,1,1\]': 'target = 12, consumption = [2,2,2,2,2,2,2,2]',

    # Coin change (LeetCode #322)
    r'coins = \[1, 2, 5\], amount = 11': 'coins = [2, 3, 7], amount = 13',
    r'coins = \[2\], amount = 3': 'coins = [3\], amount = 5',
    r'coins = \[1\], amount = 0': 'coins = [1\], amount = 0',

    # Baseball game (LeetCode #682)
    r'ops = \["5", "2", "C", "D", "\+"\]': 'ops = ["7", "3", "C", "D", "+"]',
    r'ops = \["5", "-2", "4", "C", "D", "9", "\+", "\+"\]': 'ops = ["6", "-3", "5", "C", "D", "10", "+", "+"]',
    r'ops = \["1", "C"\]': 'ops = ["8", "C"]',

    # RPN Calculator (LeetCode #150)
    r'tokens = \["2", "1", "\+", "3", "\*"\]': 'tokens = ["3", "2", "+", "4", "*"]',
    r'tokens = \["4", "13", "5", "/", "\+"\]': 'tokens = ["5", "15", "3", "/", "+"]',
    r'tokens = \["10", "6", "9", "3", "\+", "-11", "\*", "/", "\*", "17", "\+", "5", "\+"\]': 'tokens = ["12", "8", "10", "4", "+", "-15", "*", "/", "*", "20", "+", "6", "+"]',
    r'tokens = \["3", "4", "\+"\]': 'tokens = ["5", "6", "+"]',
}

def fix_examples_in_file(file_path):
    """Fix known LeetCode examples in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        modified = False

        for pattern, replacement in LEETCODE_PATTERNS.items():
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True
                print(f"✅ Fixed pattern '{pattern}' in {file_path}")

        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Process all problem files"""
    base_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems")

    total_files = 0
    modified_files = 0

    for md_file in base_dir.rglob("*.md"):
        if "SAFE" in md_file.name:
            continue

        total_files += 1
        if fix_examples_in_file(md_file):
            modified_files += 1

    print(f"\n{'='*60}")
    print(f"📊 SUMMARY:")
    print(f"Total files scanned: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Files unchanged: {total_files - modified_files}")
    print("="*60)

if __name__ == "__main__":
    print("🚀 Starting example replacement process...\n")
    main()
    print("\n✅ Process complete!")
