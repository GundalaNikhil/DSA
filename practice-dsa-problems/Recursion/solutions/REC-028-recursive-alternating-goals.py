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
            
    def evaluate(u, depth):
        if not adj[u]:
            return values[u]
            
        res_list = []
        for v_child in adj[u]:
            res_list.append(evaluate(v_child, depth + 1))
            
        if depth % 2 == 0:
            return max(res_list)
        else:
            return min(res_list)

    if root != -1:
        print(evaluate(root, 0))
    else:
        print(0)


if __name__ == "__main__":
    solve()
