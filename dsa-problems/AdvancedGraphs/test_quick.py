#!/usr/bin/env python3
"""
Quick test of AGR-006 solution against testcases for C++, Java, and Python.
"""
import os
import re
import sys
import yaml
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Optional, Tuple


class LanguageTester:
    def __init__(self, language: str):
        self.language = language
        self.file_ext = {
            'cpp': '.cpp',
            'java': '.java',
            'python': '.py'
        }[language]
        
    def extract_solution(self, editorial_file: str) -> Optional[str]:
        """Extract solution code from editorial markdown."""
        with open(editorial_file, 'r') as f:
            content = f.read()
        
        # Find code block for the language
        if self.language == 'cpp':
            pattern = r'### C\+\+\n\n```(?:cpp|c\+\+)\n(.*?)\n```'
        elif self.language == 'java':
            pattern = r'### Java\n\n```java\n(.*?)\n```'
        elif self.language == 'python':
            pattern = r'### Python\n\n```python\n(.*?)\n```'
        
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return None
        
        return match.group(1)
    
    def compile_code(self, code: str, temp_file: str) -> Tuple[bool, str]:
        """Compile code if necessary (C++, Java)."""
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
        
        else:  # Python doesn't need compilation
            return True, temp_file
    
    def run_test_case(self, solution_code: str, test_input: str) -> Tuple[Optional[str], Optional[str]]:
        """Run a single test case through the solution."""
        # Create temporary file with solution
        if self.language == 'java':
            # Extract class name to name the file correctly
            class_match = re.search(r'public\s+class\s+(\w+)', solution_code)
            if class_match:
                class_name = class_match.group(1)
                temp_dir = tempfile.mkdtemp()
                temp_file = os.path.join(temp_dir, f'{class_name}.java')
            else:
                temp_dir = tempfile.mkdtemp()
                temp_file = os.path.join(temp_dir, 'Solution.java')
        else:
            temp_dir = None
            temp_file = tempfile.NamedTemporaryFile(
                mode='w', 
                suffix=self.file_ext, 
                delete=False
            ).name
        
        try:
            with open(temp_file, 'w') as f:
                f.write(solution_code)
            
            # Compile if necessary
            success, compile_result = self.compile_code(solution_code, temp_file)
            if not success:
                return None, f"COMPILE_ERROR: {compile_result}"
            
            # Run the solution with test input
            if self.language == 'cpp':
                cmd = [compile_result]
            elif self.language == 'java':
                cmd = ['java', '-cp', temp_dir or os.path.dirname(temp_file), compile_result]
            else:  # python
                cmd = ['python3', temp_file]
            
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
        finally:
            # Cleanup
            try:
                if self.language == 'cpp':
                    os.unlink(temp_file)
                    output_file = temp_file.replace('.cpp', '')
                    if os.path.exists(output_file):
                        os.unlink(output_file)
                elif self.language == 'java':
                    if temp_dir:
                        import shutil
                        shutil.rmtree(temp_dir, ignore_errors=True)
                else:
                    os.unlink(temp_file)
            except:
                pass


def test_problem(prob_id: str, language: str) -> Dict:
    """Test all test cases for a single problem in a specific language."""
    tester = LanguageTester(language)
    
    # Find files
    editorial_files = list(Path('editorials').glob(f'{prob_id}*.md'))
    testcase_files = list(Path('testcases').glob(f'{prob_id}*.yaml'))
    
    if not editorial_files or not testcase_files:
        return {'status': 'FILES_NOT_FOUND', 'passed': 0, 'failed': 0, 'errors': []}
    
    editorial_file = editorial_files[0]
    testcase_file = testcase_files[0]
    
    # Extract solution
    solution_code = tester.extract_solution(editorial_file)
    if not solution_code:
        return {'status': 'NO_SOLUTION', 'passed': 0, 'failed': 0, 'errors': []}
    
    # Load test cases
    with open(testcase_file, 'r') as f:
        tc_data = yaml.safe_load(f)
    
    # Run all test cases
    results = {'status': 'OK', 'passed': 0, 'failed': 0, 'errors': []}
    
    for category in ['samples', 'public', 'hidden']:
        if category not in tc_data:
            continue
        
        for idx, tc in enumerate(tc_data[category]):
            tc_id = f"{category}[{idx}]"
            test_input = tc['input']
            expected_output = tc['output'].strip()
            
            actual_output, error = tester.run_test_case(solution_code, test_input)
            
            if error:
                results['failed'] += 1
                results['errors'].append({
                    'tc_id': tc_id,
                    'error': error,
                    'type': 'ERROR'
                })
            elif actual_output != expected_output:
                results['failed'] += 1
                results['errors'].append({
                    'tc_id': tc_id,
                    'expected': expected_output[:100],
                    'actual': actual_output[:100] if actual_output else 'None',
                    'type': 'WRONG_ANSWER'
                })
            else:
                results['passed'] += 1
    
    return results


def main():
    print("="*80)
    print("QUICK TEST: AGR-006 Articulation Points and BCC")
    print("="*80)
    
    languages = ['cpp', 'java', 'python']
    prob_id = 'AGR-006'
    
    for lang in languages:
        lang_name = {'cpp': 'C++', 'java': 'Java', 'python': 'Python'}[lang]
        print(f"\n{lang_name}:")
        print("-" * 40)
        
        try:
            results = test_problem(prob_id, lang)
            
            if results['status'] == 'NO_SOLUTION':
                print(f"  ⚠️  No solution found")
            elif results['status'] == 'FILES_NOT_FOUND':
                print(f"  ⚠️  Files not found")
            else:
                total = results['passed'] + results['failed']
                print(f"  Total test cases: {total}")
                print(f"  ✅ Passed: {results['passed']}")
                print(f"  ❌ Failed: {results['failed']}")
                
                if results['failed'] > 0:
                    print(f"\n  Failures:")
                    for error in results['errors']:
                        print(f"    • {error['tc_id']}: {error['type']}")
                        if error['type'] == 'WRONG_ANSWER':
                            print(f"      Expected: {error['expected'][:60]}")
                            print(f"      Actual:   {error['actual'][:60]}")
                        elif 'error' in error:
                            print(f"      {error['error'][:80]}")
        
        except Exception as e:
            print(f"  ❌ Exception: {str(e)}")


if __name__ == '__main__':
    os.chdir('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs')
    main()
