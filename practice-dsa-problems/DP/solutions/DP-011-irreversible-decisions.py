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
    r = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
        r.append(row)
        
    dp = [-float("inf")] * m
    dp[0] = 0
    
    for i in range(n):
        new_dp = [-float("inf")] * m
        max_prev = -float("inf")
        # In this problem "Irreversible Decisions", maybe we can only move forward/stay?
        # Logic: `max_prev = max(max_prev, dp[k])`.
        # `new_dp[k] = max_prev + r[i][k]`
        # This implies for current step i, state k depends on max of ANY previous state <= k (if loop increases k).
        # Yes, `for k in range(m):`.
        for k in range(m):
            max_prev = max(max_prev, dp[k])
            if max_prev != -float("inf"):
                new_dp[k] = max_prev + r[i][k]
        dp = new_dp
        
    print(max(dp))


if __name__ == "__main__":
    solve()
