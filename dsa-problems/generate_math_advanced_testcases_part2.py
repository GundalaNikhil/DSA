import os
import yaml
import random
import math
from typing import List, Tuple, Dict, Any

# --- Configuration ---
OUTPUT_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Helper Functions ---

def write_yaml(filename: str, data: Dict[str, Any]):
    """Writes data to a YAML file with proper formatting."""
    with open(filename, 'w') as f:
        f.write(f"# filepath: {filename}\n")
        yaml.dump(data, f, sort_keys=False, default_flow_style=False, allow_unicode=True, width=1000)
    print(f"Generated {filename}")

def format_output(output_data: Any) -> str:
    """Formats output data as a string for YAML."""
    if isinstance(output_data, list):
        # Check if it's a list of lists (matrix)
        if output_data and isinstance(output_data[0], list):
            return "\n".join(" ".join(map(str, row)) for row in output_data)
        return " ".join(map(str, output_data))
    return str(output_data)

def format_input(input_data: List[str]) -> str:
    """Formats input lines into a single string."""
    return "\n".join(input_data)

# --- Problem Generators ---

# MTH-009: Subset Convolution (AND/OR)
def generate_mth009():
    problem_id = "MTH-009"
    filename = os.path.join(OUTPUT_DIR, "MTH-009-subset-convolution-and-or.yaml")
    MOD = 1000000007

    def solve(A, B, op):
        # Naive O(4^n) or O(3^n) is too slow for n=20, but for generation we use small n
        # op: 0 for AND, 1 for OR
        n_len = len(A)
        C = [0] * n_len
        for i in range(n_len):
            for j in range(n_len):
                if op == 1: # OR
                    k = i | j
                else: # AND
                    k = i & j
                C[k] = (C[k] + A[i] * B[j]) % MOD
        return C

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    # OR convolution
    A = [1, 1, 0, 0]
    B = [0, 1, 1, 0]
    res = solve(A, B, 1)
    inp = f"{2} 1\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
    testcases["samples"].append({"input": inp, "output": format_output(res)})
    
    # AND convolution
    A = [1, 1, 0, 0]
    B = [0, 1, 1, 0]
    res = solve(A, B, 0)
    inp = f"{2} 0\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
    testcases["samples"].append({"input": inp, "output": format_output(res)})

    # Public
    public_cases = [
        (1, 1, [1, 0], [0, 1]), # n=1, OR
        (1, 0, [1, 1], [1, 1]), # n=1, AND
        (3, 1, [1]*8, [1]*8)
    ]
    for n, op, A, B in public_cases:
        res = solve(A, B, op)
        inp = f"{n} {op}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    # Hidden
    for _ in range(5):
        n = random.randint(2, 6) # Keep small for naive generation
        op = random.choice([0, 1])
        size = 1 << n
        A = [random.randint(0, MOD-1) for _ in range(size)]
        B = [random.randint(0, MOD-1) for _ in range(size)]
        res = solve(A, B, op)
        inp = f"{n} {op}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})
        
    for _ in range(3):
        n = random.randint(7, 8)
        op = random.choice([0, 1])
        size = 1 << n
        A = [random.randint(0, MOD-1) for _ in range(size)]
        B = [random.randint(0, MOD-1) for _ in range(size)]
        res = solve(A, B, op)
        inp = f"{n} {op}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-010: Berlekamp-Massey Sequence Reconstruction
def generate_mth010():
    problem_id = "MTH-010"
    filename = os.path.join(OUTPUT_DIR, "MTH-010-berlekamp-massey.yaml")
    MOD = 1000000007

    def solve(seq, n):
        # For generation, we can just generate a sequence from a known recurrence
        # But the problem asks to reconstruct.
        # Since we are generating test cases, we can create a random recurrence,
        # generate the sequence, and then the answer is just the n-th term.
        # We don't need to implement BM to generate test cases!
        
        # However, the input is just the sequence.
        # We need to make sure the sequence provided is long enough to uniquely determine the recurrence.
        # Usually 2*L terms are needed where L is the order.
        
        # If we generate a random recurrence of order L, and provide 2*L terms,
        # the answer is well-defined.
        
        # But wait, the input is just a sequence S.
        # The solver must find the shortest recurrence.
        # If we generate from a recurrence of order L, the shortest might be smaller (unlikely for random).
        
        # Let's implement a simple linear recurrence generator.
        pass
        
    def generate_case(L, m, n_target):
        # L: order of recurrence
        # m: number of terms provided (should be >= 2*L)
        # n_target: index to find
        
        coeffs = [random.randint(1, MOD-1) for _ in range(L)] # c_1 ... c_L
        # S_i = sum_{j=1}^L c_j * S_{i-j}
        
        seq = [random.randint(0, MOD-1) for _ in range(L)]
        
        # Generate up to max(m, n_target + 1)
        limit = max(m, n_target + 1)
        full_seq = seq[:]
        
        for i in range(L, limit):
            val = 0
            for j in range(1, L + 1):
                val = (val + coeffs[j-1] * full_seq[i-j]) % MOD
            full_seq.append(val)
            
        return full_seq[:m], full_seq[n_target]

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    # Fib: 1, 1, 2, 3, 5, 8. n=10 -> 89
    # Recurrence: S_n = S_{n-1} + S_{n-2}. Order 2. Need 4 terms. Provided 6.
    seq = [1, 1, 2, 3, 5, 8]
    n = 10
    ans = 89
    inp = f"{len(seq)} {n}\n{' '.join(map(str, seq))}"
    testcases["samples"].append({"input": inp, "output": str(ans)})

    # Public
    # Geometric: 1, 2, 4, 8, 16. S_n = 2*S_{n-1}. Order 1.
    seq = [1, 2, 4, 8, 16]
    n = 10
    ans = 1024
    inp = f"{len(seq)} {n}\n{' '.join(map(str, seq))}"
    testcases["public"].append({"input": inp, "output": str(ans)})
    
    # Constant: 5, 5, 5, 5. S_n = S_{n-1}.
    seq = [5, 5, 5, 5]
    n = 100
    ans = 5
    inp = f"{len(seq)} {n}\n{' '.join(map(str, seq))}"
    testcases["public"].append({"input": inp, "output": str(ans)})

    # Hidden
    for _ in range(5):
        L = random.randint(2, 10)
        m = 2 * L + random.randint(0, 5)
        n = random.randint(m, 100)
        seq, ans = generate_case(L, m, n)
        inp = f"{len(seq)} {n}\n{' '.join(map(str, seq))}"
        testcases["hidden"].append({"input": inp, "output": str(ans)})
        
    for _ in range(3):
        L = random.randint(20, 50)
        m = 2 * L
        n = random.randint(1000, 10000)
        seq, ans = generate_case(L, m, n)
        inp = f"{len(seq)} {n}\n{' '.join(map(str, seq))}"
        testcases["hidden"].append({"input": inp, "output": str(ans)})

    write_yaml(filename, testcases)

# MTH-011: Minimal Polynomial of Matrix (Krylov)
def generate_mth011():
    problem_id = "MTH-011"
    filename = os.path.join(OUTPUT_DIR, "MTH-011-minimal-polynomial-matrix.yaml")
    MOD = 1000000007

    def get_char_poly(matrix):
        # For small matrices, char poly is often the minimal poly (if distinct eigenvalues)
        # Or we can just compute it.
        # For generation, we can construct a matrix with known minimal poly.
        # E.g. Diagonal matrix -> min poly is prod (x - lambda_i) for distinct lambdas.
        # Jordan block J_k(lambda) -> min poly is (x - lambda)^k.
        pass

    def generate_case(n):
        # Generate a random matrix? Hard to know min poly.
        # Construct a matrix from Jordan form.
        # P * J * P^-1
        
        # Simple case: Diagonal matrix with some repeated values
        # Min poly roots are the distinct diagonal values.
        # If we have Jordan blocks, the power is the size of largest block for that eigenvalue.
        
        # Let's stick to small random matrices and compute brute force?
        # Or construct:
        # 1. Choose eigenvalues and block sizes.
        #    e.g. lambda=2, size=2 -> (x-2)^2
        #    lambda=3, size=1 -> (x-3)
        #    Min poly = (x-2)^2 (x-3)
        # 2. Construct J.
        # 3. Conjugate with random invertible P.
        
        # Construct J
        J = [[0]*n for _ in range(n)]
        current_idx = 0
        min_poly_factors = []
        
        while current_idx < n:
            rem = n - current_idx
            size = random.randint(1, min(rem, 3))
            val = random.randint(0, 10) # Small eigenvalues
            
            # Add to min poly factors: (x - val)^size
            # We need to track max size for each val
            found = False
            for i, (v, s) in enumerate(min_poly_factors):
                if v == val:
                    min_poly_factors[i] = (v, max(s, size))
                    found = True
                    break
            if not found:
                min_poly_factors.append((val, size))
                
            # Fill Jordan block
            for i in range(size):
                J[current_idx+i][current_idx+i] = val
                if i < size - 1:
                    J[current_idx+i][current_idx+i+1] = 1
            current_idx += size
            
        # Compute min poly coefficients
        # P(x) = prod (x - v)^s
        poly = [1] # Highest degree first? No, usually lowest first or standard.
        # Let's use standard representation: x^k + c_{k-1}x^{k-1} ...
        # We'll represent as list of coeffs from x^0 to x^k.
        
        # (x - v) -> [-v, 1]
        poly = [1] # Constant 1 (degree 0)
        
        for val, size in min_poly_factors:
            # Multiply by (x - val)^size
            for _ in range(size):
                # Multiply poly by (x - val) = -val + x
                # new[i] = poly[i] * (-val) + poly[i-1] * 1
                new_poly = [0] * (len(poly) + 1)
                for i in range(len(poly)):
                    new_poly[i] = (new_poly[i] + poly[i] * (MOD - val)) % MOD
                    new_poly[i+1] = (new_poly[i+1] + poly[i]) % MOD
                poly = new_poly
                
        # Now conjugate J
        # P = random matrix, check invertible?
        # Easier: just apply random row/col operations
        A = [row[:] for row in J]
        for _ in range(n * 2):
            r1 = random.randint(0, n-1)
            r2 = random.randint(0, n-1)
            if r1 == r2: continue
            
            # Row op: R1 += c * R2
            # Col op: C2 -= c * C1 (inverse)
            c = random.randint(1, MOD-1)
            
            for j in range(n):
                A[r1][j] = (A[r1][j] + c * A[r2][j]) % MOD
            
            for i in range(n):
                A[i][r2] = (A[i][r2] - c * A[i][r1]) % MOD # Note: subtraction
                A[i][r2] = (A[i][r2] + MOD) % MOD
                
        return A, poly

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    # [[1, 1], [0, 1]] -> (x-1)^2 = x^2 - 2x + 1 -> 1, -2, 1
    mat = [[1, 1], [0, 1]]
    ans = [1, MOD-2, 1]
    inp = f"{2}\n1 1\n0 1"
    testcases["samples"].append({"input": inp, "output": format_output(ans)})

    # Public
    # Identity [[2, 0], [0, 2]] -> x-2 -> -2, 1
    mat = [[2, 0], [0, 2]]
    ans = [MOD-2, 1]
    inp = f"{2}\n2 0\n0 2"
    testcases["public"].append({"input": inp, "output": format_output(ans)})
    
    # Diagonal [[1, 0], [0, 2]] -> (x-1)(x-2) = x^2 - 3x + 2 -> 2, -3, 1
    mat = [[1, 0], [0, 2]]
    ans = [2, MOD-3, 1]
    inp = f"{2}\n1 0\n0 2"
    testcases["public"].append({"input": inp, "output": format_output(ans)})

    # Hidden
    for _ in range(5):
        n = random.randint(2, 5)
        mat, poly = generate_case(n)
        inp_lines = [f"{n}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["hidden"].append({"input": format_input(inp_lines), "output": format_output(poly)})
        
    for _ in range(3):
        n = random.randint(6, 10)
        mat, poly = generate_case(n)
        inp_lines = [f"{n}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["hidden"].append({"input": format_input(inp_lines), "output": format_output(poly)})

    write_yaml(filename, testcases)

# MTH-012: Convolution Under Multiple Mods with CRT
def generate_mth012():
    problem_id = "MTH-012"
    filename = os.path.join(OUTPUT_DIR, "MTH-012-convolution-multi-mod-crt.yaml")
    # Modulo is given in input
    
    def solve(A, B, mod):
        n = len(A)
        m = len(B)
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i+j] = (res[i+j] + A[i] * B[j]) % mod
        return res

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    A = [1, 2]
    B = [3, 4]
    mod = 1000000007
    res = solve(A, B, mod)
    inp = f"{len(A)} {len(B)} {mod}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
    testcases["samples"].append({"input": inp, "output": format_output(res)})

    # Public
    public_cases = [
        ([1, 1], [1, 1], 100),
        ([1, 2, 3], [4, 5, 6], 998244353),
        ([10], [10], 13)
    ]
    for A, B, mod in public_cases:
        res = solve(A, B, mod)
        inp = f"{len(A)} {len(B)} {mod}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    # Hidden
    for _ in range(5):
        n = random.randint(5, 20)
        m = random.randint(5, 20)
        mod = random.randint(1000, 1000000000)
        A = [random.randint(0, mod-1) for _ in range(n)]
        B = [random.randint(0, mod-1) for _ in range(m)]
        res = solve(A, B, mod)
        inp = f"{len(A)} {len(B)} {mod}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})
        
    for _ in range(3):
        n = random.randint(50, 100)
        m = random.randint(50, 100)
        mod = random.randint(1000000000, 2000000000)
        A = [random.randint(0, mod-1) for _ in range(n)]
        B = [random.randint(0, mod-1) for _ in range(m)]
        res = solve(A, B, mod)
        inp = f"{len(A)} {len(B)} {mod}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-013: Fast Inversion of Vandermonde Matrix
def generate_mth013():
    problem_id = "MTH-013"
    filename = os.path.join(OUTPUT_DIR, "MTH-013-invert-vandermonde.yaml")
    MOD = 1000000007

    def modInverse(n):
        return pow(n, MOD - 2, MOD)

    def solve(x):
        # O(n^2) inversion
        # The inverse U has entries U_ji = coeff of x^j in L_i(x)
        # L_i(x) = prod_{k!=i} (x - x_k) / prod_{k!=i} (x_i - x_k)
        
        n = len(x)
        U = [[0]*n for _ in range(n)]
        
        for i in range(n):
            # Compute denominator
            den = 1
            for k in range(n):
                if i == k: continue
                den = (den * (x[i] - x[k])) % MOD
            invDen = modInverse(den)
            
            # Compute numerator poly: prod_{k!=i} (x - x_k)
            # This is a poly of degree n-1
            poly = [0] * n
            poly[0] = 1 # Constant 1
            # Current degree is 0
            
            # Multiply by (x - x_k) for each k != i
            # (x - x_k) -> [-x_k, 1]
            
            # Optimization:
            # Compute full product P(x) = prod (x - x_k) in O(n^2)
            # Then divide by (x - x_i) in O(n)
            # This makes total O(n^2)
            pass
        
        # Better O(n^2) approach:
        # 1. Compute P(x) = prod (x - x_k)
        P = [0] * (n + 1)
        P[0] = 1
        for k in range(n):
            # Multiply by (x - x_k)
            # new[j] = P[j] * (-x_k) + P[j-1]
            for j in range(k + 1, 0, -1):
                P[j] = (P[j] * (MOD - x[k]) + P[j-1]) % MOD
            P[0] = (P[0] * (MOD - x[k])) % MOD
            
        for i in range(n):
            # Compute denominator
            den = 1
            for k in range(n):
                if i == k: continue
                den = (den * (x[i] - x[k])) % MOD
            invDen = modInverse(den)
            
            # Compute L_i(x) numerator by dividing P(x) by (x - x_i)
            # Synthetic division
            # Q(x) = P(x) / (x - x_i)
            # Q[n-1] = P[n] (which is 1)
            # Q[j] = P[j+1] + Q[j+1] * x_i
            
            Q = [0] * n
            Q[n-1] = P[n]
            for j in range(n-2, -1, -1):
                Q[j] = (P[j+1] + Q[j+1] * x[i]) % MOD
                
            # Scale by invDen and store in column i
            for j in range(n):
                U[j][i] = (Q[j] * invDen) % MOD
                
        return U

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    # x=[1, 2]
    # V = [[1, 1], [1, 2]]
    # Det = 1. Inv = [[2, -1], [-1, 1]]
    x = [1, 2]
    res = solve(x)
    inp = f"{len(x)}\n{' '.join(map(str, x))}"
    testcases["samples"].append({"input": inp, "output": format_output(res)})

    # Public
    public_cases = [
        [1],
        [1, 2, 3],
        [0, 1, 2]
    ]
    for x in public_cases:
        res = solve(x)
        inp = f"{len(x)}\n{' '.join(map(str, x))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    # Hidden
    for _ in range(5):
        n = random.randint(2, 10)
        x = []
        seen = set()
        while len(x) < n:
            val = random.randint(0, MOD-1)
            if val not in seen:
                seen.add(val)
                x.append(val)
        res = solve(x)
        inp = f"{len(x)}\n{' '.join(map(str, x))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})
        
    for _ in range(3):
        n = random.randint(20, 40)
        x = []
        seen = set()
        while len(x) < n:
            val = random.randint(0, MOD-1)
            if val not in seen:
                seen.add(val)
                x.append(val)
        res = solve(x)
        inp = f"{len(x)}\n{' '.join(map(str, x))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-014: Largest Eigenvalue Power Method
def generate_mth014():
    problem_id = "MTH-014"
    filename = os.path.join(OUTPUT_DIR, "MTH-014-largest-eigenvalue-power.yaml")
    
    def solve(matrix):
        # Power iteration
        n = len(matrix)
        v = [1.0] * n
        
        for _ in range(100):
            # Av
            new_v = [0.0] * n
            for i in range(n):
                for j in range(n):
                    new_v[i] += matrix[i][j] * v[j]
            
            # Normalize
            norm = max(abs(x) for x in new_v)
            if norm < 1e-9: break
            for i in range(n):
                v[i] = new_v[i] / norm
                
        # Rayleigh quotient
        # (v^T A v) / (v^T v)
        Av = [0.0] * n
        for i in range(n):
            for j in range(n):
                Av[i] += matrix[i][j] * v[j]
        
        num = sum(v[i] * Av[i] for i in range(n))
        den = sum(v[i] * v[i] for i in range(n))
        
        return num / den

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    # [[2, 0], [0, 1]] -> 2
    mat = [[2, 0], [0, 1]]
    res = 2.0
    inp_lines = [f"{len(mat)}"]
    for row in mat:
        inp_lines.append(" ".join(map(str, row)))
    testcases["samples"].append({"input": format_input(inp_lines), "output": f"{res:.6f}"})

    # Public
    public_cases = [
        [[1, 1], [1, 1]], # 2
        [[3, 0, 0], [0, 1, 0], [0, 0, 2]], # 3
        [[0, 1], [1, 0]] # 1 (eigenvalues 1, -1)
    ]
    for mat in public_cases:
        res = solve(mat)
        inp_lines = [f"{len(mat)}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["public"].append({"input": format_input(inp_lines), "output": f"{res:.6f}"})

    # Hidden
    for _ in range(5):
        n = random.randint(2, 5)
        # Generate symmetric matrix for real eigenvalues
        mat = [[0.0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(-10, 10)
                mat[i][j] = val
                mat[j][i] = val
        res = solve(mat)
        inp_lines = [f"{len(mat)}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["hidden"].append({"input": format_input(inp_lines), "output": f"{res:.6f}"})
        
    for _ in range(3):
        n = random.randint(10, 20)
        mat = [[0.0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(-10, 10)
                mat[i][j] = val
                mat[j][i] = val
        res = solve(mat)
        inp_lines = [f"{len(mat)}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["hidden"].append({"input": format_input(inp_lines), "output": f"{res:.6f}"})

    write_yaml(filename, testcases)

# --- Main Execution ---

if __name__ == "__main__":
    generate_mth009()
    generate_mth010()
    generate_mth011()
    generate_mth012()
    generate_mth013()
    generate_mth014()
    print("Generated test cases for MTH-009 to MTH-014")
