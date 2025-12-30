def restore_matrix(row_sums: list[int], col_sums: list[int]) -> list[list[int]]:
    R = len(row_sums)
    C = len(col_sums)
    matrix = [[0] * C for _ in range(R)]
    row_sums_copy = list(row_sums)
    col_sums_copy = list(col_sums)

    def backtrack(r, c):
        if r == R:
            return all(x == 0 for x in col_sums_copy)
        next_r = r + 1 if c == C - 1 else r
        next_c = 0 if c == C - 1 else c + 1
        if c == C - 1:
            val = row_sums_copy[r]
            if 0 <= val <= col_sums_copy[c]:
                matrix[r][c] = val
                row_sums_copy[r] -= val
                col_sums_copy[c] -= val
                if backtrack(next_r, next_c):
                    return True
                row_sums_copy[r] += val
                col_sums_copy[c] += val
            return False
        max_val = min(row_sums_copy[r], col_sums_copy[c])
        for val in range(max_val, -1, -1):
            matrix[r][c] = val
            row_sums_copy[r] -= val
            col_sums_copy[c] -= val
            if backtrack(next_r, next_c):
                return True
            row_sums_copy[r] += val
            col_sums_copy[c] += val
        return False

    if backtrack(0, 0):
        return matrix
    return []

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 3:
        return
    r, c = map(int, lines[0].split())
    row_sums = list(map(int, lines[1].split()))
    col_sums = list(map(int, lines[2].split()))
    result = restore_matrix(row_sums, col_sums)
    if result:
        for row in result:
            print(' '.join(map(str, row)))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
