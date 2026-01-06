from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        b = int(next(iterator))
        fuel = []
        for _ in range(n):
            fuel.append(int(next(iterator)))
        drain = []
        for _ in range(n):
            drain.append(int(next(iterator)))
    except StopIteration:
        return


    diff = []
    for i in range(n):
        diff.append(fuel[i] - (drain[i] + b))
        
    if sum(diff) < 0:
        print("-1")
        return
        
    # Construct double array prefix sums
    pref = [0] * (2 * n + 1)
    for i in range(2 * n):
        pref[i + 1] = pref[i] + diff[i % n]
        
    # Sliding window minimum of size n on pref[1...].

    dq = deque()
    # Fill window for first potential start (k=0). Range [1, n].
    for i in range(1, n + 1):
        while dq and pref[dq[-1]] >= pref[i]:
            dq.pop()
        dq.append(i)
        
    # Check k=0
    if pref[dq[0]] >= pref[0]:
        print(1) # 1-based index if answering station index
        return
        
    # Slide window
    # For start k, we check min over [k+1, k+n] vs pref[k].
    # We already have [1, n] in deque.
    # Move to k=1. Window [2, n+1].
    
    for k in range(1, n):
        # Remove elements < k+1
        while dq and dq[0] < k + 1:
            dq.popleft()
            
        # Add k+n
        idx = k + n
        while dq and pref[dq[-1]] >= pref[idx]:
            dq.pop()
        dq.append(idx)
        
        if pref[dq[0]] >= pref[k]:
            print(k + 1)
            return
            
    # Should be guaranteed to find one if sum >= 0?
    print("-1")

if __name__ == "__main__":
    solve()
