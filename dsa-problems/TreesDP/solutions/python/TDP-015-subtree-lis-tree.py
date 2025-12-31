import sys
from bisect import bisect_left
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    values = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    lis = [0] * (n + 1)
    active = []

    def dfs(u, p):
        pos = bisect_left(active, values[u])
        saved = active[pos] if pos < len(active) else None

        if pos < len(active):
            active[pos] = values[u]
        else:
            active.append(values[u])

        lis[u] = len(active)

        for v in adj[u]:
            if v != p: dfs(v, u)

        if saved is not None:
            active[pos] = saved
        else:
            active.pop()

    dfs(1, 0)
    print(' '.join(map(str, lis[1:])))

if __name__ == "__main__":
    main()
