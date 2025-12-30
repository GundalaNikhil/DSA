def pack_combinations(values: list[int], packs: list[int], target: int) -> list[list[int]]:
    """
    Find all combinations of tickets that sum to target.
    For each value i, we can take 0 or exactly pack[i] copies of values[i].
    """
    result = []

    def backtrack(index, current_sum, current_combination):
        # Base case: we've considered all values
        if index == len(values):
            if current_sum == target:
                result.append(current_combination[:])
            return

        # Pruning: if current sum already exceeds target, no point continuing
        if current_sum > target:
            return

        value = values[index]
        pack_count = packs[index]

        # Option 1: Don't take any of the current value
        backtrack(index + 1, current_sum, current_combination)

        # Option 2: Take 1 or more packs of this value
        # Keep adding full packs as long as we don't exceed target
        for num_packs in range(1, (target - current_sum) // (value * pack_count) + 1):
            # Add num_packs * pack_count tickets of this value
            total_tickets = num_packs * pack_count
            for _ in range(total_tickets):
                current_combination.append(value)

            backtrack(index + 1, current_sum + value * total_tickets, current_combination)

            # Remove the added tickets
            for _ in range(total_tickets):
                current_combination.pop()

    backtrack(0, 0, [])

    # Sort each combination and remove duplicates
    unique_results = []
    seen = set()
    for combo in result:
        sorted_combo = tuple(sorted(combo))
        if sorted_combo not in seen:
            seen.add(sorted_combo)
            unique_results.append(list(sorted_combo))

    unique_results.sort()
    return unique_results

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    values = [int(next(it)) for _ in range(n)]
    packs = [int(next(it)) for _ in range(n)]
    target = int(next(it))

    result = pack_combinations(values, packs, target)
    if not result:
        print("NONE")
    else:
        for combo in result:
            print(" ".join(str(x) for x in combo))

if __name__ == "__main__":
    main()
