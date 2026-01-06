import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    cap = int(input_data[ptr])
    ptr += 1
    gen = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        actions.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
        
    dp = [-float("inf")] * (cap + 1)
    dp[cap] = 0
    
    for _ in range(n):
        new_dp = [-float("inf")] * (cap + 1)
        for c in range(cap + 1):
            if dp[c] == -float("inf"):
                continue
            for r, cost in actions:
                if c >= cost:
                    nc = min(cap, c - cost + gen)
                    new_dp[nc] = max(new_dp[nc], dp[c] + r)
        dp = new_dp
        
    ans = max(dp)
    print(ans if ans != -float("inf") else 0)


if __name__ == "__main__":
    solve()
