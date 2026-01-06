import sys
from collections import Counter


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        pass
    s = input_data[0]
    r = input_data[1]
    f_limit = int(input_data[2])
    target_chars = set(r)
    n = len(s)
    counts = Counter()
    satisfied = 0
    needed = len(target_chars)
    best_len = float("inf")
    best_start = -1
    l = 0
    for r_idx in range(n):
        char = s[r_idx]
        if char in target_chars:
            counts[char] += 1
            if counts[char] == f_limit:
                satisfied += 1
                while satisfied == needed:
                    curr_len = r_idx - l + 1
                    if curr_len < best_len:
                        best_len = curr_len
                        best_start = l
                        char_l = s[l]
                        if char_l in target_chars:
                            if counts[char_l] == f_limit:
                                satisfied -= 1
                                counts[char_l] -= 1
                                l += 1
                        if best_start == -1:
                            # Not improved
                            pass
                        
    if best_start == -1:
        print("-1")
    else:
        print(s[best_start : best_start + best_len])


if __name__ == "__main__":
    solve()
