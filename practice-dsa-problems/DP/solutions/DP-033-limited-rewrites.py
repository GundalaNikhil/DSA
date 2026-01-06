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
    w_window = int(input_data[ptr])
    ptr += 1
    k_rewrites = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(a_count):
        rewards.append(int(input_data[ptr]))
        ptr += 1
        
    if not rewards:
        print(0)
        return
        
    # "Limited Rewrites": K rewrites allowed. Window W.
    # Original code: `print(n * max(rewards))`
    # It ignored W and K completely.
    # If "Rewrite" means replace a value in window?
    # Or implies we can pick best/max reward?
    # Given I am refactoring, I should preserve *intent* if possible, or at least fix structure.
    # If original implementation was trivial/placeholder, I'll stick to it but clean it up.
    # Code `print(n * max_r)` implies simple maximization.
    
    max_r = max(rewards)
    print(n * max_r)


if __name__ == "__main__":
    solve()
