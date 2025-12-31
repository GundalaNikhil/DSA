def process(ops: list[list[str]]) -> list[str]:
    result = []
    main_stack = []
    max_stack = []
    
    for op in ops:
        cmd = op[0]
        
        if cmd == "PUSH":
            val = int(op[1])
            main_stack.append(val)
            if not max_stack or val >= max_stack[-1]:
                max_stack.append(val)
        elif cmd == "POP":
            if not main_stack:
                result.append("EMPTY")
            else:
                val = main_stack.pop()
                result.append(str(val))
                if val == max_stack[-1]:
                    max_stack.pop()
        elif cmd == "TOP":
            if not main_stack:
                result.append("EMPTY")
            else:
                result.append(str(main_stack[-1]))
        elif cmd == "GETMAX":
            if not main_stack:
                result.append("EMPTY")
            else:
                result.append(str(max_stack[-1]))
                
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
