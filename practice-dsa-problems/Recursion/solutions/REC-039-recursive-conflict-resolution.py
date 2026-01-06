import sys
from collections import defaultdict

sys.setrecursionlimit(500000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    node_props = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_props.append((v, p))
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    def resolve(u):
        v_own, p_own = node_props[u - 1]
        best_p = p_own
        best_v = v_own
        best_idx = u
        
        for v_child in adj[u]:
            cp, cv, cidx = resolve(v_child)
            
            if cp > best_p:
                best_p, best_v, best_idx = cp, cv, cidx
            elif cp == best_p:
                if cidx < best_idx: # Tie-break by index
                    best_idx, best_v = cidx, cv
                    
        return best_p, best_v, best_idx

    if root != -1:
        _, res_v, _ = resolve(root)
        print(res_v)
    else:
        print(0)


if __name__ == "__main__":
    solve()
