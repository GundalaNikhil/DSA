def spans(counts: list[int]) -> list[int]:
    n = len(counts)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and counts[stack[-1]] < counts[i]:
            stack.pop()
            
        if not stack:
            result[i] = i + 1
        else:
            result[i] = i - stack[-1]
            
        stack.append(i)
        
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
