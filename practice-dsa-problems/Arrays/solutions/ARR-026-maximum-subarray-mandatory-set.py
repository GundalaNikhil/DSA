import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
        s_set = set()
        for _ in range(m):
            s_set.add(int(next(iterator)))
    except StopIteration:
        return
   
    
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
        
    # Precompute min prefix sums
    global_min_for_idx = [0] * (n + 1)
    current_min = 0
    for i in range(n + 1):
        if i > 0:
            current_min = min(current_min, pref[i])
        global_min_for_idx[i] = current_min
        
    l = 0
    counts = {}
    valid_count = 0
    ans = -float("inf")
    found = False
    
   
    for r in range(n):
        val_r = a[r]
        if val_r in s_set:
            counts[val_r] = counts.get(val_r, 0) + 1
            if counts[val_r] == 1:
                valid_count += 1
                
       
        while valid_count == m:
            found = True
            current_score = pref[r + 1] - global_min_for_idx[l]
            ans = max(ans, current_score)
            
            # Try to contract
            val_l = a[l]
            if val_l in s_set:
                counts[val_l] -= 1
                if counts[val_l] == 0:
                    valid_count -= 1
            l += 1
            
    print(ans if found else "IMPOSSIBLE")

if __name__ == "__main__":
    solve()
