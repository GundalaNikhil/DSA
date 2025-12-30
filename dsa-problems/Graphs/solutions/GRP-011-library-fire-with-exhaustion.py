from collections import deque
from typing import List

def fire_spread_time(grid: List[List[int]], stamina: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    ignited = set()
    
    # Initialize with fire sources
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, stamina[i][j], 0))
                ignited.add((i, j))
    
    max_time = 0
    
    while queue:
        r, c, stam, time = queue.popleft()
        max_time = max(max_time, time)
        
        if stam > 0:
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == 0 and (nr, nc) not in ignited):
                    ignited.add((nr, nc))
                    queue.append((nr, nc, stam - 1, time + 1))
    
    # Check if all empty cells ignited
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and (i, j) not in ignited:
                return -1
    
    return max_time


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
