import sys

class SparseTable:
    def __init__(self, arr, op):
        n = len(arr)
        self.op = op
        self.st = [arr]
        # bit_length of n: e.g. 5 -> 3 bits. 1<<2 = 4.
        k = n.bit_length()
        for i in range(1, k):
            prev = self.st[-1]
            length = 1 << (i - 1)
            # Create next level. Range [j, j + 2^i - 1].
            # Combines prev[j] (covers 2^(i-1)) and prev[j + 2^(i-1)].
            # Valid j goes up to n - 2^i.
            curr = []
            for j in range(n - (1 << i) + 1):
                curr.append(op(prev[j], prev[j + length]))
            self.st.append(curr)

    def query(self, l, r):
        # l, r 0-indexed inclusive
        length = r - l + 1
        k = length.bit_length() - 1
        return self.op(self.st[k][l], self.st[k][r - (1 << k) + 1])

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        r_rules = int(next(iterator))
        q_toggles = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
            
        rules = []
        # Preprocess Sparse Tables
        st_max = SparseTable(a, max)
        st_min = SparseTable(a, min)
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + a[i]
            
        
        rule_satisfied = []
        for _ in range(r_rules):
            rtype = next(iterator)
            l = int(next(iterator)) - 1 # 1-based to 0-based
            r = int(next(iterator)) - 1
            x = int(next(iterator))
            
            is_ok = False
            if rtype == "MAX":
                is_ok = st_max.query(l, r) <= x
            elif rtype == "MIN":
                is_ok = st_min.query(l, r) >= x
            elif rtype == "SUM":
                is_ok = (pref[r + 1] - pref[l]) <= x
                
            rule_satisfied.append(is_ok)
        
        is_active = [False] * r_rules
        active_invalid_count = 0
        out = []
        
        for _ in range(q_toggles):
            rid = int(next(iterator)) - 1
            
            # Toggle
            if is_active[rid]:
                # Deactivating
                is_active[rid] = False
                if not rule_satisfied[rid]:
                    active_invalid_count -= 1
            else:
                # Activating
                is_active[rid] = True
                if not rule_satisfied[rid]:
                    active_invalid_count += 1
                    
            out.append("VALID" if active_invalid_count == 0 else "INVALID")
            
        sys.stdout.write("\n".join(out) + "\n")
            
    except StopIteration:
        return

if __name__ == "__main__":
    solve()
