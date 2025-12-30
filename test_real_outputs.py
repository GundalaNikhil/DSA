#!/usr/bin/env python3
"""
Quick fix: Use actual solutions to generate correct outputs
"""
import subprocess
import yaml

def run_solution(prob_num, input_str):
    """Run actual solution and get output"""
    sol_file = f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/solutions/python/MTH-{prob_num:03d}-*.py"
    import glob
    files = glob.glob(sol_file)
    if not files:
        return None
    
    try:
        result = subprocess.run(['python3', files[0]], input=input_str, capture_output=True, text=True, timeout=2)
        return result.stdout.strip()
    except:
        return None

# Generate testcases using real solutions
base = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases"

# MTH-004: Use solution to generate correct outputs
samples_004 = [
    "3\n1 2 3\n2\n0 1",
]
output_004 = run_solution(4, samples_004[0])
print(f"MTH-004 sample output: {output_004}")

# MTH-009: Use solution
samples_009 = [
    "2\n1 2\n2\n3 4",
]
output_009 = run_solution(9, samples_009[0])
print(f"MTH-009 sample output: {output_009}")

# MTH-012: Use solution
samples_012 = [
    "2\n1 2\n2\n3 4",
]
output_012 = run_solution(12, samples_012[0])
print(f"MTH-012 sample output: {output_012}")
