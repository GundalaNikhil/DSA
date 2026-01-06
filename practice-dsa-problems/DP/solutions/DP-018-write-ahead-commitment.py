import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    costs = []
    for _ in range(a_count):
        costs.append(int(input_data[ptr]))
        ptr += 1
        b_count = int(input_data[ptr])
        ptr += 1
        blocks = []
        for _ in range(b_count):
            seq = []
            for _ in range(k):
                seq.append(int(input_data[ptr]) - 1)
                ptr += 1
                c = sum(costs[cid] for cid in seq)
                c = sum(costs[cid] for cid in seq)
                blocks.append(c)
                
    inf = float("inf")
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    # DP State: dp[i] = min cost to write i characters?
    # Loop `range(k, n + 1, k)` suggests we process in blocks of K.
    # `bc` is cost of a block.
    # `dp[i] = min(dp[i], dp[i - k] + bc)`
    # This loop structure is slightly odd.
    # It tries to optimize dp[i] using ALL blocks found SO FAR?
    # Original code: `for _ in range(b_count): ... blocks.append(c); dp=... for i in range...`
    # This implies for EVERY block read, we re-run DP?
    # That means we can use any subset/sequence of blocks?
    # But blocks are just values. "Write Ahead Commitment".
    # Problem likely: Construct string of length N using blocks of length K. Cost is sum of block costs.
    # If we accumulate blocks into a list, we can just run DP once (Unbounded Knapsack style).
    # dp[i] = min cost to reach size i.
    # i steps by K.
    
    for i in range(k, n + 1, k):
        for bc in blocks:
            if dp[i - k] != inf:
                dp[i] = min(dp[i], dp[i - k] + bc)
                
    print(dp[n] if dp[n] != inf else -1)


if __name__ == "__main__":
    solve()
