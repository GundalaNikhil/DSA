import sys
sys.setrecursionlimit(200000)
from collections import deque

def odd_depth_levels(n: int, left: list[int], right: list[int], values: list[int]) -> list[list[int]]:
    if n == 0:
        return []
        
    result = []
    q = deque([0])
    depth = 0
    
    while q:
        size = len(q)
        current_level = []
        is_odd = (depth % 2 != 0)
        
        for _ in range(size):
            u = q.popleft()
            if is_odd:
                current_level.append(values[u])
            
            if left[u] != -1:
                q.append(left[u])
            if right[u] != -1:
                q.append(right[u])
        
        if is_odd:
            result.append(current_level)
        depth += 1
        
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    if n == 0:
        print()
        return

    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    levels = odd_depth_levels(n, left, right, values)
    if not levels:
        print()
    else:
        print("\n".join(" ".join(str(x) for x in lvl) for lvl in levels))

if __name__ == "__main__":
    main()
