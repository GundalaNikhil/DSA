#!/usr/bin/env python3
"""Comprehensive test of all Queue solutions against regenerated testcases"""
import subprocess
import yaml
import os
from pathlib import Path

def run_solution(solution_path, test_input):
    """Run a solution and get its output"""
    try:
        result = subprocess.run(
            ['python3', solution_path],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip(), True
    except:
        return "", False

def test_problem(problem_name, solution_path, testcase_path):
    """Test one Queue problem"""
    # Load testcases
    with open(testcase_path, 'r') as f:
        data = yaml.safe_load(f)

    total_tests = 0
    passed_tests = 0

    # Test samples, public, and hidden
    for section in ['samples', 'public', 'hidden']:
        if section not in data:
            continue

        for idx, test in enumerate(data[section]):
            total_tests += 1
            input_str = test['input']
            expected_output = test['output']

            actual_output, success = run_solution(solution_path, input_str)

            if not success:
                continue

            if actual_output == expected_output:
                passed_tests += 1

    return passed_tests, total_tests

def main():
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues"

    problems = [
        ("QUE-001-campus-service-line", "QUE-001-campus-service-line"),
        ("QUE-002-circular-shuttle-buffer-overwrite", "QUE-002-circular-shuttle-buffer-overwrite"),
        ("QUE-003-cafeteria-queue-rotation", "QUE-003-cafeteria-queue-rotation"),
        ("QUE-004-hallway-interleave", "QUE-004-hallway-interleave"),
        ("QUE-005-lab-printer-reversal", "QUE-005-lab-printer-reversal"),
        ("QUE-006-ticket-window-distinct-prefix", "QUE-006-ticket-window-distinct-prefix"),
        ("QUE-007-lab-window-instability", "QUE-007-lab-window-instability"),
        ("QUE-008-corridor-window-second-minimum", "QUE-008-corridor-window-second-minimum"),
        ("QUE-009-customer-service-queue", "QUE-009-battery-lab-first-negative"),
        ("QUE-010-shuttle-seat-assignment", "QUE-010-shuttle-seat-assignment"),
        ("QUE-011-event-registration-merge", "QUE-011-event-registration-merge"),
        ("QUE-012-bus-loop-one-skip", "QUE-012-bus-loop-one-skip"),
        ("QUE-013-task-stream-rate-limit", "QUE-013-task-stream-rate-limit"),
        ("QUE-014-deque-balance-rearrange", "QUE-014-deque-balance-rearrange"),
        ("QUE-015-festival-lantern-spread", "QUE-015-festival-lantern-spread"),
        ("QUE-016-assembly-line-buffer-swap", "QUE-016-assembly-line-buffer-swap"),
    ]

    print("=" * 80)
    print("QUEUE MODULE COMPREHENSIVE TEST")
    print("=" * 80)

    total_passed = 0
    total_tests = 0
    results = []

    for sol_name, test_name in problems:
        solution_path = f"{base_path}/solutions/python/{sol_name}.py"
        testcase_path = f"{base_path}/testcases/{test_name}.yaml"
        prob_name = test_name  # For display

        if not os.path.exists(solution_path):
            print(f"⚠️  {prob_name}: Solution not found")
            continue

        if not os.path.exists(testcase_path):
            print(f"⚠️  {prob_name}: Testcase not found")
            continue

        passed, total = test_problem(prob_name, solution_path, testcase_path)
        total_passed += passed
        total_tests += total

        status = "✅" if passed == total else "❌"
        pct = (passed / total * 100) if total > 0 else 0
        results.append((prob_name, passed, total, pct))
        print(f"{status} {prob_name}: {passed}/{total} ({pct:.1f}%)")

    print()
    print("=" * 80)
    print(f"TOTAL: {total_passed}/{total_tests} ({total_passed/total_tests*100:.1f}%)" if total_tests > 0 else "No tests found")
    print("=" * 80)

    # Show summary
    all_pass = all(p == t for _, p, t, _ in results)
    if all_pass:
        print("\n🎉 ALL QUEUES TESTS PASSING (100% ACCURACY)!")
    else:
        print("\n❌ Some tests still failing:")
        for name, p, t, pct in results:
            if p < t:
                print(f"  - {name}: {p}/{t}")

if __name__ == "__main__":
    main()
