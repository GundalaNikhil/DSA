import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        t_sum = int(next(iterator))
        d_diff = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return
        
    
    first_occurrence = {} # val -> index (0-based)
    best_pair = None
    
    
    for j_idx in range(n):
        val_j = a[j_idx]
        val_i = t_sum - val_j
        
        if val_i in first_occurrence:
            i_idx = first_occurrence[val_i] # This is the smallest index for val_i so far
            
            # Check diff constraint
            if abs(val_i - val_j) <= d_diff:
                curr_pair = (i_idx + 1, j_idx + 1)
                
                if best_pair is None:
                    best_pair = curr_pair
                else:
                    # Generic comparison for (i, j) tuple
                    if curr_pair < best_pair:
                        best_pair = curr_pair
                        
        # Record current val_j if not seen (to keep smallest index)
        if val_j not in first_occurrence:
            first_occurrence[val_j] = j_idx
            
    if best_pair:
        print(f"{best_pair[0]} {best_pair[1]}")
    else:
        print("-1")

if __name__ == "__main__":
    solve()
