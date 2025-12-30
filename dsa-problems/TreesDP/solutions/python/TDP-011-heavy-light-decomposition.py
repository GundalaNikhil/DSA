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
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    heavy = [-1] * (n + 1)
    head = [0] * (n + 1)
    pos = [0] * (n + 1)
    timer = [0]

    def dfs1(u, p):
        size, max_size = 1, 0
        parent[u] = p
        depth[u] = 0 if p == 0 else depth[p] + 1

        for v in adj[u]:
            if v == p: continue
            subtree_size = dfs1(v, u)
            size += subtree_size
            if subtree_size > max_size:
                max_size = subtree_size
                heavy[u] = v
        return size

    def dfs2(u, h):
        head[u] = h
        pos[u] = timer[0]
        timer[0] += 1

        if heavy[u] != -1:
            dfs2(heavy[u], h)

        for v in adj[u]:
            if v != parent[u] and v != heavy[u]:
                dfs2(v, v)

    dfs1(1, 0)
    dfs2(1, 1)

    # Build segment tree
    seg = [0] * (4 * n)
    pos_to_val = [0] * n
    for i in range(1, n + 1):
        pos_to_val[pos[i]] = values[i]

    def build(node, l, r):
        if l == r:
            seg[node] = pos_to_val[l]
            return
        mid = (l + r) // 2
        build(2 * node, l, mid)
        build(2 * node + 1, mid + 1, r)
        seg[node] = seg[2 * node] + seg[2 * node + 1]

    def query(node, l, r, ql, qr):
        if ql > r or qr < l: return 0
        if ql <= l and r <= qr: return seg[node]
        mid = (l + r) // 2
        return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)

    build(1, 0, n - 1)

    def query_path(u, v):
        result = 0
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            result += query(1, 0, n - 1, pos[head[u]], pos[u])
            u = parent[head[u]]
        if depth[u] > depth[v]:
            u, v = v, u
        result += query(1, 0, n - 1, pos[u], pos[v])
        return result

    q = int(data[idx]); idx += 1
    for _ in range(q):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        print(query_path(u, v))

if __name__ == "__main__":
    main()
