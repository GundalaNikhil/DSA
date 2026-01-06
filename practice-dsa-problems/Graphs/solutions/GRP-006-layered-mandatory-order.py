import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    num_layers = int(input_data[ptr])
    ptr += 1
    node_layers = []
    for _ in range(n):
        node_layers.append(int(input_data[ptr]))
        ptr += 1
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            w = int(input_data[ptr])
            ptr += 1
            adj[u].append((v, w))
            start_node = int(input_data[ptr])
            ptr += 1
            target_node = int(input_data[ptr])
            ptr += 1
            s_layer = node_layers[start_node - 1]
            reached = 1 if s_layer == 1 else 0
            pq = [(0, start_node, reached)]
            dist = {}
            while pq:
                d, u, r = heapq.heappop(pq)
                if (u, r) in dist and dist[(u, r)] <= d:
                    continue
                dist[(u, r)] = d
                if u == target_node and r == num_layers:
                    print(d)
                    return
                for v, w in adj[u]:
                    v_layer = node_layers[v - 1]
                    nr = r
                    if v_layer == r + 1:
                        nr = r + 1
                        if (v, nr) not in dist or dist[(v, nr)] > d + w:
                            heapq.heappush(pq, (d + w, v, nr))
                            print("-1")


if __name__ == "__main__":
    solve()
