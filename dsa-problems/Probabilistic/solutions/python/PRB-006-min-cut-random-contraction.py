import sys
import random
from collections import defaultdict

def karger_min_cut(n: int, edges):
    """
    Compute the minimum cut using Karger's algorithm.
    """
    # Create adjacency list representation - use a list of edges per node
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Keep track of which vertices are merged
    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    # Create list of edges
    edge_list = list(edges)
    random.shuffle(edge_list)
    
    num_components = n

    # Contract until 2 vertices remain
    for u, v in edge_list:
        if num_components <= 2:
            break
            
        pu, pv = find(u), find(v)

        if pu != pv:
            union(pu, pv)
            num_components -= 1

    # Count edges crossing the cut
    cut_size = 0
    for u, v in edge_list:
        if find(u) != find(v):
            cut_size += 1

    return cut_size

def main():
    input_data = sys.stdin.read
    lines = input_data().strip().split('\n')

    if not lines:
        return

    n, m = map(int, lines[0].split())
    edges = []

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        edges.append((u, v))

    # Run Karger's algorithm multiple times and return minimum
    min_cut = float('inf')

    # Number of trials - Karger's algorithm may need many runs for accuracy
    # but we need to balance with performance
    # Number of trials - Karger's algorithm succeeds with probability >= 2/(n(n-1))
    # We need enough trials to ensure high probability of finding min cut.
    # For small n, we can run many trials.
    # Theoretical bound for failure < 1/n is O(n^2 log n) trials.
    if n <= 20:
        trials = 100
    else:
        trials = int(n * n * 0.5)  # Heuristic for larger n

    for _ in range(trials):
        cut = karger_min_cut(n, edges)
        min_cut = min(min_cut, cut)

    print(min_cut)

if __name__ == "__main__":
    main()
