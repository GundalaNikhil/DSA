import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    budget = int(input_data[ptr])
    ptr += 1
    d_step = int(input_data[ptr])
    ptr += 1
    items = []
    for i in range(n):
        p = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        val_at_n = max(0, v - d_step * (n - (i + 1)))
        items.append((p, val_at_n))
    for p_i, v_i in items:
        for b in range(budget, p_i - 1, -1):
            dp[b] = max(dp[b], dp[b - p_i] + v_i)
            
    print(max(dp))


if __name__ == "__main__":
    solve()
