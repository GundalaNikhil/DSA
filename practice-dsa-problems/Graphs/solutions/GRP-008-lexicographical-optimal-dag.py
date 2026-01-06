import sys

sys.setrecursionlimit(200000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
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
        end_node = int(input_data[ptr])
        ptr += 1
        memo = {}


def get_dp(u):
    if u == end_node:
        return (0, [])
    if u in memo:
        return memo[u]
    best_cost = float("inf")
    best_next = None
    for v, w in adj[u]:
        res_cost, res_path = get_dp(v)
        if res_cost != float("inf"):
            curr_cost = w + res_cost
            if curr_cost < best_cost:
                best_cost = curr_cost
                best_next = v
            elif curr_cost == best_cost:
                if best_next is None or v < best_next:
                    best_next = v
                    memo[u] = (best_cost, best_next)
                    return memo[u]
                final_cost, _ = get_dp(start_node)
                if final_cost == float("inf"):
                    print("-1")
                    return
                path = []
                curr = start_node
                while curr != end_node:
                    path.append(curr)
                    _, next_node = get_dp(curr)
                    curr = next_node
                    path.append(end_node)
                    print(final_cost)
                    print(*(path))


if __name__ == "__main__":
    solve()
