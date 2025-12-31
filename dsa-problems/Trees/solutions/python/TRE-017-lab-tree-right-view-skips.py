import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def right_view_with_skips(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    if n == 0:
        return []
        
    view = {}
    max_depth = -1
    
    def dfs(u, depth):
        nonlocal max_depth
        if u == -1:
            return
            
        max_depth = max(max_depth, depth)
        
        if values[u] >= 0 and depth not in view:
            view[depth] = values[u]
            
        dfs(right[u], depth + 1)
        dfs(left[u], depth + 1)
        
    dfs(0, 0)
    
    result = []
    for d in range(max_depth + 1):
        if d in view:
            result.append(view[d])
            
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
    ans = right_view_with_skips(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
