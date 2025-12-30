def find_topological_order(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    Find a topological ordering of courses using Kahn's algorithm.
    edges contains (u, v) meaning course u must come before course v.
    Returns a valid ordering or empty list if a cycle exists (IMPOSSIBLE).
    """
    from collections import deque

    # Build adjacency list and in-degree count
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Initialize queue with all nodes having in-degree 0
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        # Process the node with smallest index (lexicographic order)
        node = queue.popleft()
        result.append(node)

        # Reduce in-degree for all neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we processed all nodes, we have a valid ordering
    if len(result) == n:
        return result
    else:
        return []  # Cycle detected

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]

    result = find_topological_order(n, edges)
    if not result:
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
