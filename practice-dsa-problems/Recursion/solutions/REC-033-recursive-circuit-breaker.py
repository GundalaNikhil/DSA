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
    f_limit = int(input_data[ptr])
    ptr += 1
    if f_limit == 0:
        print(0)
        return
    node_values = [0] * (n + 1)
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        val = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_values[i] = val
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    for u in adj:
        adj[u].sort()
        
    def traverse(u):
        my_successes = 1 if node_values[u] == 1 else 0
        my_failures = 1 if node_values[u] == 0 else 0
        
        # Check self
        if my_failures >= f_limit:
            return my_successes, my_failures, True
            
        for v_child in adj[u]:
            cs, cf, tripped = traverse(v_child)
            my_successes += cs
            my_failures += cf
            
            # Check cumulative failures
            if my_failures >= f_limit or tripped:
                return my_successes, my_failures, True
                
        return my_successes, my_failures, False

    if root != -1:
        s, _, _ = traverse(root)
        print(s)
    else:
        print(0)


if __name__ == "__main__":
    solve()
