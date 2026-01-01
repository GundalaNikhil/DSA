#!/usr/bin/env python3
"""
Comprehensive fix script for all remaining Geometry solution issues.
"""
import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
SOLUTIONS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Geometry", "solutions")

def fix_geo_012_java():
    """Fix GEO-012 Java input parsing - xs and ys are interleaved"""
    path = os.path.join(SOLUTIONS_DIR, "java", "GEO-012-largest-empty-circle-rect.java")
    with open(path, 'r') as f:
        content = f.read()
    
    # Replace the input parsing section
    old_parsing = """        for (int i = 0; i < n; i++) xs[i] = sc.nextInt();
        for (int i = 0; i < n; i++) ys[i] = sc.nextInt();"""
    
    new_parsing = """        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
        }"""
    
    if old_parsing in content:
        content = content.replace(old_parsing, new_parsing)
        with open(path, 'w') as f:
            f.write(content)
        print("Fixed GEO-012 Java input parsing")

def fix_cpp_return_types():
    """Fix C++ return type issues for various problems"""
    
    # GEO-005: Should return vector<pair<long long, long long>>
    # But the wrapper expects to print pairs
    # The issue might be in how we're calling the function
    
    # GEO-008, 009, 012, 016: Check actual implementations
    # These might have algorithmic issues rather than just type issues
    
    print("C++ fixes require manual inspection - skipping automated fix")

def fix_javascript_logic_issues():
    """Fix JavaScript logic issues in partially passing tests"""
    
    # GEO-003: 7/40 passing - likely BigInt issues
    path = os.path.join(SOLUTIONS_DIR, "javascript", "GEO-003-segment-intersection-count.js")
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        
        # Check if using BigInt where it shouldn't
        if "BigInt" in content:
            # This is complex - need to check the actual algorithm
            print("GEO-003 JS needs manual review for BigInt usage")
    
    # GEO-004: 9/40 passing - likely similar issues
    # GEO-007: 18/40 passing - improved but still failing some
    # GEO-010, 011: Partial passes - likely logic issues
    
    print("JavaScript partial failures require manual algorithm review")

def main():
    print("Running comprehensive Geometry fixes...")
    fix_geo_012_java()
    fix_cpp_return_types()
    fix_javascript_logic_issues()
    print("Done! Some issues require manual review.")

if __name__ == "__main__":
    main()
