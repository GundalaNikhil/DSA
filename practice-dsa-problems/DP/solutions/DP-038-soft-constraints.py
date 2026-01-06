import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_steps = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    c_count = int(input_data[ptr])
    ptr += 1
    p_penalty = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(a_count):
        rewards.append(int(input_data[ptr]))
        ptr += 1
        constraints = [[] for _ in range(a_count)]
        for _ in range(c_count):
            aid = int(input_data[ptr]) - 1
            limit = int(input_data[ptr])
            ptr += 1
            constraints[aid].append(limit)
            
    # Precalculate costs for each action A taking K steps
    # Original logic: `costs[i][k] = k * rewards[i] - penalty_sum`.
    costs = [[0] * (n_steps + 1) for _ in range(a_count)]
    for i in range(a_count):
        for k in range(n_steps + 1):
            penalty_sum = 0
            for limit in constraints[i]:
                # Penalty if we exceed 'limit' for this action?
                # "Soft Constraints": limit might be max steps allowed?
                # Original: `max(0, k - limit) * p_penalty`.
                penalty_sum += max(0, k - limit) * p_penalty
            costs[i][k] = k * rewards[i] - penalty_sum
            
    # DP: Allocate total N steps among actions
    dp = [-float("inf")] * (n_steps + 1)
    dp[0] = 0
    
    for i in range(a_count):
        new_dp = [-float("inf")] * (n_steps + 1)
        for s in range(n_steps + 1):
            if dp[s] == -float("inf"):
                continue
            # Try allocating k steps to action i
            # Remaining budget: n_steps - s.
            for k in range(n_steps - s + 1):
                new_dp[s + k] = max(
                    new_dp[s + k], dp[s] + costs[i][k]
                )
        dp = new_dp
        
    print(dp[n_steps])


if __name__ == "__main__":
    solve()
