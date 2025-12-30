import sys
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

    timer = [0]
    in_time = [0] * (n + 1)
    out_time = [0] * (n + 1)

    def dfs(u, p):
        timer[0] += 1
        in_time[u] = timer[0]
        for v in adj[u]:
            if v != p: dfs(v, u)
        out_time[u] = timer[0]

    dfs(1, 0)

    fenwick = [0] * (n + 2)

    def update(i, val):
        while i <= n:
            fenwick[i] += val
            i += i & (-i)

    def query(i):
        s = 0
        while i > 0:
            s += fenwick[i]
            i -= i & (-i)
        return s

    for i in range(1, n + 1):
        update(in_time[i], values[i])
        update(in_time[i] + 1, -values[i])

    q = int(data[idx]); idx += 1
    for _ in range(q):
        t = int(data[idx]); idx += 1
        if t == 1:
            u, val = int(data[idx]), int(data[idx + 1])
            idx += 2
            update(in_time[u], val)
            update(out_time[u] + 1, -val)
        else:
            u = int(data[idx]); idx += 1
            print(query(in_time[u]))

if __name__ == "__main__":
    main()
