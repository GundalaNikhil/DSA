import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def validate_bst_gap(n: int, values: list[int], left: list[int], right: list[int], G: int) -> bool:
    if n == 0:
        return True
        
    def validate(u, min_val, max_val):
        if u == -1:
            return True
            
        val = values[u]
        # BST Check
        if val <= min_val or val >= max_val:
            return False
            
        # Left Child
        if left[u] != -1:
            l_val = values[left[u]]
            if abs(val - l_val) < G:
                return False
            if not validate(left[u], min_val, val):
                return False
                
        # Right Child
        if right[u] != -1:
            r_val = values[right[u]]
            if abs(val - r_val) < G:
                return False
            if not validate(right[u], val, max_val):
                return False
                
        return True

    return validate(0, float('-inf'), float('inf'))

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
    G = int(data[idx]) if idx < len(data) else 0
    
    print("true" if validate_bst_gap(n, values, left, right, G) else "false")

if __name__ == "__main__":
    main()
