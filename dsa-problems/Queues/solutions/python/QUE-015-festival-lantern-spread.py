from collections import deque
from typing import List
import sys

def minutes_to_light(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    r, c = len(grid), len(grid[0])
    q = deque()
    fresh_count = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                q.append((i, j))
            else:
                fresh_count += 1

    if fresh_count == 0:
        return 0
    if not q:
        return -1

    minutes = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q and fresh_count > 0:
        minutes += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    fresh_count -= 1
                    q.append((nx, ny))

    return minutes if fresh_count == 0 else -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        r = int(next(iterator))
        c = int(next(iterator))
        grid = []
        for _ in range(r):
            row = [int(next(iterator)) for _ in range(c)]
            grid.append(row)
        
        result = minutes_to_light(grid)
        print(result)
    except (StopIteration, ValueError):
        pass

if __name__ == "__main__":
    main()
