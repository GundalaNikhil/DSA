def find_path(grid: list[list[int]], T: int) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = [(0, 0)]
    visited[0][0] = True
    
    # Directions: 0:Up, 1:Down, 2:Left, 3:Right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c, last_dir, turns):
        if r == rows - 1 and c == cols - 1:
            return True
        
        for i, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                new_turns = turns
                if last_dir != -1 and i != last_dir:
                    new_turns += 1
                
                if new_turns <= T:
                    visited[nr][nc] = True
                    path.append((nr, nc))
                    if dfs(nr, nc, i, new_turns):
                        return True
                    path.pop()
                    visited[nr][nc] = False
        return False

    if dfs(0, 0, -1, 0):
        return path
    return []


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
