import heapq
import sys
from typing import List

def merge_queues(queues: List[List[int]]) -> List[int]:
    # Min-heap stores (value, queue_index)
    pq = []
    # Pointers to current index in each queue
    indices = [0] * len(queues)
    
    for i, q in enumerate(queues):
        if q:
            heapq.heappush(pq, (q[0], i))
            
    result = []
    last_val = None
    count = 0
    
    while pq:
        val, q_idx = heapq.heappop(pq)
        
        # Check constraint
        if result and val == last_val and count == 2:
            if not pq:
                break # Deadlock
            
            # Try next best
            val2, q_idx2 = heapq.heappop(pq)
            
            # If next best is ALSO the same value, we have to keep searching
            # We need a loop to find a valid one.
            temp_storage = [(val, q_idx)]
            
            while val2 == last_val:
                temp_storage.append((val2, q_idx2))
                if not pq:
                    val2 = None
                    break
                val2, q_idx2 = heapq.heappop(pq)
            
            if val2 is None:
                # All remaining values are blocked
                break
                
            # Found valid val2
            result.append(val2)
            last_val = val2
            count = 1
            
            # Advance q_idx2
            indices[q_idx2] += 1
            if indices[q_idx2] < len(queues[q_idx2]):
                heapq.heappush(pq, (queues[q_idx2][indices[q_idx2]], q_idx2))
                
            # Push back everything in temp_storage
            for item in temp_storage:
                heapq.heappush(pq, item)
                
        else:
            # Valid
            result.append(val)
            if val == last_val:
                count += 1
            else:
                last_val = val
                count = 1
                
            # Advance q_idx
            indices[q_idx] += 1
            if indices[q_idx] < len(queues[q_idx]):
                heapq.heappush(pq, (queues[q_idx][indices[q_idx]], q_idx))
                
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        k = int(next(iterator))
    except StopIteration:
        return

    queues = []
    for _ in range(k):
        length = int(next(iterator))
        queue = []
        for _ in range(length):
            queue.append(int(next(iterator)))
        queues.append(queue)

    result = merge_queues(queues)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
