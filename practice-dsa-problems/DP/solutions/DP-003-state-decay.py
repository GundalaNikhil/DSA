import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    d_decay = int(input_data[ptr])
    ptr += 1
    d_limit = int(input_data[ptr])
    ptr += 1
    v = []
    for _ in range(m):
        v.append(int(input_data[ptr]))
        ptr += 1
        
    dp = {tuple([0] * m): 0}
    
    for _ in range(n):
        new_dp = {}
        for timers, total_val in dp.items():
            # Try selecting each state s
            for s in range(m):
                gain = max(0, v[s] - d_decay * timers[s])
                
                new_timers = list(timers)
                # Reset selected, increment others
                for i in range(m):
                    if i == s:
                        new_timers[i] = 0
                    else:
                        new_timers[i] = min(d_limit, new_timers[i] + 1)
                        
                nt_tuple = tuple(new_timers)
                new_dp[nt_tuple] = max(
                    new_dp.get(nt_tuple, -float("inf")),
                    total_val + gain,
                )
        dp = new_dp
        
    print(max(dp.values()))


if __name__ == "__main__":
    solve()
