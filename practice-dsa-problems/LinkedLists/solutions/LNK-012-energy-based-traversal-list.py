import bisect
import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    w = [0] * (n + 1)
    for i in range(1, n + 1):
        w[i] = int(input_data[ptr])
        ptr += 1
        
    jumps = [0] * (n + 1)
    for i in range(1, n + 1):
        jumps[i] = int(input_data[ptr])
        ptr += 1
        
    inf = float("inf")
    min_cost = [inf] * (n + 1)
    pq = [(w[1], 1)]
    min_cost[1] = w[1]
    
    while pq:
        c, u = heapq.heappop(pq)
        if c > min_cost[u]:
            continue
            
        # Move forward 1 step
        if u + 1 <= n:
            nc = c + w[u + 1]
            if nc < min_cost[u + 1]:
                min_cost[u + 1] = nc
                heapq.heappush(pq, (nc, u + 1))
                
        # Jump
        v = jumps[u]
        if v != 0:
            nc = c + w[v]
            if nc < min_cost[v]:
                min_cost[v] = nc
                heapq.heappush(pq, (nc, v))
                
    reachable_nodes = []
    for i in range(1, n + 1):
        if min_cost[i] != inf:
            reachable_nodes.append((min_cost[i], i))
            
    reachable_nodes.sort()
    
    filtered = []
    curr_max = -1
    for c, i in reachable_nodes:
        if i > curr_max:
            filtered.append((c, i))
            curr_max = i
            
    q = int(input_data[ptr])
    ptr += 1
    
    output = []
    for _ in range(q):
        e = int(input_data[ptr])
        ptr += 1
        idx = bisect.bisect_right(filtered, (e, float("inf"))) - 1
        
        if idx >= 0:
            output.append(str(filtered[idx][1]))
        else:
            output.append("0")
            
    print("\n".join(output))


if __name__ == "__main__":
    solve()
