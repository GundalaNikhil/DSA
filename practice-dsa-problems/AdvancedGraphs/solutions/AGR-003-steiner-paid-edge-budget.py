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
    k = int(input_data[ptr])
    ptr += 1
    budget = int(input_data[ptr])
    ptr += 1
    terminals = []
    for _ in range(k):
        terminals.append(int(input_data[ptr]) - 1)
        ptr += 1
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(input_data[ptr]) - 1
            ptr += 1
            v = int(input_data[ptr]) - 1
            ptr += 1
            p = int(input_data[ptr])
            ptr += 1
            a = int(input_data[ptr])
            ptr += 1
            adj[u].append((v, p, a))
            adj[v].append((u, p, a))
            INF = float("inf")
            dp = [[[INF] * (budget + 1) for _ in range(n)] for _ in range(1 << k)]
            for i in range(k):
                dp[1 << i][terminals[i]][0] = 0
                for mask in range(1, 1 << k):
                    for sub in range((mask - 1) & mask, 0, (mask - 1) & mask):
                        if sub < (mask ^ sub):
                            continue
                        comp = mask ^ sub
                        for u in range(n):
                            for b1 in range(budget + 1):
                                if dp[sub][u][b1] == INF:
                                    continue
                                for b2 in range(budget - b1 + 1):
                                    if dp[comp][u][b2] == INF:
                                        continue
                                    dp[mask][u][b1 + b2] = min(
                                        dp[mask][u][b1 + b2],
                                        dp[sub][u][b1] + dp[comp][u][b2],
                                    )
                                    pq = []
                                    for u in range(n):
                                        for b in range(budget + 1):
                                            if dp[mask][u][b] != INF:
                                                heapq.heappush(
                                                    pq, (dp[mask][u][b], u, b)
                                                )
                                                while pq:
                                                    d, u, b = heapq.heappop(pq)
                                                    if d > dp[mask][u][b]:
                                                        continue
                                                    for v, p, a in adj[u]:
                                                        new_b = b + p
                                                        if new_b <= budget:
                                                            if (
                                                                dp[mask][v][new_b]
                                                                > d + a
                                                            ):
                                                                dp[mask][v][new_b] = (
                                                                    d + a
                                                                )
                                                                heapq.heappush(
                                                                    pq,
                                                                    (
                                                                        dp[mask][v][
                                                                            new_b
                                                                        ],
                                                                        v,
                                                                        new_b,
                                                                    ),
                                                                )
                                                                ans = INF
                                                                final_mask = (
                                                                    1 << k
                                                                ) - 1
                                                                for u in range(n):
                                                                    for b in range(
                                                                        budget + 1
                                                                    ):
                                                                        ans = min(
                                                                            ans,
                                                                            dp[
                                                                                final_mask
                                                                            ][u][b],
                                                                        )
                                                                        print(
                                                                            ans
                                                                            if ans
                                                                            != INF
                                                                            else -1
                                                                        )


if __name__ == "__main__":
    solve()
