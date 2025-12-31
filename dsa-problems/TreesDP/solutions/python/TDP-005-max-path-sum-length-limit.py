import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx])
    L = int(data[idx + 1])
    idx += 2

    value = [0] * (n + 1)
    for i in range(1, n + 1):
        value[i] = int(data[idx])
        idx += 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)

    dp = [[float('-inf')] * (L + 1) for _ in range(n + 1)]
    max_sum = [float('-inf')]

    def dfs(u, parent):
        dp[u][0] = value[u]
        max_sum[0] = max(max_sum[0], value[u])

        child_paths = []

        for v in graph[u]:
            if v == parent:
                continue

            dfs(v, u)

            child_best = [float('-inf')] * (L + 1)

            for length in range(L):
                if dp[v][length] > float('-inf') / 2:
                    extended = dp[v][length] + value[u]
                    dp[u][length + 1] = max(dp[u][length + 1], extended)
                    child_best[length] = dp[v][length]

            child_paths.append(child_best)

        for length in range(L + 1):
            max_sum[0] = max(max_sum[0], dp[u][length])

        for i in range(len(child_paths)):
            for j in range(i + 1, len(child_paths)):
                path1 = child_paths[i]
                path2 = child_paths[j]

                for len1 in range(L + 1):
                    for len2 in range(L + 1):
                        # Total edges: len1 + 1 (to u) + 1 (from u) + len2
                        if len1 + len2 + 2 > L:
                            continue
                        if (path1[len1] > float('-inf') / 2 and
                            path2[len2] > float('-inf') / 2):
                            combined = path1[len1] + path2[len2] + value[u]
                            max_sum[0] = max(max_sum[0], combined)

    dfs(1, -1)
    print(max_sum[0])

solve()


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
