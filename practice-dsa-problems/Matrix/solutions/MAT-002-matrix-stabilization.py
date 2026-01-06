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
    grid = []
    for _ in range(n):
        row_str = input_data[ptr]
        ptr += 1
        grid.append([int(c) for c in row_str])
def get_next(curr_grid):
    next_grid = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            diff_count = 0
            n0 = 0
            n1 = 0
            deg = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    deg += 1
                    if curr_grid[nr][nc] != curr_grid[r][c]:
                        diff_count += 1
                        if curr_grid[nr][nc] == 0:
                            n0 += 1
                        else:
                            n1 += 1
                            if diff_count >= 2:
                                if n0 > n1:
                                    next_grid[r][c] = 0
                                elif n1 > n0:
                                    next_grid[r][c] = 1
                                else:
                                    next_grid[r][c] = 0
                                else:
                                    next_grid[r][c] = curr_grid[r][c]
                                    return next_grid
def grid_to_tuple(g):
    return tuple(tuple(row) for row in g)
seen = {}
history = []
curr = grid
t = 0
while True:
    curr_tuple = grid_to_tuple(curr)
    if curr_tuple in seen:
        cycle_start = seen[curr_tuple]
        if cycle_start == t:
            pass
        nxt = get_next(curr)
        if grid_to_tuple(nxt) == curr_tuple:
            print(f"STABLE {t}")
            for row in curr:
                print("".join(map(str, row)))
                return
        else:
            cycle_len = t - cycle_start
            print(f"CYCLE {cycle_len}")
            first_in_cycle = history[cycle_start]
            for row in first_in_cycle:
                print("".join(map(str, row)))
                return
            seen[curr_tuple] = t
            history.append(curr)
            curr = get_next(curr)
            t += 1
            if t > 1000:
                break
if __name__ == '__main__':
    solve()