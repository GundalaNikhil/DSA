#!/usr/bin/env python3
"""
Fix LinkedLists solution templates to have:
1. Correct helper stub signatures
2. Proper return types
3. Clean main input/output handling
4. No solution logic in main
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/LinkedLists/problems")

def extract_templates(content):
    """Extract solution template sections"""
    java_match = re.search(r'### Java\s*```java\s*(.*?)```', content, re.DOTALL)
    python_match = re.search(r'### Python\s*```python\s*(.*?)```', content, re.DOTALL)
    cpp_match = re.search(r'### C\+\+\s*```cpp\s*(.*?)```', content, re.DOTALL)
    js_match = re.search(r'### JavaScript\s*```javascript\s*(.*?)```', content, re.DOTALL)
    
    return {
        'java': java_match.group(1).strip() if java_match else None,
        'python': python_match.group(1).strip() if python_match else None,
        'cpp': cpp_match.group(1).strip() if cpp_match else None,
        'js': js_match.group(1).strip() if js_match else None
    }

def analyze_problem(filepath):
    """Analyze a single problem file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    problem_id = os.path.basename(filepath).replace('.md', '')
    
    templates = extract_templates(content)
    
    issues = []
    
    # Check Java template
    if templates['java']:
        java_code = templates['java']
        
        # Check for wrong return types in helper
        if 'public void pushBack' in java_code or 'public int[] toArray' in java_code:
            if 'return new ArrayList<>' in java_code:
                issues.append(f"Java: returns ArrayList instead of proper type")
        
        if 'public int findFirstIndex' in java_code:
            if 'return 0;' not in java_code:
                issues.append(f"Java: missing default return")
        
        if 'public ListNode deduplicateAtMostTwo' in java_code:
            if 'return new ArrayList<>' in java_code:
                issues.append(f"Java: returns ArrayList instead of ListNode")
        
        if 'public int[] cycleInfo' in java_code:
            if 'return new int[0]' not in java_code:
                issues.append(f"Java: missing default array return")
    
    # Check Python template  
    if templates['python']:
        python_code = templates['python']
        
        if 'def find_first_index' in python_code or 'def cycle_info' in python_code or 'def intersection_sum' in python_code:
            if 'return 0' in python_code:
                issues.append(f"Python: returns 0 instead of proper type")
        
        if 'def deduplicate_at_most_two' in python_code:
            if 'return 0' in python_code:
                issues.append(f"Python: returns 0 instead of ListNode")
        
        if 'def subtract_with_freq' in python_code:
            if 'return 0' in python_code:
                issues.append(f"Python: returns 0 instead of tuple")
    
    # Check JavaScript template
    if templates['js']:
        js_code = templates['js']
        
        if 'function findFirstIndex' in js_code:
            if 'return -1' in js_code:
                issues.append(f"JS: returns -1 hardcoded")
        
        if 'function deduplicateAtMostTwo' in js_code or 'function cycleInfo' in js_code:
            if 'return 0' in js_code:
                issues.append(f"JS: returns 0 instead of proper type")
        
        if 'function subtractWithFreq' in js_code:
            if not js_code.strip().endswith('}'):
                issues.append(f"JS: incomplete code")
    
    return {
        'problem_id': problem_id,
        'issues': issues,
        'has_issues': len(issues) > 0
    }

def main():
    print("=" * 80)
    print("LINKEDLISTS TEMPLATE ANALYSIS")
    print("=" * 80)
    
    problem_files = sorted(BASE_DIR.glob("LNK-*.md"))
    
    issues_found = []
    clean_files = []
    
    for filepath in problem_files:
        result = analyze_problem(filepath)
        
        if result['has_issues']:
            issues_found.append(result)
            print(f"\n❌ {result['problem_id']}")
            for issue in result['issues']:
                print(f"   • {issue}")
        else:
            clean_files.append(result['problem_id'])
    
    print(f"\n{'=' * 80}")
    print(f"SUMMARY: {len(issues_found)} files with issues, {len(clean_files)} clean")
    print(f"{'=' * 80}")
    
    if clean_files:
        print(f"\n✅ Clean files: {', '.join(clean_files)}")

if __name__ == "__main__":
    main()
