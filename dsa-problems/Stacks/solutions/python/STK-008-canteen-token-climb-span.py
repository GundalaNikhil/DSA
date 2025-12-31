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
