import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    p = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(p):
        row = [0]
        curr = 0
        for _ in range(n):
            val = int(input_data[ptr])
            ptr += 1
            curr += val
            row.append(curr)
            curr += val
            row.append(curr)
        rewards.append(row)
        
    dp = [-float("inf")] * (n + 1)
    dp[0] = 0
    
    for i in range(p):
        new_dp = [-float("inf")] * (n + 1)
        for j in range(n + 1):
            if dp[j] == -float("inf"):
                continue
            # Try allocating k items to path i
            # Path i has length n (max possible allocation)
            # rewards[i][k] is value of first k items
            # Total allocated items <= n
            for k in range(n - j + 1):
                new_dp[j + k] = max(new_dp[j + k], dp[j] + rewards[i][k])
        dp = new_dp
        
    print(dp[n])


if __name__ == "__main__":
    solve()
