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
    bases = [0] * (n + 1)
    types = [0] * (n + 1)
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        b = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        bases[i] = b
        types[i] = t
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    def get_val(u):
        if not adj[u]:
            return bases[u]
        sum_children = 0
        for v in adj[u]:
            sum_children += get_val(v)
            
        if types[u] == 0:
            return bases[u] + sum_children
        else:
            return bases[u] - sum_children
            
    if root != -1:
        print(get_val(root))
    else:
        print(0)


if __name__ == "__main__":
    solve()
