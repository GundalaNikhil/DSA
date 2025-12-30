
import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def shortest_path(grid: List[List[str]]) -> int:
    if not grid: return -1
    rows, cols = len(grid), len(grid[0])
    
    start = None
    
    for i in range(rows):
        if len(grid[i]) != cols:
             # Handle jagged/inconsistent rows by skipping or erroring?
             # For now, let's just avoid crashing if possible, or assume valid input logic
             # But if loop goes to 'cols', we crash.
             # We should probably robustly find S/E/F even if jagged.
             pass
             
        for j in range(min(len(grid[i]), cols)):
            if grid[i][j] == 'S':
                start = (i, j)
    
    if not start: return -1
    
    # State: (r, c, visited_food)
    queue = deque([(start[0], start[1], 0, 0)]) # r, c, has_food, dist
    visited = set([(start[0], start[1], 0)])
    
    while queue:
        r, c, has_food, dist = queue.popleft()
        
        # Check current cell type - robust check
        if r >= rows or c >= len(grid[r]): continue
        
        cell = grid[r][c]
        
        current_has_food = 1 if cell == 'F' or has_food else 0
        
        if cell == 'E' and current_has_food:
            return dist

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols: # Bound checkout based on theoretical cols
                 # And actual check
                 if nc < len(grid[nr]) and grid[nr][nc] != '#':
                    if (nr, nc, current_has_food) not in visited:
                        visited.add((nr, nc, current_has_food))
                        queue.append((nr, nc, current_has_food, dist + 1))
                    
    return -1

def main():
    try:
        # Use splitlines to preserve row structure
        lines = sys.stdin.read().splitlines()
    except Exception:
        return

    if not lines:
        return
        
    # Wrapper to handle potential empty lines or whitespace issues
    # Filter out empty lines?
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    
    try:
        # First valid line should be r c
        header = valid_lines[0].split()
        if len(header) < 2: return
        r, c = int(header[0]), int(header[1])
        
        # Next r lines are grid
        # If valid_lines has fewer than r+1 lines, it's partial input, fixable or crash
        # Just safely grab up to r lines
        
        grid = []
        for i in range(r):
            if i + 1 < len(valid_lines):
                row_str = valid_lines[i+1]
                # Ensure we only take first c chars if line is longer? 
                # Or just list(row_str)
                grid.append(list(row_str))
            else:
                grid.append([]) # Empty row filler
                
        result = shortest_path(grid)
        print(result)
        
    except ValueError:
        pass

if __name__ == "__main__":
    main()
