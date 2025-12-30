def longest_alternating_vc(s: str) -> tuple:
    def is_vowel(c):
        return c in 'aeiou'

    if not s:
        return (0, "")

    max_len = 1
    best_start = 0
    current_len = 1
    start = 0
    prev_is_vowel = is_vowel(s[0])

    for i in range(1, len(s)):
        curr_is_vowel = is_vowel(s[i])
        if curr_is_vowel != prev_is_vowel:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                best_start = start
        else:
            start = i
            current_len = 1
        prev_is_vowel = curr_is_vowel

    return (max_len, s[best_start:best_start + max_len])


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
