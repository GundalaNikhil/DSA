import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    ok_flags = [0] * (n + 1)
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        ok = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        ok_flags[i] = ok
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    for u in adj:
        adj[u].sort()
        
    curr = root
    while True:
        if ok_flags[curr] == 0:
            print("NO")
            return
            
        if not adj[curr]:
            print("YES")
            return
            
        # Greedy choice: pick first child?
        curr = adj[curr][0]


if __name__ == "__main__":
    solve()
