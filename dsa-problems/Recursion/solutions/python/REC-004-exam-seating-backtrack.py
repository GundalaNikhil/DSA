def count_nqueens(n: int) -> int:
    """Count the number of ways to place n queens on an n×n chessboard.
    Uses bitwise operations and memoization for optimization.
    """
    memo = {}

    def backtrack(row, cols, diag1, diag2):
        # Memoization key
        key = (row, cols, diag1, diag2)
        if key in memo:
            return memo[key]

        # Base case: all queens placed
        if row == n:
            return 1

        count = 0
        # Try placing queen in each valid column
        for col in range(n):
            # Check if column and diagonals are available using bitwise AND
            if not (cols & (1 << col)):
                d1 = row - col + n  # Offset to make positive
                d2 = row + col

                if not (diag1 & (1 << d1)) and not (diag2 & (1 << d2)):
                    # Place queen and recurse
                    count += backtrack(
                        row + 1,
                        cols | (1 << col),
                        diag1 | (1 << d1),
                        diag2 | (1 << d2)
                    )

        memo[key] = count
        return count

    return backtrack(0, 0, 0, 0)

def main():
    import sys
    n = int(sys.stdin.read().strip())
    result = count_nqueens(n)
    print(result)

if __name__ == "__main__":
    main()
