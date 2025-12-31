def sort_with_swaps(arr: list[int], S: int) -> bool:
    """Check if array can be fully sorted with at most S swaps"""
    n = len(arr)

    # Count 0s, 1s to determine zones
    # Zone 0: positions 0 to count_0-1 (should contain 0s)
    # Zone 1: positions count_0 to count_0+count_1-1 (should contain 1s)
    # Zone 2: positions count_0+count_1 to n-1 (should contain 2s)

    count_0 = arr.count(0)
    count_1 = arr.count(1)

    # Count misplaced elements (elements not in their correct zone)
    misplaced = 0
    for i in range(n):
        if arr[i] == 0 and i >= count_0:
            misplaced += 1
        elif arr[i] == 1 and (i < count_0 or i >= count_0 + count_1):
            misplaced += 1
        elif arr[i] == 2 and i < count_0 + count_1:
            misplaced += 1

    # Each swap can fix 2 misplaced elements
    swaps_needed = misplaced // 2
    return swaps_needed <= S

def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    result = sort_with_swaps(arr, s)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
