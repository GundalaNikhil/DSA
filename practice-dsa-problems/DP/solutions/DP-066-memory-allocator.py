import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    m_size = int(input_data[ptr])
    ptr += 1
    n_req = int(input_data[ptr])
    ptr += 1
    sizes = []
    for _ in range(n_req):
        sizes.append(int(input_data[ptr]))
        ptr += 1

            
    dp = {frozenset([(0, m_size)]): 0}
    # Segments: set of (start, size) free blocks.
    
    for s in sizes:
        new_dp = {}
        for segments, cost in dp.items():
            # Try to alloc s in any free segment
            # And also we might skip allocation? No, implicit must allocate?
            # Code: Iterate `segments`. If size >= s, split.
            # If we don't allocated, we fail?
            # Original code: `if segments not in new_dp ...`. It carries over `cost`?
            # Logic: `new_dp[segments] = cost` is executed FIRST (line 21).
            # Means we can SKIP allocating `s`?
            # But the problem likely requires allocating all?
            # If we skip, we just keep same segments. But we process next `s`?
            # Code: `for s in sizes:` ...
            # If we skip, we lose opportunity to alloc `s`.
            # Maybe allowed.
            
            if segments not in new_dp or new_dp[segments] > cost:
                new_dp[segments] = cost
                
            for start, size in segments:
                if size >= s:
                    new_segs = set(segments)
                    new_segs.remove((start, size))
                    if size - s > 0:
                        new_segs.add((start + s, size - s))
                    
                    fs = frozenset(new_segs)
                    # Cost: Fragmentation? len(fs) is number of fragments.
                    p_cost = len(fs)
                    
                    if fs not in new_dp or new_dp[fs] > cost + p_cost:
                        new_dp[fs] = cost + p_cost
        dp = new_dp
        
    print(min(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
