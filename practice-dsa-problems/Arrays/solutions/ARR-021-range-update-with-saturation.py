import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        low = int(next(iterator))
        high = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
            
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l_val = int(next(iterator))
            r_val = int(next(iterator))
            val = int(next(iterator))
            queries.append((l_val, r_val, val))
            
    except StopIteration:
        return
    
    diff = [0] * (n + 1)
    for l, r, val in queries:
        # 1-based to 0-based
        l_idx = l - 1
        r_idx = r - 1
        
        if 0 <= l_idx < n:
            diff[l_idx] += val
        if 0 <= r_idx + 1 < n:
            diff[r_idx + 1] -= val
        elif r_idx + 1 >= n:
            diff[min(n, r_idx + 1)] -= val
            
    curr = 0
    res = []
    for i in range(n):
        curr += diff[i]
        final_val = a[i] + curr
        
        if final_val < low:
            final_val = low
        if final_val > high:
            final_val = high
            
        res.append(str(final_val))
        
    print(*(res))

if __name__ == "__main__":
    solve()
