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
        actions.append((int(input_data[ptr]),
        int(input_data[ptr + 1]),
        int(input_data[ptr + 2])))
        ptr += 3
        
    memo = {}
    print(get_max_score(1, tuple([0] * 5), n, actions, memo))


def get_max_score(step, pending_penalties, n, actions, memo):
    if step == n + 1:
        return 0
    state = (step, pending_penalties)
    if state in memo:
        return memo[state]
        
    curr_p = pending_penalties[0]
    # Shift penalties: next_base is penalties for step+1, step+2...
    next_base = list(pending_penalties[1:]) + [0]
    
    # Option 1: Do nothing (just pay penalty)
    res = -curr_p + get_max_score(step + 1, tuple(next_base), n, actions, memo)
    
    # Option 2: Pick an action
    for r, d, p in actions:
        if step + d <= n:
            # Action valid duration
            # Penalty starts after d steps? Or for d steps?
            # "Deferred Consequences" usually means you pay later.
            # Code: `if d > 0: temp_p[d-1] += p`
            # `temp_p` is `next_base`. 
            # `next_base[0]` corresponds to `step+1`.
            # `next_base[d-1]` corresponds to `step+1 + (d-1) = step+d`.
            # So penalty `p` is added at `step+d`.
            
            temp_p = list(next_base)
            if d > 0:
                # Logic check: pending_penalties length is 5 (shifted 0s).
                # If d-1 < 5.
                if d - 1 < 5:
                    temp_p[d - 1] += p
            
            res = max(res, r - curr_p + get_max_score(step + 1, tuple(temp_p), n, actions, memo))
            
    memo[state] = res
    return res
if __name__ == '__main__':
    solve()