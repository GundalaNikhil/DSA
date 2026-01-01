import os
import sys
import yaml
import subprocess

# Configuration
DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
PROBLEMS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Stacks")
SOLUTIONS_DIR = os.path.join(PROBLEMS_DIR, "solutions", "python")
TESTCASES_DIR = os.path.join(PROBLEMS_DIR, "testcases")

PROBLEM_ID = "STK-003-conveyor-weighted-deduplication"
PYTHON_SOL = os.path.join(SOLUTIONS_DIR, f"{PROBLEM_ID}.py")
YAML_FILE = os.path.join(TESTCASES_DIR, f"{PROBLEM_ID}.yaml")

def regenerate():
    if not os.path.exists(YAML_FILE):
        print(f"YAML file not found: {YAML_FILE}")
        return

    with open(YAML_FILE, 'r') as f:
        data = yaml.safe_load(f)

    # Process samples, public, hidden
    for section in ['samples', 'public', 'hidden']:
        if section not in data:
            continue
        
        print(f"Processing {section} tests...")
        for i, test in enumerate(data[section]):
            inp = test['input']
            
            # Run python solution
            process = subprocess.run(
                ['python3', PYTHON_SOL],
                input=inp,
                capture_output=True,
                text=True
            )
            
            if process.returncode != 0:
                print(f"Error running test {i}: {process.stderr}")
                continue
                
            actual_out = process.stdout.strip()
            test['output'] = actual_out
            print(f"  Test {i}: Output updated.")

    with open(YAML_FILE, 'w') as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False)
    print("YAML file updated.")

if __name__ == "__main__":
    regenerate()
