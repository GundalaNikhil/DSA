def count_combinations(values: list[int], target: int) -> int:
    """
    Count the number of combinations (with repetition allowed) that sum to target.
    For each value, we can use it 0 or more times.
    """
    count = 0

    def backtrack(index, current_sum):
        nonlocal count

        # Base case: we've considered all values
        if index == len(values):
            if current_sum == target:
                count += 1
            return

        # Pruning: if current sum already exceeds target, no point continuing
        if current_sum > target:
            return

        value = values[index]

        # Option 1: Don't take any of the current value
        backtrack(index + 1, current_sum)

        # Option 2: Take 1 or more of this value
        # Keep adding as long as we don't exceed target
        count_used = 1
        while current_sum + value * count_used <= target:
            backtrack(index + 1, current_sum + value * count_used)
            count_used += 1

    backtrack(0, 0)
    return count

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    first_line = list(map(int, lines[0].split()))
    n = first_line[0]
    target = first_line[1]
    values = list(map(int, lines[1].split()))

    result = count_combinations(values, target)
    print(result)

if __name__ == "__main__":
    main()
