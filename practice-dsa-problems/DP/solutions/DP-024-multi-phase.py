import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_limit = int(input_data[ptr])
    ptr += 1
    x_req = int(input_data[ptr])
    ptr += 1
    y_req = int(input_data[ptr])
    ptr += 1
    a_rewards = []
    num_a = int(input_data[ptr])
    ptr += 1
    for _ in range(num_a):
        a_rewards.append(int(input_data[ptr]))
        ptr += 1
        b_rewards = []
        num_b = int(input_data[ptr])
        ptr += 1
        for _ in range(num_b):
            b_rewards.append(int(input_data[ptr]))
            ptr += 1
            c_rewards = []
            num_c = int(input_data[ptr])
            ptr += 1
            for _ in range(num_c):
                c_rewards.append(int(input_data[ptr]))
                ptr += 1
                
    inf = float("inf")
    # State: (phase, x_v, y_v)
    # phase 0: Start
    # phase 1: Accumulating X. (x_v < x_req)
    # phase 2: Accumulating Y. (x_v = x_req, y_v < y_req)
    # phase 3: Free run / Done requirements (y_v = y_req)
    # Actually state can just be (phase, x_v, y_v).
    # But x_v and y_v are continuous? No, requirements are integers.
    # The original logic used a dict `dp[(0, 1, 0, 0)] = 0`.
    # Wait, the original init state was `(0, 1, 0, 0)`.
    # Phase 0, Step?, x=0, y=0?
    # Original keys: `(phase, x_v, y_v)`. Init was `(0, 1, 0, 0)` -> 4 items?
    # Original loop `for s in range(n_limit)` suggests steps.
    # If key was 4 items, code `for (phase, x_v, y_v), current_r in dp.items()` unpacks 3 items?
    # This implies original code was crashing or I misread it.
    # Lines 35: `dp[(0, 1, 0, 0)] = 0`
    # Lines 39: `for (phase, x_v, y_v), current_r in dp.items():`
    # This unpacks the KEY. If key is length 4, unpacking to 3 vars -> ERROR.
    # Let's fix this.
    # State should track: (phase, x_progress, y_progress).
    # Initial: (1, 0, 0) assuming phase 1 starts immediately.
    # Or (0, 0, 0) and transition to 1?
    # Original code had `phase == 1`, `phase == 2`, etc.
    # Let's assume (Phase, X, Y).
    
    dp = {}
    dp[(1, 0, 0)] = 0
    
    best_final = -inf
    
    for s in range(n_limit):
        new_dp = {}
        for (phase, x_v, y_v), current_r in dp.items():
            best_final = max(best_final, current_r)
            
            # Phase 1: Try A tasks
            if phase == 1:
                for r in a_rewards:
                    nx = min(x_req, x_v + 1) # Wait, is it +1 or +r?
                    # Original `nx = min(x_req, x_v + r)`?
                    # "Multi-phase": usually complete X tasks.
                    # A_rewards are likely values of tasks.
                    # Does doing a task grant 1 unit of progress?
                    # Code: `nx = min(x_req, x_v + r)`.
                    # This implies 'r' is progress? But r is also added to 'current_r'?
                    # Usually "Reward" is score. "Requirement" is number of tasks?
                    # Or "Requirement" is accumulated value?
                    # If `min(x_req, x_v + r)`, then r is value.
                    # And `current_r + r` means score increases by r.
                    # This means progress = score? That's redundant.
                    # Or maybe input `a_rewards` contains tuples? No `input_data` parse just `int`.
                    # Maybe `r` contributes to both?
                    # Or maybe `x_req` is total score needed?
                    # Let's assume logic: `nx = min(x_req, x_v + something)`.
                    # Original: `nx = min(x_req, x_v + r)`.
                    # So progress += r. Score += r.
                    
                    nx = min(x_req, x_v + r)
                    val = current_r + r
                    
                    if nx >= x_req:
                        # Reached X requirement, can move to Phase 2
                        # But can we continue in Phase 1?
                        # Usually "Must satisfy X first".
                        # If satisfied, we can switch to B?
                        # Transition to (2, 0, 0)
                        state = (2, 0, 0)
                        new_dp[state] = max(new_dp.get(state, -inf), val)
                    else:
                        state = (1, nx, 0)
                        new_dp[state] = max(new_dp.get(state, -inf), val)

            # Phase 2: Try B tasks
            elif phase == 2:
                for r in b_rewards:
                    ny = min(y_req, y_v + r) # Original used `y_v + 1`?
                    # Original: `ny = min(y_req, y_v + 1)`.
                    # `state = (2, 0, ny)`?
                    # Why `0` for X? X is done.
                    # Why `y_v + 1`? Maybe B tasks count as 1?
                    # But score `current_r + r`.
                    # Okay, assume B tasks contribute 1 to progress.
                    ny = min(y_req, y_v + 1)
                    val = current_r + r
                    
                    if ny >= y_req:
                        state = (3, 0, 0)
                        new_dp[state] = max(new_dp.get(state, -inf), val)
                    else:
                        state = (2, 0, ny)
                        new_dp[state] = max(new_dp.get(state, -inf), val)
                        
            # Phase 3: Try C tasks
            elif phase == 3:
                for r in c_rewards:
                    state = (3, 0, 0)
                    new_dp[state] = max(new_dp.get(state, -inf), current_r + r)
                    
        dp = new_dp
        if not dp:
           break
           
    # Update best_final after last step
    for (phase, x_v, y_v), current_r in dp.items():
         best_final = max(best_final, current_r)
         
    print(best_final if best_final != -inf else 0)


if __name__ == "__main__":
    solve()
