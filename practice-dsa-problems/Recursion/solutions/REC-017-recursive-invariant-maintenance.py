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
            
    valid = True

    def dfs(u):
        nonlocal valid
        if not valid:
            return 0
            
        current_subsum = values[u]
        for v in adj[u]:
            current_subsum += dfs(v)
            
        # Invariant: Subtree sum >= node value?
        # Original: if current_subsum < values[u]: valid = False
        if current_subsum < values[u]:
            valid = False
            
        return current_subsum

    if root != -1:
        dfs(root)
        if valid:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    solve()
