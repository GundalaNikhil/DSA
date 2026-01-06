import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_states = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    adj = []
    for _ in range(a_count):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1
        c_rev = int(input_data[ptr])
        ptr += 1
        adj.append((u, v, c))
        adj.append((v, u, c_rev))
        
    inf = float("inf")
    dp = [[inf] * s_states for _ in range(n + 1)]
    dp[0][0] = 0
    
    for step in range(n):
        for u, v, cost in adj:
            if dp[step][u] != inf:
                if dp[step + 1][v] > dp[step][u] + cost:
                    dp[step + 1][v] = dp[step][u] + cost
                    
    ans = dp[n][0]
    print(ans if ans != inf else -1)


if __name__ == "__main__":
    solve()
