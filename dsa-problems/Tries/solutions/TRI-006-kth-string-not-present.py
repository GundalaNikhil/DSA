def naive(inserted, L, k):
    all_strings = []
    # Generate all strings of length 1 to L
    for length in range(1, L+1):
        for combo in all_combinations_of_length(length):
            if combo not in inserted:
                all_strings.append(combo)

    all_strings.sort()
    return all_strings[k-1] if k <= len(all_strings) else ""


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
