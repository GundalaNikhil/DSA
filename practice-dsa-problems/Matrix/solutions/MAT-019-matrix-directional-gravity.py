import sys


def solve():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    n, m = map(int, input_lines[0].split())
    grid = [list(line) for line in input_lines[1:]]
    mid_r = n // 2
    mid_c = m // 2
    res = [["0"] * m for _ in range(n)]
    # Zone 1: Top-Left
    for c in range(mid_c):
        count = sum(1 for r in range(mid_r) if grid[r][c] == "1")
        # Gravity pulls down towards mid_r?
        # Logic: count ones, fill bottom 'count' cells in range [0, mid_r)
        for r in range(mid_r - count, mid_r):
            res[r][c] = "1"
            
    # Zone 2: Top-Right
    for r in range(mid_r):
        count = sum(1 for c in range(mid_c, m) if grid[r][c] == "1")
        # Gravity pulls left towards mid_c?
        for c in range(mid_c, mid_c + count):
            res[r][c] = "1"
            
    # Zone 3: Bottom-Left
    for r in range(mid_r, n):
        count = sum(1 for c in range(mid_c) if grid[r][c] == "1")
        # Gravity pulls right towards mid_c?
        for c in range(mid_c - count, mid_c):
            res[r][c] = "1"
            
    # Zone 4: Bottom-Right
    for c in range(mid_c, m):
        count = sum(1 for r in range(mid_r, n) if grid[r][c] == "1")
        # Gravity pulls up towards mid_r?
        for r in range(mid_r, mid_r + count):
            res[r][c] = "1"
            
    for row in res:
        print("".join(row))


if __name__ == "__main__":
    solve()
