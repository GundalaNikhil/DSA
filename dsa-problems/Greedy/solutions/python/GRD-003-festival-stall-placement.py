import sys

def max_stalls(stalls: list, d: int) -> int:
    # Sort by end time (second element)
    stalls.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -float('inf')
    
    for start, end in stalls:
        if start - last_end >= d:
            count += 1
            last_end = end
            
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    d = int(next(iterator))
    
    stalls = []
    for _ in range(n):
        start = int(next(iterator))
        end = int(next(iterator))
        stalls.append([start, end])

    result = max_stalls(stalls, d)
    print(result)

if __name__ == "__main__":
    main()
