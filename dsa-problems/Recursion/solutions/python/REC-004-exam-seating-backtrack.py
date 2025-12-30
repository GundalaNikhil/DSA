def count_nqueens(n: int) -> int:
    """Count the number of ways to place n queens on an n×n chessboard."""
    def backtrack(row, cols, diag1, diag2):
        # cols: set of columns with queens
        # diag1: set of diagonals (row - col) with queens
        # diag2: set of diagonals (row + col) with queens
        if row == n:
            return 1

        count = 0
        for col in range(n):
            d1 = row - col
            d2 = row + col

            if col not in cols and d1 not in diag1 and d2 not in diag2:
                # Place queen and recurse
                count += backtrack(
                    row + 1,
                    cols | {col},
                    diag1 | {d1},
                    diag2 | {d2}
                )

        return count

    return backtrack(0, set(), set(), set())

def main():
    import sys
    n = int(sys.stdin.read().strip())
    result = count_nqueens(n)
    print(result)

if __name__ == "__main__":
    main()
