import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n, K, F = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    dp = [[[0]*2 for _ in range(K + 1)] for _ in range(n + 1)]
    answer = [0]

    def dfs(u, p):
        dp[u][0][1 if color[u] == F else 0] = 1

        for v in adj[u]:
            if v == p: continue
            dfs(v, u)

            # Save current dp[u] before merging
            temp = [[dp[u][d][h] for h in range(2)] for d in range(K + 1)]

            for d1 in range(K):
                for d2 in range(K - d1):
                    for h1 in range(2):
                        for h2 in range(2):
                            if d1 + d2 + 1 == K:
                                # Count pairs only if path is clean (no forbidden color)
                                if h1 == 0 and h2 == 0 and color[u] != F:
                                    answer[0] += temp[d1][h1] * dp[v][d2][h2]

                            # Merge: path has forbidden if any segment has it or u has it
                            new_has = h1 | h2 | (1 if color[u] == F else 0)
                            if d1 + d2 + 1 <= K:
                                dp[u][d1 + d2 + 1][new_has] += temp[d1][h1] * dp[v][d2][h2]

    dfs(1, 0)
    print(answer[0])

if __name__ == "__main__":
    main()
