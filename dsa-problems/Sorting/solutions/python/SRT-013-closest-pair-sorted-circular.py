def closest_pair_circular(arr: list[int]) -> list[int]:
    """Find two indices whose sum of values is closest to the target (max + min)"""
    n = len(arr)
    if n < 2:
        return [0, 1] if n == 2 else [0, 0]

    # Find the pivot (minimum element index)
    pivot = 0
    for i in range(1, n):
        if arr[i] < arr[pivot]:
            pivot = i

    # Use two pointers
    left = 0
    right = n - 1
    min_diff = float('inf')
    res_left, res_right = 0, 1

    # Target is ideally arr[n-1] + arr[0] (max + min in the rotated array)
    while left < right:
        i = (pivot + left) % n
        j = (pivot + right) % n

        curr_sum = arr[i] + arr[j]
        # The target sum we want is the sum of largest and smallest
        target = arr[(pivot - 1) % n] + arr[pivot]  # max + min
        diff = abs(curr_sum - target)

        if diff < min_diff:
            min_diff = diff
            res_left, res_right = i, j

        if curr_sum < target:
            left += 1
        else:
            right -= 1

    return sorted([res_left, res_right])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = closest_pair_circular(arr)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
