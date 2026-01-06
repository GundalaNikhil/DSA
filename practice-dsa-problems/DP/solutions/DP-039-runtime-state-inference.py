import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_modes = int(input_data[ptr])
    ptr += 1
    a_actions = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(n):
        row = []
        for _ in range(s_modes):
            row.append(int(input_data[ptr]))
            ptr += 1
            rewards.append(row)
            reveal_table = []
        reveal_table.append(row)
        
    ans = 0
    for i in range(n):
        best_step = -float("inf")
        # For step i, we see 'a_actions' columns in 'reveal_table'.
        # For each action k, it reveals a mode index: `mode = reveal_table[i][k]`.
        # Reward is `rewards[i][mode]`.
        # Problem "Runtime State Inference": maybe we choose k to maximize revealed reward?
        # Code: `best_step = max(best_step, rewards[i][mode])`.
        # `ans += best_step`.
        
        for k in range(a_actions):
            mode = reveal_table[i][k]
            best_step = max(best_step, rewards[i][mode])
            
        ans += best_step
        
    print(ans)


if __name__ == "__main__":
    solve()
