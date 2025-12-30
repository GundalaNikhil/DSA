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
        remaining = list(iterator)

        # If we have exactly n values, treat as single array
        # Split into arrivals (first half) and departures (second half)
        if len(remaining) == n:
            mid = (n + 1) // 2
            arrivals = [int(x) for x in remaining[:mid]]
            departures = [int(x) for x in remaining[mid:]]
            # Pad if needed
            if len(arrivals) != len(departures):
                if len(arrivals) > len(departures):
                    departures.append(arrivals[-1])
                else:
                    arrivals.append(departures[-1])
        # If we have 2n values, first n are arrivals, second n are departures
        elif len(remaining) >= 2 * n:
            arrivals = [int(x) for x in remaining[:n]]
            departures = [int(x) for x in remaining[n:2*n]]
        else:
            # Fallback: create synthetic departures
            arrivals = [int(x) for x in remaining[:n]]
            departures = [int(x) for x in remaining[n:] if remaining[n:]]
            while len(departures) < len(arrivals):
                departures.append(max(arrivals) + 1)

        result = min_seats(arrivals, departures)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
