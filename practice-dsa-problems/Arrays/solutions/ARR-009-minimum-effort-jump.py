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
        e = []
        for _ in range(n):
            e.append(int(next(iterator)))
    except StopIteration:
        return

    if n == 0:
        print(0)
        return

    dp = [0] * n
    dp[0] = e[0]
    dq = deque([0])
    
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
            
        # Min is at front
        min_prev = dp[dq[0]]
        dp[i] = e[i] + min_prev
        
        # Maintain monotonicity for next steps
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
        
    print(dp[n - 1])

if __name__ == "__main__":
    solve()
