import sys
from collections import Counter


def get_next_matrix(matrix, n, m, s_range):
    new_matrix = [[0] * m for _ in range(n)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for r in range(n):
        for c in range(m):
            neighbors = []
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    neighbors.append(matrix[nr][nc])
                    if not neighbors:
                        majority = 0
                    else:
                        counts = Counter(neighbors)
                        max_freq = max(counts.values())
                        candidates = [
                            state for state, freq in counts.items() if freq == max_freq
                        ]
                        majority = min(candidates)
                        new_matrix[r][c] = (matrix[r][c] + majority) % s_range
                        return new_matrix


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    s_range = int(input_data[ptr])
    ptr += 1
    initial = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
        initial.append(row)
        
    history = []
    seen = {}
    curr = initial
    step = 0
    
    while True:
        s_tuple = tuple(tuple(row) for row in curr)
        if s_tuple in seen:
            first_step = seen[s_tuple]
            if first_step == step - 1 and history and history[-1] == s_tuple:
                print(f"FIXED {first_step}")
                for row in curr:
                    print(*(row))
                return
            else:
                print(f"CYCLE {step - first_step}")
                first_matrix = history[first_step]
                for row in first_matrix:
                    print(*(row))
                return
                
        seen[s_tuple] = step
        history.append(s_tuple)
        nxt = get_next_matrix(curr, n, m, s_range)
        
        # Check FIXED point explicitly? Or wait for repeat 1?
        # If nxt == curr, it's fixed.
        # Original code did this check.
        if nxt == curr: # Not tuple compare? `nxt` is list of lists
             # Actually `get_next_matrix` returns new list logic.
             print(f"FIXED {step}")
             for row in curr:
                 print(*(row))
             return
             
        curr = nxt
        step += 1
        
        if step > 1000: # Safety
            break


if __name__ == "__main__":
    solve()
