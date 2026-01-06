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
    l_count = int(input_data[ptr])
    ptr += 1
    q_count = int(input_data[ptr])
    ptr += 1
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            matrix.append(row)
            matrix.append(row)
            
    is_locked = [[False] * m for _ in range(n)]
    for _ in range(l_count):
        r1 = int(input_data[ptr]) - 1
        ptr += 1
        c1 = int(input_data[ptr]) - 1
        ptr += 1
        r2 = int(input_data[ptr]) - 1
        ptr += 1
        c2 = int(input_data[ptr]) - 1
        ptr += 1
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                is_locked[r][c] = True
                
    locked_pref = [[0] * (m + 1) for _ in range(n + 1)]
    for r in range(n):
        for c in range(m):
            locked_pref[r + 1][c + 1] = (1 if is_locked[r][c] else 0) + \
                                        locked_pref[r][c + 1] + \
                                        locked_pref[r + 1][c] - \
                                        locked_pref[r][c]

    def get_locked_sum(r1, c1, r2, c2):
        return locked_pref[r2 + 1][c2 + 1] - locked_pref[r1][c2 + 1] - \
               locked_pref[r2 + 1][c1] + locked_pref[r1][c1]

    diff = [[0] * (m + 1) for _ in range(n + 1)]
    
    for _ in range(q_count):
        r1 = int(input_data[ptr]) - 1
        ptr += 1
        c1 = int(input_data[ptr]) - 1
        ptr += 1
        r2 = int(input_data[ptr]) - 1
        ptr += 1
        c2 = int(input_data[ptr]) - 1
        ptr += 1
        delta = int(input_data[ptr])
        ptr += 1
        
        # Check if fully locked? 
        # Code prints locked_sum.
        # Logic: If locked region overlap?
        # Maybe query asks "How many locked cells in range?"
        print(get_locked_sum(r1, c1, r2, c2))
        
        # Apply update (assuming update applies even if locked? Or masked later)
        # 2D Difference array update
        diff[r1][c1] += delta
        diff[r1][c2 + 1] -= delta
        diff[r2 + 1][c1] -= delta
        diff[r2 + 1][c2 + 1] += delta
        
    # Apply diffs
    for r in range(n):
        for c in range(m):
            if r > 0: diff[r][c] += diff[r - 1][c]
            if c > 0: diff[r][c] += diff[r][c - 1]
            if r > 0 and c > 0: diff[r][c] -= diff[r - 1][c - 1]
            
            # Update matrix if not locked
            if not is_locked[r][c]:
                matrix[r][c] += diff[r][c]
                
    for row in matrix:
        print(*(row))
if __name__ == '__main__':
    solve()