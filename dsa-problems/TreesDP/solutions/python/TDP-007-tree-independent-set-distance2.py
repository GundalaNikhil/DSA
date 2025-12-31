import sys
sys.setrecursionlimit(300000)

def solve():
    n = int(input())
    weight = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 0, 0] for _ in range(n + 1)]

    def dfs(u, parent):
        dp[u][0] = 0
        dp[u][1] = 0
        dp[u][2] = weight[u]

        sum_without_selected = 0
        max_gain = float('-inf')

        for v in graph[u]:
            if v == parent:
                continue

            dfs(v, u)

            best_not_selected = max(dp[v][0], dp[v][1])
            sum_without_selected += best_not_selected

            gain = dp[v][2] - best_not_selected
            max_gain = max(max_gain, gain)

            dp[u][2] += dp[v][0]

        dp[u][0] = sum_without_selected

        if max_gain > float('-inf'):
            dp[u][1] = sum_without_selected + max_gain

    dfs(1, -1)

    result = max(dp[1][0], dp[1][1], dp[1][2])
    print(result)

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
