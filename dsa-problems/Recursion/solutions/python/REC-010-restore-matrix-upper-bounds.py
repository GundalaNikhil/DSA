def restore_matrix(row_sums: list[int], col_sums: list[int], bounds: list[list[int]]) -> list[list[int]]:
    R = len(row_sums)
    C = len(col_sums)
    matrix = [[0] * C for _ in range(R)]

    def backtrack(r, c):
        if r == R:
            return all(x == 0 for x in col_sums)

        next_r = r + 1 if c == C - 1 else r
        next_c = 0 if c == C - 1 else c + 1

        # Optimization: If last column, value is fixed
        if c == C - 1:
            val = row_sums[r]
            if 0 <= val <= bounds[r][c] and val <= col_sums[c]:
                matrix[r][c] = val
                row_sums[r] -= val
                col_sums[c] -= val
                if backtrack(next_r, next_c):
                    return True
                row_sums[r] += val
                col_sums[c] += val
            return False

        # Determine range
        max_val = min(bounds[r][c], row_sums[r], col_sums[c])
        
        # Try values descending
        for val in range(max_val, -1, -1):
            matrix[r][c] = val
            row_sums[r] -= val
            col_sums[c] -= val
            if backtrack(next_r, next_c):
                return True
            row_sums[r] += val
            col_sums[c] += val
        
        return False

    if backtrack(0, 0):
        return matrix
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
