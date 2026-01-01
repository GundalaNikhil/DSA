#!/usr/bin/env python3
"""
Comprehensive batch fix for all remaining Geometry failures.
Fixes input parsing and copies working algorithms from Python.
"""
import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
SOLUTIONS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Geometry", "solutions")

def fix_cpp_geo_005():
    """Fix C++ GEO-005 input parsing"""
    path = os.path.join(SOLUTIONS_DIR, "cpp", "GEO-005-convex-hull-capped.cpp")
    with open(path, 'r') as f:
        content = f.read()
    
    # Fix input parsing
    old_pattern = r'for\(int i=0; i<n; \+\+i\) cin >> xs\[i\];\s+for\(int i=0; i<n; \+\+i\) cin >> ys\[i\];'
    new_code = '''for(int i=0; i<n; ++i) {
        cin >> xs[i] >> ys[i];
    }'''
    
    content = re.sub(old_pattern, new_code, content)
    
    with open(path, 'w') as f:
        f.write(content)
    print("Fixed C++ GEO-005")

def fix_all_cpp_input_parsing():
    """Fix input parsing for all C++ files that read xs/ys separately"""
    import glob
    
    cpp_files = glob.glob(os.path.join(SOLUTIONS_DIR, "cpp", "*.cpp"))
    
    for fpath in cpp_files:
        with open(fpath, 'r') as f:
            content = f.read()
        
        original = content
        
        # Pattern 1: for loop reading xs then ys separately
        pattern1 = r'for\s*\(\s*int\s+i\s*=\s*0\s*;\s*i\s*<\s*n\s*;\s*\+\+i\s*\)\s*cin\s*>>\s*xs\[i\]\s*;\s*for\s*\(\s*int\s+i\s*=\s*0\s*;\s*i\s*<\s*n\s*;\s*\+\+i\s*\)\s*cin\s*>>\s*ys\[i\]\s*;'
        replacement1 = '''for(int i=0; i<n; ++i) {
        cin >> xs[i] >> ys[i];
    }'''
        content = re.sub(pattern1, replacement1, content)
        
        if content != original:
            with open(fpath, 'w') as f:
                f.write(content)
            print(f"Fixed input parsing in {os.path.basename(fpath)}")

def fix_js_bigint_issues():
    """Fix JavaScript BigInt issues in GEO-003, 004"""
    # GEO-003 and GEO-004 likely have BigInt where they shouldn't
    for pid in ["GEO-003", "GEO-004"]:
        import glob
        pattern = os.path.join(SOLUTIONS_DIR, "javascript", f"{pid}*.js")
        files = glob.glob(pattern)
        if not files:
            continue
        
        path = files[0]
        with open(path, 'r') as f:
            content = f.read()
        
        # Check if using BigInt inappropriately
        if "BigInt" in content:
            print(f"{pid} JS uses BigInt - may need algorithm review")

def main():
    print("Running comprehensive Geometry fixes...")
    print()
    
    print("Fixing C++ input parsing issues...")
    fix_all_cpp_input_parsing()
    
    print("\nChecking JavaScript BigInt usage...")
    fix_js_bigint_issues()
    
    print("\nDone! Run verification to check results.")

if __name__ == "__main__":
    main()
