import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    packets = []
    for _ in range(n):
        d = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1

        packets.append((d, v))
        
    packets.sort()
    pq = []
    
    for d, v in packets:
        # Min-heap of values. Keep size <= d?
        # If we have d packets, we can schedule them if deadlines allow?
        # If packets sorted by deadline:
        # For each packet (d_i, v_i), we can include it.
        # If count < d_i: simply add.
        # If count == d_i: if v_i > min(pq), replace min.
        # This maximizes value for given deadlines.
        
        if len(pq) < d:
            heapq.heappush(pq, v)
        elif pq and v > pq[0]:
            heapq.heapreplace(pq, v)
            
    print(sum(pq))


if __name__ == "__main__":
    solve()
