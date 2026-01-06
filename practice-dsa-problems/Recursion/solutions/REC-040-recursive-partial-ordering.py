import sys
from collections import defaultdict
from itertools import permutations
sys.setrecursionlimit(500000)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    node_values = [0] * (n + 1)
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_values[i] = v
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    c_count = int(input_data[ptr])
    ptr += 1
    constraints = defaultdict(list)
    for _ in range(c_count):
        par = int(input_data[ptr])
        ptr += 1
        u_child = int(input_data[ptr])
        ptr += 1
        v_child = int(input_data[ptr])
        ptr += 1
        constraints[par].append((u_child, v_child))
        
    memo = {}

    def evaluate(u):
        if u in memo:
            return memo[u]
            
        children = adj[u]
        if not children:
            return node_values[u]
            
        c_vals = {}
        for c in children:
            res = evaluate(c)
            if res == "IMPOSSIBLE":
                memo[u] = "IMPOSSIBLE"
                return "IMPOSSIBLE"
            c_vals[c] = res
            
        local_constraints = constraints[u]
        best_child_sum = -float('inf')
        
        found_valid = False
        
        for p in permutations(children):
            is_valid = True
            pos = {node: i for i, node in enumerate(p)}
            
            for u_c, v_c in local_constraints:
                # If both constraint nodes are in our children list (usually assumed by problem)
                if u_c in pos and v_c in pos:
                    if pos[u_c] > pos[v_c]: # Violation: u must be before v but is after
                        is_valid = False
                        break
                        
            if is_valid:
                found_valid = True
                curr_sum = 0
                for i, node in enumerate(p):
                    # Index i is 0-based, maybe problem uses 1-based weights for ordering?
                    # "curr_sum += (i+1) * c_vals[node]" suggests index-based weighting.
                    curr_sum += (i + 1) * c_vals[node]
                best_child_sum = max(best_child_sum, curr_sum)
                
        if not found_valid:
            memo[u] = "IMPOSSIBLE"
            return "IMPOSSIBLE"
            
        res = node_values[u] + best_child_sum
        memo[u] = res
        return res

    if root != -1:
        ans = evaluate(root)
        print(ans if ans != "IMPOSSIBLE" else 0)
    else:
        print(0)
if __name__ == '__main__':
    solve()