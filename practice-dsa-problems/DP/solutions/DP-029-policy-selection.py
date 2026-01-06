import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    p_count = int(input_data[ptr])
    ptr += 1
    switch_cost = int(input_data[ptr])
    ptr += 1
    policies = []
    for _ in range(p_count):
        f = [int(x) for x in input_data[ptr : ptr + m - 1]]
        ptr += m - 1
        b = [int(x) for x in input_data[ptr : ptr + m - 1]]
        ptr += m - 1
        policies.append((f, b))
        policies.append((f, b))
        
    inf = float("inf")
    dp = [[[inf] * p_count for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Init
    for pol in range(p_count):
        dp[0][1][pol] = 0
        
    for move in range(n):
        for pos in range(1, m + 1):
            for pol in range(p_count):
                if dp[move][pos][pol] == inf:
                    continue
                    
                # Forward
                if pos < m:
                    c = policies[pol][0][pos - 1]
                    dp[move + 1][pos + 1][pol] = min(
                        dp[move + 1][pos + 1][pol],
                        dp[move][pos][pol] + c,
                    )
                    
                # Backward
                if pos > 1:
                    c = policies[pol][1][pos - 2]
                    dp[move + 1][pos - 1][pol] = min(
                        dp[move + 1][pos - 1][pol],
                        dp[move][pos][pol] + c,
                    )
                    
                # Switch Policy (stay in same pos, same move? or takes a move?)
                # Original code: `dp[move][pos][new_pol] = ...`
                # This updates current step. Dijkstra style propagation?
                # If switch cost exists, we can switch multiple times?
                # Usually policy switch happens instantly.
                # Code processed it inside `pos > 1` block? No.
                # It was indented weirdly in original.
                # Let's handle switching separately, or allow it at any time.
                # If we update `dp[move][pos]`, we should iterate again?
                # Or assume only 1 switch per step?
                # Let's perform a relaxation step for switching.
                pass
                
        # Relaxation for switching at state `move`
        # Since all positions processed, we can relax across policies.
        # But wait, original code did it inside `if pos > 1`.
        # That logic was likely flawed (only switch if moving back?).
        # I will apply switching relaxation at end of `move` (or beginning of `next`?).
        # Actually, if we switch, we are at `move`, `pos`, new `pol`.
        # We can then move from `move` to `move+1`.
        # So we should relax `dp[move]` BEFORE processing transitions to `move+1`.
        
    # Correct approach:
    # 1. Init dp[0]
    # 2. Loop moves 0 to n-1:
    #    a. Relax switching in dp[move]
    #    b. Transition to dp[move+1]
    
    # Re-writing loop structure
    dp = [[[inf] * p_count for _ in range(m + 1)] for _ in range(n + 1)]
    for pol in range(p_count):
        dp[0][1][pol] = 0
        
    for move in range(n + 1):
        # Relaxation (Bellman-Ford-ish or just simple pass since DAG of switch?)
        # If switch > 0, we can't cycle infinitely for gain.
        # Just simple pass or 2 passes if needed.
        for pos in range(1, m + 1):
            # Try switching FROM pol TO new_pol
            for pol in range(p_count):
                if dp[move][pos][pol] == inf: continue
                for new_pol in range(p_count):
                    if pol != new_pol:
                        dp[move][pos][new_pol] = min(dp[move][pos][new_pol], dp[move][pos][pol] + switch_cost)

        if move == n:
            break
            
        # Transitions
        for pos in range(1, m + 1):
             for pol in range(p_count):
                 if dp[move][pos][pol] == inf: continue
                 # Fwd
                 if pos < m:
                      c = policies[pol][0][pos - 1]
                      dp[move + 1][pos + 1][pol] = min(dp[move + 1][pos + 1][pol], dp[move][pos][pol] + c)
                 # Bwd
                 if pos > 1:
                      c = policies[pol][1][pos - 2]
                      dp[move + 1][pos - 1][pol] = min(dp[move + 1][pos - 1][pol], dp[move][pos][pol] + c)

    ans = min(dp[n][m])
    print(ans if ans != inf else -1)


if __name__ == "__main__":
    solve()
