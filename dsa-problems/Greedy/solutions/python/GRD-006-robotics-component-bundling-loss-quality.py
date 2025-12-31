import heapq
import math
import sys

def max_bundle_weight(n: int, T: int, weights: list, qualities: list) -> int:
    # Max-heap: store (-quality, weight)
    pq = []
    for w, q in zip(weights, qualities):
        heapq.heappush(pq, (-q, w))
        
    while len(pq) > 1:
        # Pop two highest qualities
        neg_q1, w1 = heapq.heappop(pq)
        neg_q2, w2 = heapq.heappop(pq)
        
        q1, q2 = -neg_q1, -neg_q2
        
        new_q = min(q1, q2) - 1
        
        if new_q < T:
            return -1
            
        loss = math.floor(0.1 * min(w1, w2))
        new_w = w1 + w2 - loss
        
        heapq.heappush(pq, (-new_q, new_w))
        
    return pq[0][1] if pq else -1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    T = int(next(iterator))
    
    weights = []
    for _ in range(n):
        weights.append(int(next(iterator)))
        
    qualities = []
    for _ in range(n):
        qualities.append(int(next(iterator)))

    result = max_bundle_weight(n, T, weights, qualities)
    print(result)

if __name__ == "__main__":
    main()
