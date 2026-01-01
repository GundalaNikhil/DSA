import os
import sys
import yaml
import subprocess
import glob
import time
import argparse

# Configuration
DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
PROBLEMS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "SegmentTree")
SOLUTIONS_DIR = os.path.join(PROBLEMS_DIR, "solutions")
TESTCASES_DIR = os.path.join(PROBLEMS_DIR, "testcases")

TIMEOUT_SEC = 2.0

def load_testcases(problem_id):
    # Find yaml file
    pattern = os.path.join(TESTCASES_DIR, f"{problem_id}*.yaml")
    files = glob.glob(pattern)
    if not files:
        print(f"No testcase file found for {problem_id}")
        return None
    
    with open(files[0], 'r') as f:
        data = yaml.safe_load(f)
    
    tests = []
    if 'samples' in data:
        tests.extend(data['samples'])
    if 'public' in data:
        tests.extend(data['public'])
    if 'hidden' in data:
        tests.extend(data['hidden'])
    
    # Clean inputs/outputs
    clean_tests = []
    for t in tests:
        inp = str(t['input']).rstrip() # Use rstrip to preserve leading empty lines
        out = str(t['output']).strip()
        clean_tests.append({'input': inp, 'output': out})
    return clean_tests

def get_solution_file(problem_id, lang):
    ext = {'cpp': 'cpp', 'java': 'java', 'javascript': 'js', 'python': 'py'}.get(lang)
    pattern = os.path.join(SOLUTIONS_DIR, lang, f"{problem_id}*.{ext}")
    files = glob.glob(pattern)
    if not files:
        return None
    return files[0]

def compile_cpp(source_file):
    exe_path = source_file.replace('.cpp', '.out')
    cmd = ['g++', '-O3', '-std=c++17', source_file, '-o', exe_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Compilation failed for {source_file}:\n{res.stderr}")
        return None
    return exe_path

def compile_java(source_file):
    cmd = ['javac', source_file]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Compilation failed for {source_file}:\n{res.stderr}")
        return None
    return "Main" 

def run_test(cmd, input_str, expected_out):
    try:
        start_time = time.time()
        process = subprocess.run(
            cmd,
            input=input_str,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEC
        )
        duration = time.time() - start_time
    except subprocess.TimeoutExpired:
        return False, "TLE", TIMEOUT_SEC

    if process.returncode != 0:
        return False, f"Runtime Error: {process.stderr}", duration

    actual_out = process.stdout.strip()
    
    # Segment Tree often involves integers, so exact match is usually fine.
    # However, for floating point problems, this might need refinement.
    if actual_out == expected_out:
        return True, "Passed", duration
    else:
        return False, f"WA\nExpected:\n{expected_out}\nGot:\n{actual_out}", duration

def verify(problem_id, languages):
    tests = load_testcases(problem_id)
    if not tests:
        return

    print(f"Verifying {problem_id} ({len(tests)} tests)...")

    for lang in languages:
        sol_file = get_solution_file(problem_id, lang)
        if not sol_file:
            print(f"[{lang}] Solution not found")
            continue

        print(f"[{lang}] Testing {os.path.basename(sol_file)}")
        
        run_cmd = []
        cleanup_files = []

        if lang == 'cpp':
            exe = compile_cpp(sol_file)
            if not exe: continue
            run_cmd = [exe]
            cleanup_files.append(exe)
        
        elif lang == 'java':
            main_class = compile_java(sol_file)
            if not main_class: continue
            cp = os.path.dirname(sol_file)
            run_cmd = ['java', '-cp', cp, 'Main']
            cleanup_files.extend(glob.glob(os.path.join(cp, "*.class")))

        elif lang == 'javascript':
            run_cmd = ['node', sol_file]
            
        elif lang == 'python':
            run_cmd = ['python3', sol_file]

        passed = 0
        for i, t in enumerate(tests):
            ok, msg, dur = run_test(run_cmd, t['input'], t['output'])
            
            if ok:
                passed += 1
            else:
                print(f"  Test {i+1}: FAIL ({dur:.3f}s) -> {msg[:200]}...")
                # if i > 5: 
                #     print("  ...stopping validation for this language.")
                #     break
        
        print(f"[{lang}] Result: {passed}/{len(tests)} passed.")
        
        for f in cleanup_files:
            if os.path.exists(f):
                os.remove(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_id', help="Problem ID (e.g. SGT-001)")
    parser.add_argument('--langs', nargs='+', default=['cpp', 'java', 'javascript', 'python'], help="Languages to test")
    args = parser.parse_args()

    verify(args.problem_id, args.langs)

if __name__ == "__main__":
    main()
