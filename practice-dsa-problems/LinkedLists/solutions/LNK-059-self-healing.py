import sys
from collections import Counter


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    checksums = []
    for _ in range(n):
        checksums.append(int(input_data[ptr]))
        ptr += 1
        
    initial_vals = list(vals)
    new_vals = list(vals)
    
    for i in range(n):
        prev_v = initial_vals[i - 1] if i > 0 else 0
        curr_v = initial_vals[i]
        next_v = initial_vals[i + 1] if i < n - 1 else 0
        
        if (curr_v ^ prev_v ^ next_v) != checksums[i]:
            neighbors = [prev_v, next_v]
            counts = Counter(neighbors)
            # This logic seems slightly simplified or hypothetical "self-healing"
            # It just assumes neighbor values might be correct candidates?
            max_c = max(counts.values())
            candidates = [v for v, c in counts.items() if c == max_c]
            new_vals[i] = min(candidates)
            
    print(*(new_vals))


if __name__ == "__main__":
    solve()
