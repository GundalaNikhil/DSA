import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def max_opposite_parity_gap(n: int, values: list[int], left: list[int], right: list[int]) -> int:
    if n == 0:
        return 0
        
    max_diff = 0
    
    # min_e, max_e, min_o, max_o
    # Use None for invalid
    
    def dfs(u, depth, min_e, max_e, min_o, max_o):
        nonlocal max_diff
        if u == -1:
            return
            
        val = values[u]
        
        if depth % 2 == 0:
            # Even depth: compare with Odd ancestors
            if min_o is not None:
                max_diff = max(max_diff, abs(val - min_o), abs(val - max_o))
            
            # Update Even bounds
            new_min_e = val if min_e is None else min(min_e, val)
            new_max_e = val if max_e is None else max(max_e, val)
            
            # Pass Odd bounds as is
            if left[u] != -1: dfs(left[u], depth + 1, new_min_e, new_max_e, min_o, max_o)
            if right[u] != -1: dfs(right[u], depth + 1, new_min_e, new_max_e, min_o, max_o)
            
        else:
            # Odd depth: compare with Even ancestors
            if min_e is not None:
                max_diff = max(max_diff, abs(val - min_e), abs(val - max_e))
                
            # Update Odd bounds
            new_min_o = val if min_o is None else min(min_o, val)
            new_max_o = val if max_o is None else max(max_o, val)
            
            # Pass Even bounds as is
            if left[u] != -1: dfs(left[u], depth + 1, min_e, max_e, new_min_o, new_max_o)
            if right[u] != -1: dfs(right[u], depth + 1, min_e, max_e, new_min_o, new_max_o)

    # Root is depth 0 (Even). Initialize Even bounds with root val. Odd bounds None.
    dfs(0, 0, values[0], values[0], None, None)
    return max_diff

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    print(max_opposite_parity_gap(n, values, left, right))

if __name__ == "__main__":
    main()
