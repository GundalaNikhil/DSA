def decode_with_cap(s: str, cap: int) -> str:
    result = []
    i = 0
    n = len(s)

    while i < n:
        # Read character
        char = s[i]
        i += 1

        # Read count (digits)
        count_str = ""
        while i < n and s[i].isdigit():
            count_str += s[i]
            i += 1

        # Decode with cap
        count = int(count_str) if count_str else 1
        actual_count = min(count, cap)
        result.append(char * actual_count)

    return ''.join(result)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
