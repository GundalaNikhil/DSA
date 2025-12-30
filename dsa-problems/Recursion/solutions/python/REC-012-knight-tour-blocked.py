def knight_tour_possible(n: int, blocked: list[list[bool]]) -> bool:
    total_unblocked = sum(not cell for row in blocked for cell in row)
    visited = [[False] * n for _ in range(n)]
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def dfs(r, c, count):
        if count == total_unblocked:
            return True
        for dr, dc in moves:
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
            r, c = map(int, lines[i].split())
            blocked[r][c] = True
    result = knight_tour_possible(n, blocked)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
