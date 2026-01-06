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
    u_limit = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        c = int(input_data[ptr])
        ptr += 1
        inc = int(input_data[ptr])
        ptr += 1
        dec = int(input_data[ptr])
        ptr += 1
        actions.append((c, inc, dec))

    dp = {tuple([0] * a_count): 0}
    
    for step in range(n):
        new_dp = {}
        for levels, total_cost in dp.items():
            # Choose action i
            for i in range(a_count):
                c_i, inc_i, dec_i = actions[i]
                cost = c_i + inc_i * levels[i]
                
                new_levels = list(levels)
                # Level up used action
                new_levels[i] = min(u_limit, new_levels[i] + 1)
                
                # Decay others
                for j in range(a_count):
                    if i != j:
                        _, _, dec_j = actions[j]
                        new_levels[j] = max(0, new_levels[j] - dec_j)
                        
                nl_tuple = tuple(new_levels)
                new_dp[nl_tuple] = min(
                    new_dp.get(nl_tuple, float("inf")),
                    total_cost + cost,
                )
        dp = new_dp
        
    print(min(dp.values()))


if __name__ == "__main__":
    solve()
