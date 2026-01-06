import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return
        
    
    min_dq = deque() # Increasing
    max_dq = deque() # Decreasing
    l = 0
    ans = 0
    
    for r in range(n):
        val = a[r]
        
        # Maintain min_dq
        while min_dq and a[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(r)
        
        # Maintain max_dq
        while max_dq and a[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(r)
        
        # Contract l
        while a[max_dq[0]] - a[min_dq[0]] > k:
            l += 1
            if min_dq[0] < l:
                min_dq.popleft()
            if max_dq[0] < l:
                max_dq.popleft()
                
        # [l, r] is largest valid window ending at r
        ans += (r - l + 1)
        
    print(ans)

if __name__ == "__main__":
    solve()
