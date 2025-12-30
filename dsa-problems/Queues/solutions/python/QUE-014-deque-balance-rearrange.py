from typing import List
import sys

def build_deque(values: List[int]) -> List[int]:
    n = len(values)
    result = []
    left, right = 0, n - 1
    
    while left <= right:
        result.append(values[left])
        if left != right:
            result.append(values[right])
        left += 1
        right -= 1
        
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        
        result = build_deque(values)
        print(" ".join(map(str, result)))
    except (StopIteration, ValueError):
        pass

if __name__ == "__main__":
    main()
