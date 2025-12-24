#!/usr/bin/env python3
"""
Test only the problems we fixed: AGR-006, AGR-008, AGR-016
"""
import os
import sys
sys.path.insert(0, '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs')
from test_all_languages import test_problem

def main():
    os.chdir('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs')
    
    problems = ['AGR-006', 'AGR-008', 'AGR-016']
    languages = ['cpp', 'java', 'python']
    
    print("="*80)
    print("TESTING FIXED PROBLEMS")
    print("="*80)
    
    for prob_id in problems:
        print(f"\n{prob_id}:")
        print("-" * 40)
        
        for lang in languages:
            lang_name = {'cpp': 'C++', 'java': 'Java', 'python': 'Python'}[lang]
            results = test_problem(prob_id, lang)
            
            total = results['passed'] + results['failed']
            if results['failed'] == 0:
                print(f"  {lang_name:8} ✅ {results['passed']}/{total}")
            else:
                print(f"  {lang_name:8} ❌ {results['passed']}/{total} ({results['failed']} failed)")
                if results['errors']:
                    first_error = results['errors'][0]
                    print(f"            First error: {first_error['tc_id']} - {first_error['type']}")

if __name__ == '__main__':
    main()
