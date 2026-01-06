import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    R = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    initial_vals = []
    initial_vals = []
    for _ in range(n):
        initial_vals.append(int(input_data[ptr]))
        ptr += 1
        
    replicas = [list(initial_vals) for _ in range(R)]
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "SET":
            r_idx = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            replicas[r_idx - 1][pos - 1] = x
        elif op == "READ":
            pos = int(input_data[ptr])
            ptr += 1
            Q = int(input_data[ptr])
            ptr += 1
            counts = {}
            for r in range(R):
                val = replicas[r][pos - 1]
                counts[val] = counts.get(val, 0) + 1
                
            candidates = [v for v, c in counts.items() if c >= Q]
            if not candidates:
                print("CONFLICT")
            else:
                print(min(candidates))


if __name__ == "__main__":
    solve()
