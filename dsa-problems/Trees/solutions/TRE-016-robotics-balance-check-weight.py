import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def is_balanced_weighted(n: int, weight: list[int], left: list[int], right: list[int], W: int) -> bool:
    if n == 0:
        return True
        
    # Returns (height, total_weight, is_balanced)
    def dfs(u):
        if u == -1:
            return 0, 0, True
            
        h_l, w_l, bal_l = dfs(left[u])
        if not bal_l:
            return 0, 0, False
            
        h_r, w_r, bal_r = dfs(right[u])
        if not bal_r:
            return 0, 0, False
            
        h_bal = abs(h_l - h_r) <= 1
        w_bal = abs(w_l - w_r) <= W
        
        if h_bal and w_bal:
            return max(h_l, h_r) + 1, w_l + w_r + weight[u], True
        else:
            return 0, 0, False

    return dfs(0)[2]

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    weight = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        weight[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    W = int(data[idx]) if idx < len(data) else 0
    
    print("true" if is_balanced_weighted(n, weight, left, right, W) else "false")

if __name__ == "__main__":
    main()
