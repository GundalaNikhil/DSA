import sys

def check(c, a):
    # WQS Binary Search / Alien Trick check function.
    # Returns (max_value_with_penalty, count_of_subarrays)
    # DP:
    # s0: max value using subarrays, currently NOT in a subarray (or finished one)
    # s1: max value using subarrays, currently extending a subarray
    
    # Initialization
    s0_val, s0_cnt = 0, 0
    s1_val, s1_cnt = -float("inf"), 0
    
    for x in a:
        # Evaluate transitions for current element x
        
        # Option 1: Start a new subarray from s0 state.
        # Penalty c is subtracted when starting (or per subarray).
        start_new_val = s0_val + x - c
        start_new_cnt = s0_cnt + 1
        
        # Option 2: Extend existing subarray from s1 state
        extend_val = s1_val + x
        extend_cnt = s1_cnt
        
        # New s1 (must be in subarray)
        # Choose better of Start or Extend
        if start_new_val > extend_val:
            ns1_val = start_new_val
            ns1_cnt = start_new_cnt
        elif start_new_val < extend_val:
            ns1_val = extend_val
            ns1_cnt = extend_cnt
        else:
            # Prefer larger count if values equal? Or smaller?
            # Standard WQS prefers one bound. Let's maximize count for now.
            ns1_val = extend_val
            ns1_cnt = max(start_new_cnt, extend_cnt)
            
        # New s0 (finished subarray or continued idle)
        # Option A: Continue s0 (idle)
        # Option B: Finish s1 (and become idle). Value matches s1, count matches s1.
        # But s0_val doesn't include x if we are idle *after* x?
        # Standard: s0[i] = max(s0[i-1], s1[i-1] aka finished at i-1).
        # But here x is processed.
        # If we are idle at i, we didn't pick x.
        # So s0[i] comes from s0[i-1].
        # OR we just finished a subarray ending at x (which is ns1).
        
        # In this implementation: s0 means "not extending".
        # It updates from previous s0 (ignore x) OR from NEW s1 (finish at x).
        # Wait, if we finish at x, we just transition from ns1.
        
        # Logic in original:
        # ns0 update uses `ns1_val` as candidate.
        # So `ns0_val = max(s0_val, ns1_val)`.
        
        # s0_val: previous idle.
        # ns1_val: just picked x in a subarray.
        
        if ns1_val > s0_val:
            ns0_val = ns1_val
            ns0_cnt = ns1_cnt
        elif ns1_val < s0_val:
            ns0_val = s0_val
            ns0_cnt = s0_cnt
        else:
            ns0_val = s0_val
            ns0_cnt = max(s0_cnt, ns1_cnt)
            
        s0_val, s0_cnt = ns0_val, ns0_cnt
        s1_val, s1_cnt = ns1_val, ns1_cnt
        
    return s0_val, s0_cnt

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

    # WQS Binary Search range
    # Penalty can be negative (if k is large and we want to force more subarrays?)
    # Usually penalty is positive to reduce count.
    # range logic: [-2e14, 2e14] coverage seems wide enough.
    
    low = -2 * 10**14
    high = 2 * 10**14
    best_penalty = high
    
    # Binary Search for 100 iterations (float/precision)
    for _ in range(100):
        mid = (low + high) / 2
        val, cnt = check(mid, a)
        
        if cnt >= k:
            best_penalty = mid
            low = mid
        else:
            high = mid
            
    # Calculate answer using best_penalty
    val, cnt = check(best_penalty, a)
    # The value returned has `k` penalties subtracted (roughly).
    # Correct formula: val + k * penalty
    # Round to nearest int.
    
    print(int(round(val + k * best_penalty)))

if __name__ == "__main__":
    solve()
