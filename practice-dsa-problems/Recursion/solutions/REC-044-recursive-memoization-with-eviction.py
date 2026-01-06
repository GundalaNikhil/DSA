import sys
from collections import OrderedDict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q_count = int(input_data[ptr])
    ptr += 1
    m_size = int(input_data[ptr])
    ptr += 1
    a0 = int(input_data[ptr])
    ptr += 1
    a1 = int(input_data[ptr])
    ptr += 1
    n_limit = int(input_data[ptr])
    ptr += 1
    c_vals = []
    for _ in range(n_limit + 1):
        c_vals.append(int(input_data[ptr]))
        ptr += 1
        
    queries = []
    for _ in range(q_count):
        queries.append(int(input_data[ptr]))
        ptr += 1
        
    MOD = 1_000_000_007
    cache = OrderedDict()
    miss_count = 0

    def get_f(x):
        nonlocal miss_count
        
        if x in cache:
            # LRU: move to end
            val = cache.pop(x)
            cache[x] = val
            return val
            
        miss_count += 1
        
        if x == 0:
            res = a0 % MOD
        elif x == 1:
            res = a1 % MOD
        else:
            # Recursion for missing item
            # Note: This recursion could verify large depths.
            # Python recursion limit might be hit for deep x without memo.
            # But problem implies "Recursion with Memoization".
            val1 = get_f(x - 1)
            val2 = get_f(x - 2)
            c = c_vals[x] if x < len(c_vals) else 0 # Bounds check? Or n_limit is max x?
            # Problem says n_limit is limit, so we assume x <= n_limit.
            res = (val1 + val2 + c) % MOD
            
        # Add to cache
        if len(cache) >= m_size:
            cache.popitem(last=False) # Remove first (LRU)
            
        cache[x] = res
        return res

    results = []
    sys.setrecursionlimit(500000)
    
    for x in queries:
        results.append(str(get_f(x)))
        
    print(miss_count)
    print(" ".join(results))


if __name__ == "__main__":
    solve()
