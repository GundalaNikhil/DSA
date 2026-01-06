import sys
from collections import defaultdict
import deque


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
    nodes = n * m
    l_bounds = []
    u_bounds = []
    for _ in range(nodes):
        l_bounds.append(int(input_data[ptr]))
        u_bounds.append(int(input_data[ptr + 1]))
        ptr += 2
        
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    for _ in range(k):
        r1 = int(input_data[ptr]) - 1
        ptr += 1
        c1 = int(input_data[ptr]) - 1
        ptr += 1
        r2 = int(input_data[ptr]) - 1
        ptr += 1
        c2 = int(input_data[ptr]) - 1
        ptr += 1
        u, v = r1 * m + c1, r2 * m + c2
        adj[u].append(v)
        rev_adj[v].append(u)
        
    dfn = [-1] * nodes
    low = [-1] * nodes
    stack = []
    on_stack = [False] * nodes
    timer = 0
    scc = [-1] * nodes
    scc_count = 0
    
    sys.setrecursionlimit(nodes + 2000)

    def tarjan(u):
        nonlocal timer, scc_count
        dfn[u] = low[u] = timer
        timer += 1
        stack.append(u)
        on_stack[u] = True
        
        for v in adj[u]:
            if dfn[v] == -1:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], dfn[v])
                
        if low[u] == dfn[u]:
            while True:
                node = stack.pop()
                on_stack[node] = False
                scc[node] = scc_count
                if node == u:
                    break
            scc_count += 1

    for i in range(nodes):
        if dfn[i] == -1:
            tarjan(i)
            
    # Build SCC DAG
    scc_l = [-float("inf")] * scc_count
    scc_u = [float("inf")] * scc_count
    
    for i in range(nodes):
        sid = scc[i]
        scc_l[sid] = max(scc_l[sid], l_bounds[i])
        scc_u[sid] = min(scc_u[sid], u_bounds[i])
        
    scc_adj = defaultdict(set)
    in_degree = [0] * scc_count
    
    # Edges between SCCs
    for u in range(nodes):
        for v in adj[u]:
            if scc[u] != scc[v]:
                if scc[v] not in scc_adj[scc[u]]:
                    scc_adj[scc[u]].add(scc[v])
                    in_degree[scc[v]] += 1
                    
    # Topological Sort
    dq = deque([i for i in range(scc_count) if in_degree[i] == 0])
    topo_order = []
    
    while dq:
        u = dq.popleft()
        topo_order.append(u)
        
        # Propagate Lower Bounds forward (u <= v)
        for v in scc_adj[u]:
            scc_l[v] = max(scc_l[v], scc_l[u])
            in_degree[v] -= 1
            if in_degree[v] == 0:
                dq.append(v)
                
    if len(topo_order) < scc_count:
        # Cycle in SCC DAG? Impossible by definition.
        pass
        
    # Propagate Upper Bounds backward (v >= u => u <= v)
    for u in reversed(topo_order):
        for v in scc_adj[u]: # v is successor of u
             # Constraints: u <= v. So u is bounded by v's upper bound?
             # Yes: u <= v <= v_upper. So u_upper = min(u_upper, v_upper).
             scc_u[u] = min(scc_u[u], scc_u[v])
             
    # Final Check
    for i in range(scc_count):
        if scc_l[i] > scc_u[i]:
            print("IMPOSSIBLE")
            return
            
    print("POSSIBLE")
    for r in range(n):
        row = []
        for c in range(m):
            sid = scc[r * m + c]
            row.append(int(scc_l[sid])) # Use lower bound as solution
        print(*(row))


if __name__ == "__main__":
    solve()
