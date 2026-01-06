import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_size = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    num_segments = (n + k_size - 1) // k_size
    claimed = []
    for _ in range(num_segments):
        claimed.append(int(input_data[ptr]))
        ptr += 1
        
    MOD = 1_000_000_007
    for i in range(num_segments):
        start = i * k_size
        end = min(n, (i + 1) * k_size)
        seg_sum = sum(vals[start:end])
        computed = seg_sum % MOD
        if computed != claimed[i]:
            print(i + 1)
            return
            
    print(0)


if __name__ == "__main__":
    solve()
