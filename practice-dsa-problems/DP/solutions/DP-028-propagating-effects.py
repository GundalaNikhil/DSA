import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_limit = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        actions.append(
            (
                int(input_data[ptr]),
                int(input_data[ptr + 1]),
                int(input_data[ptr + 2]),
            )
        )
        ptr += 3
        ptr += 3
        
    memo = {}
    print(get_max_reward(0, (), 0, n_limit, actions, memo))


def get_max_reward(step, timers, total_e, n_limit, actions, memo):
    if step == n_limit:
        return 0
    state = (step, timers) # total_e not in state? 
    # Original code: `state = (step, timers)`. `total_e` passed as arg but not key.
    # Wait, `curr_reward = r + total_e`. `total_e` affects result.
    # If `total_e` varies for same `(step, timers)`, memo is invalid.
    # `total_e` comes from `next_total_e` which sums `t_e` from timers.
    # So `total_e` is determined by timers? 
    # `next_total_e` calculated from `new_timers`.
    # Yes, `total_e` is derived from CURRENT timers in caller?
    # Function arg `total_e` seems redundant if timers contain it.
    # `timers` is list of `(t_d, t_e)`.
    # `next_total_e += t_e`.
    # So yes, derived. Safe to memoize on `timers`.
    
    if state in memo:
        return memo[state]
        
    res = -float("inf")
    for r, e, d in actions:
        # Current Reward depends on total active effects (total_e)
        curr_reward = r + total_e
        
        new_timers = []
        next_step_e = 0
        
        # Advance timers
        for t_d, t_e in timers:
            if t_d > 1:
                new_timers.append((t_d - 1, t_e))
                next_step_e += t_e
                
        # Add new effect if d > 0
        if d > 0:
            new_timers.append((d, e))
            next_step_e += e
            
        res = max(
            res,
            curr_reward
            + get_max_reward(
                step + 1, tuple(sorted(new_timers)), next_step_e, n_limit, actions, memo
            ),
        )
        
    memo[state] = res
    return res


if __name__ == "__main__":
    solve()
