def longest_after_change(arr: list[int]) -> int:
    """
    Find the longest strictly increasing contiguous subarray
    after changing at most one element.

    Algorithm:
    1. Compute L[i] = length of strictly increasing subarray ending at i
    2. Compute R[i] = length of strictly increasing subarray starting at i
    3. For each position i (to change arr[i]):
       - Option 1: Extend left only: L[i-1] + 1
       - Option 2: Extend right only: R[i+1] + 1
       - Option 3: Bridge both: L[i-1] + 1 + R[i+1] (if arr[i+1] - arr[i-1] >= 2)
    """
    n = len(arr)
    if n <= 1:
        return n

    # L[i] = length of strictly increasing subarray ending at i
    L = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            L[i] = L[i-1] + 1

    # R[i] = length of strictly increasing subarray starting at i
    R = [1] * n
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i+1]:
            R[i] = R[i+1] + 1

    # Maximum without any change
    max_len = max(L)

    # Try changing each position
    for i in range(n):
        # Extend left only
        if i > 0:
            max_len = max(max_len, L[i-1] + 1)

        # Extend right only
        if i < n - 1:
            max_len = max(max_len, R[i+1] + 1)

        # Bridge both sides (if gap allows)
        if i > 0 and i < n - 1 and arr[i+1] - arr[i-1] >= 2:
            max_len = max(max_len, L[i-1] + 1 + R[i+1])

    return max_len

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_after_change(arr)
    print(result)

if __name__ == "__main__":
    main()
