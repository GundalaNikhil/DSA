import sys


class Fragment:
    def __init__(self, fid, length):
        self.id = fid
        self.length = length
        self.prev = None
        self.next = None


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    for _ in range(n):
        # Original code just consumed ptr inside loop but didn't assign?
        # `ptr += 1` inside loop (line 20).
        # Ah, loop range n. Consume 1 item?
        # "skip" or dummy read?
        # Let's check original. line 20: ptr += 1.
        # It skipped `input_data[ptr]`.
        ptr += 1
        
    f_map = {}
    f1 = Fragment(1, n)
    f_map[1] = f1
    
    if ptr >= len(input_data):
        return
        
    q = int(input_data[ptr])
    ptr += 1
    
    next_fid = 2
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "SPLIT":
            fid = int(input_data[ptr])
            ptr += 1
            k = int(input_data[ptr])
            ptr += 1
            f = f_map.get(fid)
            if not f or k <= 0 or k >= f.length:
                continue
                
            new_len = f.length - k
            f.length = k
            nf = Fragment(next_fid, new_len)
            f_map[next_fid] = nf
            next_fid += 1
            
            after_f = f.next
            f.next = nf
            nf.prev = f
            nf.next = after_f
            if after_f:
                after_f.prev = nf
                
        elif op == "MERGE":
            fid = int(input_data[ptr])
            ptr += 1
            f = f_map.get(fid)
            if not f or not f.next:
                continue
            fn = f.next
            f.length += fn.length
            after_fn = fn.next
            f.next = after_fn
            if after_fn:
                after_fn.prev = f
            if fn.id in f_map:
                del f_map[fn.id]
                
        elif op == "LEN":
            fid = int(input_data[ptr])
            ptr += 1
            f = f_map.get(fid)
            if f:
                print(f.length)
            else:
                pass


if __name__ == "__main__":
    solve()
