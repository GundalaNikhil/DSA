def min_palindrome_partitions(s: str, L: int) -> list[str]:
    n = len(s)
    # Precompute palindromes
    is_pal = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length <= 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True

    min_count = [float('inf')]
    all_partitions = []

    def backtrack(start, current_path):
        if start == n:
            count = len(current_path)
            if count < min_count[0]:
                min_count[0] = count
                all_partitions.clear()
                all_partitions.append(list(current_path))
            elif count == min_count[0]:
                all_partitions.append(list(current_path))
            return

        # Pruning: don't explore beyond min_count
        if len(current_path) >= min_count[0]:
            return

        # Try all possible next palindromes
        for end in range(start, min(start + L, n)):
            if is_pal[start][end]:
                current_path.append(s[start : end + 1])
                backtrack(end + 1, current_path)
                current_path.pop()

    backtrack(0, [])

    if all_partitions:
        # Among all minimum partitions, select the first one found
        # The backtracking explores shorter palindromes first at each step
        best = all_partitions[0]
        return ' '.join(best)
    else:
        # Fallback: split into individual characters
        return ' '.join(list(s))

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    s = lines[0].strip()
    L = int(lines[1].strip())
    result = min_palindrome_partitions(s, L)
    print(result)

if __name__ == "__main__":
    main()
