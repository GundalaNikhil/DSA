import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_count = int(input_data[ptr])
    ptr += 1
    r_count = int(input_data[ptr])
    ptr += 1
    s_start = int(input_data[ptr])
    ptr += 1
    rules = []
    adj = [[] for _ in range(n_count + 1)]
    all_rules = [[] for _ in range(n_count + 1)]
    for _ in range(r_count):
        head = int(input_data[ptr])
        ptr += 1
        ln = int(input_data[ptr])
        ptr += 1
        syms = []
        for _ in range(ln):
            s = input_data[ptr]
            ptr += 1
            syms.append(s)
            
        all_rules[head].append(syms)
        if syms and syms[0].startswith("#"):
            target = int(syms[0][1:])
            adj[head].append(target)
            
    visited = [0] * (n_count + 1)
    
    def has_cycle(u):
        visited[u] = 1 # Visiting
        for v in adj[u]:
            if visited[v] == 1:
                return True
            if visited[v] == 0:
                if has_cycle(v):
                    return True
        visited[u] = 2 # Visited
        return False
        
    # Check reachability from start
    reachable = [False] * (n_count + 1)
    q = [s_start]
    reachable[s_start] = True
    
    while q:
        u = q.pop()
        for v in adj[u]:
            if not reachable[v]:
                reachable[v] = True
                q.append(v)
                
    # Detect Left Recursion
    for i in range(1, n_count + 1):
        if reachable[i] and visited[i] == 0:
            if has_cycle(i):
                print("LEFT_RECURSION")
                return
                
    target_str = input_data[ptr] if ptr < len(input_data) else ""
    m = len(target_str)
    memo = {}
    
    sys.setrecursionlimit(300000)

    def parse(nt, pos):
        if (nt, pos) in memo:
            return memo[(nt, pos)]
            
        ends = set()
        for rule in all_rules[nt]:
            curr_positions = {pos}
            
            for sym in rule:
                next_positions = set()
                
                if sym.startswith("#"):
                    child_nt = int(sym[1:])
                    for p in curr_positions:
                        if p <= m:
                            child_ends = parse(child_nt, p)
                            for ce in child_ends:
                                next_positions.add(ce)
                else: # Terminal char
                    char = sym
                    for p in curr_positions:
                        if p < m and target_str[p] == char:
                            next_positions.add(p + 1)
                            
                curr_positions = next_positions
                if not curr_positions:
                    break
                    
            for p in curr_positions:
                ends.add(p)
                
        memo[(nt, pos)] = ends
        return ends

    final_positions = parse(s_start, 0)
    if m in final_positions:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
