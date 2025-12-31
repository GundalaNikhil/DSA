import sys

def weighted_balance_point(a: list[int], L: int, R: int) -> int:
    """
    Find smallest index i where L * sum(left) == R * sum(right).
    """
    total_sum = sum(a)
    left_sum = 0

    for i, x in enumerate(a):
        # right_sum excludes current element x
        right_sum = total_sum - left_sum - x

        if left_sum * L == right_sum * R:
            return i

        left_sum += x

    return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    L, R = map(int, input().split())

    result = weighted_balance_point(a, L, R)
    print(result)

if __name__ == "__main__":
    main()

