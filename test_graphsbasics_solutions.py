#!/usr/bin/env python3
"""
GraphsBasics Solutions Test Runner
Tests all GraphsBasics Python solutions against samples, public, and hidden test cases
"""

import os
import sys
import yaml
import subprocess
from pathlib import Path

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def load_test_cases(yaml_file):
    """Load test cases from YAML file"""
    try:
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except Exception as e:
        print(f"{RED}Error loading {yaml_file}: {e}{RESET}")
        return None

def run_solution(solution_file, input_data):
    """Run a solution with given input and return output"""
    try:
        result = subprocess.run(
            ['python3', solution_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return None, -1
    except Exception as e:
        return str(e), -2

def test_solution(problem_id, solution_file, testcase_file):
    """Test a single solution against all test cases"""
    
    # Check if files exist
    if not os.path.exists(solution_file):
        print(f"{RED}✗ Solution file not found: {solution_file}{RESET}")
        return False, {"sample": 0, "public": 0, "hidden": 0}, {"sample": 0, "public": 0, "hidden": 0}
    
    if not os.path.exists(testcase_file):
        print(f"{RED}✗ Test case file not found: {testcase_file}{RESET}")
        return False, {"sample": 0, "public": 0, "hidden": 0}, {"sample": 0, "public": 0, "hidden": 0}
    
    # Load test cases
    test_data = load_test_cases(testcase_file)
    if not test_data:
        return False, {"sample": 0, "public": 0, "hidden": 0}, {"sample": 0, "public": 0, "hidden": 0}
    
    # Test all categories
    results = {"sample": [], "public": [], "hidden": []}
    
    for category in ["samples", "public", "hidden"]:
        if category not in test_data or not test_data[category]:
            continue
        
        cat_key = "sample" if category == "samples" else category
        
        for i, test_case in enumerate(test_data[category], 1):
            input_data = test_case.get('input', '')
            if isinstance(input_data, str):
                input_data = input_data.strip()
            else:
                input_data = str(input_data)
            
            expected = test_case.get('output', '')
            if isinstance(expected, str):
                expected = expected.strip()
            else:
                expected = str(expected)
            
            output, returncode = run_solution(solution_file, input_data)
            
            if returncode == -1:
                results[cat_key].append({
                    'passed': False,
                    'error': 'TIMEOUT',
                    'test_num': i
                })
            elif returncode == -2:
                results[cat_key].append({
                    'passed': False,
                    'error': 'EXECUTION ERROR',
                    'test_num': i
                })
            elif output is None:
                results[cat_key].append({
                    'passed': False,
                    'error': 'NO OUTPUT',
                    'test_num': i
                })
            else:
                passed = output == expected
                results[cat_key].append({
                    'passed': passed,
                    'input': input_data,
                    'expected': expected,
                    'got': output,
                    'test_num': i
                })
    
    # Calculate statistics
    passed = {
        "sample": sum(1 for r in results["sample"] if r['passed']),
        "public": sum(1 for r in results["public"] if r['passed']),
        "hidden": sum(1 for r in results["hidden"] if r['passed'])
    }
    
    total = {
        "sample": len(results["sample"]),
        "public": len(results["public"]),
        "hidden": len(results["hidden"])
    }
    
    all_passed = all(r['passed'] for cat in results.values() for r in cat)
    
    # Print results
    print(f"\n{BOLD}{BLUE}Testing: {problem_id}{RESET}")
    
    for cat_name, cat_key in [("Sample", "sample"), ("Public", "public"), ("Hidden", "hidden")]:
        if total[cat_key] > 0:
            status = f"{GREEN}✓{RESET}" if passed[cat_key] == total[cat_key] else f"{RED}✗{RESET}"
            print(f"  {status} {cat_name}: {passed[cat_key]}/{total[cat_key]}")
            
            # Show failures
            failures = [r for r in results[cat_key] if not r['passed']]
            if failures:
                for fail in failures[:3]:  # Show first 3 failures
                    print(f"    {RED}Failed Test {fail['test_num']}:{RESET}")
                    if 'error' in fail:
                        print(f"      Error: {fail['error']}")
                    else:
                        print(f"      Input: {fail['input'][:100]}...")
                        print(f"      Expected: {fail['expected'][:100]}...")
                        print(f"      Got: {fail['got'][:100]}...")
    
    status_icon = f"{GREEN}✓{RESET}" if all_passed else f"{RED}✗{RESET}"
    total_passed = sum(passed.values())
    total_tests = sum(total.values())
    print(f"  {status_icon} Overall: {total_passed}/{total_tests}")
    
    return all_passed, passed, total

def main():
    """Main test runner"""
    base_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/GraphsBasics")
    solutions_dir = base_dir / "solutions" / "python"
    testcases_dir = base_dir / "testcases"
    
    # Get all solution files
    solution_files = sorted([f for f in os.listdir(solutions_dir) if f.endswith('.py')])
    
    print(f"{BOLD}{BLUE}{'='*70}{RESET}")
    print(f"{BOLD}{BLUE}GraphsBasics Solutions Test Runner{RESET}")
    print(f"{BOLD}{BLUE}{'='*70}{RESET}")
    
    all_results = []
    total_stats = {"sample": {"passed": 0, "total": 0}, 
                   "public": {"passed": 0, "total": 0}, 
                   "hidden": {"passed": 0, "total": 0}}
    
    for solution_file in solution_files:
        problem_id = solution_file.replace('.py', '')
        testcase_file = testcases_dir / f"{problem_id}.yaml"
        solution_path = solutions_dir / solution_file
        
        passed, passed_counts, total_counts = test_solution(
            problem_id, 
            str(solution_path), 
            str(testcase_file)
        )
        
        all_results.append({
            'problem_id': problem_id,
            'passed': passed,
            'passed_counts': passed_counts,
            'total_counts': total_counts
        })
        
        # Update totals
        for cat in ["sample", "public", "hidden"]:
            total_stats[cat]["passed"] += passed_counts[cat]
            total_stats[cat]["total"] += total_counts[cat]
    
    # Print summary
    print(f"\n{BOLD}{BLUE}{'='*70}{RESET}")
    print(f"{BOLD}{BLUE}SUMMARY{RESET}")
    print(f"{BOLD}{BLUE}{'='*70}{RESET}")
    
    problems_passed = sum(1 for r in all_results if r['passed'])
    problems_total = len(all_results)
    
    print(f"\n{BOLD}Problems: {problems_passed}/{problems_total}{RESET}")
    
    for cat_name, cat_key in [("Sample", "sample"), ("Public", "public"), ("Hidden", "hidden")]:
        passed = total_stats[cat_key]["passed"]
        total = total_stats[cat_key]["total"]
        if total > 0:
            percentage = (passed / total * 100) if total > 0 else 0
            status = f"{GREEN}✓{RESET}" if passed == total else f"{RED}✗{RESET}"
            print(f"{status} {cat_name} Tests: {passed}/{total} ({percentage:.1f}%)")
    
    total_passed = sum(s["passed"] for s in total_stats.values())
    total_tests = sum(s["total"] for s in total_stats.values())
    overall_percentage = (total_passed / total_tests * 100) if total_tests > 0 else 0
    
    print(f"\n{BOLD}Overall: {total_passed}/{total_tests} ({overall_percentage:.1f}%){RESET}")
    
    # List failed problems
    failed_problems = [r for r in all_results if not r['passed']]
    if failed_problems:
        print(f"\n{RED}{BOLD}Failed Problems:{RESET}")
        for prob in failed_problems:
            print(f"  {RED}✗{RESET} {prob['problem_id']}")
            for cat in ["sample", "public", "hidden"]:
                if prob['total_counts'][cat] > 0:
                    print(f"    {cat}: {prob['passed_counts'][cat]}/{prob['total_counts'][cat]}")
    else:
        print(f"\n{GREEN}{BOLD}🎉 ALL PROBLEMS PASSED! 🎉{RESET}")
    
    print(f"\n{BOLD}{BLUE}{'='*70}{RESET}\n")
    
    return 0 if problems_passed == problems_total else 1

if __name__ == "__main__":
    sys.exit(main())
