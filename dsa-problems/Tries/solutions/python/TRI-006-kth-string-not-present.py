from itertools import product

def all_combinations_of_length(length):
    """Generate all strings of given length using lowercase letters"""
    for combo in product('abcdefghijklmnopqrstuvwxyz', repeat=length):
        yield ''.join(combo)

def custom_sort_key(s):
    """Sort key for lexicographic order: a, aa, ab, ..., az, b, ba, ..., zz
    First sort by first character, then by rest of string"""
    if len(s) == 1:
        return (0, s)  # Single chars come before multi-char with same prefix
    else:
        return (1, s[0], s[1:])

def naive(inserted, L, k):
    all_strings = []
    # Generate all strings of length 1 to L in the special ordering
    # Order: a, aa, ab, ..., az, b, ba, bb, ..., bz, c, ...
    for char in 'abcdefghijklmnopqrstuvwxyz':
        # Add single character if not inserted and L >= 1
        if L >= 1 and char not in inserted:
            all_strings.append(char)

        # Add all multi-char strings starting with this char
        for length in range(2, L+1):
            for rest in all_combinations_of_length(length-1):
                combo = char + rest
                if combo not in inserted:
                    all_strings.append(combo)

    return all_strings[k-1] if k <= len(all_strings) else ""


def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')

    n, L, k = map(int, input_data[0].split())
    inserted = set()
    for i in range(1, n + 1):
        inserted.add(input_data[i])

    result = naive(inserted, L, k)
    print(result)

if __name__ == "__main__":
    main()
