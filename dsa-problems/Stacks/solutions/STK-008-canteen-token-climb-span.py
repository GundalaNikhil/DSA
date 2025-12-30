def spans(demand: list[int]) -> list[int]:
    n = len(demand)
    result = [0] * n
    stack = [] # Stores indices
    
    for i in range(n):
        # Pop strictly smaller elements
        while stack and demand[stack[-1]] < demand[i]:
            stack.pop()
            
        prev_idx = stack[-1] if stack else -1
        result[i] = i - prev_idx - 1
        
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
