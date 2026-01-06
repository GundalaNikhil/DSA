import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    k = int(input_data[1])
    n = len(s)
    counts = {}
    max_freq = 0
    l = 0
    best_len = 0
    for r in range(n):
        char = s[r]
        counts[char] = counts.get(char, 0) + 1
        max_freq = max(max_freq, counts[char])
        while (r - l + 1) - max_freq > k:
            counts[s[l]] -= 1
            l += 1
            best_len = max(best_len, r - l + 1)
            best_len = max(best_len, r - l + 1)
            
    print(best_len)


if __name__ == "__main__":
    solve()
