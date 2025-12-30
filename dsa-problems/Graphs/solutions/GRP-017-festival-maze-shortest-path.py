from collections import deque
from typing import List

def shortest_path_with_walls(grid: List[List[int]], k: int) -> int:
    rows, cols = len(grid), len(grid[0])
    
    if rows == 1 and cols == 1:
        return 0
    
    queue = deque([(0, 0, k, 0)])  # (row, col, walls_left, steps)
    visited = {(0, 0, k)}
    
    while queue:
        r, c, walls, steps = queue.popleft()
        
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            
            new_walls = walls - grid[nr][nc]
            
            if new_walls >= 0 and (nr, nc, new_walls) not in visited:
                if nr == rows - 1 and nc == cols - 1:
                    return steps + 1
                
                visited.add((nr, nc, new_walls))
                queue.append((nr, nc, new_walls, steps + 1))
    
    return -1


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
