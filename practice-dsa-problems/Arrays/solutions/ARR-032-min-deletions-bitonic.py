import sys
from bisect import bisect_left

def get_lis_lengths(arr):
    n = len(arr)
    if n == 0:
        return []
    lis = []
    res = [0] * n
    for i in range(n):
        val = arr[i]
        idx = bisect_left(lis, val)
        if idx == len(lis):
            lis.append(val)
        else:
            lis[idx] = val
        res[i] = idx + 1
    return res

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    if n < 3:
        print("-1")
        return
        
    left_lis = get_lis_lengths(a)
    right_lis = get_lis_lengths(a[::-1])[::-1]
    
    max_len = 0
    for i in range(n):
        if left_lis[i] > 1 and right_lis[i] > 1: # Strict mountain peak condition
            current_len = left_lis[i] + right_lis[i] - 1
            if current_len > max_len:
                max_len = current_len
                
    if max_len < 3: # Must have at least 3 elements for mountain
        print("-1") 
    else:
        print(n - max_len)

if __name__ == "__main__":
    solve()
