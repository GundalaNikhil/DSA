import sys

# Increase recursion depth for deep grids
sys.setrecursionlimit(2000)

def count_paths(r: int, c: int) -> int:
    memo = {}

    def helper(i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        res = helper(i - 1, j) + helper(i, j - 1)
        memo[state] = res
        return res

    return helper(r - 1, c - 1)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
