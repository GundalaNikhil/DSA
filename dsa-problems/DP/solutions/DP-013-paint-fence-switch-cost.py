from typing import List

def min_cost(n: int, k: int, s: List[int]) -> int:
    if k == 1:
        return n if n <= 2 else -1
    INF = 4 * 10**18
    dp1 = [1] * k
    dp2 = [INF] * k
    for i in range(1, n):
        best = [min(dp1[c], dp2[c]) for c in range(k)]
        min1 = min2 = INF
        c1 = -1
        for c, v in enumerate(best):
            if v < min1:
                min2 = min1
                min1 = v
                c1 = c
            elif v < min2:
                min2 = v
        ndp1 = [INF] * k
        ndp2 = [INF] * k
        for c in range(k):
            if dp1[c] < INF:
                ndp2[c] = dp1[c] + 1
            best_other = min1 if c != c1 else min2
            if best_other < INF:
                ndp1[c] = best_other + 1 + s[i]
        dp1, dp2 = ndp1, ndp2
    ans = min(min(dp1), min(dp2))
    return -1 if ans >= INF else ans


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
