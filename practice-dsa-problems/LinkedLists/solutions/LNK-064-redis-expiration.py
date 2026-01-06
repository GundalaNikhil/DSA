import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    S = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    ttls = []
    for _ in range(n):
        t_val = int(input_data[ptr])
        ptr += 1
        ttls.append(t_val if t_val > 0 else float('inf'))
        
    lst = []
    for i in range(n):
        lst.append([vals[i], ttls[i]])
        
    q = int(input_data[ptr])
    ptr += 1
    op_count = 0
    
    for _ in range(q):
        op_count += 1
        # Lazy expiration logic? Or triggered every S ops?
        # Original: if op_count % S == 0: pass
        if op_count % S == 0:
            # Clean expired items
            # Need 'current time' for cleanup?
            # The problem seems to imply operations provide 't'.
            # But cleanup is mentioned before operation type reading?
            # Actually, `t` comes with operations.
            # But here, we can't clean without `t`.
            # Maybe we just defer cleanup until we read `t`.
            pass
            
        op = input_data[ptr]
        ptr += 1
        
        if op == 'SET':
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            ttl = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            
            if op_count % S == 0:
                 lst = [node for node in lst if node[1] > t]
                 
            # Note: After cleanup, indices shift!
            if 1 <= pos <= len(lst):
                 # Update existing? Wait, SET usually inserts or updates?
                 # If list index, it replaces.
                 lst[pos - 1] = [x, t + ttl if ttl > 0 else float('inf')]
                 
        elif op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            
            if op_count % S == 0:
                 lst = [node for node in lst if node[1] > t]
                 
            if 1 <= pos <= len(lst):
                if lst[pos - 1][1] <= t:
                    # Expired on access?
                    # The original logic pops it.
                    lst.pop(pos - 1)
                    print("-1")
                else:
                    print(lst[pos - 1][0])
            else:
                print("-1")