import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def tree_height(n: int, left: list[int], right: list[int]) -> int:
    if n == 0:
        return -1
        
    def dfs(u):
        if u == -1:
            return -1
        l_height = dfs(left[u])
        r_height = dfs(right[u])
        return 1 + max(l_height, r_height)
        
    return dfs(0)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    if n == 0:
        print("-1")
        return

    left = [0] * n
    right = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1 # Skip value
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print(tree_height(n, left, right))

if __name__ == "__main__":
    main()
