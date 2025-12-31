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
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    m = int(lines[0])
    ops = []
    for i in range(1, m + 1):
        parts = lines[i].split()
        ops.append(parts)

    result = process(ops)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
