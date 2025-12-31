import sys

def zero_slide_with_limit(arr: list[int], m: int) -> list[int]:
    """
    Move zeros to end with swap limit.
    """
    n = len(arr)
    write_idx = 0

    for read_idx in range(n):
        if arr[read_idx] != 0:
            if read_idx != write_idx:
                if m <= 0:
                    break
                # Swap
                arr[write_idx], arr[read_idx] = arr[read_idx], arr[write_idx]
                m -= 1
            write_idx += 1

    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    result = zero_slide_with_limit(arr, m)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

