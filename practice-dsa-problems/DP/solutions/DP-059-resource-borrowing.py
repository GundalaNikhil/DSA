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
    b_limit = int(input_data[ptr])
    ptr += 1
    interest = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        r = int(input_data[ptr])
        ptr += 1
        d = int(input_data[ptr])
        ptr += 1

        actions.append((r, d))
        
    dp = {}
    dp[0] = 0
    
    for _ in range(n):
        new_dp = {}
        for bal, score in dp.items():
            for r, d in actions:
                nbal = bal + d
                if nbal < 0:
                    nbal -= interest
                    
                if nbal >= -b_limit:
                    if nbal not in new_dp or new_dp[nbal] < score + r:
                        new_dp[nbal] = score + r
        dp = new_dp
        if not dp:
            break
            
    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
