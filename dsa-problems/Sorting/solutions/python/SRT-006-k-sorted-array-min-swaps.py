def min_swaps_to_sort(arr: list[int]) -> int:
    n = len(arr)
    # Create list of (value, original_index)
    pairs = [(arr[i], i) for i in range(n)]
    # Sort by value to get target positions
    sorted_pairs = sorted(pairs)

    # Create a position mapping: where should each position's element go?
    # position_map[i] tells us where the element at position i should go
    position_map = [0] * n
    for target_pos, (value, orig_pos) in enumerate(sorted_pairs):
        position_map[orig_pos] = target_pos

    visited = [False] * n
    swaps = 0

    # Find cycles in the permutation
    for i in range(n):
        if visited[i]:
            continue

        # Start a new cycle
        cycle_size = 0
        current = i
        while not visited[current]:
            visited[current] = True
            current = position_map[current]
            cycle_size += 1

        # Each cycle of size k needs k-1 swaps
        if cycle_size > 1:
            swaps += (cycle_size - 1)

    return swaps

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = min_swaps_to_sort(arr)
    print(result)

if __name__ == "__main__":
    main()
