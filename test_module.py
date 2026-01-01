#!/usr/bin/env python3
import os
import sys
import yaml
import subprocess
import glob
import time

def load_testcases(problem_id, module_dir):
    """Load testcases for a problem"""
    pattern = os.path.join(module_dir, "testcases", f"{problem_id}*.yaml")
    files = glob.glob(pattern)
    if not files:
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
    
    clean_tests = []
    for t in tests:
        inp = str(t['input']).strip()
        out = str(t['output']).strip()
        clean_tests.append({'input': inp, 'output': out})
    return clean_tests

def get_solution_file(problem_id, module_dir, lang):
    """Get solution file for a problem"""
    ext = {'cpp': 'cpp', 'java': 'java', 'javascript': 'js', 'python': 'py'}.get(lang)
    pattern = os.path.join(module_dir, "solutions", lang, f"{problem_id}*.{ext}")
    files = glob.glob(pattern)
    if not files:
        return None
    return files[0]

def run_test(cmd, input_str, expected_out, timeout=2.0):
    """Run a single test"""
    try:
        start_time = time.time()
        process = subprocess.run(
            cmd,
            input=input_str,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        duration = time.time() - start_time
    except subprocess.TimeoutExpired:
        return False, "TLE", timeout

    if process.returncode != 0:
        return False, f"Runtime Error: {process.stderr}", duration

    actual_out = process.stdout.strip()
    if actual_out == expected_out:
        return True, "Passed", duration
    else:
        return False, f"WA\nExpected:\n{expected_out}\nGot:\n{actual_out}", duration

def compile_cpp(source_file):
    """Compile C++ source"""
    exe_path = source_file.replace('.cpp', '.out')
    cmd = ['g++', '-O3', '-std=c++17', source_file, '-o', exe_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return None
    return exe_path

def compile_java(source_file):
    """Compile Java source"""
    cmd = ['javac', source_file]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return None
    return "Main"

def verify(problem_id, module_dir, languages):
    """Verify solutions for a problem"""
    tests = load_testcases(problem_id, module_dir)
    if not tests:
        print(f"Verifying {problem_id}: No testcases found")
        return
    
    print(f"Verifying {problem_id} ({len(tests)} tests)...")
    
    for lang in languages:
        sol_file = get_solution_file(problem_id, module_dir, lang)
        if not sol_file:
            print(f"[{lang}] Solution not found")
            continue
        
        print(f"[{lang}] Testing {os.path.basename(sol_file)}")
        
        run_cmd = []
        cleanup_files = []
        
        if lang == 'cpp':
            exe = compile_cpp(sol_file)
            if not exe:
                print(f"[{lang}] Compilation failed")
                continue
            run_cmd = [exe]
            cleanup_files.append(exe)
        elif lang == 'java':
            main_class = compile_java(sol_file)
            if not main_class:
                print(f"[{lang}] Compilation failed")
                continue
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
                if i > 5:
                    print("  ...stopping validation for this language.")
                    break
        
        print(f"[{lang}] Result: {passed}/{len(tests)} passed.")
        
        for f in cleanup_files:
            if os.path.exists(f):
                try:
                    os.remove(f)
                except:
                    pass

def main():
    if len(sys.argv) < 3:
        print("Usage: test_module.py <module_name> <problem_id> [languages...]")
        print("Example: test_module.py Arrays ARR-001 python java")
        sys.exit(1)
    
    module_name = sys.argv[1]
    problem_id = sys.argv[2]
    languages = sys.argv[3:] if len(sys.argv) > 3 else ['python', 'java', 'javascript', 'cpp']
    
    module_dir = os.path.join('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems', module_name)
    if not os.path.isdir(module_dir):
        print(f"Module directory not found: {module_dir}")
        sys.exit(1)
    
    verify(problem_id, module_dir, languages)

if __name__ == "__main__":
    main()
