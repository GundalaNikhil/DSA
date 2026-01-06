import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        e = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return


    segments = []
    i = 0
    while i < n:
        j = i
        curr_sum = 0
        curr_max = -float("inf")
        curr_min = float("inf")
        last_valid_j = i
        
        while j < n:
            val = a[j]
            curr_sum += val
            curr_max = max(curr_max, val)
            curr_min = min(curr_min, val)
            
            # fast pruning
            if curr_max - curr_min > 2 * e:
                break
                
            length = j - i + 1
            avg_floor = curr_sum // length
            
            # Check if avg is a valid representative
            # |x - avg| <= e for all x (i.e. x in [min, max])
            # implies avg >= max - e AND avg <= min + e
            
            if (curr_max - e) <= avg_floor <= (curr_min + e):
                last_valid_j = j
                
            j += 1
            
        # Segment ends at last_valid_j
        seg_len = last_valid_j - i + 1
        segments.append(seg_len)
        i = last_valid_j + 1
        
    print(len(segments))
    print(*(segments))

if __name__ == "__main__":
    solve()
