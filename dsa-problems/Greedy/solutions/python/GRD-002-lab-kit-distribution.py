import heapq
import sys

def distribute_kits(k: int, m: int, quantities: list) -> tuple:
    # Python's heapq is a min-heap. We push negative values to simulate max-heap.
    pq = []
    total_kits = 0
    
    for q in quantities:
        if q > 0:
            heapq.heappush(pq, -q)
            total_kits += q
            
    fulfilled = min(m, total_kits)
    to_distribute = fulfilled
    
    while to_distribute > 0 and pq:
        # Pop largest (most negative)
        max_q = -heapq.heappop(pq)
        max_q -= 1
        to_distribute -= 1
        
        if max_q > 0:
            heapq.heappush(pq, -max_q)
            
    # Remaining types in heap are those > 0
    remaining_types = len(pq)
    zeroed_types = k - remaining_types
    
    return (fulfilled, zeroed_types)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    k = int(next(iterator))
    m = int(next(iterator))
    
    quantities = []
    for _ in range(k):
        quantities.append(int(next(iterator)))
        
    fulfilled, zeroed = distribute_kits(k, m, quantities)
    print(f"{fulfilled} {zeroed}")

if __name__ == "__main__":
    main()
