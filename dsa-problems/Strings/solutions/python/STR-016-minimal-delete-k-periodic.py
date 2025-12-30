def minimal_delete_k_periodic(s: str, k: int) -> int:
    n = len(s)
    deletions = 0

    for pos in range(k):
        freq = {}

        # Count frequency of characters at positions pos, pos+k, pos+2k, ...
        i = pos
        while i < n:
            char = s[i]
            freq[char] = freq.get(char, 0) + 1
            i += k

        # Keep most frequent, delete others
        if freq:
            max_freq = max(freq.values())
            total_at_pos = sum(freq.values())
            deletions += total_at_pos - max_freq

    return deletions


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
