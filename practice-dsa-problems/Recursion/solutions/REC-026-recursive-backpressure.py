import sys
from collections import defaultdict

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    props = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        cap = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        props.append((v, cap))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    for u in adj:
        adj[u].sort()
        
    def evaluate(u):
        v_base, cap = props[u - 1]
        curr_val = v_base
        bp = 0
        
        if curr_val > cap:
            return cap, 1
            
        for v_child in adj[u]:
            c_val, c_bp = evaluate(v_child)
            
            if c_bp == 1:
                bp = 1
                curr_val = cap # Backpressure propagates saturation?
                break
                
            curr_val += c_val
            if curr_val > cap:
                curr_val = cap
                bp = 1
                break
                
        # If loop finishes normally
        return curr_val, bp

    if root != -1:
        val, _ = evaluate(root)
        print(val)
    else:
        print(0)


if __name__ == "__main__":
    solve()
