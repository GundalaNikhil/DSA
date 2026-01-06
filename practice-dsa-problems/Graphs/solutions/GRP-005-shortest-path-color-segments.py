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
    num_colors = int(input_data[ptr])
    ptr += 1
    k_limit = int(input_data[ptr])
    ptr += 1
    node_colors = []
    for _ in range(n):
        node_colors.append(int(input_data[ptr]) - 1)
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
            num_rules = int(input_data[ptr])
            ptr += 1
            rules = []
            for _ in range(num_rules):
                a = int(input_data[ptr]) - 1
                b = int(input_data[ptr]) - 1
                rules.append((a, b))
                ptr += 1
                start_node = int(input_data[ptr])
                ptr += 1
                target_node = int(input_data[ptr])
                ptr += 1
                invalid_mask_for_color = [0] * num_colors
                for a, b in rules:
                    invalid_mask_for_color[a] |= 1 << b
                    start_color = node_colors[start_node - 1]
                    pq = [(0, start_node, 1 << start_color, 1)]
                    dist = {}
                    while pq:
                        d, u, mask, seg_len = heapq.heappop(pq)
                        state = (u, mask, seg_len)
                        if state in dist and dist[state] <= d:
                            continue
                        dist[state] = d
                        if u == target_node:
                            print(d)
                            return
                        cur_color = node_colors[u - 1]
                        for v, w in adj[u]:
                            nv_color = node_colors[v - 1]
                            if nv_color == cur_color:
                                if seg_len < k_limit:
                                    n_state = (v, mask, seg_len + 1)
                                    if n_state not in dist or dist[n_state] > d + w:
                                        heapq.heappush(
                                            pq, (d + w, v, mask, seg_len + 1)
                                        )
                                    else:
                                        if not (mask & (1 << nv_color)):
                                            if not (
                                                mask & invalid_mask_for_color[nv_color]
                                            ):
                                                n_mask = mask | (1 << nv_color)
                                                n_state = (v, n_mask, 1)
                                                if (
                                                    n_state not in dist
                                                    or dist[n_state] > d + w
                                                ):
                                                    heapq.heappush(
                                                        pq, (d + w, v, n_mask, 1)
                                                    )
                                                    print("-1")


if __name__ == "__main__":
    solve()
