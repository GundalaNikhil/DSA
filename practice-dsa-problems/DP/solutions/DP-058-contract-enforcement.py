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
    d_window = int(input_data[ptr])
    ptr += 1
    p_penalty = int(input_data[ptr])
    ptr += 1
    actions = []
    for i in range(a_count):
        r = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1

        actions.append((r, c))
        
    dp = {}
    dp[tuple()] = 0
    
    for step in range(n):
        new_dp = {}
        for contracts, current_score in dp.items():
            for i, (rew, creates) in enumerate(actions):
                my_contracts = [c for c in contracts if c[0] == i]
                other_contracts = [c for c in contracts if c[0] != i]
                
                if my_contracts:
                    # Satisfy oldest contract first?
                    my_contracts.sort()
                    # We satisfy first one (popped), others remain.
                    fulfilled_contracts = my_contracts[1:] + other_contracts
                else:
                    fulfilled_contracts = list(contracts)
                    
                aged_contracts = []
                penalty_this_step = 0
                
                for cid, rem in fulfilled_contracts:
                    if rem == 1:
                        penalty_this_step += p_penalty
                    else:
                        aged_contracts.append((cid, rem - 1))
                        
                if creates == 1:
                    aged_contracts.append((i, d_window))
                    
                state = tuple(sorted(aged_contracts))
                score = current_score + rew - penalty_this_step
                
                if state not in new_dp or new_dp[state] < score:
                    new_dp[state] = score
        dp = new_dp
        
    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
