#!/usr/bin/env python3
"""
Diagnostic test to understand why C++/Java might fail while Python passes.
Tests AGR-006 with detailed debugging.
"""
import os
import re
import sys
import yaml
import subprocess
import tempfile
from pathlib import Path

def extract_solution(editorial_file, language):
    """Extract solution code from editorial markdown."""
    with open(editorial_file, 'r') as f:
        content = f.read()
    
    # Find code block for the language
    if language == 'cpp':
        pattern = r'### C\+\+\n\n```(?:cpp|c\+\+)\n(.*?)\n```'
    elif language == 'java':
        pattern = r'### Java\n\n```java\n(.*?)\n```'
    elif language == 'python':
        pattern = r'### Python\n\n```python\n(.*?)\n```'
    
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None
    
    return match.group(1)

def test_cpp_solution():
    """Test C++ solution with first sample test case."""
    print("="*80)
    print("TESTING C++ SOLUTION")
    print("="*80)
    
    # Extract solution
    editorial = 'editorials/AGR-006-articulation-and-bcc.md'
    code = extract_solution(editorial, 'cpp')
    
    if not code:
        print("❌ Could not extract C++ solution")
        return
    
    print(f"\n✓ Extracted C++ solution ({len(code)} chars)")
    print(f"First 200 chars:\n{code[:200]}...\n")
    
    # Write to temp file
    temp_file = '/tmp/test_agr006.cpp'
    with open(temp_file, 'w') as f:
        f.write(code)
    
    print("✓ Wrote to temp file")
    
    # Compile
    print("\nCompiling with: g++ -std=c++17 -O2...")
    compile_result = subprocess.run(
        ['g++', '-std=c++17', '-O2', temp_file, '-o', '/tmp/test_agr006'],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    if compile_result.returncode != 0:
        print(f"❌ COMPILATION FAILED:")
        print(compile_result.stderr)
        return
    
    print("✓ Compilation successful")
    
    # Test with first sample
    test_input = """4 4
0 1
1 2
2 0
1 3"""
    
    expected_output = """1
1
2
2 1 3
3 0 1 2"""
    
    print(f"\nRunning with test input:\n{test_input}\n")
    
    run_result = subprocess.run(
        ['/tmp/test_agr006'],
        input=test_input,
        capture_output=True,
        text=True,
        timeout=5
    )
    
    if run_result.returncode != 0:
        print(f"❌ RUNTIME ERROR:")
        print(run_result.stderr)
        return
    
    actual_output = run_result.stdout.strip()
    expected_output = expected_output.strip()
    
    print(f"Expected output:\n{expected_output}\n")
    print(f"Actual output:\n{actual_output}\n")
    
    if actual_output == expected_output:
        print("✅ OUTPUT MATCHES!")
    else:
        print("❌ OUTPUT MISMATCH")
        print(f"\nExpected bytes: {expected_output.encode()}")
        print(f"Actual bytes: {actual_output.encode()}")
        
        # Character by character comparison
        exp_lines = expected_output.split('\n')
        act_lines = actual_output.split('\n')
        
        print(f"\nLine count - Expected: {len(exp_lines)}, Actual: {len(act_lines)}")
        
        for i, (exp, act) in enumerate(zip(exp_lines, act_lines)):
            if exp != act:
                print(f"Line {i} differs:")
                print(f"  Expected: '{exp}'")
                print(f"  Actual:   '{act}'")

def test_java_solution():
    """Test Java solution with first sample test case."""
    print("\n" + "="*80)
    print("TESTING JAVA SOLUTION")
    print("="*80)
    
    # Extract solution
    editorial = 'editorials/AGR-006-articulation-and-bcc.md'
    code = extract_solution(editorial, 'java')
    
    if not code:
        print("❌ Could not extract Java solution")
        return
    
    print(f"\n✓ Extracted Java solution ({len(code)} chars)")
    print(f"First 200 chars:\n{code[:200]}...\n")
    
    # Extract class name
    class_match = re.search(r'public\s+class\s+(\w+)', code)
    if class_match:
        class_name = class_match.group(1)
    else:
        class_name = 'Main'
    
    print(f"✓ Main class name: {class_name}")
    
    # Write to temp file
    temp_dir = '/tmp/java_test'
    os.makedirs(temp_dir, exist_ok=True)
    temp_file = f'{temp_dir}/{class_name}.java'
    
    with open(temp_file, 'w') as f:
        f.write(code)
    
    print(f"✓ Wrote to {temp_file}")
    
    # Compile
    print("\nCompiling with: javac...")
    compile_result = subprocess.run(
        ['javac', temp_file],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    if compile_result.returncode != 0:
        print(f"❌ COMPILATION FAILED:")
        print(compile_result.stderr)
        return
    
    print("✓ Compilation successful")
    
    # Test with first sample
    test_input = """4 4
0 1
1 2
2 0
1 3"""
    
    expected_output = """1
1
2
2 1 3
3 0 1 2"""
    
    print(f"\nRunning with test input:\n{test_input}\n")
    
    run_result = subprocess.run(
        ['java', '-cp', temp_dir, class_name],
        input=test_input,
        capture_output=True,
        text=True,
        timeout=5
    )
    
    if run_result.returncode != 0:
        print(f"❌ RUNTIME ERROR:")
        print(f"stderr: {run_result.stderr}")
        print(f"stdout: {run_result.stdout}")
        return
    
    actual_output = run_result.stdout.strip()
    expected_output = expected_output.strip()
    
    print(f"Expected output:\n{expected_output}\n")
    print(f"Actual output:\n{actual_output}\n")
    
    if actual_output == expected_output:
        print("✅ OUTPUT MATCHES!")
    else:
        print("❌ OUTPUT MISMATCH")
        print(f"\nExpected bytes: {expected_output.encode()}")
        print(f"Actual bytes: {actual_output.encode()}")
        
        # Line by line comparison
        exp_lines = expected_output.split('\n')
        act_lines = actual_output.split('\n')
        
        print(f"\nLine count - Expected: {len(exp_lines)}, Actual: {len(act_lines)}")
        
        for i, (exp, act) in enumerate(zip(exp_lines, act_lines)):
            if exp != act:
                print(f"Line {i} differs:")
                print(f"  Expected: '{exp}'")
                print(f"  Actual:   '{act}'")

def main():
    os.chdir('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs')
    
    # Test both languages
    test_cpp_solution()
    test_java_solution()
    
    print("\n" + "="*80)
    print("DIAGNOSTIC COMPLETE")
    print("="*80)

if __name__ == '__main__':
    main()
