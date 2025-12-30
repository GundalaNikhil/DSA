import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def traverse_all(n, nodes):
    if n == 0:
        return [[], [], []]
    
    pre_order = []
    in_order = []
    post_order = []
    
    def dfs(u):
        if u == -1:
            return
        val, left, right = nodes[u]
        
        pre_order.append(val)
        dfs(left)
        in_order.append(val)
        dfs(right)
        post_order.append(val)
        
    dfs(0)
    return [pre_order, in_order, post_order]

def structural_identical(n1, t1, n2, t2):
    if n1 == 0 and n2 == 0:
        return True
    if n1 == 0 or n2 == 0:
        return False
        
    def check(u1, u2):
        if u1 == -1 and u2 == -1:
            return True
        if u1 == -1 or u2 == -1:
            return False
            
        # Check existence of children
        l1 = t1[u1][1]
        r1 = t1[u1][2]
        l2 = t2[u2][1]
        r2 = t2[u2][2]
        
        # Structure check: if one has child and other doesn't -> False
        if (l1 != -1) != (l2 != -1): return False
        if (r1 != -1) != (r2 != -1): return False
        
        return check(l1, l2) and check(r1, r2)
        
    return check(0, 0)

def matching_traversals(t1, t2):
    matches = []
    if t1[0] == t2[0]: matches.append("preorder")
    if t1[1] == t2[1]: matches.append("inorder")
    if t1[2] == t2[2]: matches.append("postorder")
    return matches

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    
    if idx < len(data):
        n1 = int(data[idx]); idx += 1
        t1 = []
        for _ in range(n1):
            v = int(data[idx]); l = int(data[idx + 1]); r = int(data[idx + 2])
            t1.append((v, l, r))
            idx += 3
    else:
        n1 = 0
        t1 = []

    if idx < len(data):
        n2 = int(data[idx]); idx += 1
        t2 = []
        for _ in range(n2):
            v = int(data[idx]); l = int(data[idx + 1]); r = int(data[idx + 2])
            t2.append((v, l, r))
            idx += 3
    else:
        n2 = 0
        t2 = []

    trav1 = traverse_all(n1, t1)
    trav2 = traverse_all(n2, t2)
    same = structural_identical(n1, t1, n2, t2)
    matches = matching_traversals(trav1, trav2)

    out = []
    for i in range(3):
        out.append(" ".join(str(x) for x in trav1[i]))
    for i in range(3):
        out.append(" ".join(str(x) for x in trav2[i]))
    out.append("true" if same else "false")
    out.append("NONE" if not matches else " ".join(matches))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
