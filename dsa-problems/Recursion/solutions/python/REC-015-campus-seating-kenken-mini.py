def solve_latin_square(n: int) -> list[list[int]]:
    """Generate a Latin square of size n×n (cyclic Latin square)."""
    grid = [[0] * n for _ in range(n)]

    def is_valid(row, col, num):
        # Check row
        for j in range(col):
            if grid[row][j] == num:
                return False
        # Check column
        for i in range(row):
            if grid[i][col] == num:
                return False
        return True

    def backtrack(pos):
        if pos == n * n:
            return True
        row = pos // n
        col = pos % n
        for num in range(1, n + 1):
            if is_valid(row, col, num):
                grid[row][col] = num
                if backtrack(pos + 1):
                    return True
                grid[row][col] = 0
        return False

    if backtrack(0):
        return grid
    return []

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return
    n = int(lines[0])
    result = solve_latin_square(n)
    if result:
        for row in result:
            print(' '.join(map(str, row)))
    else:
        print("NONE")

if __name__ == "__main__":
    main()
