import sys
from collections import defaultdict
import Counter


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    p = int(input_data[ptr])
    ptr += 1
    strategy = int(input_data[ptr])
    ptr += 1
    proposals = defaultdict(list)
    for _ in range(p):
        r = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1
        val = int(input_data[ptr])
        ptr += 1
        prio = int(input_data[ptr])
        ptr += 1
        time = int(input_data[ptr])
        ptr += 1
        src = int(input_data[ptr])
        ptr += 1
        proposals[(r, c)].append((val, prio, time, src))
        
    matrix = [[0] * m for _ in range(n)]
    for (r, c), props in proposals.items():
        if strategy == 1:
            props.sort(key=lambda x: (-x[1], x[2], x[3]))
            matrix[r - 1][c - 1] = props[0][0]
        elif strategy == 2:
            props.sort(key=lambda x: (x[2], -x[1], x[3]))
            matrix[r - 1][c - 1] = props[0][0]
        else:
            val_counts = Counter(p[0] for p in props)
            max_freq = max(val_counts.values())
            best_val = None
            best_prio = -1
            best_time = float("inf")
            best_src = float("inf")
            
            for v, prio, time, src in props:
                if val_counts[v] == max_freq:
                    if prio > best_prio:
                        best_prio, best_time, best_src, best_val = (prio, time, src, v)
                    elif prio == best_prio:
                        if time < best_time:
                            best_time, best_src, best_val = time, src, v
                        elif time == best_time:
                            if src < best_src:
                                best_src, best_val = src, v
                                
            matrix[r - 1][c - 1] = best_val
            
    for row in matrix:
        print(*(row))


if __name__ == "__main__":
    solve()
