import sys

# Increase recursion depth for deep trees (though path compression prevents this mostly)
sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def process_queries(n: int, queries: list[tuple[str, int, int]]) -> list[bool]:
    dsu = DSU(n)
    results = []
    for t, u, v in queries:
        if t == "union":
            dsu.union(u, v)
        else:
            results.append(dsu.find(u) == dsu.find(v))
    return results

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            t = next(iterator)
            u = int(next(iterator))
            v = int(next(iterator))
            queries.append((t, u, v))
            
        ans = process_queries(n, queries)
        print("\n".join("true" if x else "false" for x in ans))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
