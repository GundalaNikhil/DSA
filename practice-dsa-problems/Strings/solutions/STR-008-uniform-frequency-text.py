import sys
from collections import Counter


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("true")
        return
    counts = Counter(s)
    freqs = set(counts.values())
    if len(freqs) <= 1:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    solve()
