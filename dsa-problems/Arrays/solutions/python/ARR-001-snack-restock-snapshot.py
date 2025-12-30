import sys

def prefix_averages(arr: list[int]) -> list[int]:
    """
    Calculate prefix averages for each position.
    """
    n = len(arr)
    result = []
    running_sum = 0

    for i in range(n):
        running_sum += arr[i]
        # Integer division //
        result.append(running_sum // (i + 1))

    return result

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = prefix_averages(arr)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

