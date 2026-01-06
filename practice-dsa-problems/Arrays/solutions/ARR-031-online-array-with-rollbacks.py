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

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
            
        queries = []
        for _ in range(q):
            op = next(iterator)
            if op == "SET":
                idx = int(next(iterator))
                val = int(next(iterator))
                queries.append((op, idx, val))
            elif op == "SUM":
                l = int(next(iterator))
                r = int(next(iterator))
                queries.append((op, l, r))
            elif op == "UNDO":
                queries.append((op,))
                
    except StopIteration:
        return


    ft = FenwickTree(n)
    for i in range(1, n + 1):
        ft.update(i, a[i - 1])
        
    curr_a = list(a) # 0-indexed
    undo_stack = [] # stores (index, previous_value) for SET ops
    
    # Process queries
    
    for query_args in queries:
        op = query_args[0]
        
        if op == "SET":
            idx, val = query_args[1], query_args[2]
            # idx is likely 1-based? Original code `curr_a[idx - 1]`. Yes.
            old_val = curr_a[idx - 1]
            diff = val - old_val
            
            ft.update(idx, diff)
            curr_a[idx - 1] = val
            undo_stack.append((idx, old_val)) # Store old value to restore
            
        elif op == "SUM":
            l, r = query_args[1], query_args[2]
            print(ft.query(r) - ft.query(l - 1))
            
        elif op == "UNDO":
            if undo_stack:
                idx, val_to_restore = undo_stack.pop()
                current_val = curr_a[idx - 1]
                diff = val_to_restore - current_val
                
                ft.update(idx, diff)
                curr_a[idx - 1] = val_to_restore

if __name__ == "__main__":
    solve()
