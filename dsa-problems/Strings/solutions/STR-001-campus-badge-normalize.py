def normalize_badge(s: str) -> str:
    if not s:
        return ""

    result = []
    last_was_alnum = False

    for c in s:
        if c.isalnum():
            result.append(c.lower())
            last_was_alnum = True
        else:
            # Non-alphanumeric character
            if last_was_alnum and result:
                result.append('-')
                last_was_alnum = False

    # Remove trailing hyphen if present
    if result and result[-1] == '-':
        result.pop()

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
