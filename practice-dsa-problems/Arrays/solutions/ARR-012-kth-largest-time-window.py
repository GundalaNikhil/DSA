import sys

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, i, delta):
        i += 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s 

    def find_kth(self, k):
        idx = 0
        for i in range(self.size.bit_length() - 1, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx <= self.size and self.tree[next_idx] < k:
                idx = next_idx
                k -= self.tree[idx]
        return idx


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k_val = int(next(iterator))
        w_size = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    sorted_a = sorted(list(set(a)))
    rank = {val: i for i, val in enumerate(sorted_a)}
    num_vals = len(sorted_a)
    
    ft = FenwickTree(num_vals)
    ans = []
    
    for i in range(n):
        # Add current element
        ft.update(rank[a[i]], 1)
        
        # Remove element leaving window
        if i >= w_size:
            ft.update(rank[a[i - w_size]], -1)
            
        curr_w_size = min(i + 1, w_size)
        
        if curr_w_size < k_val:
            ans.append(-1)
        else:
            target_rank = curr_w_size - k_val + 1
            idx = ft.find_kth(target_rank)
            ans.append(sorted_a[idx])
            
    print(*(ans))

if __name__ == "__main__":
    solve()
