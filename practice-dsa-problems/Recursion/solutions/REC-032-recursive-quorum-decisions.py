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
    node_data = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        q = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_data.append((q, v))
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    def decide(u):
        q, v = node_data[u - 1]
        
        if not adj[u]:
            return v
            
        success_count = 0
        for v_child in adj[u]:
            if decide(v_child) == 1:
                success_count += 1
                
        return 1 if success_count >= q else 0

    if root != -1:
        print(decide(root))
    else:
        print(0)


if __name__ == "__main__":
    solve()
