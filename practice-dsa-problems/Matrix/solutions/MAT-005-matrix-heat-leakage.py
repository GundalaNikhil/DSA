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
    t_steps = int(input_data[ptr])
    ptr += 1
    p_leak = int(input_data[ptr])
    ptr += 1
    grid = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            grid.append(row)
            
    degs = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            d = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= r + dr < n and 0 <= c + dc < m:
                    d += 1
            degs[r][c] = d # Fixed indentation logic for d calc
            
    for _ in range(t_steps):
        next_grid = [[0.0] * m for _ in range(n)] # Use float? Problem says heat usually float or large int.
        # Original: Used // so int.
        # next_grid = [[0] * m for _ in range(n)]
        
        # Need to init next_grid with current values?
        # Model: Heat Transfer.
        # usually: next[i] = current[i] - outflow + inflow.
        # Or simultaneous update?
        # Code: `next_grid[nr][nc] += each_leak`
        # `next_grid[r][c] += grid[r][c] - ...`
        # So we start with 0 and accumulate?
        # Yes.
        
        for r in range(n):
            for c in range(m):
                # Init next_grid[r][c] if not done? 
                # Actually logic adds to next_grid.
                # Do we preserve mass?
                # grid[r][c] splits into (retained) + (leaked).
                
                total_leak = (grid[r][c] * p_leak) // 100
                deg = degs[r][c]
                
                if deg > 0:
                    each_leak = total_leak // deg
                    retained = grid[r][c] - (each_leak * deg)
                    
                    next_grid[r][c] += retained
                    
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            next_grid[nr][nc] += each_leak
                else:
                    next_grid[r][c] += grid[r][c]
                    
        grid = [[int(x) for x in row] for row in next_grid] # Cast back to int if needed?
        
    total_heat = sum(sum(row) for row in grid)
    print(total_heat)
    for row in grid:
        print(*(row))


if __name__ == "__main__":
    solve()
