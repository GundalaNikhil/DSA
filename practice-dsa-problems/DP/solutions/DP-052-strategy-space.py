import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_len = int(input_data[ptr])
    ptr += 1
    s_strategies = int(input_data[ptr])
    ptr += 1
    c_switch = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(s_strategies):
        rewards.append(int(input_data[ptr]))
        ptr += 1
        
    num_blocks = n // k_len
    if num_blocks == 0:
        print(0)
        return
        
    inf = float("inf")
    dp = [[-inf] * s_strategies for _ in range(num_blocks)]
    
    # Init first block
    for s in range(s_strategies):
        dp[0][s] = rewards[s]
        
    for b in range(1, num_blocks):
        prev_max = max(dp[b - 1])
        for s in range(s_strategies):
            # Option 1: Stay in strategy s
            val_stay = dp[b - 1][s] + rewards[s]
            # Option 2: Switch to strategy s from any best previous (PAY COST)
            val_switch = prev_max - c_switch + rewards[s]
            
            dp[b][s] = max(val_stay, val_switch)
            
    print(max(dp[num_blocks - 1]))


if __name__ == "__main__":
    solve()
