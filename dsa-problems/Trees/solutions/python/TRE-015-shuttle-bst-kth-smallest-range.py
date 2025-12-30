import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, val):
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def kth_in_range(values: list[int], L: int, R: int, k: int) -> int:
    root = None
    for v in values:
        root = insert(root, v)
        
    count = 0
    result = -1
    
    def inorder(node):
        nonlocal count, result
        if node is None or result != -1:
            return
            
        # Visit left if potentially valid
        if node.val > L:
            inorder(node.left)
            
        if result != -1: return
        
        if L <= node.val <= R:
            count += 1
            if count == k:
                result = node.val
                return
                
        # Visit right if potentially valid
        if node.val < R:
            inorder(node.right)

    inorder(root)
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [int(data[idx + i]) for i in range(n)]
    idx += n
    L = int(data[idx]); idx += 1
    R = int(data[idx]); idx += 1
    k = int(data[idx]) if idx < len(data) else 1
    
    print(kth_in_range(values, L, R, k))

if __name__ == "__main__":
    main()
