import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    head_id = int(input_data[ptr])
    ptr += 1
    nodes = {}
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        nxt = int(input_data[ptr])
        ptr += 1
        nodes[i] = [v, nxt]
        
    visited = [0] * (n + 1)
    removed_count = 0
    
    # 1. Detect and remove cycles
    # Iterate all nodes to ensure all components processed
    for i in range(1, n + 1):
        if visited[i] == 0:
            path = []
            curr = i
            while curr != 0 and visited[curr] == 0:
                visited[curr] = 1 # Visiting
                path.append(curr)
                curr = nodes[curr][1]
                
            if curr != 0 and visited[curr] == 1:
                # Cycle detected
                cycle = []
                in_cycle = False
                for node in path:
                    if node == curr:
                        in_cycle = True
                    if in_cycle:
                        cycle.append(node)
                        
                min_id = min(cycle)
                nodes[min_id][1] = 0 # Break cycle
                removed_count += 1
                
            # Mark processed
            for node in path:
                visited[node] = 2 # Visited processed
                
    print(removed_count)
    
    # 2. Traverse from head
    res = []
    curr = head_id
    traversed = set()
    while curr != 0 and curr not in traversed:
        res.append(nodes[curr][0])
        traversed.add(curr)
        curr = nodes[curr][1]
        
    print(*(res))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()
