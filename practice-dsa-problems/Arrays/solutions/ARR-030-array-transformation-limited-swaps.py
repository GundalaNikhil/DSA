from collections import deque
from collections import Counter
import sys

class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k_limit = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
        b = []
        for _ in range(n):
            b.append(int(next(iterator)))
    except StopIteration:
        return

    
    if Counter(a) != Counter(b):
        print("NO")
        return
        
    # Map each element to its positions in `a`.
    indices = {}
    for i, x in enumerate(a):
        if x not in indices:
            indices[x] = deque()
        indices[x].append(i)
        
    # Construct permutation `p`.
    
    p = []
    for x in b:
        # Get index of this value in a
        idx = indices[x].popleft()
        p.append(idx)
        
    # Count inversions in p.
    # Inversion: pair (i, j) i < j such that p[i] > p[j].
    # Use Fenwick Tree.
    # Iterate right to left?
    
    ft = FenwickTree(n)
    inversions = 0
    
    
    for i in range(n - 1, -1, -1):
        # Count elements to right smaller than current
        # Actually p[i] values are distinct (0..n-1).
        inversions += ft.query(p[i])
        ft.update(p[i] + 1, 1)
        
    print("YES" if inversions <= k_limit else "NO")

if __name__ == "__main__":
    solve()
