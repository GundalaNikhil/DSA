import sys

def has_pair_with_forbidden(arr: list[int], target: int, forbidden: set[int]) -> bool:
    left = 0
    right = len(arr) - 1

    while left < right:
        # Skip forbidden indices on the left
        while left < right and left in forbidden:
            left += 1
        # Skip forbidden indices on the right
        while left < right and right in forbidden:
            right -= 1

        # Check if we still have valid pointers
        if left >= right:
            break

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    f = int(input())
    forbidden = set(map(int, input().split())) if f > 0 else set()

    result = has_pair_with_forbidden(arr, target, forbidden)
    print("true" if result else "false")

if __name__ == "__main__":
    main()

