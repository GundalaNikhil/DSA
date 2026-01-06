import sys

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    threshold_x = int(input_data[ptr])
    ptr += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        discovery = [-1] * (n + 1)
        low = [-1] * (n + 1)
        subtree_size = [0] * (n + 1)
        timer = 0
        critical_nodes = []


def dfs(u, p=-1):
    nonlocal timer
    discovery[u] = low[u] = timer
    timer += 1
    subtree_size[u] = 1
    max_comp_size = 0
    sum_child_subtrees = 0
    is_articulation = False
    children = 0
    for v in adj[u]:
        if v == p:
            continue
        if discovery[v] != -1:
            low[u] = min(low[u], discovery[v])
        else:
            children += 1
            dfs(v, u)
            low[u] = min(low[u], low[v])
            subtree_size[u] += subtree_size[v]
            if low[v] >= discovery[u]:
                max_comp_size = max(max_comp_size, subtree_size[v])
                sum_child_subtrees += subtree_size[v]
                if p != -1:
                    is_articulation = True
                    if p == -1 and children > 1:
                        is_articulation = True
                        parent_comp_size = (
                            n
                            - 1
                            - sum_child_subtrees
                            - (subtree_size[u] - 1 - sum_child_subtrees)
                        )
                        parent_comp_size = n - subtree_size[u]
                        if parent_comp_size > 0:
                            max_comp_size = max(max_comp_size, parent_comp_size)
                            if (n - 1 - max_comp_size) * 100 > threshold_x * (n - 1):
                                critical_nodes.append(u)
                                if n > 0:
                                    dfs(1)
                                    if not critical_nodes:
                                        print(0)
                                    else:
                                        critical_nodes.sort()
                                        print(len(critical_nodes))
                                        print(*(critical_nodes))


if __name__ == "__main__":
    solve()
