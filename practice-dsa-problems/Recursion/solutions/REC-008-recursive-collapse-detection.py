import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    start_node = int(input_data[ptr])
    ptr += 1
    values = []
    values = []
    for _ in range(n):
        values.append(int(input_data[ptr]))
        ptr += 1
        
    adj = defaultdict(list)
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        
    for u in adj:
        adj[u].sort()
        
    on_stack = [False] * (n + 1)
    # memo = {} # Possible optimization? Code didn't have it, but "recursive collapse" sounds like cycle detection or similar.
    # The original function `get_sum` was:
    # if on_stack[u]: return 0 (cycle detection?)
    # total = values[u-1]
    # for v in adj[u]: total += get_sum(v)
    # return total
    # But it had `sys.setrecursionlimit` inside check?
    
    sys.setrecursionlimit(1000000)

    def get_sum(u):
        if on_stack[u]:
            return 0
        on_stack[u] = True
        total = values[u - 1]
        for v in adj[u]:
            total += get_sum(v)
        on_stack[u] = False
        return total

    try:
        print(get_sum(start_node))
    except RecursionError:
        print("0")


if __name__ == "__main__":
    solve()
