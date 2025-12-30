from collections import deque
from typing import List

def shortest_distances(n: int, adj: List[List[int]], source: int) -> List[int]:
    dist = [-1] * n
    dist[source] = 0
    queue = deque([source])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
