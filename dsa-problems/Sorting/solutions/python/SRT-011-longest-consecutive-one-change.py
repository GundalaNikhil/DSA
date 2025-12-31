def longest_after_change(arr: list[int]) -> int:
    """Max length of strictly increasing subarray with at most one change"""
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # L[i] = longest strictly increasing ending at i
    L = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            L[i] = L[i - 1] + 1

    # R[i] = longest strictly increasing starting at i
    R = [1] * n
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            R[i] = R[i + 1] + 1

    # Answer without changes
    answer = max(L)

    # Try changing each position
    for i in range(n):
        # Option 1: extend left (change arr[i] to arr[i-1] + 1)
        if i > 0:
            answer = max(answer, L[i - 1] + 1)

        # Option 2: extend right (change arr[i] to arr[i+1] - 1)
        if i < n - 1:
            answer = max(answer, 1 + R[i + 1])

        # Option 3: bridge left and right (change arr[i] to something in between)
        if i > 0 and i < n - 1:
            if arr[i + 1] - arr[i - 1] >= 2:
                answer = max(answer, L[i - 1] + 1 + R[i + 1])

    return answer

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_after_change(arr)
    print(result)

if __name__ == "__main__":
    main()
