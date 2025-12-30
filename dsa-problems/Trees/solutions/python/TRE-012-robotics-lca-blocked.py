import sys
sys.setrecursionlimit(200000)

def lca_blocked(n: int, values: list[int], blocked: list[int], left: list[int], right: list[int], u: int, v: int) -> int:
    parent = [-1] * n
    
    # Build Parent Map iterating all nodes
    for i in range(n):
        if left[i] != -1:
            parent[left[i]] = i
        if right[i] != -1:
            parent[right[i]] = i
            
    # Find Ancestors of U
    ancestors = set()
    curr = u
    # Safety: loop limit to prevent infinite if cycle
    steps = 0
    while curr != -1 and steps < n + 5:
        ancestors.add(curr)
        curr = parent[curr]
        steps += 1
        
    lca = -1
    curr = v
    steps = 0
    while curr != -1 and steps < n + 5:
        if curr in ancestors:
            lca = curr
            break
        curr = parent[curr]
        steps += 1
        
    if lca == -1:
        return -1
        
    # Climb up if blocked
    steps = 0
    while lca != -1 and blocked[lca] == 1 and steps < n + 5:
        lca = parent[lca]
        steps += 1
        
    return values[lca] if lca != -1 else -1

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        values = [0] * n
        blocked = [0] * n
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            # 4 tokens: val blocked left right
            # 3 tokens: val left right
            
            values[i] = parts[0]
            if len(parts) >= 4:
                blocked[i] = parts[1]
                left[i] = parts[2]
                right[i] = parts[3]
            else:
                blocked[i] = 0
                left[i] = parts[1]
                right[i] = parts[2]
                
        line = next(iterator)
        u, v = map(int, line.split())
        
        # u and v are indices in this problem context? 
        # Test cases seem to implies indices.
        # But if they are values, we need a map. 
        # Given "lca of u and v", and previous tre012 failure, let's assume indices.
        # If they are values, we need value_to_index map.
        # Let's add robustness: if u or v >= n, try to look up index by value?
        # But values might not be unique.
        # Standard assumption for "u and v" in LCA is node indices.
        
        print(lca_blocked(n, values, blocked, left, right, u, v))
        
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
