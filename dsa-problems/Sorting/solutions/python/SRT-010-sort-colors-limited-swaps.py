def sort_with_swaps(arr: list[int], S: int) -> bool:
    """Check if array can be fully sorted with at most S adjacent swaps"""
    n = len(arr)

    # Count minimum swaps needed (inversions)
    swaps_needed = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps_needed += 1

    return swaps_needed <= S

def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    result = sort_with_swaps(arr, s)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
