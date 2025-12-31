def count_visible(h: list[int]) -> int:
    """
    Count buildings that can see the sunset.
    A building can see the sunset if there is no taller building to its right.
    Use monotonic decreasing stack, scanning right to left.
    """
    n = len(h)
    stack = []  # Stores indices
    count = 0

    # Scan from right to left
    for i in range(n - 1, -1, -1):
        # Remove buildings shorter than current
        while stack and h[stack[-1]] < h[i]:
            stack.pop()

        # If stack empty, current building can see sunset (nothing taller to right)
        if not stack:
            count += 1

        stack.append(i)

    return count


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    h = list(map(int, lines[1].split()))
    result = count_visible(h)
    print(result)

if __name__ == "__main__":
    main()
