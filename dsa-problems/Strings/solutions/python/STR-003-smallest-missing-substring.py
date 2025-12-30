def smallest_missing_substring(s: str, k: int) -> str:
    # Extract all k-length substrings
    substrings = set()
    for i in range(len(s) - k + 1):
        substrings.add(s[i:i+k])

    def dfs(current: str, remaining: int) -> str:
        if remaining == 0:
            return current if current not in substrings else None

        for c in 'abcdefghijklmnopqrstuvwxyz':
            result = dfs(current + c, remaining - 1)
            if result is not None:
                return result

        return None

    result = dfs("", k)
    return result if result else ""


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
