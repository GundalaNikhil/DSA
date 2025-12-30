import yaml
import subprocess
import sys
import os

def run_test(problem_id, solution_path, testcases_path):
    with open(testcases_path, 'r') as f:
        tests = yaml.safe_load(f)
    
    results = {"passed": 0, "total": 0, "failures": []}
    
    categories = ["samples", "public", "hidden"]
    for cat in categories:
        if cat not in tests or not tests[cat]:
            continue
        
        cat_passed = 0
        cat_total = 0
        cat_fail = None
        
        for i, test in enumerate(tests[cat]):
            input_str = test['input']
            expected_output = test['output'].strip()
            
            try:
                process = subprocess.Popen(
                    [sys.executable, solution_path],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                stdout, stderr = process.communicate(input=input_str, timeout=5)
                
                actual_output = stdout.strip()
                cat_total += 1
                results["total"] += 1
                
                if actual_output == expected_output:
                    cat_passed += 1
                    results["passed"] += 1
                else:
                    if cat_fail is None:
                        # Truncate for readability
                        cat_fail = f"Exp '{expected_output[:50]}...' Got '{actual_output[:50]}...'"
            except subprocess.TimeoutExpired:
                process.kill()
                cat_total += 1
                results["total"] += 1
                if cat_fail is None:
                    cat_fail = "Timeout"
            except Exception as e:
                cat_total += 1
                results["total"] += 1
                if cat_fail is None:
                    cat_fail = str(e)
        
        print(f"  {cat.upper()}: {cat_passed}/{cat_total} PASSED")
        if cat_fail:
            print(f"    First Fail: {cat_fail}")

    return results

def main():
    base_dir = "dsa-problems/Probabilistic"
    problems = [
        "PRB-001-coin-flip-streak-probability",
        "PRB-002-expected-steps-random-walk-1d",
        "PRB-003-reservoir-sampling-k",
        "PRB-004-monte-carlo-pi",
        "PRB-005-bloom-filter-fpr",
        "PRB-006-min-cut-random-contraction",
        "PRB-007-skip-list-expected-height",
        "PRB-008-quickselect-expected-comparisons",
        "PRB-009-treap-priority-invariants",
        "PRB-010-markov-chain-absorption",
        "PRB-011-coupon-collector-expected",
        "PRB-012-poisson-approx-binomial",
        "PRB-013-random-walk-hitting-prob-2d",
        "PRB-014-randomized-mst-verification",
        "PRB-015-median-uniforms-clt",
        "PRB-016-permutation-cycle-structure"
    ]
    
    print("="*80)
    print("PROBABILISTIC SOLUTIONS AUDIT")
    print("="*80)
    
    failed_any = False
    for prob in problems:
        print(f"\nTesting: {prob}")
        sol_path = os.path.join(base_dir, "solutions/python", f"{prob}.py")
        yaml_path = os.path.join(base_dir, "testcases", f"{prob}.yaml")
        
        if not os.path.exists(sol_path):
            print(f"  ERROR: Solution not found at {sol_path}")
            failed_any = True
            continue
        if not os.path.exists(yaml_path):
            print(f"  ERROR: Yaml not found at {yaml_path}")
            failed_any = True
            continue
            
        res = run_test(prob, sol_path, yaml_path)
        if res["passed"] < res["total"]:
            failed_any = True

    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    if failed_any:
        print("✗ Some problems failed or are missing test cases.")
    else:
        print("✓ All current test cases passed!")

if __name__ == "__main__":
    main()
