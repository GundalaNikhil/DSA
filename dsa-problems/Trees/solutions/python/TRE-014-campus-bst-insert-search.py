import sys

# Increase recursion depth just in case
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

def get_inorder(node, result):
    if node is None:
        return
    get_inorder(node.left, result)
    result.append(node.val)
    get_inorder(node.right, result)

def search(node, x):
    if node is None:
        return False
    if node.val == x:
        return True
    if x < node.val:
        return search(node.left, x)
    return search(node.right, x)

# Global root for simplicity in functional style
root = None

def build_inorder(values: list[int]) -> list[int]:
    global root
    root = None
    for v in values:
        root = insert(root, v)
    result = []
    get_inorder(root, result)
    return result

def search_value(values: list[int], x: int) -> bool:
    global root
    # If root is not built (e.g. direct call), rebuild
    if root is None and values:
        for v in values:
            root = insert(root, v)
    return search(root, x)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [int(data[idx + i]) for i in range(n)]
    idx += n
    x = int(data[idx]) if idx < len(data) else 0
    
    inorder = build_inorder(values)
    print(" ".join(str(v) for v in inorder))
    print("true" if search_value(values, x) else "false")

if __name__ == "__main__":
    main()
