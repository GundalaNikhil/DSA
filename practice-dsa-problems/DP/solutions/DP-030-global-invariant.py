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
    mod = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        v = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        actions.append((v % mod, r))
        actions.append((v % mod, r))
        
    inf = float("inf")
    dp = {0: 0}
    
    for _ in range(n):
        new_dp = {}
        for rem, reward in dp.items():
            for v, r in actions:
                nrem = (rem + v) % mod
                new_dp[nrem] = max(new_dp.get(nrem, -inf), reward + r)
        dp = new_dp
        if not dp:
            break
            
    print(dp.get(0, -1))


if __name__ == "__main__":
    solve()
