def solve_latin_square(n: int) -> list[list[int]]:
    """Generate a cyclic Latin square of size n×n."""
    # A cyclic Latin square has row i containing elements shifted by i positions
    grid = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            grid[i][j] = ((i + j) % n) + 1

    return grid

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
