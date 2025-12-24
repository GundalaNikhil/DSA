#!/usr/bin/env python3
"""
Multi-language test verification for Arrays editorial solutions.
Tests Java, C++, and JavaScript implementations against all test cases.
"""

import yaml
import re
import subprocess
import tempfile
import sys
from pathlib import Path
from io import StringIO

class LanguageTester:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.testcases_dir = self.base_dir / "testcases"
        self.editorials_dir = self.base_dir / "editorials"
        
    def extract_solution(self, editorial_file, language):
        """Extract solution code for specified language from editorial."""
        with open(editorial_file) as f:
            content = f.read()
        
        patterns = {
            'java': r'### Java\s*```java\s*(.*?)```',
            'cpp': r'### C\+\+\s*```cpp\s*(.*?)```',
            'javascript': r'### JavaScript\s*```javascript\s*(.*?)```',
        }
        
        match = re.search(patterns[language], content, re.DOTALL)
        if not match:
            return None
        return match.group(1).strip()
    
    def run_java_solution(self, code, input_data):
        """Compile and run Java solution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            
            # Write Java file
            java_file = tmppath / "Main.java"
            with open(java_file, 'w') as f:
                f.write(code)
            
            # Compile
            compile_result = subprocess.run(
                ['javac', 'Main.java'],
                cwd=tmppath,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if compile_result.returncode != 0:
                return f"COMPILE_ERROR: {compile_result.stderr}"
            
            # Run
            run_result = subprocess.run(
                ['java', 'Main'],
                input=input_data,
                capture_output=True,
                text=True,
                cwd=tmppath,
                timeout=5
            )
            
            if run_result.returncode != 0:
                return f"RUNTIME_ERROR: {run_result.stderr}"
            
            return run_result.stdout.rstrip('\n')
    
    def run_cpp_solution(self, code, input_data):
        """Compile and run C++ solution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            
            # Write C++ file
            cpp_file = tmppath / "solution.cpp"
            with open(cpp_file, 'w') as f:
                f.write(code)
            
            # Compile
            compile_result = subprocess.run(
                ['g++', '-std=c++17', '-o', 'solution', 'solution.cpp'],
                cwd=tmppath,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if compile_result.returncode != 0:
                return f"COMPILE_ERROR: {compile_result.stderr}"
            
            # Run
            run_result = subprocess.run(
                ['./solution'],
                input=input_data,
                capture_output=True,
                text=True,
                cwd=tmppath,
                timeout=5
            )
            
            if run_result.returncode != 0:
                return f"RUNTIME_ERROR: {run_result.stderr}"
            
            return run_result.stdout.rstrip('\n')
    
    def run_javascript_solution(self, code, input_data):
        """Run JavaScript solution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            
            # Write JS file
            js_file = tmppath / "solution.js"
            with open(js_file, 'w') as f:
                f.write(code)
            
            # Run
            run_result = subprocess.run(
                ['node', 'solution.js'],
                input=input_data,
                capture_output=True,
                text=True,
                cwd=tmppath,
                timeout=5
            )
            
            if run_result.returncode != 0:
                return f"RUNTIME_ERROR: {run_result.stderr}"
            
            return run_result.stdout.rstrip('\n')
    
    def test_problem(self, problem_id, language):
        """Test a single problem in specified language."""
        yaml_file = self.testcases_dir / f"{problem_id}.yaml"
        editorial_file = self.editorials_dir / f"{problem_id}.md"
        
        # Special case for ARR-004
        if problem_id == "ARR-004-lab-temperature-ranges":
            editorial_file = self.editorials_dir / "ARR-004-lab-temperature-offline-ranges.md"
        
        if not editorial_file.exists():
            return {'error': f'Editorial not found: {editorial_file}'}
        
        # Extract solution
        code = self.extract_solution(editorial_file, language)
        if not code:
            return {'error': f'No {language} solution found in editorial'}
        
        # Load test cases
        with open(yaml_file) as f:
            data = yaml.safe_load(f)
        
        # Run tests
        runners = {
            'java': self.run_java_solution,
            'cpp': self.run_cpp_solution,
            'javascript': self.run_javascript_solution,
        }
        
        runner = runners[language]
        results = {'passed': 0, 'failed': 0, 'errors': []}
        
        # Test samples
        for i, test in enumerate(data.get('samples', []), 1):
            try:
                output = runner(code, test['input'])
                expected = test['output'].rstrip('\n')
                
                if output == expected:
                    results['passed'] += 1
                else:
                    results['failed'] += 1
                    results['errors'].append({
                        'type': 'sample',
                        'index': i,
                        'expected': expected,
                        'got': output
                    })
            except Exception as e:
                results['failed'] += 1
                results['errors'].append({
                    'type': 'sample',
                    'index': i,
                    'error': str(e)
                })
        
        return results
    
    def test_all_problems(self, language):
        """Test all Arrays problems in specified language."""
        problems = [
            f"ARR-{i:03d}-{name}" for i, name in enumerate([
                "snack-restock-snapshot",
                "bench-flip-locked-ends",
                "shuttle-shift-blackout",
                "lab-temperature-ranges",
                "weighted-balance-point",
                "zero-slide-limit",
                "hostel-roster-merge-gap",
                "partner-pair-sum-forbidden",
                "best-streak-one-smoothing",
                "early-discount-stay-window",
                "leaky-roof-reinforcement",
                "longest-zero-sum-even",
                "tool-frequency-top-k-decay",
                "boarding-order-fixed-ones",
                "seat-gap-after-removals",
                "power-window-with-drop",
            ], 1)
        ]
        
        print(f"\n{'='*60}")
        print(f"Testing {language.upper()} solutions")
        print(f"{'='*60}\n")
        
        total_passed = 0
        total_failed = 0
        
        for problem in problems:
            print(f"Testing {problem}...", end=' ')
            results = self.test_problem(problem, language)
            
            if 'error' in results:
                print(f"❌ {results['error']}")
                continue
            
            total_passed += results['passed']
            total_failed += results['failed']
            
            if results['failed'] == 0:
                print(f"✅ All {results['passed']} tests passed")
            else:
                print(f"⚠️  {results['passed']} passed, {results['failed']} failed")
                for error in results['errors'][:3]:  # Show first 3 errors
                    if 'error' in error:
                        print(f"   - {error['type']} {error['index']}: {error['error']}")
                    else:
                        print(f"   - {error['type']} {error['index']}: Expected '{error['expected']}', got '{error['got']}'")
        
        print(f"\n{'='*60}")
        print(f"{language.upper()} Summary: {total_passed} passed, {total_failed} failed")
        print(f"{'='*60}\n")

def main():
    base = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays")
    tester = LanguageTester(base)
    
    languages = ['java', 'cpp', 'javascript']
    
    if len(sys.argv) > 1:
        languages = [sys.argv[1]]
    
    for lang in languages:
        tester.test_all_problems(lang)

if __name__ == "__main__":
    main()
