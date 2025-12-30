import sys
sys.setrecursionlimit(200000)
from typing import List, Tuple
from collections import defaultdict, deque

def course_schedule(n: int, prerequisites: List[Tuple[int, int]], pairs: List[Tuple[int, int]]) -> List[int]:
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    for a, b in pairs:
        union(a, b)
    
    contracted = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Sort roots for deterministic behavior
    roots = sorted(list(set(find(i) for i in range(n))))
    for root in roots:
        in_degree[root] = 0
    
    for u, v in prerequisites:
        from_root = find(u)
        to_root = find(v)
        if from_root != to_root:
            contracted[from_root].append(to_root)
            in_degree[to_root] += 1
    
    # Sort for deterministic topological sort if multiple zero in-degree
    # But queue order handles it if inserted in sorted order
    queue = deque([node for node in roots if in_degree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        # Sort neighbors for deterministic processing
        neighbors = sorted(contracted[node])
        for neighbor in neighbors:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) != len(roots):
        return []
    
    result = []
    for super_node in topo_order:
        # Sort members of super_node
        members = sorted([i for i in range(n) if find(i) == super_node])
        result.extend(members)
    
    return result

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        prerequisites = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            prerequisites.append((u, v))
        
        # Handle optional pairs input
        try:
            p = int(next(iterator))
            pairs = []
            for _ in range(p):
                a = int(next(iterator))
                b = int(next(iterator))
                pairs.append((a, b))
        except StopIteration:
            pairs = []
            
        result = course_schedule(n, prerequisites, pairs)
        
        if not result:
            print(-1)
        else:
            print(' '.join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
