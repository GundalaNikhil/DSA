import sys
from collections import deque, defaultdict

def vertical_order_with_weights(n: int, values: list[int], weights: list[int],
                                left: list[int], right: list[int], W: int) -> list[list[int]]:
    if n == 0:
        return []
        
    cols = defaultdict(list)
    q = deque([(0, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    while q:
        u, c, d = q.popleft()
        cols[c].append((values[u], weights[u], d))
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if left[u] != -1:
            q.append((left[u], c - 1, d + 1))
        if right[u] != -1:
            q.append((right[u], c + 1, d + 1))
            
    result = []
    for c in range(min_col, max_col + 1):
        if c in cols:
            nodes = cols[c]
            total_weight = sum(node[1] for node in nodes)
            
            if total_weight >= W:
                # Sort: depth asc, weight desc, val asc
                nodes.sort(key=lambda x: (x[2], -x[1], x[0]))
                result.append([x[0] for x in nodes])
                
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    weights = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        weights[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    W = int(data[idx]) if idx < len(data) else 0
    
    cols = vertical_order_with_weights(n, values, weights, left, right, W)
    if not cols:
        print()
    else:
        print("\n".join(" ".join(str(x) for x in col) for col in cols))

if __name__ == "__main__":
    main()
