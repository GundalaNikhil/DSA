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
        remaining = list(iterator)

        # If we have exactly 2n values, split them in half
        if len(remaining) == 2 * n:
            a = [int(x) for x in remaining[:n]]
            b = [int(x) for x in remaining[n:]]
        # If we have n values, use as array a, create empty b
        elif len(remaining) == n:
            a = [int(x) for x in remaining]
            b = []
        # If we have n + m + 1 values, first is m, rest split
        elif len(remaining) > n:
            m = int(remaining[0]) if remaining else n
            if len(remaining) >= n + m:
                a = [int(x) for x in remaining[1:n+1]]
                b = [int(x) for x in remaining[n+1:n+1+m]]
            else:
                a = [int(x) for x in remaining[1:n+1]]
                b = [int(x) for x in remaining[n+1:]]
        else:
            a = [int(x) for x in remaining]
            b = []

        result = merge_queues(a, b)
        print(" ".join(map(str, result)))
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
