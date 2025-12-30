def count_nqueens(n: int) -> int:
    """Count the number of ways to place n queens on an n×n chessboard."""
    def is_safe(row, col, placements):
        # placements[i] = column of queen in row i
        for i in range(row):
            # Check column
            if placements[i] == col:
                return False
            # Check diagonals
            if abs(placements[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row, placements):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(row, col, placements):
                placements[row] = col
                count += backtrack(row + 1, placements)
                placements[row] = -1
        return count

    return backtrack(0, [-1] * n)

def main():
    import sys
    n = int(sys.stdin.read().strip())
    result = count_nqueens(n)
    print(result)

if __name__ == "__main__":
    main()
