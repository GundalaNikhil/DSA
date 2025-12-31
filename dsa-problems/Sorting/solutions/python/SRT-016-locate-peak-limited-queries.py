def find_peak(arr: list[int], q_limit: int) -> int:
    """Find any peak index in the array"""
    n = len(arr)

    # Edge cases
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # Binary search for peak
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        left_ok = (mid == 0 or arr[mid] > arr[mid - 1])
        right_ok = (mid == n - 1 or arr[mid] > arr[mid + 1])

        if left_ok and right_ok:
            return mid

        # If left side is higher, peak must be on left
        if mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            # Peak must be on right
            low = mid + 1

    return 0  # Should not reach here

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_peak(arr, n)
    print(result)

if __name__ == "__main__":
    main()
