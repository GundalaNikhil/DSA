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
    m_limit = int(input_data[ptr])
    ptr += 1
    p_switch = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        base = int(input_data[ptr])
        ptr += 1
        bonus = int(input_data[ptr])
        ptr += 1
        actions.append((base, bonus))
        
    # dp[(last_action_idx, current_streak)] = max_reward
    dp = {}
    
    # Init step 0 (implicit first choice) or is "n" steps start from 0?
    # Usually choose 1st action.
    # Base case: Just started.
    for i in range(a_count):
        # Action i, streak 1
        dp[(i, 1)] = actions[i][0] + actions[i][1] * 1 
        # Wait, if formula is base + bonus * streak, 
        # for streak 1 is it base + bonus? or base + bonus*1?
        # Code used `actions[i][0]`. Logic: `base`.
        # Code later used `base + bonus * new_streak`.
        # If "streak" means consecutive usage count INCLUDING current.
        # Let's trust logic: for first time, streak is 1.
        # Original code: `new_dp[(i, 1)] = actions[i][0]` (line 29)
        # So first use gets NO bonus? Or bonus * 0?
        # Line 35: `r = base + bonus * new_streak`.
        # Line 29 used just `actions[i][0]`.
        # I'll stick to original behavior but clean up structure.
        pass

    # Actually the loop structure suggests we do N steps.
    # The first step we just pick an action.
    # Code had `if not dp: ... else ...` inside the loop.
    # So first iteration initializes.
    
    for step in range(n):
        new_dp = {}
        if step == 0:
            for i in range(a_count):
                new_dp[(i, 1)] = actions[i][0] 
        else:
            for (last_a, streak), reward in dp.items():
                for i in range(a_count):
                    # Continue streak
                    if i == last_a:
                        new_streak = min(m_limit, streak + 1)
                        r = actions[i][0] + actions[i][1] * new_streak
                        state = (i, new_streak)
                        new_dp[state] = max(new_dp.get(state, -float("inf")), reward + r)
                    else:
                        # Switch
                        new_streak = 1
                        # Penalty applies on switch?
                        # Original: `r = base + bonus * 1 - p_switch`
                        # Wait, original for switch used `actions[i][0] + actions[i][1] * new_streak - p_switch`
                        # But for init (line 29) it used `actions[i][0]`.
                        # This implies logic: First use: Base. 2nd use: Base + Bonus*2.
                        # BUT line 43-45 adds bonus * 1.
                        # This contradicts line 29.
                        # I will assume:
                        # 1. Streak 1 => Base + Bonus * 1 (maybe?)
                        # 2. Or Streak 1 => Base.
                        # DP-006 "DP with Momentum".
                        # Usually momentum implies growing reward.
                        # If I preserve original logic:
                        #  Init: Base.
                        #  Switch: Base + Bonus*1 - Penalty.
                        #  Continue: Base + Bonus*Streak.
                        # This is inconsistent. Why does switching give Bonus*1 but starting doesn't?
                        # Maybe `actions[i][1]` is negative? Or specific?
                        # I'll keep accurate to code:
                        #  Switch: `r = actions[i][0] + actions[i][1] * 1 - p_switch`
                        r = actions[i][0] + actions[i][1] - p_switch
                        state = (i, 1)
                        new_dp[state] = max(new_dp.get(state, -float("inf")), reward + r)
        dp = new_dp
        
    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
