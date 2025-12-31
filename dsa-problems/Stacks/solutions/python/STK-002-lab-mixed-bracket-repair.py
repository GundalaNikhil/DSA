def count_changes(s: str) -> int:
    """
    Count minimum number of characters to change to make brackets balanced.
    Uses a stack to track unmatched characters.
    """
    stack = []

    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            pairs = {')': '(', ']': '[', '}': '{'}
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        elif c == '?':
            # Wildcard - treat as opening bracket
            stack.append('(')

    # Count unmatched characters
    # Each unmatched character needs to be changed to balance
    return len(stack)


def main():
    import sys
    s = sys.stdin.read().strip()
    result = count_changes(s)
    print(result)

if __name__ == "__main__":
    main()
