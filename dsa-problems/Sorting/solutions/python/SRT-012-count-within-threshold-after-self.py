def count_within_threshold(arr: list[int], T: int) -> list[int]:
    """For each i, count elements j>i where a[j]-a[i] <= T"""
    n = len(arr)
    counts = [0] * n

    # For each element, count right elements where a[j] - a[i] <= T
    # This means a[j] <= a[i] + T
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] - arr[i] <= T:
                counts[i] += 1

    return counts

def main():
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_within_threshold(arr, t)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
