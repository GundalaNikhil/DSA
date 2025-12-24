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

# MTH-001: Polynomial Multiplication via FFT
def generate_mth001():
    problem_id = "MTH-001"
    filename = os.path.join(OUTPUT_DIR, "MTH-001-polynomial-multiplication-fft.yaml")
    MOD = 1000000007

    def solve(A, B):
        n = len(A)
        m = len(B)
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i+j] = (res[i+j] + A[i] * B[j]) % MOD
        return res

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    # Samples
    samples = [
        ([1, 2], [3, 4]),
        ([1, 1], [1, -1]), # (1+x)(1-x) = 1-x^2 -> [1, 0, -1] mod MOD
        ([0], [5, 6])
    ]
    
    for A, B in samples:
        # Adjust negative for sample 2
        B_mod = [(x + MOD) % MOD for x in B]
        res = solve(A, B_mod)
        inp = f"{len(A)} {len(B)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B_mod))}"
        testcases["samples"].append({"input": inp, "output": format_output(res)})

    # Public
    public_cases = [
        ([1], [1]),
        ([1, 2, 3], [4, 5, 6]),
        ([0, 0, 1], [1, 0, 0]),
        ([1]*5, [1]*5),
        ([i for i in range(10)], [i for i in range(10)])
    ]
    for A, B in public_cases:
        res = solve(A, B)
        inp = f"{len(A)} {len(B)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    # Hidden
    # Edge: Single elements, zeros
    hidden_cases = []
    hidden_cases.append(([0], [0]))
    hidden_cases.append(([1], [0]))
    hidden_cases.append(([1000000006], [1000000006])) # -1 * -1 = 1
    
    # Normal: Random small
    for _ in range(5):
        n = random.randint(5, 20)
        m = random.randint(5, 20)
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(m)]
        hidden_cases.append((A, B))

    # Stress: Larger (but keep small enough for O(N^2) python reference solution to run reasonably fast for generation)
    # Real solution uses FFT, but for generation we use O(N^2) with N up to 100-200 is fine.
    # For actual stress tests in hidden, we can't easily generate output with O(N^2) python if N is 10^5.
    # We will generate up to N=100 for correctness verification.
    for _ in range(3):
        n = random.randint(50, 100)
        m = random.randint(50, 100)
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(m)]
        hidden_cases.append((A, B))

    for A, B in hidden_cases:
        res = solve(A, B)
        inp = f"{len(A)} {len(B)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-002: Convolution Mod Prime Using NTT
def generate_mth002():
    problem_id = "MTH-002"
    filename = os.path.join(OUTPUT_DIR, "MTH-002-convolution-ntt.yaml")
    MOD = 998244353

    def solve(A, B):
        n = len(A)
        m = len(B)
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i+j] = (res[i+j] + A[i] * B[j]) % MOD
        return res

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        ([1, 1, 1], [1, 2]),
        ([1, 2], [3, 4]),
        ([5], [10])
    ]
    for A, B in samples:
        res = solve(A, B)
        inp = f"{len(A)} {len(B)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["samples"].append({"input": inp, "output": format_output(res)})

    public_cases = [
        ([1], [1]),
        ([1, 2, 3], [1]),
        ([1]*10, [1]*10),
        ([i for i in range(5)], [5-i for i in range(5)])
    ]
    for A, B in public_cases:
        res = solve(A, B)
        inp = f"{len(A)} {len(B)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    hidden_cases = []
    hidden_cases.append(([0], [0]))
    hidden_cases.append(([MOD-1], [MOD-1]))
    
    for _ in range(5):
        n = random.randint(10, 30)
        m = random.randint(10, 30)
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(m)]
        hidden_cases.append((A, B))
        
    for _ in range(3):
        n = random.randint(80, 120)
        m = random.randint(80, 120)
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(m)]
        hidden_cases.append((A, B))

    for A, B in hidden_cases:
        res = solve(A, B)
        inp = f"{len(A)} {len(B)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-003: Inverse Polynomial Mod x^n
def generate_mth003():
    problem_id = "MTH-003"
    filename = os.path.join(OUTPUT_DIR, "MTH-003-inverse-polynomial.yaml")
    MOD = 998244353

    def modInverse(n):
        return pow(n, MOD - 2, MOD)

    def solve(P, n):
        # Naive O(n^2) polynomial inversion
        # P * Q = 1 mod x^n
        # Q[0] = 1/P[0]
        # sum_{j=0}^i P[j]*Q[i-j] = 0 for i > 0
        # P[0]*Q[i] + sum_{j=1}^i P[j]*Q[i-j] = 0
        # Q[i] = - (1/P[0]) * sum_{j=1}^i P[j]*Q[i-j]
        
        Q = [0] * n
        invP0 = modInverse(P[0])
        Q[0] = invP0
        
        for i in range(1, n):
            s = 0
            for j in range(1, i + 1):
                if j < len(P):
                    s = (s + P[j] * Q[i-j]) % MOD
            Q[i] = (MOD - (s * invP0) % MOD) % MOD
        return Q

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        ([1, 1], 3), # 1/(1+x) = 1 - x + x^2 ... -> [1, MOD-1, 1]
        ([1, 2, 3], 4),
        ([2], 2)
    ]
    for P, n in samples:
        res = solve(P, n)
        inp = f"{len(P)} {n}\n{' '.join(map(str, P))}"
        testcases["samples"].append({"input": inp, "output": format_output(res)})

    public_cases = [
        ([1], 5),
        ([1, MOD-1], 5), # 1/(1-x) = 1+x+x^2...
        ([1, 0, 1], 5),
        ([5, 2, 1], 3)
    ]
    for P, n in public_cases:
        res = solve(P, n)
        inp = f"{len(P)} {n}\n{' '.join(map(str, P))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    hidden_cases = []
    # Edge: n=1
    hidden_cases.append(([5], 1))
    # Edge: P has more terms than n
    hidden_cases.append(([1, 2, 3, 4, 5], 3))
    
    for _ in range(5):
        deg = random.randint(1, 20)
        n = random.randint(deg, 30)
        P = [random.randint(1, MOD-1)] + [random.randint(0, MOD-1) for _ in range(deg)]
        hidden_cases.append((P, n))
        
    for _ in range(3):
        deg = random.randint(50, 100)
        n = random.randint(deg, 150)
        P = [random.randint(1, MOD-1)] + [random.randint(0, MOD-1) for _ in range(deg)]
        hidden_cases.append((P, n))

    for P, n in hidden_cases:
        res = solve(P, n)
        inp = f"{len(P)} {n}\n{' '.join(map(str, P))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-004: Multipoint Evaluation
def generate_mth004():
    problem_id = "MTH-004"
    filename = os.path.join(OUTPUT_DIR, "MTH-004-multipoint-evaluation.yaml")
    MOD = 1000000007

    def solve(P, points):
        # Naive O(N*M) evaluation
        res = []
        for x in points:
            val = 0
            for coeff in reversed(P):
                val = (val * x + coeff) % MOD
            res.append(val)
        return res

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        ([1, 0, 1], [0, 1, 2]), # x^2+1 at 0,1,2 -> 1, 2, 5
        ([1, 2], [3, 4]), # 2x+1 at 3,4 -> 7, 9
        ([5], [1, 2, 3]) # 5 at ... -> 5, 5, 5
    ]
    for P, points in samples:
        res = solve(P, points)
        inp = f"{len(P)} {len(points)}\n{' '.join(map(str, P))}\n{' '.join(map(str, points))}"
        testcases["samples"].append({"input": inp, "output": format_output(res)})

    public_cases = [
        ([0, 1], [10, 20]),
        ([1, 1, 1], [0, 1, MOD-1]),
        ([1]*5, [2]),
        ([i for i in range(5)], [i for i in range(5)])
    ]
    for P, points in public_cases:
        res = solve(P, points)
        inp = f"{len(P)} {len(points)}\n{' '.join(map(str, P))}\n{' '.join(map(str, points))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    hidden_cases = []
    hidden_cases.append(([0], [100]))
    hidden_cases.append(([1], [0, 1, 2]))
    
    for _ in range(5):
        deg = random.randint(5, 20)
        num_pts = random.randint(5, 20)
        P = [random.randint(0, MOD-1) for _ in range(deg+1)]
        points = [random.randint(0, MOD-1) for _ in range(num_pts)]
        hidden_cases.append((P, points))
        
    for _ in range(3):
        deg = random.randint(50, 100)
        num_pts = random.randint(50, 100)
        P = [random.randint(0, MOD-1) for _ in range(deg+1)]
        points = [random.randint(0, MOD-1) for _ in range(num_pts)]
        hidden_cases.append((P, points))

    for P, points in hidden_cases:
        res = solve(P, points)
        inp = f"{len(P)} {len(points)}\n{' '.join(map(str, P))}\n{' '.join(map(str, points))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-005: Lagrange Interpolation Mod Prime
def generate_mth005():
    problem_id = "MTH-005"
    filename = os.path.join(OUTPUT_DIR, "MTH-005-lagrange-interpolation-mod.yaml")
    MOD = 1000000007

    def modInverse(n):
        return pow(n, MOD - 2, MOD)

    def solve(points, X):
        # Lagrange formula O(k^2)
        k = len(points)
        ans = 0
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        
        for i in range(k):
            term = ys[i]
            for j in range(k):
                if i == j: continue
                num = (X - xs[j] + MOD) % MOD
                den = (xs[i] - xs[j] + MOD) % MOD
                term = (term * num * modInverse(den)) % MOD
            ans = (ans + term) % MOD
        return ans

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        ([(0, 1), (1, 3)], 2), # y=2x+1 -> at 2 is 5
        ([(1, 1), (2, 4), (3, 9)], 4), # y=x^2 -> at 4 is 16
        ([(0, 5)], 100) # y=5 -> 5
    ]
    for pts, X in samples:
        res = solve(pts, X)
        inp_lines = [f"{len(pts)} {X}"]
        for x, y in pts:
            inp_lines.append(f"{x} {y}")
        testcases["samples"].append({"input": format_input(inp_lines), "output": format_output(res)})

    public_cases = [
        ([(1, 2), (2, 3)], 3),
        ([(0, 0), (1, 1), (2, 8)], 3), # x^3
        ([(i, i) for i in range(5)], 10),
        ([(i, 1) for i in range(5)], 100)
    ]
    for pts, X in public_cases:
        res = solve(pts, X)
        inp_lines = [f"{len(pts)} {X}"]
        for x, y in pts:
            inp_lines.append(f"{x} {y}")
        testcases["public"].append({"input": format_input(inp_lines), "output": format_output(res)})

    hidden_cases = []
    
    for _ in range(5):
        k = random.randint(3, 15)
        X = random.randint(0, MOD-1)
        pts = []
        seen_x = set()
        while len(pts) < k:
            x = random.randint(0, MOD-1)
            if x not in seen_x:
                seen_x.add(x)
                y = random.randint(0, MOD-1)
                pts.append((x, y))
        hidden_cases.append((pts, X))
        
    for _ in range(3):
        k = random.randint(30, 50)
        X = random.randint(0, MOD-1)
        pts = []
        seen_x = set()
        while len(pts) < k:
            x = random.randint(0, MOD-1)
            if x not in seen_x:
                seen_x.add(x)
                y = random.randint(0, MOD-1)
                pts.append((x, y))
        hidden_cases.append((pts, X))

    for pts, X in hidden_cases:
        res = solve(pts, X)
        inp_lines = [f"{len(pts)} {X}"]
        for x, y in pts:
            inp_lines.append(f"{x} {y}")
        testcases["hidden"].append({"input": format_input(inp_lines), "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-006: Determinant via Gaussian Elimination
def generate_mth006():
    problem_id = "MTH-006"
    filename = os.path.join(OUTPUT_DIR, "MTH-006-determinant-gaussian.yaml")
    MOD = 1000000007

    def modInverse(n):
        return pow(n, MOD - 2, MOD)

    def solve(matrix):
        n = len(matrix)
        mat = [row[:] for row in matrix] # Copy
        det = 1
        for i in range(n):
            pivot = i
            while pivot < n and mat[pivot][i] == 0:
                pivot += 1
            if pivot == n:
                return 0
            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                det = (MOD - det) % MOD
            
            det = (det * mat[i][i]) % MOD
            inv = modInverse(mat[i][i])
            
            for j in range(i + 1, n):
                factor = (mat[j][i] * inv) % MOD
                for k in range(i, n):
                    mat[j][k] = (mat[j][k] - factor * mat[i][k]) % MOD
        return det

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        [[1, 2], [3, 4]], # 4-6 = -2
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]], # Identity -> 1
        [[1, 2], [2, 4]] # Singular -> 0
    ]
    for mat in samples:
        res = solve(mat)
        inp_lines = [f"{len(mat)}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["samples"].append({"input": format_input(inp_lines), "output": format_output(res)})

    public_cases = [
        [[2]],
        [[0, 1], [1, 0]], # -1
        [[2, 0], [0, 3]], # 6
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], # 0
        [[5, 2, 1], [2, 5, 2], [1, 2, 5]]
    ]
    for mat in public_cases:
        res = solve(mat)
        inp_lines = [f"{len(mat)}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["public"].append({"input": format_input(inp_lines), "output": format_output(res)})

    hidden_cases = []
    
    for _ in range(5):
        n = random.randint(2, 10)
        mat = [[random.randint(0, MOD-1) for _ in range(n)] for _ in range(n)]
        hidden_cases.append(mat)
        
    for _ in range(3):
        n = random.randint(20, 40)
        mat = [[random.randint(0, MOD-1) for _ in range(n)] for _ in range(n)]
        hidden_cases.append(mat)

    for mat in hidden_cases:
        res = solve(mat)
        inp_lines = [f"{len(mat)}"]
        for row in mat:
            inp_lines.append(" ".join(map(str, row)))
        testcases["hidden"].append({"input": format_input(inp_lines), "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-007: Matrix Exponentiation for Linear Recurrence
def generate_mth007():
    problem_id = "MTH-007"
    filename = os.path.join(OUTPUT_DIR, "MTH-007-matrix-exp-linear-recurrence.yaml")
    MOD = 1000000007

    def mat_mul(A, B):
        C = [[0]*len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    def mat_pow(A, p):
        res = [[0]*len(A) for _ in range(len(A))]
        for i in range(len(A)): res[i][i] = 1
        while p > 0:
            if p % 2 == 1:
                res = mat_mul(res, A)
            A = mat_mul(A, A)
            p //= 2
        return res

    def solve(coeffs, init_vals, n):
        k = len(coeffs)
        if n < k:
            return init_vals[n] # init_vals are a_0, a_1 ... a_{k-1}
        
        # State vector V_i = [a_i, a_{i-1}, ..., a_{i-k+1}]^T
        # Transition T:
        # Row 0: coeffs (c_0, c_1 ... c_{k-1}) -> a_{i+1} = c_0 a_i + ...
        # Row 1: 1 0 ... -> a_i = a_i
        # ...
        
        # Note: Problem statement says a_n = c_0 a_{n-1} + ...
        # And input gives c_0 ... c_{k-1}
        # And initial terms a_0 ... a_{k-1}
        
        # We want a_n.
        # V_{k-1} = [a_{k-1}, a_{k-2}, ..., a_0]^T
        # V_n = T^{n-(k-1)} * V_{k-1}
        # The top element of V_n is a_n.
        
        T = [[0]*k for _ in range(k)]
        for j in range(k):
            T[0][j] = coeffs[j]
        for i in range(1, k):
            T[i][i-1] = 1
            
        Tn = mat_pow(T, n - (k - 1))
        
        # V_{k-1}
        V = [[init_vals[k-1-i]] for i in range(k)]
        
        res_vec = mat_mul(Tn, V)
        return res_vec[0][0]

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        ([1, 1], [0, 1], 5), # Fib: 0, 1, 1, 2, 3, 5 -> 5
        ([1, 1], [0, 1], 10), # Fib(10) = 55
        ([2], [1], 5) # a_n = 2*a_{n-1}, a_0=1 -> 1, 2, 4, 8, 16, 32 -> 32
    ]
    for c, init, n in samples:
        res = solve(c, init, n)
        inp = f"{len(c)} {n}\n{' '.join(map(str, c))}\n{' '.join(map(str, init))}"
        testcases["samples"].append({"input": inp, "output": format_output(res)})

    public_cases = [
        ([1, 1], [0, 1], 0),
        ([1, 1], [0, 1], 1),
        ([1, -1], [1, 2], 5),
        ([1, 2, 3], [1, 1, 1], 10)
    ]
    for c, init, n in public_cases:
        # Adjust negative
        c_mod = [(x + MOD) % MOD for x in c]
        res = solve(c_mod, init, n)
        inp = f"{len(c)} {n}\n{' '.join(map(str, c_mod))}\n{' '.join(map(str, init))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    hidden_cases = []
    
    for _ in range(5):
        k = random.randint(2, 5)
        n = random.randint(k, 100)
        c = [random.randint(0, MOD-1) for _ in range(k)]
        init = [random.randint(0, MOD-1) for _ in range(k)]
        hidden_cases.append((c, init, n))
        
    for _ in range(3):
        k = random.randint(5, 10)
        n = random.randint(1000, 1000000) # Large n
        c = [random.randint(0, MOD-1) for _ in range(k)]
        init = [random.randint(0, MOD-1) for _ in range(k)]
        hidden_cases.append((c, init, n))

    for c, init, n in hidden_cases:
        res = solve(c, init, n)
        inp = f"{len(c)} {n}\n{' '.join(map(str, c))}\n{' '.join(map(str, init))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)
def generate_mth008():
    problem_id = "MTH-008"
    filename = os.path.join(OUTPUT_DIR, "MTH-008-fwht-xor-convolution.yaml")
    MOD = 1000000007

    def solve(A, B):
        # Naive O(N^2) XOR convolution
        n = len(A)
        C = [0] * n
        for i in range(n):
            for j in range(n):
                k = i ^ j
                C[k] = (C[k] + A[i] * B[j]) % MOD
        return C

    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}

    samples = [
        ([1, 2], [3, 4]), # 0^0=0(1*3), 0^1=1(1*4), 1^0=1(2*3), 1^1=0(2*4) -> C[0]=3+8=11, C[1]=4+6=10
        ([1, 0, 0, 0], [0, 1, 0, 0]), # 1 at 0, 1 at 1 -> 1 at 1
        ([1, 1], [1, 1])
    ]
    for A, B in samples:
        res = solve(A, B)
        inp = f"{len(A)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["samples"].append({"input": inp, "output": format_output(res)})

    public_cases = [
        ([1], [1]),
        ([1, 2, 3, 4], [1, 0, 0, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1])
    ]
    for A, B in public_cases:
        res = solve(A, B)
        inp = f"{len(A)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["public"].append({"input": inp, "output": format_output(res)})

    hidden_cases = []
    
    for _ in range(5):
        k = random.randint(2, 5)
        n = 1 << k
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(n)]
        hidden_cases.append((A, B))
        
    for _ in range(3):
        k = random.randint(6, 8) # Keep small for O(N^2) generation
        n = 1 << k
        A = [random.randint(0, MOD-1) for _ in range(n)]
        B = [random.randint(0, MOD-1) for _ in range(n)]
        hidden_cases.append((A, B))

    for A, B in hidden_cases:
        res = solve(A, B)
        inp = f"{len(A)}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        testcases["hidden"].append({"input": inp, "output": format_output(res)})

    write_yaml(filename, testcases)

# --- Main Execution ---

if __name__ == "__main__":
    generate_mth001()
    generate_mth002()
    generate_mth003()
    generate_mth004()
    generate_mth005()
    generate_mth006()
    generate_mth007()
    generate_mth008()
    print("Generated test cases for MTH-001 to MTH-008")
