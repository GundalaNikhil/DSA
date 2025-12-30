import sys
from collections import deque

def top_view(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    if n == 0:
        return []
        
    # Map: col -> (depth, val)
    view_map = {}
    q = deque([(0, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    while q:
        u, c, d = q.popleft()
        
        if c not in view_map:
            view_map[c] = (d, values[u])
        else:
            existing_depth, existing_val = view_map[c]
            if d < existing_depth:
                view_map[c] = (d, values[u])
            elif d == existing_depth:
                if values[u] > existing_val:
                    view_map[c] = (d, values[u])
                    
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if left[u] != -1:
            q.append((left[u], c - 1, d + 1))
        if right[u] != -1:
            q.append((right[u], c + 1, d + 1))
            
    result = []
    for c in range(min_col, max_col + 1):
        if c in view_map:
            result.append(view_map[c][1])
            
    return result

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
    ans = top_view(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
