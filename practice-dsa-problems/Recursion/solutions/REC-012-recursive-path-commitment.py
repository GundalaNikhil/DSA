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
    l_limit = int(input_data[ptr])
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
            
    max_sum = -float("inf")
    found = False

    def dfs(u, current_sum, length):
        nonlocal max_sum, found
        current_sum += values[u]
        
        if not adj[u]:
             # Leaf node logic? Or path exact length?
             # Problem statement implies exact length l_limit check
            if length == l_limit:
                max_sum = max(max_sum, current_sum)
                found = True
            return
            
        if length >= l_limit:
            return
            
        for v in adj[u]:
            dfs(v, current_sum, length + 1)
            
    if root != -1:
        dfs(root, 0, 1)
        if found:
            print(max_sum)
        else:
            print("-1")
    else:
        print("-1")


if __name__ == "__main__":
    solve()
