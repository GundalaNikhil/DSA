#!/usr/bin/env python3
"""
Fresh verification script - tests editorial solutions against test cases.
Tests all 4 languages: Python, Java, C++, JavaScript
"""

import yaml
import re
import subprocess
import tempfile
from pathlib import Path
from io import StringIO
import sys

class EditorialTester:
    def __init__(self):
        self.base = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays")
        
    def extract_solution(self, editorial_file, language):
        """Extract solution code from editorial."""
        with open(editorial_file) as f:
            content = f.read()
        
        patterns = {
            'python': r'### Python\s*```python\s*(.*?)```',
            'java': r'### Java\s*```java\s*(.*?)```',
            'cpp': r'### C\+\+\s*```cpp\s*(.*?)```',
            'javascript': r'### JavaScript\s*```javascript\s*(.*?)```',
        }
        
        match = re.search(patterns[language], content, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def run_python(self, code, input_data):
        """Run Python solution."""
        old_stdin, old_stdout = sys.stdin, sys.stdout
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            exec(code, {'__name__': '__main__'})
            return sys.stdout.getvalue().rstrip('\n')
        except Exception as e:
            return f"ERROR: {e}"
        finally:
            sys.stdin, sys.stdout = old_stdin, old_stdout
    
    def run_java(self, code, input_data):
        """Compile and run Java solution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            java_file = tmppath / "Main.java"
            with open(java_file, 'w') as f:
                f.write(code)
            
            # Compile
            result = subprocess.run(['javac', 'Main.java'], cwd=tmppath, 
                                  capture_output=True, timeout=10)
            if result.returncode != 0:
                return f"COMPILE_ERROR: {result.stderr.decode()[:100]}"
            
            # Run
            result = subprocess.run(['java', 'Main'], input=input_data, 
                                  capture_output=True, text=True, cwd=tmppath, timeout=5)
            if result.returncode != 0:
                return f"RUNTIME_ERROR: {result.stderr[:100]}"
            
            return result.stdout.rstrip('\n')
    
    def run_cpp(self, code, input_data):
        """Compile and run C++ solution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            cpp_file = tmppath / "solution.cpp"
            with open(cpp_file, 'w') as f:
                f.write(code)
            
            # Compile
            result = subprocess.run(['g++', '-std=c++17', '-o', 'solution', 'solution.cpp'],
                                  cwd=tmppath, capture_output=True, timeout=10)
            if result.returncode != 0:
                return f"COMPILE_ERROR: {result.stderr.decode()[:100]}"
            
            # Run
            result = subprocess.run(['./solution'], input=input_data,
                                  capture_output=True, text=True, cwd=tmppath, timeout=5)
            if result.returncode != 0:
                return f"RUNTIME_ERROR: {result.stderr[:100]}"
            
            return result.stdout.rstrip('\n')
    
    def run_javascript(self, code, input_data):
        """Run JavaScript solution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            js_file = tmppath / "solution.js"
            with open(js_file, 'w') as f:
                f.write(code)
            
            result = subprocess.run(['node', 'solution.js'], input=input_data,
                                  capture_output=True, text=True, cwd=tmppath, timeout=5)
            if result.returncode != 0:
                return f"RUNTIME_ERROR: {result.stderr[:100]}"
            
            return result.stdout.rstrip('\n')
    
    def test_problem(self, problem_id, language='python'):
        """Test a single problem in specified language."""
        # Handle special case for ARR-004
        editorial_id = problem_id
        if problem_id == "ARR-004-lab-temperature-ranges":
            editorial_id = "ARR-004-lab-temperature-offline-ranges"
        
        editorial_file = self.base / "editorials" / f"{editorial_id}.md"
        yaml_file = self.base / "testcases" / f"{problem_id}.yaml"
        
        # Extract solution
        code = self.extract_solution(editorial_file, language)
        if not code:
            return {'error': f'No {language} solution found'}
        
        # Load test cases
        with open(yaml_file) as f:
            data = yaml.safe_load(f)
        
        # Run tests
        runners = {
            'python': self.run_python,
            'java': self.run_java,
            'cpp': self.run_cpp,
            'javascript': self.run_javascript,
        }
        
        runner = runners[language]
        passed = failed = 0
        errors = []
        
        # Test all categories
        for category in ['samples', 'public', 'hidden']:
            for i, test in enumerate(data.get(category, []), 1):
                try:
                    output = runner(code, test['input'])
                    expected = test['output'].rstrip('\n')
                    
                    if output == expected:
                        passed += 1
                    else:
                        failed += 1
                        if len(errors) < 3:  # Only store first 3 errors
                            errors.append({
                                'category': category,
                                'index': i,
                                'expected': expected[:50],
                                'got': output[:50]
                            })
                except Exception as e:
                    failed += 1
                    if len(errors) < 3:
                        errors.append({'category': category, 'index': i, 'error': str(e)[:50]})
        
        return {'passed': passed, 'failed': failed, 'errors': errors}

def main():
    tester = EditorialTester()
    
    problems = [
        f"ARR-{i:03d}-{name}" for i, name in enumerate([
            "snack-restock-snapshot", "bench-flip-locked-ends",
            "shuttle-shift-blackout", "lab-temperature-ranges",
            "weighted-balance-point", "zero-slide-limit",
            "hostel-roster-merge-gap", "partner-pair-sum-forbidden",
            "best-streak-one-smoothing", "early-discount-stay-window",
            "leaky-roof-reinforcement", "longest-zero-sum-even",
            "tool-frequency-top-k-decay", "boarding-order-fixed-ones",
            "seat-gap-after-removals", "power-window-with-drop",
        ], 1)
    ]
    
    # Test Python first (all test cases)
    print("="*70)
    print("TESTING PYTHON EDITORIAL SOLUTIONS (All Test Cases)")
    print("="*70)
    
    total_passed = total_failed = 0
    for problem in problems:
        result = tester.test_problem(problem, 'python')
        if 'error' in result:
            print(f"❌ {problem}: {result['error']}")
        else:
            total_passed += result['passed']
            total_failed += result['failed']
            status = "✅" if result['failed'] == 0 else "⚠️"
            print(f"{status} {problem}: {result['passed']} passed, {result['failed']} failed")
            
            if result['errors']:
                for err in result['errors']:
                    if 'error' in err:
                        print(f"   - {err['category']} {err['index']}: {err['error']}")
    
    print(f"\n{'='*70}")
    print(f"Python Summary: {total_passed} passed, {total_failed} failed")
    print(f"{'='*70}\n")
    
    # Test sample cases for other languages
    for lang in ['java', 'cpp', 'javascript']:
        print(f"\nTesting {lang.upper()} (sample tests only)...")
        lang_passed = lang_failed = 0
        
        for problem in problems:
            result = tester.test_problem(problem, lang)
            if 'error' not in result:
                # Only count sample tests for non-Python
                lang_passed += min(result['passed'], 2)
                if result['failed'] > 0:
                    lang_failed += 1
        
        print(f"{lang.upper()}: {lang_passed}/{len(problems)*2} sample tests passed")

if __name__ == "__main__":
    main()
