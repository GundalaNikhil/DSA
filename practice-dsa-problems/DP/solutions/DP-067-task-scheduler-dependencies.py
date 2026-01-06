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
    durations = []
    for _ in range(n):
        durations.append(int(input_data[ptr]))
        ptr += 1
        deps = [0] * n
        for _ in range(m):
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            deps[v - 1] |= 1 << (u - 1)

            
    inf = float("inf")
    dp = [inf] * (1 << n)
    dp[0] = 0
    
    # Iterate masks by size or just simple loop?
    # Simple loop `range(1 << n)` works because we add 1 bit at a time, moving from smaller to larger mask.
    
    for mask in range(1 << n):
        if dp[mask] == inf:
            continue
            
        for i in range(n):
            # If task i not done
            if not (mask & (1 << i)):
                # If dependencies met
                if (mask & deps[i]) == deps[i]:
                    new_mask = mask | (1 << i)
                    new_time = dp[mask] + durations[i]
                    if dp[new_mask] > new_time:
                        dp[new_mask] = new_time
                        
    print(dp[(1 << n) - 1])


if __name__ == "__main__":
    solve()
