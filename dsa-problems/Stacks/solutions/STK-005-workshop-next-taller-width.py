def next_taller_within(h: list[int], w: int) -> list[int]:
    n = len(h)
    result = [-1] * n
    stack = [] # Stores indices
    
    for i in range(n - 1, -1, -1):
        while stack and h[stack[-1]] <= h[i]:
            stack.pop()
            
        if stack:
            j = stack[-1]
            if j - i <= w:
                result[i] = h[j]
            else:
                result[i] = -1
        
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
