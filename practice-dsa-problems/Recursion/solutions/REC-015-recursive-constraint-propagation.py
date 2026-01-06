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
    l0 = int(input_data[ptr])
    ptr += 1
    r0 = int(input_data[ptr])
    ptr += 1
    values = [0] * (n + 1)
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        values[i] = v
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    is_valid = True

    def check(u, l, r):
        nonlocal is_valid
        if not is_valid:
            return
            
        if l > r:
            is_valid = False
            return
            
        v = values[u]
        # Check constraint? Original code didn't check v vs [l, r], just propagated adjusted bounds.
        # Assuming v must be within [l, r] implicitly or just modifies bounds.
        # Original: nl = l + v, nr = r - v.
        
        nl = l + v
        nr = r - v
        
        for v_child in adj[u]:
            check(v_child, nl, nr)
            if not is_valid:
                return
                
    if root != -1:
        check(root, l0, r0)
        if is_valid:
            print("YES")
        else:
            print("NO")
    else:
        # Empty tree is valid?
        print("YES")


if __name__ == "__main__":
    solve()
