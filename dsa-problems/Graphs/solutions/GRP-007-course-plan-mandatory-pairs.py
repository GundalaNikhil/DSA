from typing import List, Tuple
from collections import defaultdict, deque

def course_schedule(n: int, prerequisites: List[Tuple[int, int]], pairs: List[Tuple[int, int]]) -> List[int]:
    # Union-Find for pairs
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Union pairs
    for a, b in pairs:
        union(a, b)
    
    # Build contracted graph
    contracted = defaultdict(list)
    in_degree = defaultdict(int)
    
    roots = set(find(i) for i in range(n))
    for root in roots:
        in_degree[root] = 0
    
    for u, v in prerequisites:
        from_root = find(u)
        to_root = find(v)
        if from_root != to_root:
            contracted[from_root].append(to_root)
            in_degree[to_root] += 1
    
    # Topological sort (Kahn's algorithm)
    queue = deque([node for node in roots if in_degree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in contracted[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) != len(roots):
        return []  # Cycle detected
    
    # Expand super-nodes
    result = []
    for super_node in topo_order:
        for i in range(n):
            if find(i) == super_node:
                result.append(i)
    
    return result


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
