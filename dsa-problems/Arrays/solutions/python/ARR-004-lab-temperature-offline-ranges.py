import sys

# Increase recursion depth for deep trees if necessary
sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, size, arr):
        self.n = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)
        # Build tree
        self._build(arr, 0, 0, size - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node + 1, start, mid)
            self._build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            # Apply lazy to current node
            self.tree[node] += self.lazy[node] * (end - start + 1)
            # Push to children if not leaf
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, l, r, val):
        self._update(0, 0, self.n - 1, l, r, val)

    def _update(self, node, start, end, l, r, val):
        # Push pending updates
        self._push(node, start, end)
        
        if start > end or start > r or end < l:
            return

        if start >= l and end <= r:
            self.lazy[node] += val
            self._push(node, start, end)
            return

        mid = (start + end) // 2
        self._update(2 * node + 1, start, mid, l, r, val)
        self._update(2 * node + 2, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        self._push(node, start, end)
        
        if start > end or start > r or end < l:
            return 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        return self._query(2 * node + 1, start, mid, l, r) + \
               self._query(2 * node + 2, mid + 1, end, l, r)

def process_temperature_queries(temps: list[int], queries: list[tuple]) -> list[int]:
    n = len(temps)
    st = SegmentTree(n, temps)
    results = []
    
    for q in queries:
        type = q[0]
        if type == "add":
            l, r, x = q[1], q[2], q[3]
            st.update(l, r, x)
        else:
            l, r = q[1], q[2]
            results.append(st.query(l, r))
            
    return results

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
        temps = [int(next(iterator)) for _ in range(n)]
        q_count = int(next(iterator))
        
        queries = []
        for _ in range(q_count):
            type = next(iterator)
            l = int(next(iterator))
            r = int(next(iterator))
            if type == "add":
                x = int(next(iterator))
                queries.append((type, l, r, x))
            else:
                queries.append((type, l, r))
                
        result = process_temperature_queries(temps, queries)
        print("\n".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()


