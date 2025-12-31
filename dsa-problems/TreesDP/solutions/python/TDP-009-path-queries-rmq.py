import sys
import math
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1

    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    first = [0] * (n + 1)
    depth = [0] * (n + 1)  # Tree depth (number of edges from root)
    dist = [0] * (n + 1)   # Weighted distance from root
    euler = []

    def dfs(u, p, d, distance):
        depth[u] = d
        dist[u] = distance
        first[u] = len(euler)
        euler.append(u)

        for v, w in adj[u]:
            if v != p:
                dfs(v, u, d + 1, distance + w)
                euler.append(u)

    dfs(1, 0, 0, 0)

    # Build sparse table for RMQ on Euler tour (minimum depth)
    size = len(euler)
    log_size = int(math.log2(size)) + 1
    st = [[0] * log_size for _ in range(size)]

    for i in range(size):
        st[i][0] = i

    for j in range(1, log_size):
        i = 0
        while i + (1 << j) <= size:
            left = st[i][j - 1]
            right = st[i + (1 << (j - 1))][j - 1]
            st[i][j] = left if depth[euler[left]] <= depth[euler[right]] else right
            i += 1

    def query_lca(u, v):
        l, r = first[u], first[v]
        if l > r:
            l, r = r, l

        length = r - l + 1
        k = int(math.log2(length))

        left = st[l][k]
        right = st[r - (1 << k) + 1][k]

        lca_idx = left if depth[euler[left]] <= depth[euler[right]] else right
        return euler[lca_idx]

    def query_distance(u, v):
        lca = query_lca(u, v)
        return dist[u] + dist[v] - 2 * dist[lca]

    q = int(input_data[idx]); idx += 1
    for _ in range(q):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        print(query_distance(u, v))

if __name__ == "__main__":
    main()
