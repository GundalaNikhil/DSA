def cyclic_shift_equivalence_classes(strings: list[str]) -> int:
    def minimal_rotation(s):
        """Booth's algorithm for minimal rotation"""
        s_doubled = s + s
        n = len(s)
        failure = [-1] * (2 * n)
        k = 0

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

        return s[k:] + s[:k]

    canonical_set = set()
    for s in strings:
        canonical = minimal_rotation(s)
        canonical_set.add(canonical)

    return len(canonical_set)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
