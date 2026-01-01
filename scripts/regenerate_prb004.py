import sys
import os
import yaml
import subprocess

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
PROBLEMS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Probabilistic")
SOLUTIONS_DIR = os.path.join(PROBLEMS_DIR, "solutions", "python")
TESTCASES_DIR = os.path.join(PROBLEMS_DIR, "testcases")
PROBLEM_ID = "PRB-004-monte-carlo-pi"

def regenerate_tests():
    # Path to Python solution
    sol_file = os.path.join(SOLUTIONS_DIR, f"{PROBLEM_ID}.py")
    test_file = glob.glob(os.path.join(TESTCASES_DIR, f"{PROBLEM_ID}*.yaml"))[0]
    
    with open(test_file, 'r') as f:
        data = yaml.safe_load(f)
    
    sections = ['samples', 'public', 'hidden']
    
    for sec in sections:
        if sec in data:
            print(f"Processing {sec}...")
            for test in data[sec]:
                inp = str(test['input']).strip()
                if not inp: continue
                
                # Run solution
                process = subprocess.run(
                    ['python3', sol_file],
                    input=inp,
                    capture_output=True,
                    text=True
                )
                
                if process.returncode != 0:
                    print(f"Error running solution: {process.stderr}")
                    continue
                    
                new_out = process.stdout.strip()
                test['output'] = new_out
                # print(f"Updated: {inp} -> {new_out}")

    # Write back
    with open(test_file, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    print("Test cases updated.")
    
import glob
if __name__ == "__main__":
    regenerate_tests()
