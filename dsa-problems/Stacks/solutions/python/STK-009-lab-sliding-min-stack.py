def process(ops: list[list[str]]) -> list[str]:
    result = []
    n = 100005
    tree = [float('inf')] * (4 * n)
    current_size = 0
    stack_vals = [] # Keep a simple list for O(1) access to popped values
    
    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])
        
    def query(node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return min(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r))
                   
    for op in ops:
        cmd = op[0]
        if cmd == "PUSH":
            val = int(op[1])
            stack_vals.append(val)
            update(1, 0, n - 1, current_size, val)
            current_size += 1
        elif cmd == "POP":
            if current_size == 0:
                result.append("EMPTY")
            else:
                val = stack_vals.pop()
                result.append(str(val))
                current_size -= 1
        elif cmd == "MIN":
            k = int(op[1])
            if current_size < k:
                result.append("NA")
            else:
                min_val = query(1, 0, n - 1, current_size - k, current_size - 1)
                result.append(str(min_val))
                
    return result


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
