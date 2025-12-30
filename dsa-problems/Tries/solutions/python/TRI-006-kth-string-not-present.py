from itertools import product

def all_combinations_of_length(length):
    """Generate all strings of given length using lowercase letters"""
    for combo in product('abcdefghijklmnopqrstuvwxyz', repeat=length):
        yield ''.join(combo)

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
    input_data = sys.stdin.read().strip().split('\n')

    n, L, k = map(int, input_data[0].split())
    inserted = set()
    for i in range(1, n + 1):
        inserted.add(input_data[i])

    result = naive(inserted, L, k)
    print(result)

if __name__ == "__main__":
    main()
