import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def weighted_diameter(n: int, left: list[int], right: list[int], lw: list[int], rw: list[int]) -> int:
    if n == 0:
        return 0
        
    max_diameter = 0
    
    def dfs(u):
        nonlocal max_diameter
        if u == -1:
            return 0
            
        l_path = 0
        r_path = 0
        
        if left[u] != -1:
            l_path = lw[u] + dfs(left[u])
        if right[u] != -1:
            r_path = rw[u] + dfs(right[u])
            
        max_diameter = max(max_diameter, l_path + r_path)
        
        return max(l_path, r_path)
        
    dfs(0)
    return max_diameter

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    left = [0] * n
    right = [0] * n
    lw = [0] * n
    rw = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        lw[i] = int(data[idx]); idx += 1
        rw[i] = int(data[idx]); idx += 1
        
    print(weighted_diameter(n, left, right, lw, rw))

if __name__ == "__main__":
    main()
