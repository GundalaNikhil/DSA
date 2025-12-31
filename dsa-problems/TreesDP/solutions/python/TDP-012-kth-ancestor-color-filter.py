import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    LOG = 20

    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    up = [[0] * LOG for _ in range(n + 1)]

    def dfs(u, p):
        up[u][0] = p
        for i in range(1, LOG):
            up[u][i] = up[up[u][i - 1]][i - 1]
        for v in adj[u]:
            if v != p:
                dfs(v, u)

    dfs(1, 0)

    def find_kth(v, c, k):
        count = 0
        while v != 0:
            if color[v] == c:
                count += 1
                if count == k: return v
            v = up[v][0]
        return -1

    q = int(data[idx]); idx += 1
    for _ in range(q):
        v, c, k = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        print(find_kth(v, c, k))

if __name__ == "__main__":
    main()
