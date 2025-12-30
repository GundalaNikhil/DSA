def process(arr: list[int], mod: int, ops: list[list[str]]) -> list[int]:
    n = len(arr)
    bit = [0] * (n + 1)
    
    def add(idx, val):
        idx += 1  # 1-based
        while idx <= n:
            bit[idx] = (bit[idx] + val) % mod
            idx += idx & (-idx)
            
    def query(idx):
        idx += 1
        s = 0
        while idx > 0:
            s = (s + bit[idx]) % mod
            idx -= idx & (-idx)
        return s

    # Build BIT
    for i, x in enumerate(arr):
        add(i, x)
        
    current_arr = list(arr)
    history = [] # Stack of (index, old_value)
    results = []
    
    for op in ops:
        type = op[0]
        if type == "UPDATE":
            idx = int(op[1])
            val = int(op[2])
            
            old_val = current_arr[idx]
            history.append((idx, old_val))
            
            diff = (val - old_val) % mod
            add(idx, diff)
            current_arr[idx] = val
            
        elif type == "QUERY":
            l = int(op[1])
            r = int(op[2])
            # Sum [l, r] is query(r) - query(l-1)
            
            # query(l-1) returns sum 0..l-1
            res = (query(r) - query(l - 1)) % mod
            results.append(res)
            
        elif type == "UNDO":
            k = int(op[1])
            while k > 0 and history:
                idx, old_val = history.pop()
                current_val = current_arr[idx]
                
                diff = (old_val - current_val) % mod
                add(idx, diff)
                current_arr[idx] = old_val
                k -= 1
                
    return results

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    q = int(next(it))
    mod = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "UNDO":
            ops.append([type, next(it)])
        else:
            ops.append([type, next(it), next(it)])
    
    results = process(arr, mod, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
