def min_swaps_to_sort(arr: list[int]) -> int:
    n = len(arr)
    if n <= 1:
        return 0

    # Create indexed pairs with stable sort for duplicates
    indexed = [(arr[i], i) for i in range(n)]
    sorted_indexed = sorted(indexed, key=lambda x: (x[0], x[1]))

    # Create position mapping
    position_map = [0] * n
    for sorted_pos, (val, orig_pos) in enumerate(sorted_indexed):
        position_map[orig_pos] = sorted_pos

    visited = [False] * n
    swaps = 0

    # Count cycles
    for i in range(n):
        if visited[i]:
            continue

        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = position_map[j]
            cycle_len += 1

        if cycle_len > 1:
            swaps += cycle_len - 1

    return swaps

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = min_swaps_to_sort(arr)
    print(result)

if __name__ == "__main__":
    main()
