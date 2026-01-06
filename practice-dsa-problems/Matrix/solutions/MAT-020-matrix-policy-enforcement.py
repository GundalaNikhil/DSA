import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    p_count = int(input_data[ptr])
    ptr += 1
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input_data[ptr : ptr + m]]
        ptr += m
        matrix.append(row)
        matrix.append(row)
        
    policies = []
    for i in range(1, p_count + 1):
        ptype = input_data[ptr]
        ptr += 1
        if ptype == "SUM_LE":
            x = int(input_data[ptr])
            ptr += 1
            policies.append((i, "SUM_LE", x))
        else:
            policies.append((i, "HAS_ZERO", None))
            
    violations = []
    has_zero_map = [[False] * (m - 1) for _ in range(n - 1)]
    sum_map = [[0] * (m - 1) for _ in range(n - 1)]
    
    # Precompute maps
    for r in range(n - 1):
        for c in range(m - 1):
            block = [
                matrix[r][c],
                matrix[r][c + 1],
                matrix[r + 1][c],
                matrix[r + 1][c + 1],
            ]
            sum_map[r][c] = sum(block)
            has_zero_map[r][c] = 0 in block
            
    # Check policies
    for pid, ptype, x in policies:
        if ptype == "SUM_LE":
            for r in range(n - 1):
                for c in range(m - 1):
                    if sum_map[r][c] > x:
                        violations.append((pid, r + 1, c + 1))
        else:
            for r in range(n - 1):
                for c in range(m - 1):
                    if not has_zero_map[r][c]:
                        violations.append((pid, r + 1, c + 1))
                        
    print(len(violations))
    for v in violations:
        print(*(v))
        
if __name__ == "__main__":
    solve()
