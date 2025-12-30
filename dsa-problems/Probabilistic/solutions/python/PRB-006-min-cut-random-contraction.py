import sys
from collections import defaultdict
import random

def find_min_cut(n, edges):
    """
    Find minimum cut using Karger's randomized contraction algorithm.
    Run multiple times to increase success probability.
    """
    if n <= 1:
        return 0
    
    best_cut = float('inf')
    # Run enough iterations for high probability of finding min-cut
    iterations = max(1, n * n * 2)
    
    for _ in range(iterations):
        # Create adjacency list for this iteration
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Track which original nodes are in each super-node
        nodes = {i: {i} for i in range(1, n + 1)}
        active_nodes = set(range(1, n + 1))
        
        # Contract until 2 nodes remain
        while len(active_nodes) > 2:
            # Pick a random edge from active nodes
            u = random.choice(list(active_nodes))
            if u not in graph or not graph[u]:
                if u in active_nodes:
                    active_nodes.remove(u)
                continue
                
            v = random.choice(graph[u])
            if v not in active_nodes:
                # Remove this edge and continue
                graph[u] = [x for x in graph[u] if x != v]
                continue
            
            # Contract edge (u, v) - merge v into u
            nodes[u] = nodes[u].union(nodes[v])
            
            # Update edges: redirect all v's edges to u
            if v in graph:
                for neighbor in graph[v]:
                    if neighbor != u and neighbor in active_nodes:
                        graph[u].append(neighbor)
                        # Update neighbor's edge to point to u instead of v
                        if neighbor in graph:
                            graph[neighbor] = [u if x == v else x for x in graph[neighbor]]
            
            # Remove self-loops
            graph[u] = [x for x in graph[u] if x != u]
            
            # Remove v
            if v in graph:
                del graph[v]
            if v in active_nodes:
                active_nodes.remove(v)
        
        # Count edges between the two remaining super-nodes
        remaining = list(active_nodes)
        if len(remaining) == 2:
            cut_size = len(graph[remaining[0]])
            best_cut = min(best_cut, cut_size)
    
    return best_cut if best_cut != float('inf') else 0

def main():
    input_data = sys.stdin.read
    lines = input_data().strip().split('\n')
    
    if not lines:
        return
    
    first_line = lines[0].split()
    n = int(first_line[0])
    m = int(first_line[1])
    
    edges = []
    for i in range(1, m + 1):
        if i < len(lines):
            u, v = map(int, lines[i].split())
            edges.append((u, v))
    
    # Seed for reproducibility
    random.seed(42)
    
    result = find_min_cut(n, edges)
    print(result)

if __name__ == "__main__":
    main()
