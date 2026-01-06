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
    budget = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(a_count):
        rewards.append(int(input_data[ptr]))
        ptr += 1
        
    if not rewards:
        print(0)
        return
        
    max_r = max(rewards)
    # Opportunity Cost = Max Possible - Actual
    # If we always pick max, Cost is 0?
    # Original logic just printed `n * max_r`.
    # Maybe problem is: "What is max total reward?"
    # If we have budget, and actions have cost?
    # Variable `budget` was read but unused.
    # Code `costs = [max_r - r for r in rewards]` computed but unused.
    # Original printed `n * max_r` TWICE?
    # I will assume simple greedy max reward.
    print(n * max_r)


if __name__ == "__main__":
    solve()
