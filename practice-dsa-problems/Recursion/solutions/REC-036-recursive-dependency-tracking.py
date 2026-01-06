import sys
from collections import defaultdict

sys.setrecursionlimit(500000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    s_start = int(input_data[ptr])
    ptr += 1
    base = []
    for _ in range(n):
        base.append(int(input_data[ptr]))
        ptr += 1
        
    adj = defaultdict(list)
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        
    state = [0] * (n + 1)
    memo = [0] * (n + 1)

    def get_val(u):
        if state[u] == 1:
            return None # Cycle detected
        if state[u] == 2:
            return memo[u]
            
        state[u] = 1
        total = base[u - 1]
        
        for v in adj[u]:
            res = get_val(v)
            if res is None:
                return None
            total += res
            
        state[u] = 2
        memo[u] = total
        return total

    ans = get_val(s_start)
    if ans is None:
        print("CYCLE")
    else:
        print(ans)


if __name__ == "__main__":
    solve()
