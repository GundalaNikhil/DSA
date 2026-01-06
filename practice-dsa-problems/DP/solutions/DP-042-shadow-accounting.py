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
    actions = []
    for _ in range(a_count):
        actions.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
        
    inf = float("inf")
    dp = [[-inf] * 201 for _ in range(n + 1)]
    dp[0][0] = 0
    
    for s in range(n):
        for b in range(201):
            if dp[s][b] == -inf:
                continue
            for r, cost in actions:
                nb = b + cost
                if 0 <= nb <= 200:
                    dp[s + 1][nb] = max(dp[s + 1][nb], dp[s][b] + r)
                    
    ans = max(dp[n])
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
