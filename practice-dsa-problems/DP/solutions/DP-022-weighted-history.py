import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a = int(input_data[ptr])
    ptr += 1
    p = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    base = []
    w = []
    for _ in range(a):
        base.append(int(input_data[ptr]))
        ptr += 1
        w.append(int(input_data[ptr]))
        ptr += 1
        
    memo = {}
    ans = get_max_reward(0, tuple([0.0] * a), n, a, p, q, base, w, memo)
    print(round(ans * (q**n)))


def get_max_reward(step, h_vals, n, a, p, q, base, w, memo):
    if step == n:
        return 0
    state = (step, h_vals)
    if state in memo:
        return memo[state]
        
    res = -float("inf")
    for i in range(a):
        curr_h = h_vals[i]
        reward = base[i] - w[i] * curr_h
        
        next_h = list(h_vals)
        for j in range(a):
            # Update history: (p * (h + indicator)) / q
            next_h[j] = (p * (next_h[j] + (1 if j == i else 0))) / q
            
        res = max(res, reward + get_max_reward(step + 1, tuple(next_h), n, a, p, q, base, w, memo))
        
    memo[state] = res
    return res


if __name__ == "__main__":
    solve()
