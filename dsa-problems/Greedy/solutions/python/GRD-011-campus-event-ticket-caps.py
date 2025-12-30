import heapq
import sys

def max_tickets(n: int, requests: list) -> int:
    # Sort by deadline
    requests.sort(key=lambda x: x[1])
    
    pq = [] # Min-heap for quantities
    
    for q, d in requests:
        heapq.heappush(pq, q)
        
        if len(pq) > d:
            heapq.heappop(pq)
            
    return sum(pq)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    requests = []
    for _ in range(n):
        q = int(next(iterator))
        d = int(next(iterator))
        requests.append([q, d])

    result = max_tickets(n, requests)
    print(result)

if __name__ == "__main__":
    main()
