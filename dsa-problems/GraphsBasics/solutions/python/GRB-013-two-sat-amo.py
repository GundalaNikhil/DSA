import sys

# Increase recursion depth
sys.setrecursionlimit(400000)

def solve_two_sat(n: int, clauses: list[tuple[int, int]], groups: list[list[int]]):
    total_group_size = sum(len(g) for g in groups)
    N = n + total_group_size
    
    adj = [[] for _ in range(2 * N + 2)]
    rev_adj = [[] for _ in range(2 * N + 2)]
    
    def add_edge(u, v):
        adj[u].append(v)
        rev_adj[v].append(u)
        
    def get_node(lit):
        if lit > 0: return lit
        return -lit + N
        
    def get_neg(lit):
        if lit > 0: return lit + N
        return -lit
        
    def add_implication(a, b):
        u, v = get_node(a), get_node(b)
        not_b, not_a = get_neg(b), get_neg(a)
        add_edge(u, v)
        add_edge(not_b, not_a)
        
    def add_clause(a, b):
        # a or b <=> -a -> b
        add_implication(-a, b)
        
    # Add Clauses
    for a, b in clauses:
        add_clause(a, b)
        
    # Add AMO
    current_aux = n + 1
    for group in groups:
        k = len(group)
        if k <= 1: continue
        
        for i in range(k):
            x = group[i]
            p = current_aux + i
            
            # x -> P_i
            add_implication(x, p)
            
            # P_i -> P_{i+1}
            if i < k - 1:
                add_implication(p, p + 1)
                
            # P_{i-1} -> -x
            if i > 0:
                add_implication(p - 1, -x)
                
        current_aux += k
        
    # Iterative Tarjan's Algorithm for SCC
    stack = []
    on_stack = [False] * (2 * N + 2)
    ids = [-1] * (2 * N + 2)
    low = [-1] * (2 * N + 2)
    scc_ids = [-1] * (2 * N + 2)
    
    timer = 0
    scc_count = 0
    
    # State for iterative DFS: (u, neighbor_idx)
    # We can simulate call stack
    
    work_stack = []
    
    for i in range(1, 2 * N + 1):
        if ids[i] == -1:
            work_stack.append((i, 0))
            
            while work_stack:
                u, idx = work_stack[-1]
                
                if idx == 0:
                    ids[u] = low[u] = timer
                    timer += 1
                    stack.append(u)
                    on_stack[u] = True
                    
                neighbors = adj[u]
                if idx < len(neighbors):
                    v = neighbors[idx]
                    work_stack[-1] = (u, idx + 1) # Advance index for return
                    
                    if ids[v] == -1:
                        work_stack.append((v, 0)) # Recurse
                    elif on_stack[v]:
                        low[u] = min(low[u], ids[v])
                else:
                    # Post-order
                    work_stack.pop()
                    if work_stack:
                        p, p_idx = work_stack[-1]
                        low[p] = min(low[p], low[u])
                        
                    if ids[u] == low[u]:
                        while True:
                            node = stack.pop()
                            on_stack[node] = False
                            scc_ids[node] = scc_count
                            if node == u: break
                        scc_count += 1
                        
    # Check 1..N
    for i in range(1, N + 1):
        if scc_ids[i] == scc_ids[i + N]:
            return None
            
    # Build assignment
    # Tarjan generates SCCs in reverse topological order
    # So if scc_id[x] < scc_id[!x], then !x matches an earlier SCC (closer to leaves / sink in DAG of SCCs? No)
    # Reverse Topological: First found SCC is a "sink" in SCC graph.
    # So scc_ids[sink] = 0. scc_ids[source] = High.
    # x -> !x. x is Source-like. !x Sink-like.
    # So scc_id[x] > scc_id[!x].
    # If x -> !x, we want x False.
    # If scc_id[x] > scc_id[!x] (Source > Sink), then x False.
    # Result = 1 if scc_id[x] < scc_id[!x].
    
    # Let's verify:
    # x -> !x. 
    # Tarjan finds !x (sink) first. ID=0.
    # x (source) found later. ID=1.
    # scc_id[x] = 1, scc_id[!x] = 0.
    # 1 > 0.
    # Condition: x must be False.
    # So if scc_id[x] > scc_id[!x] -> False (0).
    # Else True (1).
    
    result = []
    for i in range(1, n + 1):
        result.append(1 if scc_ids[i] < scc_ids[i + N] else 0)
        
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        clauses = []
        for _ in range(m):
            a = int(next(iterator))
            b = int(next(iterator))
            clauses.append((a, b))
            
        g = int(next(iterator))
        groups = []
        for _ in range(g):
            k = int(next(iterator))
            vars_list = [int(next(iterator)) for _ in range(k)]
            groups.append(vars_list)
            
        assign = solve_two_sat(n, clauses, groups)
        if assign is None:
            print("UNSAT")
        else:
            print("SAT")
            print(" ".join(map(str, assign)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
