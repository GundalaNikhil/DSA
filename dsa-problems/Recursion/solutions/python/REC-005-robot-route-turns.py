def count_paths(r: int, c: int, T: int) -> int:
    """
    Count all paths from (0,0) to (r-1,c-1) with at most T turns.
    Can move right (dir 0) or down (dir 1).
    First move doesn't count as a turn.
    """
    memo = {}

    def dfs(row, col, last_dir, turns):
        # Base case: reached destination
        if row == r - 1 and col == c - 1:
            return 1

        # Pruning: too many turns
        if turns > T:
            return 0

        # Memoization key
        key = (row, col, last_dir, turns)
        if key in memo:
            return memo[key]

        count = 0

        # Direction 0: Right (col + 1)
        if col + 1 <= c - 1:
            new_turns = turns
            if last_dir != -1 and last_dir != 0:
                new_turns += 1
            count += dfs(row, col + 1, 0, new_turns)

        # Direction 1: Down (row + 1)
        if row + 1 <= r - 1:
            new_turns = turns
            if last_dir != -1 and last_dir != 1:
                new_turns += 1
            count += dfs(row + 1, col, 1, new_turns)

        memo[key] = count
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
