import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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


    curr_gcds = [] # list of (gcd_val, left_bound)
    max_cost = 0
    
    # Precompute prefix sums
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
        
    for r in range(n):
        val = a[r]
        next_gcds = []
        
        # New subarray [r, r]
        next_gcds.append((val, r))
        
        # Extend previous
        for g, l in curr_gcds:
            new_g = gcd(g, val)
            if new_g != next_gcds[-1][0]:
                next_gcds.append((new_g, l))
            else:
                

        curr_gcds = []
        if candidates:
            # First one (smallest L) is always kept
            curr_gcds.append(candidates[0])
            for i in range(1, len(candidates)):
                g_curr, l_curr = candidates[i]
                g_prev, l_prev = curr_gcds[-1]
                
                if g_curr != g_prev:
                    curr_gcds.append((g_curr, l_curr))
                else:
                    # Same GCD. l_curr > l_prev.
                    # We already have smaller l in `l_prev`. 
                    # Do nothing.
                    pass
                    
        # Calculate costs for all valid (g, l) at r
        
        for g, l in curr_gcds:
            current_sum = pref[r + 1] - pref[l]
            max_cost = max(max_cost, g * current_sum)
            
    print(max_cost)

if __name__ == "__main__":
    solve()
