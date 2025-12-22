#!/usr/bin/env python3
"""
Comprehensive LaTeX fix for PRB editorial files.
Handles all edge cases and malformed patterns.
"""

import re
import sys
from pathlib import Path

def fix_file_content(content, filename):
    """Apply all fixes to file content."""
    
    # Track changes
    changes = []
    
    # 1. Fix incomplete $ at end of line or sentence
    # "p = 0.5$," -> "p = 0.5,"
    pattern = r'([a-z])\s*=\s*([0-9.]+)\$([,;.\s])'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1 = \2\3', content)
        changes.append("Fixed incomplete $ after numbers")
    
    # 2. Fix "If p \neq 0.5$," -> "If p ≠ 0.5,"
    pattern = r'If ([a-z])\s*\\neq\s*([0-9.]+)\$'
    if re.search(pattern, content):
        content = re.sub(pattern, r'If \1 ≠ \2', content)
        changes.append("Fixed \\neq patterns")
    
    # 3. Fix "i = a$ or" -> "i = a or"
    pattern = r'([a-z])\s*=\s*([a-z])\$\s+(or|and)'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1 = \2 \3', content)
        changes.append("Fixed variable equations before or/and")
    
    # 4. Fix "in [0, N]$," -> "in [0, N],"
    pattern = r'\[([^\]]+)\]\$'
    if re.search(pattern, content):
        content = re.sub(pattern, r'[\1]', content)
        changes.append("Fixed $ after brackets")
    
    # 5. Fix "Let $E_i$ be" -> "Let E_i be" (but keep if complex subscript)
    # Simple subscript: fix it
    pattern = r'Let \$([A-Z])_([a-z])\$\s+be'
    if re.search(pattern, content):
        content = re.sub(pattern, r'Let \1_\2 be', content)
        changes.append("Fixed 'Let' variable declarations")
    
    # 6. Fix "a \to a+b$" -> "a → a+b"
    pattern = r'([a-z])\s*\\to\s*([a-z+]+)\$'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1 → \2', content)
        changes.append("Fixed arrow notation")
    
    # 7. Fix "on $i-1, i+1$)" -> "on i-1, i+1)"
    pattern = r'on \$([a-z])-1,\s*([a-z])\+1\$\)'
    if re.search(pattern, content):
        content = re.sub(pattern, r'on \1-1, \2+1)', content)
        changes.append("Fixed dependency notation")
    
    # 8. Fix "($ at end or start: "(2p-1)$ is" -> "(2p-1) is"
    pattern = r'\(([^)]+)\)\$\s+is'
    if re.search(pattern, content):
        content = re.sub(pattern, r'(\1) is', content)
        changes.append("Fixed $ after parentheses")
    
    # 9. Fix "**term1** = $..." to "**term1** = ..." (bullets with formulas)
    pattern = r'\*\*([a-z0-9]+)\*\*\s*=\s*\$([^$]+)\$\s*:'
    if re.search(pattern, content):
        # Keep these as they're formula definitions
        pass
    
    # 10. Fix "formula for p = 0.5$ (" -> "formula for p = 0.5 ("
    pattern = r'for ([a-z])\s*=\s*([0-9.]+)\$\s*\('
    if re.search(pattern, content):
        content = re.sub(pattern, r'for \1 = \2 (', content)
        changes.append("Fixed 'for p = value' patterns")
    
    # 11. Fix standalone $ at line boundaries
    content = re.sub(r'\$\s*\.\s*System', r'. System', content)
    content = re.sub(r'\$\s*,\s*the', r', the', content)
    content = re.sub(r'\$\s*\?', r'?', content)
    
    # 12. Fix "boundary conditions ($E_0=0" -> "boundary conditions (E_0=0"
    pattern = r'conditions\s*\(\$([A-Z])_([0-9])=([0-9])'
    if re.search(pattern, content):
        content = re.sub(pattern, r'conditions (\1_\2=\3', content)
        changes.append("Fixed boundary conditions notation")
    
    # 13. Fix remaining stray $ before punctuation
    content = re.sub(r'\$([,;.)])', r'\1', content)
    
    # 14. Fix size notation: "size ≈ 400$." -> "size ≈ 400."
    content = re.sub(r'≈\s*([0-9]+)\$\.', r'≈ \1.', content)
    
    # 15. Fix: "Wrong: Using general formula for p = 0.5$ (" -> no $
    pattern = r'formula for ([a-z])\s*=\s*([0-9.]+)\$\s*\('
    content = re.sub(pattern, r'formula for \1 = \2 (', content)
    
    if changes:
        print(f"  ✓ {filename}: {len(changes)} types of fixes applied")
        for change in changes:
            print(f"    - {change}")
    
    return content

def process_all_files():
    """Process all PRB editorial files."""
    
    editorials_dir = Path('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/editorials')
    
    if not editorials_dir.exists():
        print(f"Error: Directory not found: {editorials_dir}")
        return
    
    files = sorted(editorials_dir.glob('PRB-*.md'))
    
    if not files:
        print("No PRB editorial files found!")
        return
    
    print(f"\n{'='*70}")
    print(f"Processing {len(files)} PRB editorial files")
    print(f"{'='*70}\n")
    
    total_fixed = 0
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            fixed_content = fix_file_content(original_content, filepath.name)
            
            if fixed_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                total_fixed += 1
            else:
                print(f"  - {filepath.name}: No changes needed")
        
        except Exception as e:
            print(f"  ✗ Error processing {filepath.name}: {e}")
    
    print(f"\n{'='*70}")
    print(f"✅ Complete! Fixed {total_fixed} out of {len(files)} files")
    print(f"{'='*70}\n")

if __name__ == '__main__':
    process_all_files()
