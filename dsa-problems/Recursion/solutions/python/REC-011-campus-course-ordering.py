def find_topological_order(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    Find A SINGLE valid topological ordering of courses given prerequisites.
    edges contains (u, v) meaning course u must come before course v.
    Returns one valid ordering or empty list if no valid ordering exists.
    """
    # Build adjacency list and in-degree count
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    current_order = []
    used = [False] * n

    def backtrack(remaining_indegrees):
        # Base case: we've ordered all courses
        if len(current_order) == n:
            return True

        # Find a course that has no prerequisites (in-degree = 0)
        for course in range(n):
            if remaining_indegrees[course] == 0 and not used[course]:
                current_order.append(course)
                used[course] = True

                # Reduce in-degree of all courses that depend on this course
                for dependent in graph[course]:
                    remaining_indegrees[dependent] -= 1

                if backtrack(remaining_indegrees):
                    return True

                # Backtrack
                for dependent in graph[course]:
                    remaining_indegrees[dependent] += 1

                current_order.pop()
                used[course] = False

        return False

    if backtrack(in_degree[:]):
        return current_order
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

    result = find_topological_order(n, edges)
    if not result:
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
