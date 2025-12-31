import sys

def bench_flip_locked_ends(arr: list[int]) -> None:
    """
    Reverse array in-place, locking first and last elements.
    """
    n = len(arr)
    if n < 3:
        return
        
    left = 1
    right = n - 2
    
    while left < right:
        # Swap
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    bench_flip_locked_ends(arr)
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()

