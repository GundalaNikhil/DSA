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
    p_step = int(input_data[ptr])
    ptr += 1
    k_mult = int(input_data[ptr])
    ptr += 1
    values = [0] * (n + 1)
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        values[i] = v
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    def corrected_sum(u, depth):
        total = values[u]
        for v_child in adj[u]:
            total += corrected_sum(v_child, depth + 1)
            
        if depth % p_step == 0:
            low = (total // k_mult) * k_mult
            high = low + k_mult
            d_low = abs(total - low)
            d_high = abs(high - total)
            if d_low <= d_high:
                return low
            else:
                return high
                
        return total

    if root != -1:
        print(corrected_sum(root, 0))
    else:
        print(0)


if __name__ == "__main__":
    solve()
