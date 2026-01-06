import sys
from collections import defaultdict

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_count = int(input_data[ptr])
    ptr += 1
    thresholds = []
    for _ in range(s_count):
        thresholds.append(int(input_data[ptr]))
        ptr += 1
        node_values = [0] * (n + 1)
        adj = defaultdict(list)
        root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_values[i] = v
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    passed_stage = [0] * (n + 1)
    
    # Pre-calculate Post Order for bottom-up processing
    post_order = []
    if root != -1:
        stack = [root]
        visited = {root}
        # Actually proper post order needs specific traversal
        # Iterative post-order: 2 stacks
        s1 = [root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            for child in adj[node]:
                s1.append(child)
        post_order = s2[::-1] # Reverse of s2 is topological sort / BFS-ish? No, s2 pop order is reversed pre-order (root, right, left -> left, right, root).
        # Actually s2 contains nodes in Reverse Post Order. Wait.
        # Root is last in s2. Children before parents.
        # Yes, processing s2 from end (root) is wrong for bottom-up.
        # Processing s2 from start (children) is correct for bottom-up.
        # But wait, s2 structure:
        # Push Root. Pop Root -> S2. Push children.
        # S2: [Root]
        # Pop Child1 -> S2. Push Grandchildren.
        # S2: [Root, Child1]
        # So S2 has Root at bottom (index 0). Top has leaves.
        # Reading S2 from popping (Right to Left) gives Root last. Correct.
        # So iterating s2 reversed (or popping) gives correct bottom-up order?
        # Actually, let's use standard recursive post-order generator if simple; or iterative correct one.
        # Or simple: Recursion depth is limited, we can use recursion for post-order given n is reasonable or setrecursionlimit.
        pass
        
    def get_post_order(u, lst):
        for v in adj[u]:
            get_post_order(v, lst)
        lst.append(u)
        
    post_order = []
    if root != -1:
        get_post_order(root, post_order)
        
    for s in range(s_count):
        current_threshold = thresholds[s]
        stage_vals = [0] * (n + 1)
        
        # Bottom-up calculation
        for u in post_order:
            if passed_stage[u] == s:
                val = node_values[u]
                for v in adj[u]:
                    # If child passed this stage (is at s+1 or higher), contribute its value?
                    # "passed_stage[v] > s" implies child is valid for current stage aggregation
                    if passed_stage[v] > s:
                        val += stage_vals[v]
                        
                stage_vals[u] = val
                
                if val >= current_threshold:
                    passed_stage[u] = s + 1
                    
        # If root didn't pass this stage, subsequent stages impossible?
        if root != -1 and passed_stage[root] < s + 1:
            break
            
    print(passed_stage[root] if root != -1 else 0)


if __name__ == "__main__":
    solve()
