import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    actions = []
    
    for i in range(a_count):
        c = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        actions.append((c, p))

        
    pq = []
    # Initial costs: C + P. Count 1.
    for i in range(a_count):
        c, p = actions[i]
        heapq.heappush(pq, (c + p, i, 1))
        
    total_cost = 0
    # Process N items
    for _ in range(n):
        cost, idx, count = heapq.heappop(pq)
        total_cost += cost
        
        # Next cost for this action type: C + P * (count + 1)
        c, p = actions[idx]
        new_count = count + 1
        heapq.heappush(pq, (c + p * new_count, idx, new_count))
        
    print(total_cost)


if __name__ == "__main__":
    solve()
