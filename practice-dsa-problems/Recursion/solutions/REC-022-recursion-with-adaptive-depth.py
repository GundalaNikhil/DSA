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
    l_init = int(input_data[ptr])
    ptr += 1
    node_props = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        delta = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        node_props.append((v, delta))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    def evaluate(u, limit):
        if limit < 0:
            return 0
            
        v_idx = u - 1
        # Correctly accessing 0-indexed props with 1-indexed u
        # Since loop ran 1 to n+1 and appended.
        v = node_props[v_idx][0]
        delta = node_props[v_idx][1]
        
        res = v
        for v_child in adj[u]:
            res += evaluate(v_child, limit + delta)
        return res

    if root != -1:
        print(evaluate(root, l_init))
    else:
        print(0)


if __name__ == "__main__":
    solve()
