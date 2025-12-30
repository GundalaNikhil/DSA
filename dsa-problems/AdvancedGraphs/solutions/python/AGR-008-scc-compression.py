import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def scc_compress(n: int, adj: list[list[int]]):
    tin = [-1] * n
    low = [-1] * n
    on_stack = [False] * n
    stack = []
    timer = 0
    sccs = []

    def dfs(u):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if tin[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], tin[v])

        if low[u] == tin[u]:
            component = []
            while True:
                v = stack.pop()
                on_stack[v] = False
                component.append(v)
                if u == v:
                    break
            sccs.append(component)

    for i in range(n):
        if tin[i] == -1:
            dfs(i)

    k = len(sccs)
    comp = [0] * n
    # Tarjan finds SCCs in reverse topological order
    # Assign IDs 0 to k-1 based on discovery order (sccs list order)
    for i, component in enumerate(sccs):
        for node in component:
            comp[node] = i

    dag_edges = set()
    for u in range(n):
        for v in adj[u]:
            if comp[u] != comp[v]:
                dag_edges.add((comp[u], comp[v]))

    return k, comp, sorted(list(dag_edges))

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)

        k, comp, edges = scc_compress(n, adj)

        out = [str(k), " ".join(map(str, comp)), str(len(edges))]
        for u, v in edges:
            out.append(f"{u} {v}")

        sys.stdout.write("\n".join(out).strip())
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
