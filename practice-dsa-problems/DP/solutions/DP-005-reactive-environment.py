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
    p_factor = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        c = int(input_data[ptr])
        ptr += 1
        e = int(input_data[ptr])
        ptr += 1
        actions.append((c, e))
        
    e_max = 2000
    dp = [float("inf")] * (e_max + 1)
    dp[0] = 0
    
    for _ in range(n_steps):
        new_dp = [float("inf")] * (e_max + 1)
        for env in range(e_max + 1):
            if dp[env] == float("inf"):
                continue
            for c_i, e_i in actions:
                cost = c_i + p_factor * env
                new_env = min(e_max, env + e_i)
                new_dp[new_env] = min(new_dp[new_env], dp[env] + cost)
        dp = new_dp
        
    ans = min(dp)
    print(ans)


if __name__ == "__main__":
    solve()
