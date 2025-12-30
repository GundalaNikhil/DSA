import sys

def min_planks_for_roof(height: list[int]) -> int:
    n = len(height)
    if n == 0: return 0

    L = [0] * n
    SumL = [0] * n

    L[0] = height[0]
    SumL[0] = height[0]
    for i in range(1, n):
        L[i] = max(height[i], L[i-1])
        SumL[i] = SumL[i-1] + L[i]

    R = [0] * n
    SumR = [0] * n

    R[n-1] = height[n-1]
    SumR[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        R[i] = max(height[i], R[i+1])
        SumR[i] = SumR[i+1] + R[i]

    min_total_height = float('inf')

    for i in range(n):
        # min(L[i], R[i]) is subtracted because it is double counted in SumL and SumR
        # And peak must be max(L[i], R[i]).
        # Formula derivation: SumL (ends at L[i]) + SumR (starts at R[i]).
        # If we align at Peak = H, we add (H-L[i]) to LeftSum and (H-R[i]) to RightSum
        # Total = SumL + (H-L) + SumR + (H-R) - H (overlap)
        # = SumL + SumR + H - L - R
        # With H = max(L, R), this simplifies to SumL + SumR - min(L, R).

        current_total = SumL[i] + SumR[i] - min(L[i], R[i])
        min_total_height = min(min_total_height, current_total)

    return min_total_height - sum(height)

def main():
    n = int(input())
    height = list(map(int, input().split()))

    result = min_planks_for_roof(height)
    print(result)

if __name__ == "__main__":
    main()

