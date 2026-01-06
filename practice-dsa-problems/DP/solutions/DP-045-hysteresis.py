import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    A_on = int(input_data[ptr])
    ptr += 1
    B_off = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        actions.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
    inf = float("inf")
    dp = [[-inf] * 2 for _ in range(51)]
    dp[0][0] = 0 # Starting at level 0, mode 0 (OFF)?
    
    for _ in range(n):
        new_dp = [[-inf] * 2 for _ in range(51)]
        for L in range(51):
            for mode in range(2):
                if dp[L][mode] == -inf:
                    continue
                for d, r in actions:
                    nL = max(0, min(50, L + d))
                    nmode = mode
                    
                    # Hysteresis Logic
                    if nmode == 0 and nL >= A_on:
                        nmode = 1
                    elif nmode == 1 and nL <= B_off:
                        nmode = 0
                        
                    gain = r if nmode == 1 else 0
                    
                    new_dp[nL][nmode] = max(
                        new_dp[nL][nmode], dp[L][mode] + gain
                    )
        dp = new_dp
        
    ans = 0
    for L in range(51):
        ans = max(ans, max(dp[L]))
        
    print(ans)


if __name__ == "__main__":
    solve()
