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
        
    # Find root - node with no incoming edges (no parent)
    has_parent = [False] * n
    for i in range(n):
        if left[i] != -1: has_parent[left[i]] = True
        if right[i] != -1: has_parent[right[i]] = True
        
    root = 0
    for i in range(n):
        if not has_parent[i]:
            root = i
            break
            
    dfs(root)
    return max_diameter

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        left = [0] * n
        right = [0] * n
        lw = [0] * n
        rw = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            left[i] = parts[1]
            right[i] = parts[2]
            if len(parts) >= 5:
                lw[i] = parts[3]
                rw[i] = parts[4]
            else:
                lw[i] = 1
                rw[i] = 1
                
        print(weighted_diameter(n, left, right, lw, rw))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
