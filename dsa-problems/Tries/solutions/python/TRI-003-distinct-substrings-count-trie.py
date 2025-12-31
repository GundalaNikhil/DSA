def count_distinct_naive(s):
    unique = set()
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            unique.add(s[i:j])
    return len(unique)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    s = input_data
    result = count_distinct_naive(s)
    print(result)

if __name__ == "__main__":
    main()
