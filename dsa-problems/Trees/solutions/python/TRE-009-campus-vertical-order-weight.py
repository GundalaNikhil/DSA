import sys
sys.setrecursionlimit(200000)
from collections import deque, defaultdict

def vertical_order_with_weights(n: int, values: list[int], weights: list[int],
                                left: list[int], right: list[int], W: int) -> list[list[int]]:
    if n == 0:
        return []

    # Identify Root
    has_parent = [False] * n
    for i in range(n):
        if left[i] != -1: has_parent[left[i]] = True
        if right[i] != -1: has_parent[right[i]] = True
        
    root = 0
    for i in range(n):
        if not has_parent[i]:
            root = i
            break
            
    cols = defaultdict(list)
    q = deque([(root, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    visited = {root} # Safety against cycles/bad input
    
    while q:
        u, c, d = q.popleft()
        cols[c].append((values[u], weights[u], d))
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if left[u] != -1 and left[u] not in visited:
            visited.add(left[u])
            q.append((left[u], c - 1, d + 1))
        if right[u] != -1 and right[u] not in visited:
            visited.add(right[u])
            q.append((right[u], c + 1, d + 1))
            
    result = []
    for c in range(min_col, max_col + 1):
        if c in cols:
            nodes = cols[c]
            total_weight = sum(node[1] for node in nodes)
            if total_weight >= W:
                # Priority: depth asc (x[2]), weight desc (-x[1]), value asc (x[0])
                nodes.sort(key=lambda x: (x[2], -x[1], x[0]))
                result.append([x[0] for x in nodes])
                
    return result

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        values = [0] * n
        weights = [0] * n
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            # 4 tokens: val weight left right
            # 3 tokens: val left right (default weight 1)
            
            values[i] = parts[0]
            if len(parts) >= 4:
                weights[i] = parts[1]
                left[i] = parts[2]
                right[i] = parts[3]
            else:
                weights[i] = 1
                left[i] = parts[1]
                right[i] = parts[2]
                
        # W might be on next line
        try:
            line = next(iterator)
            W = int(line)
        except StopIteration:
            W = 0
            
        cols = vertical_order_with_weights(n, values, weights, left, right, W)
        if not cols:
            print()
        else:
            print("\n".join(" ".join(str(x) for x in col) for col in cols))
            
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
