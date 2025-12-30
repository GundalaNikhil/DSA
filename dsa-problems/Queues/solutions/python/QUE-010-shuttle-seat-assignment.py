from typing import List
import heapq
import sys

def min_seats(arrivals: List[int], departures: List[int]) -> int:
    intervals = sorted(zip(arrivals, departures))
    min_heap = [] # Stores departure times
    max_seats = 0
    
    for start, end in intervals:
        # Free up seats
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
            
        heapq.heappush(min_heap, end)
        max_seats = max(max_seats, len(min_heap))
        
    return max_seats

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        arrivals = [int(next(iterator)) for _ in range(n)]
        departures = [int(next(iterator)) for _ in range(n)]
        
        result = min_seats(arrivals, departures)
        print(result)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
