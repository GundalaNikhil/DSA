def all_orderings(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    Find one valid topological ordering of courses given prerequisites.
    Returns a single valid ordering or empty list if cycle exists (impossible).
    edges contains (u, v) meaning course u must come before course v.
    """
    # Build adjacency list and in-degree count
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Try to find one valid topological sort using backtracking
    def backtrack(current_order, remaining_indegrees):
        # Base case: we've ordered all courses
        if len(current_order) == n:
            return True

        # Find all courses that have no prerequisites (in-degree = 0)
        available = []
        for course in range(n):
            if remaining_indegrees[course] == 0 and course not in current_order:
                available.append(course)

        # Pruning: if no course is available, we have a cycle
        if not available:
            return False

        # Try each available course
        for course in available:
            current_order.append(course)

            # Reduce in-degree of all courses that depend on this course
            for dependent in graph[course]:
                remaining_indegrees[dependent] -= 1

            if backtrack(current_order, remaining_indegrees):
                return True

            # Backtrack
            for dependent in graph[course]:
                remaining_indegrees[dependent] += 1

            current_order.pop()

        return False

    current_order = []
    if backtrack(current_order, in_degree[:]):
        return [current_order]
    else:
        return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]

    result = all_orderings(n, edges)
    if not result:
        print("IMPOSSIBLE")
    else:
        for order in result:
            print(" ".join(str(x) for x in order))

if __name__ == "__main__":
    main()
