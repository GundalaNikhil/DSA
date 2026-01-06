import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    L_limit = int(input_data[ptr])
    ptr += 1
    U_limit = int(input_data[ptr])
    ptr += 1
    vals = []
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    shards = [vals]
    q = int(input_data[ptr])
    ptr += 1
    
    splits = 0
    merges = 0
    
    for _ in range(q):
        tp = input_data[ptr]
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        
        curr_pos = 0
        target_shard_idx = -1
        offset = -1
        
        for i, shard in enumerate(shards):
            if curr_pos + len(shard) >= pos:
                target_shard_idx = i
                offset = pos - curr_pos - 1
                break
            curr_pos += len(shard)
            
        if tp == 'INS':
            x = int(input_data[ptr])
            ptr += 1
            if target_shard_idx == -1:
                # Append to end of last shard if pos is end?
                # Or make new shard?
                # Usually logic handles appending to last shard.
                # Assuming pos was valid or just append if beyond.
                if shards:
                    shards[-1].append(x)
                    target_shard_idx = len(shards) - 1
            else:
                shards[target_shard_idx].insert(offset, x)
        else: # DEL
            if target_shard_idx != -1:
                shards[target_shard_idx].pop(offset)
                
        if target_shard_idx != -1:
            if len(shards[target_shard_idx]) > U_limit:
                s = shards[target_shard_idx]
                mid = len(s) // 2
                shards[target_shard_idx:target_shard_idx + 1] = [s[:mid], s[mid:]]
                splits += 1
            elif len(shards[target_shard_idx]) < L_limit:
                if target_shard_idx < len(shards) - 1:
                    shards[target_shard_idx] += shards[target_shard_idx + 1]
                    shards.pop(target_shard_idx + 1)
                    merges += 1
                    # Re-check upper limit after merge
                    if len(shards[target_shard_idx]) > U_limit:
                        s = shards[target_shard_idx]
                        mid = len(s) // 2
                        shards[target_shard_idx:target_shard_idx + 1] = [s[:mid], s[mid:]]
                        splits += 1
                        
        print(f"{splits} {merges}")
        print(*(len(s) for s in shards))
if __name__ == '__main__':
    solve()