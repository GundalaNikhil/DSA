import sys
from collections import Counter


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print(0)
        return
    counts = Counter(s)
    total = 0
    for char in counts:
        n = counts[char]
        total += (n * (n + 1)) // 2
        
    print(total)


if __name__ == "__main__":
    solve()
