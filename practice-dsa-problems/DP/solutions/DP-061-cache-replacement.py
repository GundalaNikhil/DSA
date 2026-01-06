import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    c_cap = int(input_data[ptr])
    ptr += 1
    keys = []
    for _ in range(n):
        keys.append(int(input_data[ptr]))
        ptr += 1
    dp = {frozenset(): 0}
    # State: dp[cache_set] = misses
    
    for k in keys:
        new_dp = {}
        for cache, misses in dp.items():
            # If hit
            if k in cache:
                if cache not in new_dp or new_dp[cache] > misses:
                    new_dp[cache] = misses
            else:
                # Miss
                # Option 1: Add to cache if space
                if len(cache) < c_cap:
                    new_cache = frozenset(list(cache) + [k])
                    if (
                        new_cache not in new_dp
                        or new_dp[new_cache] > misses + 1
                    ):
                        new_dp[new_cache] = misses + 1
                else:
                    # Option 2: Evict LRU? Optimal policy (Belady's) is usually greedy (furthest in future).
                    # But if we use DP, we explore all eviction choices?
                    # Code: Iterate `to_evict` in `cache`. Try all evictions.
                    # This solves Optimal Replacement.
                    
                    for to_evict in cache:
                        new_cache = frozenset(
                            [x for x in cache if x != to_evict] + [k]
                        )
                        if (
                            new_cache not in new_dp
                            or new_dp[new_cache] > misses + 1
                        ):
                            new_dp[new_cache] = misses + 1
        dp = new_dp
        
    print(min(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
