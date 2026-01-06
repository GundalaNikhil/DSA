import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_vars = int(input_data[ptr])
    ptr += 1
    r_regs = int(input_data[ptr])
    ptr += 1
    intervals = []
    for _ in range(n_vars):
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1

        intervals.append((l, r, c))
        
    intervals.sort()
    # Linear scan DP?
    # State: set of active intervals ending points?
    # If active set size < R, we can alloc. Else spill cost.
    # Code uses `dp` with keys `active_ends`.
    
    dp = {tuple(): 0}
    
    for l, r, c in intervals:
        new_dp = {}
        for active_ends, current_spill in dp.items():
            # Remove ends <= l (expired)
            remaining_ends = tuple(sorted([e for e in active_ends if e > l]))
            
            # Option 1: Spill this interval (cost c)
            cost_spill = current_spill + c
            if remaining_ends not in new_dp or new_dp[remaining_ends] > cost_spill:
                new_dp[remaining_ends] = cost_spill
                
            # Option 2: Alloc register (if available)
            if len(remaining_ends) < r_regs:
                with_new = tuple(sorted(list(remaining_ends) + [r]))
                if with_new not in new_dp or new_dp[with_new] > current_spill:
                    new_dp[with_new] = current_spill
                    
        dp = new_dp
        
    print(min(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
