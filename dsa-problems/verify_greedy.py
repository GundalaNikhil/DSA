#!/usr/bin/env python3
"""Quick verification script for Greedy test cases."""

import os
import yaml

def verify_greedy():
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Greedy/testcases"
    files = sorted([f for f in os.listdir(testcases_dir) if f.endswith('.yaml')])
    
    print("=" * 80)
    print("GREEDY TEST CASE VERIFICATION")
    print("=" * 80)
    
    total_files = 0
    total_tests = 0
    issues = []
    
    for filename in files:
        filepath = os.path.join(testcases_dir, filename)
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                data = yaml.safe_load(content)
            
            problem_id = data.get('problem_id', 'MISSING')
            samples = len(data.get('samples', []))
            public = len(data.get('public', []))
            hidden = len(data.get('hidden', []))
            total = samples + public + hidden
            
            # Check for proper multiline syntax
            has_multiline = '|-' in content
            
            total_files += 1
            total_tests += total
            
            status = "✅" if total >= 38 and has_multiline else "⚠️"
            print(f"{status} {filename}: {total} tests (S:{samples}, P:{public}, H:{hidden})")
            
            if total < 38:
                issues.append(f"  - {filename}: Only {total} tests (expected 38)")
            if not has_multiline:
                issues.append(f"  - {filename}: Missing |- multiline syntax")
            
        except Exception as e:
            issues.append(f"  - {filename}: ERROR - {str(e)}")
            print(f"❌ {filename}: ERROR - {str(e)}")
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: {total_files} files, {total_tests} total test cases")
    print("=" * 80)
    
    if issues:
        print("\n⚠️ ISSUES FOUND:")
        for issue in issues:
            print(issue)
    else:
        print("\n✅ ALL CHECKS PASSED!")
    
    return len(issues) == 0

if __name__ == "__main__":
    success = verify_greedy()
    exit(0 if success else 1)
