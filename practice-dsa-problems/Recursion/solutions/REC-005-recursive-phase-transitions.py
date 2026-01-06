import sys

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    d_limit = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
        
    total_val = 0

    def process_segment(l, r, depth):
        nonlocal total_val
        if l > r:
            return
            
        total_val += pref[r + 1] - pref[l]
        length = r - l + 1
        if length == 1:
            return
            
        if depth < d_limit:
            # Binary split
            mid_idx = (l + r) // 2
            process_segment(l, mid_idx, depth + 1)
            process_segment(mid_idx + 1, r, depth + 1)
        else:
            # Ternary split
            q = length // 3
            rem = length % 3
            size1 = q + (1 if rem >= 1 else 0)
            size2 = q + (1 if rem >= 2 else 0)
            size3 = q
            
            process_segment(l, l + size1 - 1, depth + 1)
            process_segment(l + size1, l + size1 + size2 - 1, depth + 1)
            process_segment(l + size1 + size2, r, depth + 1)

    process_segment(0, n - 1, 0)
    print(total_val)


if __name__ == "__main__":
    solve()
