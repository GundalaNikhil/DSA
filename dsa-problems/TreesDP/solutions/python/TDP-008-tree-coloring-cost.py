import sys
from collections import defaultdict
sys.setrecursionlimit(200005)

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1

    cost = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cost[i][j] = int(input_data[idx]); idx += 1

    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(u):
        visited[u] = True
        for c in range(1, k + 1):
            dp[u][c] = cost[u][c]

        for v in adj[u]:
            if not visited[v]:
                dfs(v)

                # For each color c at u, add minimum cost from child v
                # where child uses any color except c
                for c in range(1, k + 1):
                    min_child_cost = float('inf')
                    for c2 in range(1, k + 1):
                        if c2 != c:
                            min_child_cost = min(min_child_cost, dp[v][c2])
                    dp[u][c] += min_child_cost

    dfs(1)
    print(min(dp[1][c] for c in range(1, k + 1)))

if __name__ == "__main__":
    main()
