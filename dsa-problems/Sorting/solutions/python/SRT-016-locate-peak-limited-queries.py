def find_peak(arr: list[int], q_limit: int) -> int:
    """Find peak index using linear scan"""
    n = len(arr)

    if n == 1:
        return 0

    # Check first element
    if arr[0] > arr[1]:
        return 0

    # Check middle elements
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i

    # Check last element
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    return 0

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_peak(arr, n)
    print(result)

if __name__ == "__main__":
    main()
