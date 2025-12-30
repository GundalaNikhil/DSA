import sys

def merge_with_priority(A: list[int], B: list[int]) -> list[int]:
    n = len(A)
    m = len(B)
    result = []

    i = 0
    j = 0

    while i < n and j < m:
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    # Append remaining
    if i < n:
        result.extend(A[i:])
    if j < m:
        result.extend(B[j:])

    return result

def main():
    n = int(input())
    A = list(map(int, input().split())) if n > 0 else []
    m = int(input())
    B = list(map(int, input().split())) if m > 0 else []

    result = merge_with_priority(A, B)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
