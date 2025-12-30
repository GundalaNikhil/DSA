def minimal_unique_rotation(s: str) -> str:
    n = len(s)

    # Booth's algorithm to find minimal rotation
    def booth_minimal_rotation_index(s):
        s_doubled = s + s
        n = len(s)
        failure = [-1] * (2 * n)
        k = 0  # minimal rotation start index

        for j in range(1, 2 * n):
            i = failure[j - k - 1]
            while i != -1 and s_doubled[j] != s_doubled[k + i + 1]:
                if s_doubled[j] < s_doubled[k + i + 1]:
                    k = j - i - 1
                i = failure[i]

            if s_doubled[j] != s_doubled[k + i + 1]:
                if s_doubled[j] < s_doubled[k + i + 1]:
                    k = j
                failure[j - k] = -1
            else:
                failure[j - k] = i + 1

        return k

    # Find minimal rotation index
    min_idx = booth_minimal_rotation_index(s)
    min_rotation = s[min_idx:] + s[:min_idx]

    # If minimal rotation equals original, all rotations identical
    if min_rotation == s:
        return s
    else:
        return min_rotation


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
