def count_equal_distinct_splits(s: str) -> int:
    n = len(s)
    if n < 2:
        return 0

    # Build suffix distinct counts
    suffix_distinct = [0] * (n + 1)
    char_set = set()
    for i in range(n - 1, -1, -1):
        char_set.add(s[i])
        suffix_distinct[i] = len(char_set)

    # Scan left and compare
    left_set = set()
    count = 0
    for i in range(n - 1):
        left_set.add(s[i])
        if len(left_set) == suffix_distinct[i + 1]:
            count += 1

    return count


def main():
    import sys


    # Read input string
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    # Call solution
    result = count_equal_distinct_splits(input_data)
    print(result)

if __name__ == "__main__":
    main()
