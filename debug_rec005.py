def count_paths(r: int, c: int, T: int) -> int:
    memo = {}
    path_trace = []

    def dfs(row, col, last_dir, turns):
        if row == r - 1 and col == c - 1:
            print(f"Path found! Turns: {turns} trace: {path_trace}")
            return 1

        if turns > T:
            # print(f"Pruned at {row},{col} turns {turns}")
            return 0

        key = (row, col, last_dir, turns)
        if key in memo:
            return memo[key]

        count = 0

        # Dir 0: Right (col + 1)
        if col + 1 <= c - 1:
            new_turns = turns
            if last_dir != -1 and last_dir != 0:
                new_turns += 1
            path_trace.append('R')
            count += dfs(row, col + 1, 0, new_turns)
            path_trace.pop()

        # Dir 1: Down (row + 1)
        if row + 1 <= r - 1:
            new_turns = turns
            if last_dir != -1 and last_dir != 1:
                new_turns += 1
            path_trace.append('D')
            count += dfs(row + 1, col, 1, new_turns)
            path_trace.pop()

        memo[key] = count
        return count

    return dfs(0, 0, -1, 0)

import sys
print(count_paths(3, 3, 2))
