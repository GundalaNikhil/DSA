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
    limit = int(input_data[ptr])
    ptr += 1
    fatigue = []
    for _ in range(n):
        fatigue.append(int(input_data[ptr]))
        ptr += 1
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            adj[u].append(v)
            adj[v].append(u)
            s = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            pq = [(fatigue[s - 1], s)]
            dist = [float("inf")] * (n + 1)
            dist[s] = fatigue[s - 1]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                if d > limit:
                    break
                if u == t:
                    print("YES")
                    return
                for v in adj[u]:
                    new_dist = d + fatigue[v - 1]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
                        print("NO")


if __name__ == "__main__":
    solve()
