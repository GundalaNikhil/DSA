def closest_pair_circular(arr: list[int]) -> list[int]:
    """Find pair of adjacent indices with minimum difference"""
    n = len(arr)
    if n < 2:
        return [0, 1] if n == 2 else [0, 0]

    # Find the pair of adjacent indices with minimum difference
    min_diff = float('inf')
    min_idx = 0

    for i in range(n):
        next_i = (i + 1) % n
        diff = abs(arr[i] - arr[next_i])
        if diff < min_diff:
            min_diff = diff
            min_idx = i

    next_idx = (min_idx + 1) % n
    return sorted([min_idx, next_idx])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = closest_pair_circular(arr)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
