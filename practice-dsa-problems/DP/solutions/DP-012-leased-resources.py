import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    r_types = int(input_data[ptr])
    ptr += 1
    l_limit = int(input_data[ptr])
    ptr += 1
    costs = []
    for _ in range(r_types):
        costs.append(int(input_data[ptr]))
        ptr += 1
        t_types = int(input_data[ptr])
        ptr += 1
        tasks = []
        for _ in range(t_types):
            tasks.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
        
    memo = {}
    print(get_max_reward(0, tuple([0] * r_types), n, r_types, l_limit, costs, tasks, memo))


def get_max_reward(day, timers, n, r_types, l_limit, costs, tasks, memo):
    if day == n:
        return 0
    state = (day, timers)
    if state in memo:
        return memo[state]
        
    # Option 1: Do nothing (or just time pass) - wait, is "no task" an option?
    # Code: `res = get_max_reward(day + 1, new_timers)`
    new_timers_idle = tuple(max(0, t - 1) for t in timers)
    res = get_max_reward(day + 1, new_timers_idle, n, r_types, l_limit, costs, tasks, memo)
    
    for val, mask in tasks:
        curr_reward = val
        next_timers = list(timers)
        possible = True
        cost_for_task = 0
        
        # Calculate cost/feasibility
        # Code loop:
        # for j in r_types: if mask has j: if timers[j] == 0: cost+=costs[j], next=l_limit. else: next=timers-1.
        # Wait, the checking logic in original code was nested/broken. 
        # `next_timers[j] = max(0, timers[j] - 1)` was in else.
        # But if we use resource j, does timer reset?
        # "Leased Resources": usually pay cost to lease for L days.
        # If timer > 0, we have it. If timer == 0, we pay cost and get it for L days.
        
        temp_timers = list(timers)
        current_step_cost = 0
        
        for j in range(r_types):
            if (mask >> j) & 1:
                if temp_timers[j] == 0:
                    current_step_cost += costs[j]
                    temp_timers[j] = l_limit
                # If timer > 0, we use it. Does it consume it? 
                # "Leased" usually means time-based expiry, not consumption.
                # So we just verify we have it.
                # But we move to next day. so all timers decrement.
            
            # Decrement happens for next day.
            
        # Prepare next day timers
        next_day_timers = []
        for j in range(r_types):
            if (mask >> j) & 1:
                # We used it. If we bought it, it is L_limit.
                # If we had it, is it L_limit or just decrement?
                # Usually lease is "Unlock for X days".
                # If we bought, `temp_timers[j]` became `l_limit`.
                # If we had it, `temp_timers[j]` was `>0`.
                pass
            
            # Everyone decrements at end of day
            t = temp_timers[j]
            next_day_timers.append(max(0, t - 1))
            
        res = max(res, val - current_step_cost + get_max_reward(day + 1, tuple(next_day_timers), n, r_types, l_limit, costs, tasks, memo))
        
    memo[state] = res
    return res


if __name__ == "__main__":
    solve()
