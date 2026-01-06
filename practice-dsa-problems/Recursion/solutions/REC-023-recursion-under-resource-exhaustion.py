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
    b_limit = int(input_data[ptr])
    ptr += 1
    node_props = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        val = int(input_data[ptr])
        ptr += 1
        mem = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        node_props.append((val, mem))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    max_path_sum = 0
    found_any = False

    def dfs(u, curr_sum, curr_mem):
        nonlocal max_path_sum, found_any
        val, mem = node_props[u - 1]
        new_mem = curr_mem + mem
        
        if new_mem > b_limit:
            return
            
        new_sum = curr_sum + val
        
        # If leaf or just process node?
        # Usually path means root to some node.
        # Check if valid path so far.
        if not found_any or new_sum > max_path_sum:
            max_path_sum = new_sum
            found_any = True
            
        for v in adj[u]:
            dfs(v, new_sum, new_mem)
            
    if root != -1:
        dfs(root, 0, 0)
        print(max_path_sum if found_any else 0)
    else:
        print(0)


if __name__ == "__main__":
    solve()
