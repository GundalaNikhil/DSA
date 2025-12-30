from typing import List
import sys

def interleave_queue(values: List[int]) -> List[int]:
    n = len(values)
    mid = n // 2
    result = []
    
    for i in range(mid):
        result.append(values[i])
        result.append(values[mid + i])
        
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        
        result = interleave_queue(values)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
