#!/usr/bin/env python3
"""
Expand PRB-014, PRB-015, PRB-016 from 3 simplified cases to 30+ comprehensive test cases.
Following the Universal Test Case Generation Prompt.
"""

import math
import random

def format_testcase_yaml(data):
    """Format test cases in proper YAML with |- syntax."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section_name in ['samples', 'public', 'hidden']:
        if section_name not in data or not data[section_name]:
            continue
        lines.append(f"{section_name}:")
        for case in data[section_name]:
            lines.append("- input: |-")
            for line in case['input'].strip().split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            for line in case['output'].strip().split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines)


# ============================================================================
# PRB-014: Randomized MST Verification
# ============================================================================

def min_trials_mst(n, C):
    """
    Compute minimum trials needed for MST verification.
    Per-trial detection probability: p = 1 / n^2
    Target confidence: C
    Formula: t = ceil(log(1-C) / log(1-p))
    """
    p = 1.0 / (n * n)
    
    # Handle edge cases
    if C >= 1.0:
        return float('inf')
    if C <= 0.0:
        return 0
    
    # Compute using logarithms
    num = math.log(1.0 - C)
    den = math.log(1.0 - p)
    
    t = num / den
    return math.ceil(t)


def generate_prb014_cases():
    """Generate comprehensive test cases for PRB-014."""
    cases = {
        'problem_id': 'PRB-014',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample cases (3 cases)
    sample_params = [
        (10, 0.99),
        (100, 0.999),
        (5, 0.95)
    ]
    
    for n, C in sample_params:
        result = min_trials_mst(n, C)
        cases['samples'].append({
            'input': f"{n} {C}",
            'output': str(result)
        })
    
    # Public cases (5 cases) - basic and edge cases
    public_params = [
        (2, 0.5),          # Minimum n
        (3, 0.9),          # Small n, high confidence
        (10, 0.5),         # Medium n, medium confidence
        (20, 0.99999),     # Very high confidence
        (50, 0.1),         # Low confidence
    ]
    
    for n, C in public_params:
        result = min_trials_mst(n, C)
        cases['public'].append({
            'input': f"{n} {C}",
            'output': str(result)
        })
    
    # Hidden cases (30 cases) - comprehensive coverage
    hidden_params = []
    
    # Category 1: Small n (5 cases)
    for n in [4, 5, 7, 8, 9]:
        C = random.uniform(0.8, 0.999)
        hidden_params.append((n, C))
    
    # Category 2: Medium n, varying confidence (8 cases)
    for n in [15, 25, 30, 40, 50, 60, 70, 80]:
        C = random.choice([0.5, 0.9, 0.95, 0.99, 0.999])
        hidden_params.append((n, C))
    
    # Category 3: Large n (7 cases)
    for n in [100, 200, 500, 1000, 5000, 10000, 50000]:
        C = random.uniform(0.9, 0.9999)
        hidden_params.append((n, C))
    
    # Category 4: Very large n (5 cases)
    for n in [100000, 500000, 1000000, 10000000, 100000000]:
        C = random.uniform(0.95, 0.99)
        hidden_params.append((n, C))
    
    # Category 5: Edge cases with confidence (5 cases)
    edge_cases = [
        (1000, 0.999999),   # Very high confidence
        (10000, 0.5),       # Low confidence, large n
        (99999, 0.999),     # Near constraint boundary
        (2, 0.999999),      # Minimum n, very high confidence
        (3, 0.1),           # Minimum region, low confidence
    ]
    hidden_params.extend(edge_cases)
    
    for n, C in hidden_params:
        result = min_trials_mst(n, C)
        cases['hidden'].append({
            'input': f"{n} {C}",
            'output': str(result)
        })
    
    return cases


# ============================================================================
# PRB-015: Median of Uniforms CLT
# ============================================================================

def median_clt(n):
    """
    Compute mean and variance of sample median using CLT approximation.
    For uniform distribution on [0,1]:
    - Mean of median: 0.5
    - Variance of median: 1 / (4n)
    """
    mean = 0.5
    variance = 1.0 / (4.0 * n)
    return mean, variance


def generate_prb015_cases():
    """Generate comprehensive test cases for PRB-015."""
    cases = {
        'problem_id': 'PRB-015',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample cases (3 cases)
    sample_ns = [5, 10, 20]
    
    for n in sample_ns:
        mean, var = median_clt(n)
        cases['samples'].append({
            'input': str(n),
            'output': f"{mean:.6f} {var:.6f}"
        })
    
    # Public cases (5 cases)
    public_ns = [1, 2, 3, 4, 100]
    
    for n in public_ns:
        mean, var = median_clt(n)
        cases['public'].append({
            'input': str(n),
            'output': f"{mean:.6f} {var:.6f}"
        })
    
    # Hidden cases (30 cases)
    hidden_ns = []
    
    # Category 1: Small n (8 cases)
    hidden_ns.extend([6, 7, 8, 9, 11, 12, 15, 18])
    
    # Category 2: Medium n (8 cases)
    hidden_ns.extend([25, 30, 40, 50, 60, 75, 80, 90])
    
    # Category 3: Large n (8 cases)
    hidden_ns.extend([150, 200, 250, 300, 400, 500, 600, 700])
    
    # Category 4: Very large n (6 cases)
    hidden_ns.extend([800, 900, 950, 999, 1000])
    hidden_ns.append(random.randint(750, 850))
    
    for n in hidden_ns:
        mean, var = median_clt(n)
        cases['hidden'].append({
            'input': str(n),
            'output': f"{mean:.6f} {var:.6f}"
        })
    
    return cases


# ============================================================================
# PRB-016: Random Permutation Cycle Structure
# ============================================================================

def cycle_expectations(n, k):
    """
    Compute expected values for random permutation cycles.
    - Expected number of cycles of length k: 1/k
    - Expected longest cycle length: 0.624330 * n (Golomb-Dickman constant)
    """
    expected_cycles_k = 1.0 / k
    expected_longest = 0.624330 * n
    return expected_cycles_k, expected_longest


def generate_prb016_cases():
    """Generate comprehensive test cases for PRB-016."""
    cases = {
        'problem_id': 'PRB-016',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample cases (3 cases)
    sample_params = [
        (5, 2),
        (10, 3),
        (20, 5)
    ]
    
    for n, k in sample_params:
        exp_k, exp_longest = cycle_expectations(n, k)
        cases['samples'].append({
            'input': f"{n} {k}",
            'output': f"{exp_k:.6f} {exp_longest:.6f}"
        })
    
    # Public cases (5 cases)
    public_params = [
        (1, 1),    # Edge case: n=1
        (2, 1),    # Small n
        (5, 1),
        (10, 5),
        (100, 10)
    ]
    
    for n, k in public_params:
        exp_k, exp_longest = cycle_expectations(n, k)
        cases['public'].append({
            'input': f"{n} {k}",
            'output': f"{exp_k:.6f} {exp_longest:.6f}"
        })
    
    # Hidden cases (30 cases)
    hidden_params = []
    
    # Category 1: k=1 with varying n (5 cases)
    for n in [3, 7, 15, 50, 200]:
        hidden_params.append((n, 1))
    
    # Category 2: Small n, varying k (5 cases)
    for n in [10, 12, 15, 20, 25]:
        k = random.randint(1, n)
        hidden_params.append((n, k))
    
    # Category 3: Medium n, varying k (8 cases)
    for n in [30, 50, 75, 100, 150, 200, 300, 500]:
        k = random.randint(1, min(n, 50))
        hidden_params.append((n, k))
    
    # Category 4: Large n (7 cases)
    for n in [1000, 2000, 5000, 10000, 20000, 50000, 99999]:
        k = random.choice([1, 2, 5, 10, random.randint(1, 100)])
        hidden_params.append((n, k))
    
    # Category 5: Edge cases (5 cases)
    edge_cases = [
        (100000, 1),        # Maximum n, k=1
        (100000, 100000),   # k=n
        (50000, 50000),     # k=n
        (1000, 1000),       # k=n
        (10000, 5000),      # k=n/2
    ]
    hidden_params.extend(edge_cases)
    
    for n, k in hidden_params:
        exp_k, exp_longest = cycle_expectations(n, k)
        cases['hidden'].append({
            'input': f"{n} {k}",
            'output': f"{exp_k:.6f} {exp_longest:.6f}"
        })
    
    return cases


# ============================================================================
# Main Generation
# ============================================================================

def main():
    """Generate all expanded test cases."""
    
    print("=" * 80)
    print("EXPANDING PROBABILISTIC PROBLEMS: PRB-014, PRB-015, PRB-016")
    print("=" * 80)
    
    # PRB-014
    print("\n[1/3] Generating PRB-014: Randomized MST Verification...")
    prb014_cases = generate_prb014_cases()
    prb014_yaml = format_testcase_yaml(prb014_cases)
    
    output_path_014 = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases/PRB-014-randomized-mst-verification.yaml"
    with open(output_path_014, 'w') as f:
        f.write(prb014_yaml)
    
    total_014 = len(prb014_cases['samples']) + len(prb014_cases['public']) + len(prb014_cases['hidden'])
    print(f"✅ PRB-014: {total_014} test cases generated")
    print(f"   - Samples: {len(prb014_cases['samples'])}")
    print(f"   - Public: {len(prb014_cases['public'])}")
    print(f"   - Hidden: {len(prb014_cases['hidden'])}")
    
    # PRB-015
    print("\n[2/3] Generating PRB-015: Median of Uniforms CLT...")
    prb015_cases = generate_prb015_cases()
    prb015_yaml = format_testcase_yaml(prb015_cases)
    
    output_path_015 = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases/PRB-015-median-uniforms-clt.yaml"
    with open(output_path_015, 'w') as f:
        f.write(prb015_yaml)
    
    total_015 = len(prb015_cases['samples']) + len(prb015_cases['public']) + len(prb015_cases['hidden'])
    print(f"✅ PRB-015: {total_015} test cases generated")
    print(f"   - Samples: {len(prb015_cases['samples'])}")
    print(f"   - Public: {len(prb015_cases['public'])}")
    print(f"   - Hidden: {len(prb015_cases['hidden'])}")
    
    # PRB-016
    print("\n[3/3] Generating PRB-016: Random Permutation Cycle Structure...")
    prb016_cases = generate_prb016_cases()
    prb016_yaml = format_testcase_yaml(prb016_cases)
    
    output_path_016 = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases/PRB-016-permutation-cycle-structure.yaml"
    with open(output_path_016, 'w') as f:
        f.write(prb016_yaml)
    
    total_016 = len(prb016_cases['samples']) + len(prb016_cases['public']) + len(prb016_cases['hidden'])
    print(f"✅ PRB-016: {total_016} test cases generated")
    print(f"   - Samples: {len(prb016_cases['samples'])}")
    print(f"   - Public: {len(prb016_cases['public'])}")
    print(f"   - Hidden: {len(prb016_cases['hidden'])}")
    
    # Summary
    total_all = total_014 + total_015 + total_016
    print("\n" + "=" * 80)
    print("✅ EXPANSION COMPLETE!")
    print(f"Total test cases generated: {total_all}")
    print(f"  - PRB-014: {total_014} cases")
    print(f"  - PRB-015: {total_015} cases")
    print(f"  - PRB-016: {total_016} cases")
    print("=" * 80)


if __name__ == "__main__":
    main()
