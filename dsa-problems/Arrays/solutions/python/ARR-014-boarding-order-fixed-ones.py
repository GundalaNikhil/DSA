import sys

def sort_with_fixed_ones(arr: list[int]) -> None:
    left = 0
    right = len(arr) - 1

    while left < right:
        # Move left past 0s and 1s
        while left < right and (arr[left] == 0 or arr[left] == 1):
            left += 1

        # Move right past 2s and 1s
        while left < right and (arr[right] == 2 or arr[right] == 1):
            right -= 1

        if left < right:
            # Swap arr[left] (which is 2) and arr[right] (which is 0)
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sort_with_fixed_ones(arr)
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()

