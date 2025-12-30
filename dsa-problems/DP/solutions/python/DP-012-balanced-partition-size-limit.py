def min_larger_group_size(a: list[int], D: int) -> int:
    n = len(a)
    total = sum(a)
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for x in a:
        for k in range(n - 1, -1, -1):
            for s in list(dp[k]):
                dp[k + 1].add(s + x)

    ans = None
    for k in range(n + 1):
        for s in dp[k]:
            if abs(total - 2 * s) <= D:
                cand = max(k, n - k)
                if ans is None or cand < ans:
                    ans = cand
    return -1 if ans is None else ans


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
