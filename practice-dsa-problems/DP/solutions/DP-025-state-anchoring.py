import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_count = int(input_data[ptr])
    ptr += 1
    l_limit = int(input_data[ptr])
    ptr += 1
    r = []
    for _ in range(s_count):
        r.append(int(input_data[ptr]))
        ptr += 1
        num_a = int(input_data[ptr])
        ptr += 1
        anchors = set()
        for _ in range(num_a):
            anchors.add(int(input_data[ptr]) - 1)
            ptr += 1
            
    inf = float("inf")
    dp = [[-inf] * (l_limit + 1) for _ in range(s_count)]
    
    # Init first step
    for j in range(s_count):
        dist = 0 if j in anchors else 1
        if dist <= l_limit:
            dp[j][dist] = r[j]
            
    # Iterate steps
    for step in range(1, n):
        new_dp = [[-inf] * (l_limit + 1) for _ in range(s_count)]
        for prev_s in range(s_count):
            for d in range(l_limit + 1):
                if dp[prev_s][d] == -inf:
                    continue
                # Try all next states
                for next_s in range(s_count):
                    # Distance update
                    # If next_s is anchor, dist resets to 0?
                    # Original code: `nd = 0 if next_s in anchors else d + 1`
                    nd = 0 if next_s in anchors else d + 1
                    
                    if nd <= l_limit:
                        new_dp[next_s][nd] = max(
                            new_dp[next_s][nd],
                            dp[prev_s][d] + r[next_s],
                        )
        dp = new_dp
        
    ans = -inf
    for j in range(s_count):
        ans = max(ans, max(dp[j]))
        
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
