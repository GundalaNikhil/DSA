#!/usr/bin/env python3
"""Verify Probabilistic test cases."""

import os
import yaml

TESTCASES_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases"
PROBLEMS = [f"PRB-{i:03d}" for i in range(1, 17)]

def verify_testcases():
    report = []
    total_cases = 0
    
    print(f"{'Problem ID':<12} | {'Samples':<8} | {'Public':<8} | {'Hidden':<8} | {'Total':<8} | {'Status':<10}")
    print("-" * 70)
    
    for problem_id in PROBLEMS:
        # Find the file
        found_file = None
        for filename in os.listdir(TESTCASES_DIR):
            if filename.startswith(problem_id) and filename.endswith(".yaml"):
                found_file = filename
                break
        
        if not found_file:
            print(f"{problem_id:<12} | {'MISSING':<48}")
            continue
            
        filepath = os.path.join(TESTCASES_DIR, found_file)
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                
            # Check if empty
            if 'YAML content to be added' in content or len(content) < 100:
                print(f"{problem_id:<12} | {'EMPTY':<48}")
                continue
                
            data = yaml.safe_load(content)
            
            samples = len(data.get('samples', []))
            public = len(data.get('public', []))
            hidden = len(data.get('hidden', []))
            total = samples + public + hidden
            total_cases += total
            
            status = "✅ OK" if total > 0 else "EMPTY"
            
            print(f"{problem_id:<12} | {samples:<8} | {public:<8} | {hidden:<8} | {total:<8} | {status:<10}")
            
            report.append({
                "id": problem_id,
                "file": found_file,
                "samples": samples,
                "public": public,
                "hidden": hidden,
                "total": total
            })
            
        except Exception as e:
            print(f"{problem_id:<12} | Error: {str(e)}")

    print("-" * 70)
    print(f"Total Test Cases Generated: {total_cases}")
    return report

if __name__ == "__main__":
    verify_testcases()
