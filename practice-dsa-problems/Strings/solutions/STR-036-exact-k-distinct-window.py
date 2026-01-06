import sys


def count_at_most(s, k):
    if k == 0:
        return 0
    n = len(s)
    l = 0
    counts = {}
    distinct = 0
    total = 0
    for r in range(n):
        char = s[r]
        if char not in counts or counts[char] == 0:
            distinct += 1
            counts[char] = 1
        else:
            counts[char] += 1
            while distinct > k:
                left_char = s[l]
                counts[left_char] -= 1
                if counts[left_char] == 0:
                    distinct -= 1
                    l += 1
                    total += r - l + 1
                    distinct -= 1
                    l += 1
            total += r - l + 1
            
    return total


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    k = int(input_data[1])
    print(count_at_most(s, k) - count_at_most(s, k - 1))


if __name__ == "__main__":
    solve()
