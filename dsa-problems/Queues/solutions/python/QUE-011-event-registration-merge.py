from typing import List
import sys

def merge_queues(a: List[int], b: List[int]) -> List[int]:
    n, m = len(a), len(b)
    i, j = 0, 0
    result = []
    
    while i < n and j < m:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            
    # Append remaining
    if i < n:
        result.extend(a[i:])
    if j < m:
        result.extend(b[j:])
        
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        m = int(next(iterator))
        b = [int(next(iterator)) for _ in range(m)]
        
        result = merge_queues(a, b)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
