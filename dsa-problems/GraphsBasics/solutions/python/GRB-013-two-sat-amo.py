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
        
    # SCC (Kosaraju)
    visited = [False] * (2 * N + 2)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(1, 2 * N + 1):
        if not visited[i]:
            dfs1(i)
            
    component = [-1] * (2 * N + 2)
    comp_count = 0
    
    def dfs2(u, c):
        component[u] = c
        for v in rev_adj[u]:
            if component[v] == -1:
                dfs2(v, c)
                
    for i in range(len(order) - 1, -1, -1):
        u = order[i]
        if component[u] == -1:
            dfs2(u, comp_count)
            comp_count += 1
            
    # Check
    result = []
    for i in range(1, n + 1):
        if component[i] == component[i + N]:
            return None
        result.append(1 if component[i] > component[i + N] else 0)
        
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
