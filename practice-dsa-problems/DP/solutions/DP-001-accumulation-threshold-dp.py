import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        a_base = int(next(iterator))
        u_unlock = int(next(iterator))
        
        thresholds = []
        for _ in range(m):
            thresholds.append(int(next(iterator)))
            
        base_actions = []
        for _ in range(a_base):
            r = int(next(iterator))
            gains = []
            for _ in range(m):
                gains.append(int(next(iterator)))
            base_actions.append((r, gains))
            
        unlocked_actions = []
        for _ in range(u_unlock):
            meter_idx = int(next(iterator)) - 1
            r = int(next(iterator))
            gains = []
            for _ in range(m):
                gains.append(int(next(iterator)))
            unlocked_actions.append((meter_idx, r, gains))
            
    except StopIteration:
        return

    # DP State: tuple of meter values -> max reward
    # Start: (0, 0, ...) -> 0
    
    dp = {tuple([0] * m): 0}
    
    for step in range(n):
        new_dp = {}
        # Iterate over all reachable states
        for states, current_reward in dp.items():
            
            # 1. Apply Base Actions
            for r_val, gains in base_actions:
                new_states = list(states)
                for i in range(m):
                    # Meters cap at thresholds[i]
                    new_states[i] = min(thresholds[i], new_states[i] + gains[i])
                
                ns_tuple = tuple(new_states)
                new_dp[ns_tuple] = max(new_dp.get(ns_tuple, -float("inf")), current_reward + r_val)
                
            # 2. Apply Unlocked Actions (if condition met)
            for meter_idx, r_val, gains in unlocked_actions:
                # unlocking condition: meter[meter_idx] >= threshold[meter_idx]
                if states[meter_idx] >= thresholds[meter_idx]:
                    new_states = list(states)
                    for i in range(m):
                         new_states[i] = min(thresholds[i], new_states[i] + gains[i])
                    
                    ns_tuple = tuple(new_states)
                    new_dp[ns_tuple] = max(new_dp.get(ns_tuple, -float("inf")), current_reward + r_val)
        
        dp = new_dp
        if not dp:
            # No valid moves? (Should not happen if base actions always exist or valid)
            # If dp is empty, we break or return 0?
            break
            
    if not dp:
        print(0)
    else:
        print(max(dp.values()))

if __name__ == "__main__":
    solve()


if __name__ == "__main__":
    solve()
