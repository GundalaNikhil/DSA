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
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = []
        for _ in range(n):
            A.append(int(next(iterator)))
            
        m = int(next(iterator))
        B = []
        for _ in range(m):
            B.append(int(next(iterator)))
            
        result = merge_with_priority(A, B)
        print(" ".join(map(str, result)))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
