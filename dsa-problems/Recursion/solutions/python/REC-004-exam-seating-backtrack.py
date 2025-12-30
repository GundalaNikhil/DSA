def count_arrangements(n: int, k: int, d: int) -> int:
    memo = {}

    def backtrack(idx, remaining_k):
        if remaining_k == 0:
            return 1
        if idx >= n:
            return 0
        
        state = (idx, remaining_k)
        if state in memo:
            return memo[state]
        
        # Option 1: Place student here
        # Next valid index is idx + 1 (current occupied) + d (gap)
        res = backtrack(idx + 1 + d, remaining_k - 1)
        
        # Option 2: Skip this seat
        res += backtrack(idx + 1, remaining_k)
        
        memo[state] = res
        return res

    return backtrack(0, k)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
