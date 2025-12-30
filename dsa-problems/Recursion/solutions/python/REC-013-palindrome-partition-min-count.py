def min_palindrome_partitions(s: str, L: int) -> list[list[str]]:
    n = len(s)
    # Precompute palindromes
    is_pal = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length <= 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True

    results = []
    min_len = [float('inf')]

    def backtrack(start, current_path):
        if start == n:
            if len(current_path) < min_len[0]:
                min_len[0] = len(current_path)
                results.clear()
                results.append(list(current_path))
            elif len(current_path) == min_len[0]:
                results.append(list(current_path))
            return

        if len(current_path) >= min_len[0]:
            return

        for end in range(start, n):
            if end - start + 1 > L:
                break
            if is_pal[start][end]:
                current_path.append(s[start : end + 1])
                backtrack(end + 1, current_path)
                current_path.pop()

    backtrack(0, [])
    return results


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
