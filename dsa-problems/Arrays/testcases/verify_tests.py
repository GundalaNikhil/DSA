#!/usr/bin/env python3
"""
Test case verification script for Arrays problems.
Runs generated test cases against editorial solutions.
"""

import yaml
import sys
import re
from io import StringIO
from pathlib import Path
from typing import Dict, List, Tuple

class TestCaseVerifier:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.testcases_dir = self.base_path / "testcases"
        self.editorials_dir = self.base_path / "editorials"
        
    def extract_python_solution(self, editorial_path: Path) -> str:
        """Extract Python solution code from editorial markdown."""
        with open(editorial_path, 'r') as f:
            content = f.read()
        
        # Find Python section
        python_pattern = r'### Python\s*```python\s*(.*?)```'
        match = re.search(python_pattern, content, re.DOTALL)
        
        if not match:
            raise ValueError(f"No Python solution found in {editorial_path}")
        
        return match.group(1).strip()
    
    def run_test_case(self, solution_code: str, input_data: str) -> str:
        """Run solution with given input and return output."""
        # Create a namespace for execution
        namespace = {'__name__': '__main__'}
        
        # Redirect stdin and stdout
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            # Execute the solution code (this will define functions and run main())
            exec(solution_code, namespace)
            
            # Get the output
            output = sys.stdout.getvalue()
            
            return output.rstrip('\n')  # Remove trailing newline
            
        except Exception as e:
            # Return error info for debugging
            return f"ERROR: {str(e)}"
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def normalize_output(self, output: str) -> str:
        """Normalize output for comparison."""
        # Strip trailing whitespace from each line
        lines = [line.rstrip() for line in output.split('\n')]
        # Join and remove any trailing blank lines
        return '\n'.join(lines).rstrip()
    
    def verify_problem(self, problem_id: str) -> Dict:
        """Verify all test cases for a problem."""
        print(f"\n{'='*60}")
        print(f"Verifying {problem_id}")
        print(f"{'='*60}")
        
        # Load test cases
        yaml_file = self.testcases_dir / f"{problem_id}.yaml"
        if not yaml_file.exists():
            return {"error": f"Test case file not found: {yaml_file}"}
        
        with open(yaml_file, 'r') as f:
            test_data = yaml.safe_load(f)
        
        # Extract editorial solution
        editorial_file = self.editorials_dir / f"{problem_id}.md"
        if not editorial_file.exists():
            return {"error": f"Editorial file not found: {editorial_file}"}
        
        try:
            solution_code = self.extract_python_solution(editorial_file)
        except Exception as e:
            return {"error": f"Failed to extract solution: {e}"}
        
        results = {
            "problem": problem_id,
            "total": 0,
            "passed": 0,
            "failed": 0,
            "failures": []
        }
        
        # Test samples
        print("\nTesting samples...")
        for i, test in enumerate(test_data.get('samples', [])):
            results["total"] += 1
            if not self._run_single_test(solution_code, test, f"Sample {i+1}", results):
                results["failed"] += 1
            else:
                results["passed"] += 1
        
        # Test public cases
        print("\nTesting public cases...")
        for i, test in enumerate(test_data.get('public', [])):
            results["total"] += 1
            if not self._run_single_test(solution_code, test, f"Public {i+1}", results):
                results["failed"] += 1
            else:
                results["passed"] += 1
        
        # Test hidden cases (show summary only)
        print("\nTesting hidden cases...")
        hidden_failed = 0
        for i, test in enumerate(test_data.get('hidden', [])):
            results["total"] += 1
            if not self._run_single_test(solution_code, test, f"Hidden {i+1}", results, quiet=True):
                results["failed"] += 1
                hidden_failed += 1
            else:
                results["passed"] += 1
        
        if hidden_failed > 0:
            print(f"  ❌ {hidden_failed} hidden test(s) failed")
        else:
            print(f"  ✅ All {len(test_data.get('hidden', []))} hidden tests passed")
        
        return results
    
    def _run_single_test(self, solution_code: str, test: Dict, name: str, 
                        results: Dict, quiet: bool = False) -> bool:
        """Run a single test case."""
        try:
            input_data = test['input']
            expected = self.normalize_output(test['output'])
            
            actual = self.run_test_case(solution_code, input_data)
            actual = self.normalize_output(actual)
            
            if actual == expected:
                if not quiet:
                    print(f"  ✅ {name} passed")
                return True
            else:
                if not quiet:
                    print(f"  ❌ {name} FAILED")
                    print(f"     Expected: {repr(expected[:100])}")
                    print(f"     Got:      {repr(actual[:100])}")
                
                results["failures"].append({
                    "test": name,
                    "input": input_data[:100],
                    "expected": expected[:100],
                    "actual": actual[:100]
                })
                return False
                
        except Exception as e:
            if not quiet:
                print(f"  ❌ {name} ERROR: {e}")
            results["failures"].append({
                "test": name,
                "error": str(e)
            })
            return False

def main():
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays"
    verifier = TestCaseVerifier(base_path)
    
    # List of all problems to verify
    problems = [
        "ARR-001-snack-restock-snapshot",
        "ARR-002-bench-flip-locked-ends",
        "ARR-003-shuttle-shift-blackout",
        "ARR-004-lab-temperature-ranges",
        "ARR-005-weighted-balance-point",
        "ARR-006-zero-slide-limit",
        "ARR-007-hostel-roster-merge-gap",
        "ARR-008-partner-pair-sum-forbidden",
        "ARR-009-best-streak-one-smoothing",
        "ARR-010-early-discount-stay-window",
        "ARR-011-leaky-roof-reinforcement",
        "ARR-012-longest-zero-sum-even",
        "ARR-013-tool-frequency-top-k-decay",
        "ARR-014-boarding-order-fixed-ones",
        "ARR-015-seat-gap-after-removals",
        "ARR-016-power-window-with-drop",
    ]
    
    if len(sys.argv) > 1:
        # Verify specific problem
        problems = [sys.argv[1]]
    
    all_results = []
    total_passed = 0
    total_failed = 0
    
    for problem in problems:
        result = verifier.verify_problem(problem)
        all_results.append(result)
        
        if "error" not in result:
            total_passed += result["passed"]
            total_failed += result["failed"]
    
    # Print summary
    print(f"\n{'='*60}")
    print("VERIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total Tests: {total_passed + total_failed}")
    print(f"Passed: {total_passed} ✅")
    print(f"Failed: {total_failed} ❌")
    
    if total_failed > 0:
        print(f"\n⚠️  {total_failed} test case(s) need attention")
        sys.exit(1)
    else:
        print(f"\n🎉 All test cases passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
