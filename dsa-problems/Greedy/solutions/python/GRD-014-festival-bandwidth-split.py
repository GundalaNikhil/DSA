import sys

def max_stages(n: int, B: int, bandwidths: list) -> int:
    bandwidths.sort()
    
    current_sum = 0
    count = 0
    
    for b in bandwidths:
        if current_sum + b <= B:
            current_sum += b
            count += 1
        else:
            break
            
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    B = int(next(iterator))
    
    bandwidths = []
    for _ in range(n):
        bandwidths.append(int(next(iterator)))

    result = max_stages(n, B, bandwidths)
    print(result)

if __name__ == "__main__":
    main()
