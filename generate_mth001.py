#!/usr/bin/env python3
"""
Simple test case generation for MTH-001 with proper YAML formatting
"""
import random
import yaml

def multiply_poly_naive(A, B, mod):
    if not A or not B: return []
    res = [0] * (len(A) + len(B) - 1)
    for i in range(len(A)):
        for j in range(len(B)):
            res[i+j] = (res[i+j] + A[i] * B[j]) % mod
    return res

def main():
    MOD = 1000000007
    
    testcases = {
        'problem_id': 'MTH_POLYNOMIAL_MULTIPLICATION_FFT__2847',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample
    testcases['samples'].append({
        'input': "3\n1 2 3\n3\n4 5 6",
        'output': "4 13 28 27 18"
    })
    
    # Public  
    testcases['public'].append({'input': "1\n5\n1\n10", 'output': "50"})
    testcases['public'].append({'input': "2\n1 1\n2\n1 1000000006", 'output': "1 0 1000000006"})
    
    # Hidden - Edge
    testcases['hidden'].append({'input': "1\n0\n3\n1 2 3", 'output': "0 0 0"})
    testcases['hidden'].append({'input': "1\n7\n1\n9", 'output': "63"})
    
    # Hidden - Small
    for _ in range(10):
        n = random.randint(2, 10)
        m = random.randint(2, 10)
        A = [random.randint(0, 1000) for _ in range(n)]
        B = [random.randint(0, 1000) for _ in range(m)]
        res = multiply_poly_naive(A, B, MOD)
        inp = f"{n}\n{' '.join(map(str, A))}\n{m}\n{' '.join(map(str, B))}"
        out = ' '.join(map(str, res))
        testcases['hidden'].append({'input': inp, 'output': out})
    
    # Hidden - Medium
    for _ in range(15):
        n = random.randint(50, 200)
        m = random.randint(50, 200)
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(m)]
        res = multiply_poly_naive(A, B, MOD)
        inp = f"{n}\n{' '.join(map(str, A))}\n{m}\n{' '.join(map(str, B))}"
        out = ' '.join(map(str, res))
        testcases['hidden'].append({'input': inp, 'output': out})
    
    # Write with standard yaml dump (default handles newlines correctly)
    outfile = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases/MTH-001-polynomial-multiplication-fft.yaml"
    
    with open(outfile, 'w') as f:
        yaml.dump(testcases, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Generated MTH-001 with {len(testcases['samples'])} samples, {len(testcases['public'])} public, {len(testcases['hidden'])} hidden")
    
    # Verify loading
    with open(outfile) as f:
        loaded = yaml.safe_load(f)
    
    sample_inp = loaded['samples'][0]['input']
    print(f"Sample has actual newlines: {chr(10) in sample_inp}")
    print(f"First 50 chars of sample input: {repr(sample_inp[:50])}")

if __name__ == "__main__":
    main()
