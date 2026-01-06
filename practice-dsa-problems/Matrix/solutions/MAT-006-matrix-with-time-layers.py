import bisect
import sys
from bisect import bisect_right
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    histories = [[[] for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            v = int(input_data[ptr])
            ptr += 1
            histories[r][c].append((-1, v))
            histories[r][c].append((-1, v))
            
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'SET':
            t = int(input_data[ptr])
            ptr += 1
            r = int(input_data[ptr])
            ptr += 1
            c = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            r -= 1
            c -= 1
            h = histories[r][c]
            
            # Insert sorted by time? Or replace?
            # Code: bisect_left.
            idx = bisect.bisect_left(h, (t, ))
            if idx < len(h) and h[idx][0] == t:
                h[idx] = (t, v)
            else:
                h.insert(idx, (t, v))
        else: # GET
            t = int(input_data[ptr])
            ptr += 1
            r = int(input_data[ptr])
            ptr += 1
            c = int(input_data[ptr])
            ptr += 1
            r -= 1
            c -= 1
            h = histories[r][c]
            
            # Find value at time t. 
            # bisect_right returns index after elements <= t.
            # subtract 1 to get element <= t.
            # Tuple comparison (t, inf) ensures we search properly.
            idx = bisect_right(h, (t, float('inf'))) - 1
            if idx >= 0:
                print(h[idx][1])
            else:
                # Should not happen as we init with (-1, v)
                print(0)
if __name__ == '__main__':
    solve()