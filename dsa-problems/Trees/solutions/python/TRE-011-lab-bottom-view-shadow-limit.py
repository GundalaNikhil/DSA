import sys
sys.setrecursionlimit(200000)
from collections import deque

def bottom_view_with_limit(n: int, values: list[int], left: list[int], right: list[int], D: int) -> list[int]:
    if n == 0:
        return []
        
    view_map = {}
    q = deque([(0, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    # If root depth > D (impossible since root is 0 and D >= 0), but safe check
    if D < 0:
        return []
        
    while q:
        u, c, d = q.popleft()
        
        view_map[c] = values[u]
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if d < D:
            if left[u] != -1:
                q.append((left[u], c - 1, d + 1))
            if right[u] != -1:
                q.append((right[u], c + 1, d + 1))
                
    result = []
    for c in range(min_col, max_col + 1):
        if c in view_map:
            result.append(view_map[c])
            
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
    D = int(data[idx]) if idx < len(data) else 0
    ans = bottom_view_with_limit(n, values, left, right, D)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
