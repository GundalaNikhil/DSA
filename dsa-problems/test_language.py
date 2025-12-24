#!/usr/bin/env python3
"""
Multi-Language Test Framework for DSA Problems
Tests C++, Java, Python, and JavaScript solutions separately
"""
import os
import re
import sys
import yaml
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Dict, Optional, Tuple, List
from dataclasses import dataclass


@dataclass
class TestResult:
    """Result of a single test case execution."""
    passed: bool
    expected: str
    actual: Optional[str]
    error: Optional[str]
    test_id: str


@dataclass
class ProblemResult:
    """Result for all test cases of a problem."""
    problem_id: str
    total: int
    passed: int
    failed: int
    test_results: List[TestResult]


class LanguageTester:
    """Base class for language-specific testing."""
    
    def __init__(self, language: str, topic_dir: str):
        self.language = language
        self.topic_dir = topic_dir
        self.file_ext = {
            'cpp': '.cpp',
            'java': '.java',
            'python': '.py',
            'javascript': '.js'
        }[language]
    
    def validate_hsh011_collision(self, test_input: str, actual_output: str, expected_output: str) -> Tuple[bool, Optional[str]]:
        """Custom validator for HSH-011: Rolling Hash Collision problem.
        
        Validates that the output contains two distinct strings of length L
        that hash to the same value under the given parameters B and M.
        
        Args:
            test_input: Input string containing "B M L"
            actual_output: Student's output (two strings, one per line)
            expected_output: Expected output (reference collision pair)
        
        Returns:
            (is_valid, error_message): True if valid collision, with optional error message
        """
        try:
            # Parse input parameters
            params = test_input.strip().split()
            if len(params) != 3:
                return False, "Invalid input format"
            
            B = int(params[0])
            M = int(params[1])
            L = int(params[2])
            
            # Parse actual output
            lines = actual_output.strip().split('\n')
            if len(lines) != 2:
                return False, f"Expected 2 strings, got {len(lines)}"
            
            s1 = lines[0].strip()
            s2 = lines[1].strip()
            
            # Check string lengths
            if len(s1) != L:
                return False, f"String 1 has length {len(s1)}, expected {L}"
            if len(s2) != L:
                return False, f"String 2 has length {len(s2)}, expected {L}"
            
            # Check strings are distinct
            if s1 == s2:
                return False, "Both strings are identical - not a collision"
            
            # Check all characters are lowercase letters
            if not s1.isalpha() or not s1.islower():
                return False, "String 1 contains non-lowercase letters"
            if not s2.isalpha() or not s2.islower():
                return False, "String 2 contains non-lowercase letters"
            
            # Compute hash for both strings
            def compute_hash(s: str) -> int:
                h = 0
                for char in s:
                    h = (h * B + ord(char)) % M
                return h
            
            h1 = compute_hash(s1)
            h2 = compute_hash(s2)
            
            # Check if hashes collide
            if h1 != h2:
                return False, f"Not a collision: hash({s1})={h1}, hash({s2})={h2}"
            
            # Valid collision!
            return True, None
            
        except Exception as e:
            return False, f"Validation error: {str(e)}"
        
    def extract_solution(self, editorial_file: str) -> Optional[str]:
        """Extract solution code from editorial markdown."""
        if not os.path.exists(editorial_file):
            return None
            
        with open(editorial_file, 'r') as f:
            content = f.read()
        
        # Find code block for the language
        patterns = {
            'cpp': r'### C\+\+\n\n```(?:cpp|c\+\+)\n(.*?)\n```',
            'java': r'### Java\n\n```java\n(.*?)\n```',
            'python': r'### Python\n\n```python\n(.*?)\n```',
            'javascript': r'### JavaScript\n\n```(?:javascript|js)\n(.*?)\n```'
        }
        
        pattern = patterns[self.language]
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return None
        
        return match.group(1)
    
    def compile_code(self, code: str, temp_file: str) -> Tuple[bool, str]:
        """Compile code if necessary (C++, Java)."""
        try:
            if self.language == 'cpp':
                output_file = temp_file.replace('.cpp', '')
                result = subprocess.run(
                    ['g++', '-std=c++17', '-O2', temp_file, '-o', output_file],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode != 0:
                    return False, result.stderr
                return True, output_file
            
            elif self.language == 'java':
                result = subprocess.run(
                    ['javac', temp_file],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode != 0:
                    return False, result.stderr
                # Extract class name from code
                class_match = re.search(r'public\s+class\s+(\w+)', code)
                if class_match:
                    class_name = class_match.group(1)
                else:
                    class_name = 'Solution'
                return True, class_name
            
            elif self.language == 'javascript':
                # Node.js doesn't need compilation
                return True, temp_file
            
            else:  # Python doesn't need compilation
                return True, temp_file
        except Exception as e:
            return False, str(e)
    
    def run_executable(self, cmd: List[str], temp_dir: Optional[str], temp_file: str, test_input: str) -> Tuple[Optional[str], Optional[str]]:
        """Run the already compiled/prepared solution with test input."""
        try:
            result = subprocess.run(
                cmd,
                input=test_input,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                return None, f"RUNTIME_ERROR: {result.stderr[:200]}"
            
            return result.stdout.strip(), None
        
        except subprocess.TimeoutExpired:
            return None, "TIMEOUT"
        except Exception as e:
            return None, f"ERROR: {str(e)}"

    def run_test_case(self, solution_code: str, test_input: str) -> Tuple[Optional[str], Optional[str]]:
        """Run a single test case through the solution (deprecated for optimized runs)."""
        # This is kept for backward compatibility if needed, but not used in the optimized loop
        return self._run_single_test_full(solution_code, test_input)

    def _run_single_test_full(self, solution_code: str, test_input: str) -> Tuple[Optional[str], Optional[str]]:
        # Original logic moved here if needed
        pass
    
    def test_problem(self, prob_id: str) -> ProblemResult:
        """Test all test cases for a single problem."""
        # Find files
        editorial_files = list(Path(self.topic_dir).glob(f'editorials/{prob_id}*.md'))
        testcase_files = list(Path(self.topic_dir).glob(f'testcases/{prob_id}*.yaml'))
        
        if not editorial_files or not testcase_files:
            return ProblemResult(prob_id, 0, 0, 0, [])
        
        editorial_file = editorial_files[0]
        testcase_file = testcase_files[0]
        
        # Extract solution
        solution_code = self.extract_solution(editorial_file)
        if not solution_code:
            return ProblemResult(prob_id, 0, 0, 0, [])
        
        # Load test cases
        with open(testcase_file, 'r') as f:
            tc_data = yaml.safe_load(f)

        # PREPARE SOLUTION ONCE
        if self.language == 'java':
            class_match = re.search(r'public\s+class\s+(\w+)', solution_code)
            class_name = class_match.group(1) if class_match else 'Solution'
            temp_dir = tempfile.mkdtemp()
            temp_file = os.path.join(temp_dir, f'{class_name}.java')
        else:
            temp_dir = None
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix=self.file_ext, delete=False).name

        try:
            with open(temp_file, 'w') as f:
                f.write(solution_code)
            
            success, compile_result = self.compile_code(solution_code, temp_file)
            if not success:
                return ProblemResult(prob_id, 1, 0, 1, [TestResult(False, "", None, f"COMPILE_ERROR: {compile_result[:200]}", "compile")])
            
            if self.language == 'cpp':
                cmd = [compile_result]
            elif self.language == 'java':
                cmd = ['java', '-cp', temp_dir or os.path.dirname(temp_file), compile_result]
            elif self.language == 'javascript':
                cmd = ['node', temp_file]
            else:  # python
                cmd = ['python3', temp_file]
            
            # Run all test cases
            test_results = []
            passed = 0
            failed = 0
            
            for category in ['samples', 'public', 'hidden']:
                if category not in tc_data:
                    continue
                
                for idx, tc in enumerate(tc_data[category]):
                    tc_id = f"{category}[{idx}]"
                    test_input = tc['input']
                    expected_output = tc['output'].strip()
                    
                    actual_output, error = self.run_executable(cmd, temp_dir, temp_file, test_input)
                    
                    if error:
                        failed += 1
                        test_results.append(TestResult(
                            passed=False,
                            expected=expected_output[:100],
                            actual=None,
                            error=error[:200],
                            test_id=tc_id
                        ))
                    else:
                        # Check match
                        is_match = False
                        validation_error = "WRONG_ANSWER"
                        
                        if prob_id.startswith('HSH-011'):
                            is_valid, val_error = self.validate_hsh011_collision(
                                test_input, actual_output, expected_output
                            )
                            if is_valid:
                                is_match = True
                            else:
                                validation_error = val_error if val_error else "INVALID_COLLISION"
                        else:
                            is_match = (actual_output == expected_output)
                        
                        if not is_match:
                            failed += 1
                            test_results.append(TestResult(
                                passed=False,
                                expected=expected_output[:100],
                                actual=actual_output[:100] if actual_output else 'None',
                                error=validation_error,
                                test_id=tc_id
                            ))
                        else:
                            passed += 1
                            test_results.append(TestResult(
                                passed=True,
                                expected=expected_output[:100],
                                actual=actual_output[:100] if actual_output else 'None',
                                error=None,
                                test_id=tc_id
                            ))
            
            total = passed + failed
            return ProblemResult(prob_id, total, passed, failed, test_results)

        finally:
            # Cleanup
            try:
                if self.language == 'cpp':
                    if os.path.exists(temp_file): os.unlink(temp_file)
                    output_file = temp_file.replace('.cpp', '')
                    if os.path.exists(output_file): os.unlink(output_file)
                elif self.language == 'java':
                    if temp_dir: shutil.rmtree(temp_dir, ignore_errors=True)
                else:
                    if os.path.exists(temp_file): os.unlink(temp_file)
            except:
                pass
    
    def test_all_problems(self, problem_ids: List[str]) -> Dict[str, ProblemResult]:
        """Test all problems in the topic."""
        results = {}
        for prob_id in problem_ids:
            results[prob_id] = self.test_problem(prob_id)
        return results


def print_results(language: str, results: Dict[str, ProblemResult]):
    """Print test results for a language."""
    print(f"\n{'='*80}")
    print(f"{language.upper()} TEST RESULTS")
    print(f"{'='*80}\n")
    
    total_passed = 0
    total_failed = 0
    total_tests = 0
    
    for prob_id, result in results.items():
        if result.total == 0:
            print(f"{prob_id}: ⚠️  No tests or solution not found")
            continue
        
        total_tests += result.total
        total_passed += result.passed
        total_failed += result.failed
        
        if result.failed == 0:
            print(f"{prob_id}: ✅ {result.passed}/{result.total}")
        else:
            print(f"{prob_id}: ❌ {result.passed}/{result.total} (Failed: {result.failed})")
            
            # Show first 2 failures
            failures = [tr for tr in result.test_results if not tr.passed][:2]
            for failure in failures:
                print(f"  • {failure.test_id}: {failure.error}")
                if failure.error == "WRONG_ANSWER":
                    print(f"    Expected: {failure.expected[:40]}...")
                    print(f"    Actual:   {failure.actual[:40] if failure.actual else 'None'}...")
    
    print(f"\n{'='*80}")
    print(f"SUMMARY - {language.upper()}")
    print(f"{'='*80}")
    print(f"Total Tests: {total_tests}")
    print(f"✅ Passed: {total_passed}")
    print(f"❌ Failed: {total_failed}")
    
    if total_tests > 0:
        pass_rate = (total_passed / total_tests) * 100
        print(f"Pass Rate: {pass_rate:.1f}%")
    
    if total_failed == 0 and total_tests > 0:
        print(f"\n🎉 ALL {total_tests} TESTS PASSED!")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python test_language.py <language> <topic_dir> [problem_ids...]")
        print("Example: python test_language.py python AdvancedGraphs AGR-001 AGR-002")
        print("Example: python test_language.py cpp Arrays ARR-001 ARR-002 ARR-003")
        sys.exit(1)
    
    language = sys.argv[1].lower()
    topic_dir = sys.argv[2]
    problem_ids = sys.argv[3:] if len(sys.argv) > 3 else []
    
    # If no problem IDs specified, find all problems
    if not problem_ids:
        testcase_dir = Path(topic_dir) / 'testcases'
        if testcase_dir.exists():
            yaml_files = testcase_dir.glob('*.yaml')
            problem_ids = [f.stem for f in yaml_files]
            problem_ids.sort()
    
    if not problem_ids:
        print(f"No problems found in {topic_dir}")
        sys.exit(1)
    
    print(f"Testing {len(problem_ids)} problems in {language}...")
    
    tester = LanguageTester(language, topic_dir)
    results = tester.test_all_problems(problem_ids)
    print_results(language, results)
