import sys
from bisect import bisect_left, bisect_right

class Summary:
    def __init__(self):
        self.candidates = {} # val -> count
        self.K = 40
        
    def add(self, val, count):
        self.candidates[val] = self.candidates.get(val, 0) + count
        if len(self.candidates) > self.K:
            min_cnt = min(self.candidates.values())
            to_remove = []
            for k, v in self.candidates.items():
                self.candidates[k] -= min_cnt
                if self.candidates[k] <= 0:
                    to_remove.append(k)
            for k in to_remove:
                del self.candidates[k]
                
    def merge(self, other):
        for val, count in other.candidates.items():
            self.add(val, count)

def process(arr: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    n = len(arr)
    
    # Positions map
    positions = {}
    for i, x in enumerate(arr):
        if x not in positions:
            positions[x] = []
        positions[x].append(i)
        
    tree = [None] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            s = Summary()
            s.add(arr[start], 1)
            tree[node] = s
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            
            s = Summary()
            s.merge(tree[2 * node + 1])
            s.merge(tree[2 * node + 2])
            tree[node] = s

    def query_tree(node, start, end, l, r):
        if l > end or r < start:
            return Summary()
        if l <= start and end <= r:
            return tree[node]
            
        mid = (start + end) // 2
        s1 = query_tree(2 * node + 1, start, mid, l, r)
        s2 = query_tree(2 * node + 2, mid + 1, end, l, r)
        
        res = Summary()
        res.merge(s1)
        res.merge(s2)
        return res

    build(0, 0, n - 1)
    
    import random
    results = []
    for l, r, t in queries:
        s = query_tree(0, 0, n - 1, l, r)
        cands = set(s.candidates.keys())
        for _ in range(40):
            cands.add(arr[random.randint(l, r)])
            
        best_val = -1
        max_freq = -1
        
        for val in cands:
            pos = positions[val]
            freq = bisect_right(pos, r) - bisect_left(pos, l)
            if freq >= t:
                if freq > max_freq:
                    max_freq, best_val = freq, val
                elif freq == max_freq:
                    if best_val == -1 or val < best_val:
                        best_val = val
        results.append(best_val)
    return results

def main():
    import sys
    # Increase recursion depth for deep trees
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        type = next(it) # MAJ
        l = int(next(it))
        r = int(next(it))
        t = int(next(it))
        queries.append((l, r, t))
    
    results = process(arr, queries)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
