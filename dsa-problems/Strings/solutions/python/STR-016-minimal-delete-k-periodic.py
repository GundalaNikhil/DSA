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
        else:
             pass

    return deletions


def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            k = int(parts[1])
            print(minimal_delete_k_periodic(s, k))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
