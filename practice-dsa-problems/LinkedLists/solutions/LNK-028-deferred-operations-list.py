import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    current_list = []
    for _ in range(n):
        current_list.append(int(input_data[ptr]))
        ptr += 1
        
    q_count = int(input_data[ptr])
    ptr += 1
    
    queue = []
    for _ in range(q_count):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'QUEUE':
            sub_op = input_data[ptr]
            ptr += 1
            if sub_op == 'INS':
                pos = int(input_data[ptr])
                ptr += 1
                val = int(input_data[ptr])
                ptr += 1
                prio = int(input_data[ptr])
                ptr += 1
                queue.append(('INS', pos, val, prio, len(queue)))
            else:
                pos = int(input_data[ptr])
                ptr += 1
                prio = int(input_data[ptr])
                ptr += 1
                queue.append(('DEL', pos, None, prio, len(queue)))
                
        elif op == 'APPLY':
            if not queue:
                continue
                
            ins_winners = {}
            del_winners = {}
            
            for q_op in queue:
                type_op, pos, val, prio, q_idx = q_op
                if type_op == 'INS':
                    score = (prio, 1, -q_idx)
                    if pos not in ins_winners or score > ins_winners[pos][0]:
                        ins_winners[pos] = (score, val)
                else:
                    score = (prio, 0, -q_idx)
                    if pos not in del_winners or score > del_winners[pos][0]:
                        del_winners[pos] = (score, None)
                        
            all_resolved = {}
            merged_positions = set(ins_winners.keys()) | set(del_winners.keys())
            
            for pos in merged_positions:
                candidates = []
                if pos in ins_winners:
                    candidates.append(('INS', ins_winners[pos]))
                if pos in del_winners:
                    candidates.append(('DEL', del_winners[pos]))
                    
                if candidates:
                    best = max(candidates, key=lambda x: x[1][0])
                    all_resolved[pos] = best
                    
            new_list = []
            cur_n = len(current_list)
            
            for i in range(1, cur_n + 2):
                # Check for insert before this index (conceptually)
                # The logic in original code was: check if 'i' is in resolved.
                if i in all_resolved and all_resolved[i][0] == 'INS':
                    new_list.append(all_resolved[i][1][1])
                    
                if i <= cur_n:
                    # Check if current element is deleted
                    # i corresponds to index i-1 in 0-indexed list
                    # Original logic checked delete on 'i'
                    if not (i in all_resolved and all_resolved[i][0] == 'DEL'):
                        new_list.append(current_list[i - 1])
                        
            current_list = new_list
            queue = []
            
        elif op == 'PRINT':
            print(*(current_list))
if __name__ == '__main__':
    solve()