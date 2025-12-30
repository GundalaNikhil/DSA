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

    best_partition = []

    def backtrack(start, current_path):
        nonlocal best_partition

        if start == n:
            # Found a valid partition
            if not best_partition or len(current_path) < len(best_partition):
                best_partition = list(current_path)
            return

        # Pruning: if current path is already worse than best, skip
        if best_partition and len(current_path) >= len(best_partition):
            return

        # Try all possible next palindromes
        for end in range(start, n):
            # Check length constraint
            if end - start + 1 > L:
                break
            # Check if it's a palindrome
            if is_pal[start][end]:
                current_path.append(s[start : end + 1])
                backtrack(end + 1, current_path)
                current_path.pop()

    backtrack(0, [])

    if best_partition:
        return ' '.join(best_partition)
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
