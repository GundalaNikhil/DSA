import sys
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
    def find_kth(self, k):
        idx = 0
        current_sum = 0
        for i in range(17, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx < len(self.tree) and current_sum + self.tree[next_idx] < k:
                idx = next_idx
                current_sum += self.tree[idx]
                return idx + 1
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    values = []
    for _ in range(n):
        values.append(int(input_data[ptr]))
        ptr += 1
        
    q = int(input_data[ptr])
    ptr += 1
    
    deleted = [False] * (n + 1)
    ft = FenwickTree(n)
    
    # Initialize FT: all present
    for i in range(1, n + 1):
        ft.update(i, 1)
        
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'DEL':
            u = int(input_data[ptr])
            ptr += 1
            if not deleted[u]:
                deleted[u] = True
                ft.update(u, -1)
                
        elif op == 'RESTORE':
            u = int(input_data[ptr])
            ptr += 1
            if deleted[u]:
                deleted[u] = False
                ft.update(u, 1)
                
        elif op == 'KTH':
            k = int(input_data[ptr])
            ptr += 1
            mode = int(input_data[ptr])
            ptr += 1
            
            if mode == 1:
                # Kth original element (raw index)
                if 1 <= k <= n:
                    print(values[k - 1])
                else:
                    print("-1")
            else:
                # Kth active element
                total_alive = ft.query(n)
                if 1 <= k <= total_alive:
                    idx = ft.find_kth(k)
                    print(values[idx - 1])
                else:
                    print("-1")
if __name__ == '__main__':
    solve()