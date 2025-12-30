def knight_tour_possible(n: int, blocked: list[list[bool]]) -> bool:
    """
    Check if a knight can visit all unblocked cells starting from (0,0).
    Uses backtracking with DFS to find a Hamiltonian path.
    """
    total_unblocked = sum(not cell for row in blocked for cell in row)
    visited = [[False] * n for _ in range(n)]
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    def dfs(r, c, count):
        # Found a complete tour
        if count == total_unblocked:
            return True

        # Pruning: if remaining unblocked cells are less than what we can reach, return False
        # This is an optional optimization
        for dr, dc in knight_moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not blocked[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                if dfs(nr, nc, count + 1):
                    return True
                visited[nr][nc] = False

        return False

    if blocked[0][0]:
        return False

    visited[0][0] = True
    return dfs(0, 0, 1)

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    n = int(lines[0])
    b = int(lines[1])
    blocked = [[False] * n for _ in range(n)]

    for i in range(2, 2 + b):
        if i < len(lines):
            parts = lines[i].strip().split()
            if len(parts) >= 2:
                r, c = int(parts[0]), int(parts[1])
                if 0 <= r < n and 0 <= c < n:
                    blocked[r][c] = True

    result = knight_tour_possible(n, blocked)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
