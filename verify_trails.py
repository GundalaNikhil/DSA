# Test case 12:
# 4 nodes, 6 edges
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 0),
    (3, 0)
]

def verify_trail(trail, edges):
    """Verify if a trail uses all edges exactly once"""
    if not trail:
        return False
    
    # Create edge list for verification
    edge_multiset = sorted(edges)
    trail_edges = []
    
    for i in range(len(trail) - 1):
        trail_edges.append((trail[i], trail[i+1]))
    
    trail_edges_sorted = sorted(trail_edges)
    
    print(f"Expected edges: {edge_multiset}")
    print(f"Trail edges:   {trail_edges_sorted}")
    print(f"Match: {edge_multiset == trail_edges_sorted}")
    
    # Check starting node
    out_deg = {}
    in_deg = {}
    for u, v in edges:
        out_deg[u] = out_deg.get(u, 0) + 1
        in_deg[v] = in_deg.get(v, 0) + 1
    
    start_node = None
    for i in range(4):
        if out_deg.get(i, 0) == in_deg.get(i, 0) + 1:
            start_node = i
            break
    
    print(f"Expected start node: {start_node}")
    print(f"Actual start node: {trail[0]}")
    print()

print("Python/JavaScript trail: [0, 2, 3, 0, 1, 3, 0]")
verify_trail([0, 2, 3, 0, 1, 3, 0], edges)

print("Java trail: [0, 1, 3, 0, 2, 3, 0]")
verify_trail([0, 1, 3, 0, 2, 3, 0], edges)
