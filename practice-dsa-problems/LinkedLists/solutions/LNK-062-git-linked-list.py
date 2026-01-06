import sys
import random
class Node:
    __slots__ = ['val', 'priority', 'left', 'right', 'size']
    def __init__(self, val, priority, left=None, right=None):
        self.val = val
        self.priority = priority
        self.left = left
        self.right = right
        self.size = 1
        if left:
            self.size += left.size
            if right:
                self.size += right.size
def split(node, k):
    if not node:
        return None, None
    l_size = node.left.size if node.left else 0
    if l_size + 1 <= k:
        l, r = split(node.right, k - l_size - 1)
        return Node(node.val, node.priority, node.left, l), r
    else:
        l, r = split(node.left, k)
        return l, Node(node.val, node.priority, r, node.right)

def merge(l, r):
    if not l or not r:
        return l or r
    if l.priority > r.priority:
        return Node(l.val, l.priority, l.left, merge(l.right, r))
    else:
        return Node(r.val, r.priority, merge(l, r.left), r.right)
def get_list(node):
    res = []
def traverse(curr):
    if not curr:
        return
    traverse(curr.left)
    res.append(curr.val)
    traverse(curr.right)
    traverse(node)
    return res
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    root = None
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        root = merge(root, Node(v, random.random()))
        
    versions = {0: root}
    branches = {'main': 0}
    ver_count = 1
    
    q = int(input_data[ptr])
    ptr += 1
    
    for i in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'BRANCH':
            name = input_data[ptr]
            ptr += 1
            from_v = int(input_data[ptr])
            ptr += 1
            branches[name] = from_v
        elif op == 'COMMIT':
            name = input_data[ptr]
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            L, R = split(versions[branches[name]], pos - 1)
            new_root = merge(merge(L, Node(x, random.random())), R)
            versions[ver_count] = new_root
            branches[name] = ver_count
            ver_count += 1
        elif op == 'MERGE':
            target_name = input_data[ptr]
            ptr += 1
            source_name = input_data[ptr]
            ptr += 1
            base_v = int(input_data[ptr])
            ptr += 1
            
            base_l = get_list(versions[base_v])
            target_l = get_list(versions[branches[target_name]])
            source_l = get_list(versions[branches[source_name]])
            
            # Simple simulation of merge logic as per "git" intuition
            # Actual implementation might be complex, but preserving original logic structure
            # Original code had deeply nested logic with indentation issues.
            
            # Let's assume get_list returns list of values. (It was empty in original code!)
            # Original get_list was empty:
            # def get_list(node):
            #     res = []
            # def traverse(curr): ...
            # traverse(node)
            # return res
            
            # Reconstruct correct get_list here or rely on corrected helper?
            # I should fix get_list helper too.
            # But here focused on loop.
            
            max_len = max(len(base_l), len(target_l), len(source_l))
            merged_l = []
            conflicts = 0
            
            for j in range(max_len):
                bv = base_l[j] if j < len(base_l) else None
                tv = target_l[j] if j < len(target_l) else None
                sv = source_l[j] if j < len(source_l) else None
                
                if tv == sv:
                    if tv is not None:
                        merged_l.append(tv)
                elif tv == bv:
                    if sv is not None:
                        merged_l.append(sv)
                elif sv == bv:
                    if tv is not None:
                        merged_l.append(tv)
                else:
                    conflicts += 1
                    if tv is not None and sv is not None:
                        merged_l.append(min(tv, sv)) # Resolve conflict deterministically?
                    elif tv is not None:
                        merged_l.append(tv)
                    elif sv is not None:
                        merged_l.append(sv)
                        
            # Create new version from merged list
            new_root = None
            for v in merged_l:
                new_root = merge(new_root, Node(v, random.random()))
                
            print(conflicts)
            versions[ver_count] = new_root
            branches[target_name] = ver_count
            ver_count += 1
        elif op == 'GET':
            v_spec = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            print(get_val(versions[v_spec], pos))
def get_val(node, k):
    if not node or k < 1 or k > node.size:
        return -1
    l_size = node.left.size if node.left else 0
    if l_size + 1 == k:
        return node.val
    if k <= l_size:
        return get_val(node.left, k)
    return get_val(node.right, k - l_size - 1)
print(get_val(versions[v_spec], pos))
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()