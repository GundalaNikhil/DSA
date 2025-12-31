def min_swaps_to_sort(arr: list[int], k: int) -> int:
    """
    Count elements that violate the k-sorted property.

    An element violates k-sorted if it is more than k positions away
    from its target position in the sorted array.

    Returns: (violation_count // (k + 1))
    """
    n = len(arr)
    if n <= 1:
        return 0

    # Get sorted array to find target positions
    sorted_arr = sorted(arr)

    # Count violations: elements more than k distance from their target
    violations = 0
    for i in range(n):
        # Find where arr[i] should be in sorted array
        # For duplicates, we need to match greedily
        sorted_pos = -1
        for j in range(n):
            if sorted_arr[j] == arr[i]:
                sorted_pos = j
                sorted_arr[j] = None  # Mark as used
                break

        # Restore for next iteration
        sorted_arr[sorted_pos] = arr[i]

        # Check if distance exceeds k
        distance = abs(i - sorted_pos)
        if distance > k:
            violations += 1

    # Return violations scaled by (k+1)
    return violations // (k + 1)

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = min_swaps_to_sort(arr, k)
    print(result)

if __name__ == "__main__":
    main()
