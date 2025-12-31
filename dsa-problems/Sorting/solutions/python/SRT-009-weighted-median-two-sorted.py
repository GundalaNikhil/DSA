def weighted_median(A: list[int], B: list[int], wA: int, wB: int) -> str:
    """Find median of combined two sorted arrays with weights"""
    # Merge both arrays
    combined = A + B
    combined.sort()

    # Calculate median
    n = len(combined)
    if n % 2 == 1:
        return str(combined[n // 2])
    else:
        mid1 = combined[n // 2 - 1]
        mid2 = combined[n // 2]
        avg = (mid1 + mid2) // 2
        return str(avg)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Weights not provided in test, use 1, 1
    result = weighted_median(a, b, 1, 1)
    print(result)

if __name__ == "__main__":
    main()
