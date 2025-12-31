def closest_pair_circular(arr: list[int]) -> list[int]:
    """Find two indices of pair with minimum sum"""
    n = len(arr)
    if n < 2:
        return [0, 1] if n == 2 else [0, 0]

    # Find the indices of min and second min
    min_val = min(arr)
    min_idx = arr.index(min_val)

    # Find second min (could be same value if duplicates)
    second_min_val = float('inf')
    second_min_idx = -1
    for i in range(n):
        if i != min_idx and arr[i] < second_min_val:
            second_min_val = arr[i]
            second_min_idx = i

    return sorted([min_idx, second_min_idx])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = closest_pair_circular(arr)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
