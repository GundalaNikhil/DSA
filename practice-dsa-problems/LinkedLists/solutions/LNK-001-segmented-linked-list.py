import sys


class Node:
    def __init__(self, val, seg):
        self.val = val
        self.seg = seg
        self.next = None
        self.prev = None


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    values = []
    for _ in range(n):
        values.append(int(input_data[ptr]))
        ptr += 1
        
    segs = []
    for _ in range(n):
        segs.append(int(input_data[ptr]))
        ptr += 1
        
    segment_data = {}
    node_to_seg = {}
    for i in range(n):
        s = segs[i]
        v = values[i]
        if s not in segment_data:
            segment_data[s] = []
        segment_data[s].append(v)
        node_to_seg[v] = s
        
    num_q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(num_q):
        op = input_data[ptr]
        ptr += 1
        if op == "MOVE":
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            if u in node_to_seg and v in node_to_seg:
                s_u = node_to_seg[u]
                s_v = node_to_seg[v]
                if s_u == s_v:
                    lst = segment_data[s_u]
                    try:
                        u_idx = lst.index(u)
                        lst.pop(u_idx)
                        v_idx = lst.index(v)
                        lst.insert(v_idx + 1, u)
                    except ValueError:
                        pass
        elif op == "DEL":
            u = int(input_data[ptr])
            ptr += 1
            if u in node_to_seg:
                s = node_to_seg[u]
                lst = segment_data[s]
                try:
                    lst.remove(u)
                    del node_to_seg[u]
                except ValueError:
                    pass
        elif op == "INS":
            v = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            s = int(input_data[ptr])
            ptr += 1
            if v in node_to_seg:
                s_v = node_to_seg[v]
                if s == s_v:
                    lst = segment_data[s]
                    try:
                        v_idx = lst.index(v)
                        lst.insert(v_idx + 1, x)
                        node_to_seg[x] = s
                    except ValueError:
                        pass
        elif op == "PRINT":
            s = int(input_data[ptr])
            ptr += 1
            if s in segment_data:
                print(*(segment_data[s]))
            else:
                print()


if __name__ == "__main__":
    solve()
