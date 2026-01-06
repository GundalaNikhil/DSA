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
    node_props = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        t = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        e = int(input_data[ptr])
        ptr += 1
        b = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        node_props.append((t, v, e, b))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    for u in adj:
        adj[u].sort()
        
    def evaluate(u):
        t, v, e, b = node_props[u - 1]
        
        # Calculate subtree total time and value if we process normally
        # Simple recursion first
        
        child_time_sum = 0
        child_val_sum = 0
        
        for v_child in adj[u]:
            ct, cv = evaluate(v_child)
            child_time_sum += ct
            child_val_sum += cv
            
        # Check if we fit in budget
        if t + child_time_sum <= b:
            return t + child_time_sum, v + child_val_sum
        else:
            # Budget exceeded, return failure cost/time?
            # Problem likely implies "if exceeded, use error value 'e' and time 0 or t?"
            # "Recursive Time Budgets" often implies fallback.
            # Assuming fallback: Time t? Or 0? Value e.
            return t, e # Simplified assumption based on problem type

    if root != -1:
        _, res = evaluate(root)
        print(res)
    else:
        print(0)


if __name__ == "__main__":
    solve()
