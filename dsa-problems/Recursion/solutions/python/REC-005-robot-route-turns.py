def count_paths(r: int, c: int, T: int) -> int:
    memo = {}
    def dfs(row, col, last_dir, turns):
        if row == r - 1 and col == c - 1:
            return 1
        if (row, col, last_dir, turns) in memo:
            return memo[(row, col, last_dir, turns)]
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir_idx, (dr, dc) in enumerate(directions):
            nr, nc = row + dr, col + dc
            if 0 <= nr < r and 0 <= nc < c:
                new_turns = turns
                if last_dir != -1 and dir_idx != last_dir:
                    new_turns += 1
                if new_turns <= T:
                    count += dfs(nr, nc, dir_idx, new_turns)
        memo[(row, col, last_dir, turns)] = count
        return count
    return dfs(0, 0, -1, 0)

def main():
    import sys
    first_line = sys.stdin.read().strip().split()
    r = int(first_line[0])
    c = int(first_line[1])
    T = int(first_line[2])
    result = count_paths(r, c, T)
    print(result)

if __name__ == "__main__":
    main()
