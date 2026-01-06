import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    base_lst = []
    for _ in range(n):
        base_lst.append(int(input_data[ptr]))
        ptr += 1
        
    q = int(input_data[ptr])
    ptr += 1
    
    sagas = {}
    saga_failed = set()
    lst = list(base_lst)
    current_saga_steps = []
    
    for _ in range(q):
        sid = int(input_data[ptr])
        ptr += 1
        tp = input_data[ptr]
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        
        if sid in saga_failed:
            if tp == 'INS':
                ptr += 1 # Skip value
            continue
            
        success = False
        if tp == 'INS':
            x = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(lst) + 1:
                lst.insert(pos - 1, x)
                current_saga_steps.append((sid, 'INS', pos, x))
                success = True
        else: # DEL
            if 1 <= pos <= len(lst):
                del_val = lst.pop(pos - 1)
                current_saga_steps.append((sid, 'DEL', pos, del_val))
                success = True
                
        if not success:
            saga_failed.add(sid)
            # Rollback this saga
            # Note: current logic rolls back EVERYTHING in current_saga_steps that matches sid?
            # Or is current_saga_steps global for all sagas intermixed?
            # The logic pops from current_saga_steps.
            
            # Filter out steps for this saga to rollback, but we must process them in reverse order of occurrence.
            # However, if other sagas interleaved, rolling back by index might be tricky if we don't track indices carefully.
            # But here `lst` is modified in place.
            # The provided logic seems to assume simple LIFO rollback for the specific saga?
            # Let's preserve the original logic's intent but clean it up.
            
            temp_history = []
            while current_saga_steps:
                last_sid, last_tp, last_pos, last_val = current_saga_steps.pop()
                if last_sid == sid:
                    if last_tp == 'INS':
                        # Undo INS -> DEL
                        # But wait, position might have shifted if other sagas did stuff?
                        # This problem is complex. The original code just did:
                        # lst.pop(last_pos - 1)
                        # This implies it trusts the position is still valid relative to current state?
                        # That's dubious for interleaved ops, but let's stick to cleaning formatting first.
                        if 1 <= last_pos <= len(lst):
                             lst.pop(last_pos - 1)
                    else:
                        # Undo DEL -> INS
                        lst.insert(last_pos - 1, last_val)
                else:
                    temp_history.append((last_sid, last_tp, last_pos, last_val))
            
            # Restore other sagas' steps to history
            while temp_history:
                current_saga_steps.append(temp_history.pop())
                
        print(*(lst))
if __name__ == '__main__':
    solve()