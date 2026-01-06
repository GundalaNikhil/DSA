import sys


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
    initial = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            initial.append(row)
            initial.append(row)
            
    target = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
        target.append(row)
        
    curr = initial
    for i in range(1, q + 1):
        op = input_data[ptr]
        ptr += 1
        if op == "SET":
            r = int(input_data[ptr]) - 1
            ptr += 1
            c = int(input_data[ptr]) - 1
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            if not (0 <= r < n and 0 <= c < m):
                print(i)
                return
            curr[r][c] = v
        elif op == "ADD":
            r = int(input_data[ptr]) - 1
            ptr += 1
            c = int(input_data[ptr]) - 1
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            if not (0 <= r < n and 0 <= c < m):
                print(i)
                return
            curr[r][c] += v
        elif op == "SWAPROW":
            r1 = int(input_data[ptr]) - 1
            ptr += 1
            r2 = int(input_data[ptr]) - 1
            ptr += 1
            if not (0 <= r1 < n and 0 <= r2 < n):
                print(i)
                return
            curr[r1], curr[r2] = curr[r2], curr[r1]
        elif op == "SWAPCOL":
            c1 = int(input_data[ptr]) - 1
            ptr += 1
            c2 = int(input_data[ptr]) - 1
            ptr += 1
            if not (0 <= c1 < m and 0 <= c2 < m):
                print(i)
                return
            for r in range(n):
                curr[r][c1], curr[r][c2] = curr[r][c2], curr[r][c1]
                
        if curr == target:
            print(0) # Reached target (earlier than q)
            # Problem: "Event Replay", find WHEN it matches or fail?
            # Or print 0 if success at end?
            # Code structure: `if curr == target: print(0)` inside loop implies earliest match.
            return
            
    print(q + 1) # Never matched


if __name__ == "__main__":
    solve()
