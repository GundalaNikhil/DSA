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
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
