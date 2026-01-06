import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        v = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        actions.append((v, r))
        
    inf = float("inf")
    dp = {}
    dp[(0, 0)] = 0
    # State: (current_sum, max_val_so_far)
    # Condition: max_val <= current_sum ??
    # `nmv = max(mv, v)`. `if nmv <= ns`.
    # Yes.
    
    for _ in range(n):
        new_dp = {}
        for (s, mv), reward in dp.items():
            for v, r in actions:
                ns = s + v
                nmv = max(mv, v)
                if nmv <= ns:
                    new_dp[(ns, nmv)] = max(new_dp.get((ns, nmv), -inf), reward + r)
        dp = new_dp
        if not dp:
            print("-1")
            return
            
    ans = -inf
    for r in dp.values():
        ans = max(ans, r)
        
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
