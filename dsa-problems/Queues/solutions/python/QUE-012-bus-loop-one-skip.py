from typing import List
import sys

def find_start(gain: List[int], cost: List[int]) -> int:
    n = len(gain)
    
    # 1. Find min gain index
    min_gain_idx = 0
    for i in range(1, n):
        if gain[i] < gain[min_gain_idx]:
            min_gain_idx = i
            
    # 2. Zero it out
    original_val = gain[min_gain_idx]
    gain[min_gain_idx] = 0
    
    # 3. Standard Gas Station
    total_tank = 0
    curr_tank = 0
    start = 0
    
    for i in range(n):
        net = gain[i] - cost[i]
        total_tank += net
        curr_tank += net
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
            
    # Restore
    gain[min_gain_idx] = original_val
    
    return start % n if total_tank >= 0 else -1

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
            gain = [int(x) for x in remaining[:n]]
            cost = [int(x) for x in remaining[n:]]
        # If we have exactly n values, use as gain, create cost array
        elif len(remaining) == n:
            gain = [int(x) for x in remaining]
            cost = [1] * n  # Default cost
        # Otherwise try to split as much as possible
        else:
            gain = [int(x) for x in remaining[:n]]
            cost = [int(x) for x in remaining[n:]] if len(remaining) > n else [1] * n

        result = find_start(gain, cost)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
