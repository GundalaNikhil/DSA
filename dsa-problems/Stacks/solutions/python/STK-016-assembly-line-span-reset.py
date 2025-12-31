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
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    counts = list(map(int, lines[1].split()))
    result = spans(counts)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
