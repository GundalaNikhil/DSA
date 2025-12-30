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
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly n values, treat as 1D grid (1 x n)
        if len(remaining) == n:
            grid = [[int(x) for x in remaining]]
            r, c = 1, n
        # If we have r and c, parse as 2D grid
        elif len(remaining) > n:
            r = n
            c_val = int(remaining[0]) if remaining else n
            # Check if we have enough for a r x c grid
            if len(remaining) >= r * c_val:
                c = c_val
                grid = []
                idx = 1
                for _ in range(r):
                    row = [int(remaining[idx + j]) for j in range(c)]
                    grid.append(row)
                    idx += c
            else:
                # Fallback: treat as 1D
                c = n
                grid = [[int(x) for x in remaining[:n]]]
        else:
            grid = [[int(x) for x in remaining]]
            r, c = 1, len(remaining)

        result = minutes_to_light(grid)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
