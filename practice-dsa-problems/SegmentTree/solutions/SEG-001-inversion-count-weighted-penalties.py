import sys
import math


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
            return s


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    p_percent = int(input_data[ptr])
    ptr += 1
    a = []
    for i in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    # Pre-processing (moved out of loop)
    h_size = math.ceil(p_percent * n / 100)
    
    # "is_h": Heaviest elements?
    # Logic: sort a, take top h_size?
    # Original code: `indexed_a.append((-a[i], i, i))`. Sorts. Takes top h_size.
    # Why `(-a[i], i, i)`? To sort descending by value.
    indexed_a = []
    for i in range(n):
        indexed_a.append((-a[i], i)) # Value, Original Index
        
    indexed_a.sort() # Sorts by -value (desc), then index (asc)
    
    is_h = [False] * n
    for i in range(h_size):
        idx = indexed_a[i][1]
        is_h[idx] = True
        
    sorted_a = sorted(list(set(a)))
    rank_map = {v: i + 1 for i, v in enumerate(sorted_a)}
    a_ranks = [rank_map[x] for x in a]
    
    bit_all = FenwickTree(len(sorted_a))
    bit_h = FenwickTree(len(sorted_a))
    
    total_inv = 0
    inv_h = 0
    
    for i in range(n):
        r = a_ranks[i]
        
        # Inversion Count:
        # Count elements > current element that appeared before?
        # Standard Inversion: i < j and A[i] > A[j].
        # Here we iterate i from 0 to n.
        # We query BIT for elements seen so far that are GREATER than current.
        # BIT stores counts of ranks seen.
        # `i` is count of elements seen so far.
        # `bit_all.query(r)` is count of elements <= r seen so far.
        # `i - bit_all.query(r)` is count of elements > r seen so far.
        # This gives pairs (j, i) where j < i and A[j] > A[i]. Correct.
        
        cnt_all = i - bit_all.query(r)
        
        # bit_h tracks only heavy elements seen so far?
        # bit_h.query(len) - bit_h.query(r) = count of heavy elements > r seen so far.
        cnt_h_prev = bit_h.query(len(sorted_a)) - bit_h.query(r)
        
        total_inv += cnt_all
        
        if is_h[i]:
            # If current is heavy:
            # It contributes to "Weighted Penalties" of previous heavy inversions?
            # Or does it add `cnt_all` to `inv_h`?
            # Original code: `if is_h[i]: inv_h += cnt_all`
            # This means if current is heavy, ALL inversions it forms (with any prev element) add to inv_h?
            inv_h += cnt_all
        else:
            # If current is NOT heavy:
            # `inv_h += cnt_h_prev`
            # This adds inversions formed with PREVIOUS HEAVY elements?
            inv_h += cnt_h_prev
            
        bit_all.update(r, 1)
        if is_h[i]:
            bit_h.update(r, 1)
            
    # Output result at end
    print(total_inv + inv_h)


if __name__ == "__main__":
    solve()
