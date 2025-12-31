import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]

    def dfs(u, p):
        dp[u][0] = 0
        dp[u][1] = 0
        total = 0

        for v in adj[u]:
            if v == p: continue
            dfs(v, u)
            total += max(dp[v][0], dp[v][1])

        dp[u][0] = total

        for v in adj[u]:
            if v == p: continue
            dp[u][1] = max(dp[u][1], 1 + dp[v][0] + total - max(dp[v][0], dp[v][1]))

    dfs(1, 0)
    print(max(dp[1][0], dp[1][1]))

if __name__ == "__main__":
    main()
