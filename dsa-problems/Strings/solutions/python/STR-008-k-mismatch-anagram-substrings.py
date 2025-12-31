def count_k_mismatch_anagrams(s: str, p: str, k: int) -> int:
    m = len(p)
    n = len(s)

    if n < m:
        return 0

    # Build pattern frequency
    freq_p = [0] * 26
    for c in p:
        freq_p[ord(c) - ord('a')] += 1

    # Initialize window frequency
    freq_window = [0] * 26
    for i in range(m):
        freq_window[ord(s[i]) - ord('a')] += 1

    def mismatch_cost(freq_w, freq_p):
        cost = 0
        for i in range(26):
            if freq_p[i] > freq_w[i]:
                cost += freq_p[i] - freq_w[i]
        return cost

    count = 0

    # Check first window
    if mismatch_cost(freq_window, freq_p) <= k:
        count += 1

    # Slide window
    for i in range(1, n - m + 1):
        # Remove leftmost char of previous window
        freq_window[ord(s[i - 1]) - ord('a')] -= 1
        # Add rightmost char of new window
        freq_window[ord(s[i + m - 1]) - ord('a')] += 1

        if mismatch_cost(freq_window, freq_p) <= k:
            count += 1

    return count


def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
        
    parts = input_data.split()
    if len(parts) >= 3:
        s = parts[0]
        p = parts[1]
        try:
            k = int(parts[2])
            print(count_k_mismatch_anagrams(s, p, k))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
