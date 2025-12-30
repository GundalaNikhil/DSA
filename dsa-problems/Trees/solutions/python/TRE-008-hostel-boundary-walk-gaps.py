import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def boundary_with_gaps(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    if n == 0:
        return []
        
    result = []
    
    # 1. Root
    if values[0] >= 0:
        result.append(values[0])
        
    if left[0] == -1 and right[0] == -1:
        return result

    # 2. Left Boundary
    curr = left[0]
    while curr != -1:
        if left[curr] == -1 and right[curr] == -1:
            break # Leaf
        if values[curr] >= 0:
            result.append(values[curr])
        if left[curr] != -1:
            curr = left[curr]
        else:
            curr = right[curr]
            
    # 3. Leaves
    def add_leaves(u):
        if u == -1:
            return
        if left[u] == -1 and right[u] == -1:
            if values[u] >= 0:
                result.append(values[u])
            return
        add_leaves(left[u])
        add_leaves(right[u])
        
    add_leaves(0)
    
    # 4. Right Boundary
    right_bound = []
    curr = right[0]
    while curr != -1:
        if left[curr] == -1 and right[curr] == -1:
            break # Leaf
        if values[curr] >= 0:
            right_bound.append(values[curr])
        if right[curr] != -1:
            curr = right[curr]
        else:
            curr = left[curr]
            
    result.extend(reversed(right_bound))
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
    ans = boundary_with_gaps(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
