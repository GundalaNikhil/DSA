from collections import deque
from typing import List

def reachable_nodes(n: int, adj: List[List[tuple]], source: int, threshold: int) -> List[int]:
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        node = queue.popleft()
        
        for neighbor, weight in adj[node]:
            if weight <= threshold and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return list(visited)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
