def process(ops: list[list[str]]) -> list[str]:
    stack = []
    result = []
    
    for op in ops:
        command = op[0]
        
        if command == "PUSH":
            stack.append(op[1])
        elif command == "POP":
            if not stack:
                result.append("EMPTY")
            else:
                result.append(stack.pop())
        elif command == "TOP":
            if not stack:
                result.append("EMPTY")
            else:
                result.append(stack[-1])
                
    return result


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
