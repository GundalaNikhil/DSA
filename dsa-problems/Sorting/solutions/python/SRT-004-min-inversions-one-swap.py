def min_inversions_after_swap(arr: list[int]) -> int:
    n = len(arr)

    def count_inversions(a):
        """Count inversions using merge sort approach"""
        if len(a) <= 1:
            return 0
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        inv = count_inversions(left) + count_inversions(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                inv += len(left) - i
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

        return inv

    initial = count_inversions(arr.copy())

    max_reduction = 0
    # Try all possible swaps
    for i in range(n):
        for j in range(i + 1, n):
            # Swap and count inversions
            arr[i], arr[j] = arr[j], arr[i]
            inversions = count_inversions(arr.copy())
            reduction = initial - inversions
            max_reduction = max(max_reduction, reduction)
            # Swap back
            arr[i], arr[j] = arr[j], arr[i]

    return initial - max_reduction

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = min_inversions_after_swap(arr)
    print(result)

if __name__ == "__main__":
    main()
