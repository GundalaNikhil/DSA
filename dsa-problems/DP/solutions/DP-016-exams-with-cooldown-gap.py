from bisect import bisect_right
from typing import List, Tuple

def max_score(exams: List[Tuple[int, int, int]], g: int) -> int:
    exams = sorted(exams, key=lambda x: x[1])
    ends = [e for _, e, _ in exams]
    n = len(exams)
    dp = [0] * (n + 1)
    for i, (s, e, w) in enumerate(exams, start=1):
        j = bisect_right(ends, s - g)
        dp[i] = max(dp[i - 1], dp[j] + w)
    return dp[n]


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
