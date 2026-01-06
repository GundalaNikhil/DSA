import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    priorities = []
    for _ in range(n):
        priorities.append(int(input_data[ptr]))
        ptr += 1
        
    group_indices = {}
    group_values = {}
    
    for i in range(n):
        p = priorities[i]
        if p not in group_indices:
            group_indices[p] = []
            group_values[p] = []
        group_indices[p].append(i)
        group_values[p].append(vals[i])
        
    global_to_local = [0] * n
    counts = {}
    for i in range(n):
        p = priorities[i]
        global_to_local[i] = counts.get(p, 0)
        counts[p] = global_to_local[i] + 1
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        u = int(input_data[ptr]) - 1
        ptr += 1
        v = int(input_data[ptr]) - 1
        ptr += 1
        
        # Original code had logic: "if priorities[u] != priorities[v]: continue".
        # Assuming we just skip.
        if priorities[u] != priorities[v]:
            continue
            
        p = priorities[u]
        vals_list = group_values[p]
        r_u = global_to_local[u]
        r_v = global_to_local[v]
        
        if op == 'MOVE':
            # Logic: pop u, insert at v?
            # Original code: `val = vals_list.pop(r_u)` then `val = vals_list.pop(r_u)` (duplicate?)
            # Wait, popping from list shifts indices.
            # If `pop(r_u)`, then insert.
            # If r_u < r_v, removing u shifts v to v-1? 
            # Original code:
            # `val = vals_list.pop(r_u)`
            # `val = vals_list.pop(r_u)` (Typo?)
            # `if r_u < r_v: vals_list.insert(r_v, val)` ...
            # The duplicate pop line is likely a typo I should remove.
            # And standard list move logic.
            
            try:
                val = vals_list[r_u]
                vals_list.pop(r_u)
                
                # Adjust destination index if needed
                dest = r_v
                # Logic in original: `if r_u < r_v: insert(r_v, val) else: insert(r_v + 1, val)`
                # Let's think:
                # [A, B, C, D], u=0(A), v=2(C). r_u=0, r_v=2
                # pop 0 -> [B, C, D]. insert at 2 -> [B, C, A, D] (After C)
                # Correct logic usually: insert at new index.
                # If we want to move u TO position of v (or after?)
                # Code: `insert(r_v, val)` means before old v (now at r_v-1?).
                # Let's stick closer to intended logic:
                if r_u < r_v:
                    vals_list.insert(r_v, val) # Insert at v (which shifted left) implies after old v? No, at index.
                else:
                    vals_list.insert(r_v + 1, val) # ?
                    
                # The logic `insert(r_v + 1)` implies inserting AFTER?
                # Without explicit problem statement, sticking to code logic (minus typo) is safer.
                
            except IndexError:
                pass
                
        elif op == 'SWAP':
            # Swap values
            vals_list[r_u], vals_list[r_v] = vals_list[r_v], vals_list[r_u]
            
    # Reconstruct result
    result = [0] * n
    ptrs = {p: 0 for p in group_values}
    
    for i in range(n):
        p = priorities[i]
        result[i] = group_values[p][ptrs[p]]
        ptrs[p] += 1
        
    print(*(result))
if __name__ == '__main__':
    solve()