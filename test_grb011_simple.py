import sys

def count_edges_below_threshold(n: int, edges: list[tuple[int, int, int]], T: int) -> int:
    """Count edges with capacity < T"""
    count = 0
    for u, v, c in edges:
        if c < T:
            count += 1
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        T = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
        
        ans = count_edges_below_threshold(n, edges, T)
        print(ans)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
