import sys
from collections import deque
import heapq
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q_count = int(input_data[ptr])
    ptr += 1
    list_deque = deque()
    expiry_heap = []
    removed = set()
    node_id_counter = 0
    current_time = 0
    for _ in range(q_count):
        current_time += 1
        # Remove expired
        while expiry_heap and expiry_heap[0][0] <= current_time:
            _, nid = heapq.heappop(expiry_heap)
            removed.add(nid)
            
        # Clean front of deque
        while list_deque and list_deque[0][2] in removed:
            list_deque.popleft()
            
        op = input_data[ptr]
        ptr += 1
        
        if op == 'PUSH':
            x = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            node_id_counter += 1
            expiry = current_time + t
            list_deque.append((x, expiry, node_id_counter))
            heapq.heappush(expiry_heap, (expiry, node_id_counter))
            
        elif op == 'POP':
            if list_deque:
                _, _, nid = list_deque.popleft()
                removed.add(nid)
                
        elif op == 'FRONT':
            # Ensure front is valid again (though loop above handles it)
            while list_deque and list_deque[0][2] in removed:
                list_deque.popleft()
            print(list_deque[0][0] if list_deque else -1)
            
        elif op == 'COUNT':
            # Count valid items? 
            # Deque might contain removed items in middle.
            # But we only lazily remove from front.
            # So len(list_deque) might be incorrect if items are removed via expiry but not yet popped from deque.
            # However, code says `removed` set tracks expired/popped items.
            # Counting valid items in deque requires filtering.
            # Simpler: just count items in deque not in removed?
            # Or assume lazy removal only at front is sufficient?
            # For exact count, we might need to purge?
            # Let's count properly.
            
            cnt = 0
            for item in list_deque:
                if item[2] not in removed:
                    cnt += 1
            print(cnt)
if __name__ == '__main__':
    solve()