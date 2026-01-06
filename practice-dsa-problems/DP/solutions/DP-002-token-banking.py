import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    b_limit = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    p_count = int(input_data[ptr])
    ptr += 1
    normal_actions = []
    for _ in range(a_count):
        r = int(input_data[ptr])
        ptr += 1
        ptr += 1
        d = int(input_data[ptr])
        ptr += 1
        normal_actions.append((r, d))
        
    power_actions = []
    for _ in range(p_count):
        r = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1
        power_actions.append((r, c))

    # Initialize DP
    # dp[mask][bal] = max reward
    dp = [[-float("inf")] * (b_limit + 1) for _ in range(1 << p_count)]
    dp[0][b_limit] = 0
    
    for _ in range(n):
        new_dp = [[-float("inf")] * (b_limit + 1) for _ in range(1 << p_count)]
        for mask in range(1 << p_count):
            for bal in range(b_limit + 1):
                if dp[mask][bal] == -float("inf"):
                    continue
                    
                # Try all normal actions
                for r, d in normal_actions:
                    new_bal = bal + d
                    if 0 <= new_bal <= b_limit:
                        new_dp[mask][new_bal] = max(
                            new_dp[mask][new_bal], dp[mask][bal] + r
                        )
                        
                # Try all power actions (can only be used once per type globally? 
                # Problem name "Token Banking" suggests distinct power actions. 
                # Mask implies each used once.
                # Assuming can combine normal action with power action? 
                # Or power action is a separate move?
                # Usually mask DP implies one move per turn or accumulated state.
                # If code had nested loops, it might imply trying power action *after* normal action in same turn?
                # Original code structure:
                # Iterate normal actions -> update new_dp
                # Iterate power actions -> update new_dp based on ... wait.
                # The original code had power action logic deeply nested.
                # It looked like: for each normal action update, then check power actions?
                # Let's assume one normal action per turn.
                # AND potentially one power action (or multiple?)
                # If the original code was:
                # new_dp[mask][new_bal] = ... (normal)
                # for i in range(p_count): ... new_dp[new_mask][new_bal] = ...
                # It suggests power actions can be taken *instead* or *in addition*?
                # Let's assume standard transition: From state `dp`, one can reach `new_dp` via normal action.
                # Power actions often are "free" or "alternative".
                # Given mask, maybe one can use a power action to transition state?
                # Actually, typically "n steps", in each step you pick an action.
                # Let's stick to: One Normal Action per step.
                # AND potentially standard mask updates if they are instantaneous?
                # Or is a "Power Action" a type of step?
                # "Token Banking" - maybe spend tokens for power actions.
                # Input has normal actions (rate r, delta d) and power (rate r, cost c).
                # If original logic was `new_dp[new_mask][new_bal] = max(..., dp[mask][bal] + r)` 
                # it means from PREVIOUS state `dp`.
                # If it was based on `new_dp`, it would be chained.
                # Original code used `dp` source for both. 
                # So in one step, you can perform one Normal Action OR one Power Action (if unused).
                
                for i in range(p_count):
                    if not (mask & (1 << i)):
                        r, c = power_actions[i]
                        if bal >= c:
                            new_bal = bal - c
                            new_mask = mask | (1 << i)
                            new_dp[new_mask][new_bal] = max(
                                new_dp[new_mask][new_bal],
                                dp[mask][bal] + r,
                            )
        dp = new_dp

    ans = -float("inf")
    for m_dp in dp:
        ans = max(ans, max(m_dp))
    print(ans)


if __name__ == "__main__":
    solve()
