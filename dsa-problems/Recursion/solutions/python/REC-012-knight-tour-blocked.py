def knight_tour(n: int, blocked: list[list[bool]]) -> list[tuple[int, int]]:
    total_unblocked = sum(not cell for row in blocked for cell in row)
    visited = [[False] * n for _ in range(n)]
    path = [(0, 0)]
    visited[0][0] = True
    
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    def dfs(r, c, count):
        if count == total_unblocked:
            return True
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not blocked[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                path.append((nr, nc))
                if dfs(nr, nc, count + 1):
                    return True
                path.pop()
                visited[nr][nc] = False
        return False

    if dfs(0, 0, 1):
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
