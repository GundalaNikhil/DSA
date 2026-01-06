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
    k_factor = int(input_data[ptr])
    ptr += 1
    e_max = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        actions.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
        
    inf = float("inf")
    dp = [[-inf] * (e_max + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for s in range(n):
        for e in range(e_max + 1):
            if dp[s][e] == -inf:
                continue
            for r, error_gain in actions:
                ne = k_factor * e + error_gain
                if 0 <= ne <= e_max:
                    dp[s + 1][ne] = max(dp[s + 1][ne], dp[s][e] + r)
                    
    ans = max(dp[n])
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
