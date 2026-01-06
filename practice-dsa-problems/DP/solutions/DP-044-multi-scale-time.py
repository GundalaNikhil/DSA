import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_block = int(input_data[ptr])
    ptr += 1
    s_count = int(input_data[ptr])
    ptr += 1
    f_count = int(input_data[ptr])
    ptr += 1
    multipliers = []
    for _ in range(s_count):
        multipliers.append(int(input_data[ptr]))
        ptr += 1
        rewards = []
        for _ in range(f_count):
            rewards.append(int(input_data[ptr]))
            ptr += 1
            
    num_blocks = n // k_block
    block_reward = get_best_block_reward(multipliers, rewards, k_block)
    print(num_blocks * block_reward)


def get_best_block_reward(multipliers, rewards, k_block):
    best_block = -float("inf")
    for m in multipliers:
        best_action_val = -float("inf")
        for r in rewards:
            best_action_val = max(best_action_val, m * r)
        best_block = max(best_block, k_block * best_action_val)
    return best_block


if __name__ == "__main__":
    solve()
