import sys

memo = {}


def get_encoded(s):
    if len(s) < 5:
        return s
    if s in memo:
        return memo[s]
    n = len(s)
    best = s
    for i in range(1, n):
        left = get_encoded(s[:i])
        right = get_encoded(s[i:])
        cand = left + right
        if len(cand) < len(best):
            best = cand
        elif len(cand) == len(best):
            best = min(best, cand)
            for k in range(1, n // 2 + 1):
                if n % k == 0:
                    sub = s[:k]
                    is_periodic = True
                    for start in range(k, n, k):
                        if s[start : start + k] != sub:
                            is_periodic = False
                            break
                        if is_periodic:
                            count = n // k
                            compressed = f"{count}({get_encoded(sub)})"
                            if len(compressed) < len(best):
                                best = compressed
                            elif len(compressed) == len(best):
                                best = min(best, compressed)
                                memo[s] = best
                                return best


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("")
        return
    print(get_encoded(s))


if __name__ == "__main__":
    solve()
