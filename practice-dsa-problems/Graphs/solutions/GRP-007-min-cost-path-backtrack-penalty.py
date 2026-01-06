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
    back_penalty = int(input_data[ptr])
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
        adj[v].append((u, w))
        s = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        pq = [(0, s, -1)]
        dist = {}
        while pq:
            d, u, p = heapq.heappop(pq)
            if (u, p) in dist and dist[(u, p)] <= d:
                continue
            dist[(u, p)] = d
            if u == t:
                print(d)
                return
            for v, w in adj[u]:
                move_cost = w
                if v == p:
                    move_cost += back_penalty
                    if (v, u) not in dist or dist[(v, u)] > d + move_cost:
                        heapq.heappush(pq, (d + move_cost, v, u))
                        print("-1")


if __name__ == "__main__":
    solve()
