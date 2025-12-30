import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1

    weight = [0] * (n + 1)
    for i in range(1, n + 1):
        weight[i] = int(data[idx])
        idx += 1

    total_weight = sum(weight)

    graph = defaultdict(list)
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)

    subtree_weight = [0] * (n + 1)
    down = [0] * (n + 1)
    up = [0] * (n + 1)

    def dfs_down(u, parent):
        subtree_weight[u] = weight[u]
        down[u] = 0

        for v in graph[u]:
            if v == parent:
                continue

            dfs_down(v, u)

            child_contribution = down[v] + 2 * subtree_weight[v] + subtree_weight[v]
            down[u] += child_contribution
            subtree_weight[u] += subtree_weight[v]

    def dfs_up(u, parent):
        if parent != -1:
            outside_weight = total_weight - subtree_weight[u]

            parent_total_down = down[parent]
            u_contribution = down[u] + 2 * subtree_weight[u] + subtree_weight[u]
            parent_down_without_u = parent_total_down - u_contribution

            up[u] = up[parent] + parent_down_without_u + 2 * outside_weight + outside_weight

        for v in graph[u]:
            if v == parent:
                continue
            dfs_up(v, u)

    dfs_down(1, -1)
    dfs_up(1, -1)

    min_cost = float('inf')
    best_node = 1

    for i in range(1, n + 1):
        total_cost = down[i] + up[i]
        if total_cost < min_cost:
            min_cost = total_cost
            best_node = i

    print(best_node)

solve()


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
