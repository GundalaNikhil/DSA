from typing import List
import sys

def rotate_queue(values: List[int], k: int) -> List[int]:
    n = len(values)
    if n == 0:
        return []
    
    k = k % n
    # Slicing is O(N)
    return values[k:] + values[:k]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        k = int(next(iterator))
        
        result = rotate_queue(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
