import sys
sys.setrecursionlimit(300000)

def solve():
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]

    def dfs(u, parent):
        dp[u][0] = 0  # Not including u
        dp[u][1] = 1  # Including u

        for v in graph[u]:
            if v == parent:
                continue

            dfs(v, u)

            # If u not included, all children must be included
            dp[u][0] += dp[v][1]

            # If u included, take minimum for each child
            dp[u][1] += min(dp[v][0], dp[v][1])

    dfs(1, -1)

    result = min(dp[1][0], dp[1][1])
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
