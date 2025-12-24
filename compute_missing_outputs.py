#!/usr/bin/env python3
"""Script to compute missing outputs for AGR-001 test cases by reading from YAML."""

import yaml

def min_cut(n: int, edges: list[tuple[int, int, int]]) -> int:
    adj = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        adj[u][v] += w
        adj[v][u] += w
        
    global_min_cut = float('inf')
    merged = [False] * n
    nodes_remaining = n
    
    while nodes_remaining > 1:
        # Minimum Cut Phase
        weights = [0] * n
        in_set = [False] * n
        prev, curr = -1, -1
        
        for _ in range(nodes_remaining):
            max_weight = -1
            next_node = -1
            for i in range(n):
                if not merged[i] and not in_set[i] and weights[i] > max_weight:
                    max_weight = weights[i]
                    next_node = i
            
            if next_node == -1:
                break
                
            in_set[next_node] = True
            prev = curr
            curr = next_node
            
            # Update weights
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    weights[i] += adj[curr][i]
        
        # Update global min cut
        global_min_cut = min(global_min_cut, weights[curr])
        
        # Merge curr into prev
        if prev != -1:
            for i in range(n):
                if i != curr and i != prev and not merged[i]:
                    adj[prev][i] += adj[curr][i]
                    adj[i][prev] += adj[curr][i]
                    
        merged[curr] = True
        nodes_remaining -= 1
        
    return global_min_cut if global_min_cut != float('inf') else 0


def parse_test_input(input_str):
    """Parse test input from YAML format."""
    lines = input_str.strip().split('\n')
    n, m = map(int, lines[0].split())
    edges = []
    for i in range(1, m + 1):
        if i < len(lines):
            parts = lines[i].split()
            if len(parts) == 3:
                u, v, w = map(int, parts)
                edges.append((u, v, w))
    return n, edges


# Read the YAML file
yaml_path = 'dsa-problems/AdvancedGraphs/testcases/AGR-001-min-cut-small-graph.yaml'
with open(yaml_path, 'r') as f:
    data = yaml.safe_load(f)

# Find test cases with empty outputs
test_cases_to_fix = []
for idx, test in enumerate(data['hidden']):
    if test['output'].strip() == '':
        test_cases_to_fix.append(('hidden', idx, test['input']))

print(f"Found {len(test_cases_to_fix)} test cases with empty outputs\n")

# Compute outputs
for category, idx, input_str in test_cases_to_fix:
    print(f"Computing output for {category}[{idx}]...")
    n, edges = parse_test_input(input_str)
    print(f"  Graph: {n} nodes, {len(edges)} edges")
    output = min_cut(n, edges)
    print(f"  Output: {output}\n")
    
    # Update the YAML data
    data[category][idx]['output'] = str(output)

# Write back to YAML
with open(yaml_path, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print("Updated YAML file successfully!")
