def knight_tour_possible(n: int, blocked: list[list[bool]]) -> bool:
    """
    Check if a knight can visit all unblocked cells starting from (0,0).
    Uses backtracking with Warnsdorff's heuristic.
    """
    total_unblocked = sum(not cell for row in blocked for cell in row)
    if total_unblocked == 0 or (total_unblocked == 1 and not blocked[0][0]):
        return True
    if blocked[0][0]:
        return False

    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    visited = [[False] * n for _ in range(n)]

    def count_onward(r, c):
        """Count valid onward moves from position (r,c)"""
        cnt = 0
        for dr, dc in knight_moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not blocked[nr][nc] and not visited[nr][nc]:
                cnt += 1
        return cnt

    def is_isolated():
        """Check if any unvisited cell is unreachable from any other unvisited cell"""
        # For performance, skip expensive connectivity checks for larger boards
        if n > 6:
            return False

        unvisited = []
        for i in range(n):
            for j in range(n):
                if not blocked[i][j] and not visited[i][j]:
                    unvisited.append((i, j))

        if not unvisited:
            return False

        # BFS from first unvisited to see if all others are reachable
        from collections import deque
        q = deque([unvisited[0]])
        seen = {unvisited[0]}

        while q:
            r, c = q.popleft()
            for dr, dc in knight_moves:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and not blocked[nr][nc] and
                    not visited[nr][nc] and (nr, nc) not in seen):
                    if (nr, nc) in set(unvisited):
                        seen.add((nr, nc))
                        q.append((nr, nc))

        return len(seen) < len(unvisited)

    def dfs(r, c, count):
        # Found a complete tour
        if count == total_unblocked:
            return True

        # Connectivity check for small boards
        if is_isolated():
            return False

        # Get all valid next moves and sort by Warnsdorff's heuristic
        next_moves = []
        for dr, dc in knight_moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not blocked[nr][nc] and not visited[nr][nc]:
                priority = count_onward(nr, nc)
                next_moves.append((priority, nr, nc))

        if not next_moves:
            return False

        # Sort by priority (ascending) - visit less accessible cells first
        next_moves.sort()

        for _, nr, nc in next_moves:
            visited[nr][nc] = True
            if dfs(nr, nc, count + 1):
                return True
            visited[nr][nc] = False

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
