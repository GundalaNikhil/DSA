def reduce_stack(s: str, w: list[int]) -> tuple[str, int]:
    stack = [] # List of tuples (char, weight)
    total_removed = 0
    
    for char, weight in zip(s, w):
        if stack and stack[-1][0] == char and (stack[-1][1] + weight) % 2 == 0:
            total_removed += stack[-1][1] + weight
            stack.pop()
        else:
            stack.append((char, weight))
            
    reduced_s = "".join(item[0] for item in stack)
    return reduced_s, total_removed


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
