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
    rules = [None] * (n + 1)
    for _ in range(m):
        rtype = input_data[ptr]
        ptr += 1
        target_i = int(input_data[ptr])
        ptr += 1
        k_count = int(input_data[ptr])
        ptr += 1
        terms = []
        for _ in range(k_count):
            j = int(input_data[ptr])
            ptr += 1
            w = int(input_data[ptr])
            ptr += 1
            terms.append((j, w))
            rules[target_i] = (rtype, terms)
            
    base_val = int(input_data[ptr])
    ptr += 1
    
    inf = float("inf")
    dp = [None] * (n + 1)
    dp[1] = base_val
    
    for i in range(2, n + 1):
        rule = rules[i]
        if rule is None:
            dp[i] = 0
            continue
            
        rtype, terms = rule
        if rtype == "MIN":
            res = inf
            for j, w in terms:
                val = dp[j] if dp[j] is not None else inf
                res = min(res, val + w)
            dp[i] = res
        else: # MAX
            res = -inf
            for j, w in terms:
                val = dp[j] if dp[j] is not None else -inf
                res = max(res, val + w)
            dp[i] = res
            
    print(dp[n] if dp[n] is not None else 0)


if __name__ == "__main__":
    solve()
