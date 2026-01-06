import sys
from collections import Counter


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    s = input_data[0]
    l_len = int(input_data[1])
    k_top = int(input_data[2])
    if l_len > len(s):
        return
    counts = Counter()
    for i in range(len(s) - l_len + 1):
        counts[s[i : i + l_len]] += 1
        
    items = list(counts.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    for i in range(min(k_top, len(items))):
        print(f"{items[i][0]} {items[i][1]}")


if __name__ == "__main__":
    solve()
