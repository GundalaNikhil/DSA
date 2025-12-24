#!/usr/bin/env python3
"""
Fix unnecessary LaTeX $ symbols in PRB editorial markdown files.
Only fixes $ in regular text, preserves $$ for display math.
"""

import os
import re
from pathlib import Path

def fix_latex_in_text(content):
    """Fix LaTeX symbols that should be plain text."""
    
    # Patterns to fix - single $ in inline text (not display math $$)
    fixes = [
        # Variables in prose
        (r'\$([a-zA-Z])\$', r'\1'),  # $n$ -> n
        (r'\$([a-zA-Z])\s*=\s*', r'\1 = '),  # $n =  -> n = 
        (r'\s+\$([a-zA-Z])\s+', r' \1 '),  # space $n space -> space n space
        
        # Common expressions
        (r'\$2\^([a-z0-9]+)\$', r'2^\1'),  # $2^n$ -> 2^n (keep superscript)
        (r'\$O\(([^)]+)\)\$', r'O(\1)'),  # $O(n)$ -> O(n)
        (r'\$([a-z]+)\[([^\]]+)\]\$', r'\1[\2]'),  # $dp[i]$ -> dp[i]
        
        # Inequalities
        (r'\$\\le\$', r'≤'),  # $\le$ -> ≤
        (r'\$\\ge\$', r'≥'),  # $\ge$ -> ≥
        (r'\$\\lt\$', r'<'),  # $\lt$ -> <
        (r'\$\\gt\$', r'>'),  # $\gt$ -> >
        (r'\$<\$', r'<'),     # $<$ -> <
        (r'\$>\$', r'>'),     # $>$ -> >
        
        # Math operators in text
        (r'\$\\cdot\$', r'·'),  # $\cdot$ -> ·
        (r'\$\\times\$', r'×'),  # $\times$ -> ×
        
        # Superscripts/subscripts in simple cases
        (r'\$\^([0-9])\$', r'^\1'),  # $^2$ -> ^2
        (r'\$\_([0-9])\$', r'_\1'),  # $_i$ -> _i
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_specific_patterns(content):
    """Fix specific common patterns found in PRB files."""
    
    # Fix: "with probability $p$" -> "with probability p"
    content = re.sub(r'probability \$([a-z])\$', r'probability \1', content)
    
    # Fix: "of $k$ consecutive" -> "of k consecutive"
    content = re.sub(r'of \$([a-z])\$ consecutive', r'of \1 consecutive', content)
    
    # Fix: "length $i$" -> "length i"
    content = re.sub(r'length \$([a-z])\$', r'length \1', content)
    
    # Fix: "from $i$ to" -> "from i to"
    content = re.sub(r'from \$([a-z])\$ to', r'from \1 to', content)
    
    # Fix: "at position $i$" -> "at position i"
    content = re.sub(r'position \$([a-z])\$', r'position \1', content)
    
    # Fix: "state $s$" -> "state s"
    content = re.sub(r'state \$([a-z])\$', r'state \1', content)
    
    # Fix: "for $p=0.5$" -> "for p=0.5"
    content = re.sub(r'for \$([a-z])=([0-9.]+)\$', r'for \1=\2', content)
    
    # Fix: "with $N$ elements" -> "with N elements"
    content = re.sub(r'with \$([A-Z])\$ elements', r'with \1 elements', content)
    
    # Fix: "of $N$" -> "of N"
    content = re.sub(r'of \$([A-Z])\$', r'of \1', content)
    
    # Fix: "$N \\le 60$" -> "N ≤ 60"
    content = re.sub(r'\$([A-Z])\s*\\le\s*([0-9]+)\$', r'\1 ≤ \2', content)
    
    # Fix: "$N=31$" -> "N=31"
    content = re.sub(r'\$([A-Z])=([0-9]+)\$', r'\1=\2', content)
    
    # Fix: "at $+\$a" -> "at +a" (escaped dollar signs)
    content = re.sub(r'\$\+\\([a-z])\b', r'+\1', content)
    content = re.sub(r'\$-\\([a-z])\b', r'-\1', content)
    
    # Fix: "with $p = 0.5$" -> "with p = 0.5"
    content = re.sub(r'with \$([a-z])\s*=\s*([0-9.]+)\$', r'with \1 = \2', content)
    
    # Fix remaining single variables in dollar signs
    content = re.sub(r'\$([a-zA-Z])\$(?!\$)', r'\1', content)
    
    return content

def process_file(filepath):
    """Process a single markdown file."""
    print(f"Processing: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply fixes
    content = fix_latex_in_text(content)
    content = fix_specific_patterns(content)
    
    # Write back if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed {filepath.name}")
        return True
    else:
        print(f"  - No changes needed for {filepath.name}")
        return False

def main():
    """Process all PRB editorial files."""
    editorials_dir = Path('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/editorials')
    
    if not editorials_dir.exists():
        print(f"Error: Directory not found: {editorials_dir}")
        return
    
    # Get all PRB editorial files
    files = sorted(editorials_dir.glob('PRB-*.md'))
    
    if not files:
        print("No PRB editorial files found!")
        return
    
    print(f"\nFound {len(files)} editorial files to process\n")
    print("=" * 60)
    
    fixed_count = 0
    for filepath in files:
        if process_file(filepath):
            fixed_count += 1
        print()
    
    print("=" * 60)
    print(f"\n✅ Complete! Fixed {fixed_count} out of {len(files)} files\n")

if __name__ == '__main__':
    main()
