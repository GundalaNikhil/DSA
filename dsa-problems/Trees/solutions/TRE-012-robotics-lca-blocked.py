import sys
from collections import deque

def lca_blocked(n: int, values: list[int], blocked: list[int], left: list[int], right: list[int], u: int, v: int) -> int:
    parent = [-1] * n
    
    # 1. Build Parent Map
    q = deque([0])
    while q:
        curr = q.popleft()
        if left[curr] != -1:
            parent[left[curr]] = curr
            q.append(left[curr])
        if right[curr] != -1:
            parent[right[curr]] = curr
            q.append(right[curr])
            
    # 2. Find Standard LCA
    ancestors = set()
    curr = u
    while curr != -1:
        ancestors.add(curr)
        curr = parent[curr]
        
    lca = -1
    curr = v
    while curr != -1:
        if curr in ancestors:
            lca = curr
            break
        curr = parent[curr]
        
    if lca == -1:
        return -1
        
    # 3. Climb up
    while lca != -1 and blocked[lca] == 1:
        lca = parent[lca]
        
    return values[lca] if lca != -1 else -1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    blocked = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        blocked[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    u = int(data[idx]); idx += 1
    v = int(data[idx]); idx += 1
    
    print(lca_blocked(n, values, blocked, left, right, u, v))

if __name__ == "__main__":
    main()
