def longest_chunked_decomposition(s: str, L: int) -> int:
    n = len(s)
    left, right = 0, n - 1
    chunks = 0

    while left < right:
        matched = False
        # Try chunk sizes from 1 to min(L, available space)
        max_len = min(L, (right - left + 1) // 2)

        for length in range(1, max_len + 1):
            left_chunk = s[left:left + length]
            right_chunk = s[right - length + 1:right + 1]

            if left_chunk == right_chunk:
                chunks += 2  # Matched pair
                left += length
                right -= length
                matched = True
                break

        if not matched:
            # No valid match found, middle portion
            break

    # Add middle chunk if exists
    if left <= right:
        chunks += 1

    return chunks


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
            L = int(parts[1])
            print(longest_chunked_decomposition(s, L))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
