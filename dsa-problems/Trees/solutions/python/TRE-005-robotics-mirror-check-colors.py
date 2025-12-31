import sys
from collections import deque

# Increase recursion depth
sys.setrecursionlimit(200000)

def mirror_check(n: int, values: list[int], colors: list[int], left: list[int], right: list[int]) -> bool:
    if n == 0:
        return True
        
    # 1. Check Symmetry
    def is_mirror(u, v):
        if u == -1 and v == -1:
            return True
        if u == -1 or v == -1:
            return False
        if values[u] != values[v]:
            return False
        return is_mirror(left[u], right[v]) and is_mirror(right[u], left[v])
        
    if left[0] == -1 and right[0] == -1:
        return True
    if not is_mirror(left[0], right[0]):
        return False
        
    # 2. Check Color Balance
    qL = deque([left[0]])
    qR = deque([right[0]])
    
    while qL and qR:
        if len(qL) != len(qR):
            return False
            
        sumL = 0
        size = len(qL)
        for _ in range(size):
            u = qL.popleft()
            sumL += colors[u]
            if left[u] != -1: qL.append(left[u])
            if right[u] != -1: qL.append(right[u])
            
        sumR = 0
        for _ in range(size):
            v = qR.popleft()
            sumR += colors[v]
            if left[v] != -1: qR.append(left[v])
            if right[v] != -1: qR.append(right[v])
            
        if sumL != sumR:
            return False
            
    return not qL and not qR

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    values = [0] * n
    colors = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        colors[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print("true" if mirror_check(n, values, colors, left, right) else "false")

if __name__ == "__main__":
    main()
