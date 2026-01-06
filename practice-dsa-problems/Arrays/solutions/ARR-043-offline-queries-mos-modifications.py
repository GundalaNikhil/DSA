import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        q_count = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
            
        queries = [] # (l, r, time, original_idx)
        updates = [] # (idx, old_val, new_val)
        
        # Initial array copy to track updates
        current_array_state = list(a) 
        
        for i in range(q_count):
            op = next(iterator)
            if op == "Q":
                l = int(next(iterator))
                r = int(next(iterator))
                # Time is number of updates before this query
                time = len(updates)
                queries.append((l, r, time, len(queries)))
            else:
                idx = int(next(iterator))
                val = int(next(iterator))
                # Update: a[idx-1] = val.
                # Record old value to undo.
                old_val = current_array_state[idx - 1]
                updates.append((idx, old_val, val))
                current_array_state[idx - 1] = val
                
    except StopIteration:
        return

    # Coordinate Compression
    all_vals = set(a)
    for _, old, new in updates:
        all_vals.add(old)
        all_vals.add(new)
        
    sorted_vals = sorted(list(all_vals))
    val_map = {v: i for i, v in enumerate(sorted_vals)}
    
    # Map array and updates to compressed values
    a = [val_map[x] for x in a]
    mapped_updates = []
    for idx, old, new in updates:
        mapped_updates.append((idx, val_map[old], val_map[new]))
        
    if n > 0:
        block_size = int(pow(n, 2/3))
    else:
        block_size = 1
    if block_size == 0: block_size = 1
    
    queries.sort(key=lambda x: (x[0] // block_size, x[1] // block_size, x[2]))
    

    counts = [0] * len(sorted_vals)
    curr_score = 0
    curr_a = list(a) # Make a mutable copy for Mo's current state
    
    def add(pos):
        nonlocal curr_score
        val_idx = curr_a[pos]
        val = sorted_vals[val_idx]
        
        curr_score -= val * (counts[val_idx] ** 2)
        counts[val_idx] += 1
        curr_score += val * (counts[val_idx] ** 2)
        
    def remove(pos):
        nonlocal curr_score
        val_idx = curr_a[pos]
        val = sorted_vals[val_idx]
        
        curr_score -= val * (counts[val_idx] ** 2)
        counts[val_idx] -= 1
        curr_score += val * (counts[val_idx] ** 2)
        
    def reflect_update(t, l, r): # Apply or Undo update t
        idx, old_compressed, new_compressed = mapped_updates[t]
        pos = idx - 1
        
        is_in_range = (l <= pos + 1 <= r)
        
        if is_in_range:
            remove(pos)
            
        
        if curr_a[pos] == old_compressed:
            curr_a[pos] = new_compressed
        else:
            curr_a[pos] = old_compressed
            
        if is_in_range:
            add(pos)
            
    # Process queries
    cur_l = 1
    cur_r = 0
    cur_t = 0 # Time: number of updates applied. Initially 0.
    
    ans = [0] * len(queries)
    
    for q_l, q_r, q_t, q_idx in queries:
        # Adjust Time
        while cur_t < q_t:
            # Apply update `cur_t`
            reflect_update(cur_t, cur_l, cur_r)
            cur_t += 1
        while cur_t > q_t:
            # Undo update `cur_t - 1`
            cur_t -= 1
            reflect_update(cur_t, cur_l, cur_r)

        while cur_r < q_r:
            cur_r += 1
            add(cur_r - 1)
        while cur_l > q_l:
            cur_l -= 1
            add(cur_l - 1)
        # Shrink R
        while cur_r > q_r:
            remove(cur_r - 1)
            cur_r -= 1
        # Shrink L (increment L)
        while cur_l < q_l:
            remove(cur_l - 1)
            cur_l += 1
            
        ans[q_idx] = curr_score
        
    for x in ans:
        print(x)

if __name__ == "__main__":
    solve()
