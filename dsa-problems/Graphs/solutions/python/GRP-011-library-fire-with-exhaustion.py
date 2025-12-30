import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def fire_spread_time(grid: List[List[int]], stamina: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    ignited = set()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                # Use default stamina 0 if stamina grid missing/incomplete
                s = stamina[i][j] if i < len(stamina) and j < len(stamina[i]) else 0
                queue.append((i, j, s, 0))
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
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and (i, j) not in ignited:
                return -1
    
    return max_time

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        r = int(next(iterator))
        c = int(next(iterator))
        
        grid = []
        for _ in range(r):
            row = []
            for _ in range(c):
                row.append(int(next(iterator)))
            grid.append(row)
            
        stamina = []
        try:
            for _ in range(r):
                row = []
                for _ in range(c):
                    row.append(int(next(iterator)))
                stamina.append(row)
        except StopIteration:
            # Fill remaining with 0s
            while len(stamina) < r:
                stamina.append([0] * c)
        
        result = fire_spread_time(grid, stamina)
        print(result)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
