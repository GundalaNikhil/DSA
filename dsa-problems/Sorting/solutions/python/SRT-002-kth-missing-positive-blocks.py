def solve(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    results = []
    n = len(arr)

    for k, b in queries:
        m = k * b

        # Binary search
        low, high = 0, n - 1
        idx = -1

        while low <= high:
            mid = (low + high) // 2
            missing_count = arr[mid] - (mid + 1)
            if missing_count < m:
                idx = mid
                low = mid + 1
            else:
                high = mid - 1

        results.append(m + idx + 1)

    return results

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        k, b = map(int, input().split())
        queries.append((k, b))

    results = solve(arr, queries)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
