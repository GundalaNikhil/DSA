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
    caps = []
    for _ in range(n):
        caps.append(int(input_data[ptr]))
        ptr += 1
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            adj[u].append(v)
            s = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            disc = [-1] * (n + 1)
            low = [-1] * (n + 1)
            stack = []
            on_stack = [False] * (n + 1)
            sccs = []
            scc_id = [-1] * (n + 1)
            timer = 0


def find_sccs(u):
    nonlocal timer
    disc[u] = low[u] = timer
    timer += 1
    stack.append(u)
    on_stack[u] = True
    for v in adj[u]:
        if disc[v] == -1:
            find_sccs(v)
            low[u] = min(low[u], low[v])
        elif on_stack[v]:
            low[u] = min(low[u], disc[v])
            if low[u] == disc[u]:
                new_scc = []
                while True:
                    node = stack.pop()
                    on_stack[node] = False
                    new_scc.append(node)
                    scc_id[node] = len(sccs)
                    if node == u:
                        break
                    sccs.append(new_scc)
                    for i in range(1, n + 1):
                        if disc[i] == -1:
                            find_sccs(i)
                            num_sccs = len(sccs)
                            scc_cap = [float("inf")] * num_sccs
                            for i in range(num_sccs):
                                for node in sccs[i]:
                                    scc_cap[i] = min(scc_cap[i], caps[node - 1])
                                    cond_adj = [set() for _ in range(num_sccs)]
                                    for u in range(1, n + 1):
                                        u_scc = scc_id[u]
                                        for v in adj[u]:
                                            v_scc = scc_id[v]
                                            if u_scc != v_scc:
                                                cond_adj[u_scc].add(v_scc)
                                                max_bottleneck = [-1] * num_sccs
                                                start_scc = scc_id[s]
                                                target_scc = scc_id[t]
                                                max_bottleneck[start_scc] = scc_cap[
                                                    start_scc
                                                ]
                                                for i in range(num_sccs - 1, -1, -1):
                                                    if max_bottleneck[i] == -1:
                                                        continue
                                                    for next_scc in cond_adj[i]:
                                                        potential = min(
                                                            max_bottleneck[i],
                                                            scc_cap[next_scc],
                                                        )
                                                        if (
                                                            potential
                                                            > max_bottleneck[next_scc]
                                                        ):
                                                            max_bottleneck[next_scc] = (
                                                                potential
                                                            )
                                                            if (
                                                                max_bottleneck[
                                                                    target_scc
                                                                ]
                                                                == -1
                                                            ):
                                                                print("0")
                                                            else:
                                                                print(
                                                                    max_bottleneck[
                                                                        target_scc
                                                                    ]
                                                                )
                                                                if (
                                                                    __name__
                                                                    == "__main__"
                                                                ):
                                                                    solve()
