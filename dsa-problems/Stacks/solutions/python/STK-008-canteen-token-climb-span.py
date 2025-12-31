def spans(demand: list[int]) -> list[int]:
    n = len(demand)
    result = [0] * n
    stack = []  # Stores indices

    for i in range(n):
        # Pop elements strictly smaller than current
        while stack and demand[stack[-1]] < demand[i]:
            stack.pop()

        # Calculate span based on top of stack
        if not stack:
            # No previous element >= current, so span includes all prior days
            result[i] = i
        elif demand[stack[-1]] == demand[i]:
            # Found equal element, span resets to 0
            result[i] = 0
        else:
            # Found greater element, span is distance from previous >= element
            result[i] = i - stack[-1] - 1

        stack.append(i)

    return result


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    demand = list(map(int, lines[1].split()))
    result = spans(demand)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
