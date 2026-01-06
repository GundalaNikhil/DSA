from typing import List


class GraphOp:
    def __init__(self, type: str, u: int, v: int):
        self.type = type
        self.u = u
        self.v = v


class RollbackDSU:
    """Union-Find with rollback capability using stack-based history"""
    
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.history = []
    
    def find(self, i):
        """Find root without path compression (needed for rollback)"""
        while self.parent[i] != i:
            i = self.parent[i]
        return i
    
    def union(self, i, j):
        """Union by size with history tracking"""
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False
        
        # Always attach smaller tree to larger tree
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i
        
        # Record the change for rollback
        self.history.append((root_j, root_i))
        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        return True
    
    def rollback(self, target_len):
        """Rollback to a previous state"""
        while len(self.history) > target_len:
            child, parent = self.history.pop()
            self.size[parent] -= self.size[child]
            self.parent[child] = child


class Solution:
    def solveDynamicConnectivity(self, n: int, q: int, ops: List[GraphOp]) -> List[str]:
        """
        Solve offline dynamic connectivity using segment tree over time with rollback DSU.
        
        Algorithm:
        1. Build edge intervals: track when each edge exists
        2. Build segment tree over time and assign edges to nodes
        3. DFS through segment tree, maintaining DSU state with rollback
        4. Answer queries at leaf nodes
        """
        # Build edge intervals
        edge_intervals = {}  # (u, v) -> start_time
        edge_spans = []  # (start, end, u, v)
        
        for t, op in enumerate(ops):
            u, v = op.u, op.v
            if u > v:
                u, v = v, u
            edge = (u, v)
            
            if op.type == "ADD":
                edge_intervals[edge] = t
            elif op.type == "REM":
                start = edge_intervals.pop(edge)
                edge_spans.append((start, t - 1, u, v))
        
        # Edges that remain active till the end
        for edge, start in edge_intervals.items():
            u, v = edge
            edge_spans.append((start, q - 1, u, v))
        
        # Build segment tree
        tree_edges = [[] for _ in range(4 * q)]
        
        def add_to_tree(node, l, r, ql, qr, edge):
            """Add edge to segment tree nodes covering [ql, qr]"""
            if qr < l or ql > r:
                return
            if ql <= l and r <= qr:
                tree_edges[node].append(edge)
                return
            
            mid = (l + r) // 2
            add_to_tree(2 * node, l, mid, ql, qr, edge)
            add_to_tree(2 * node + 1, mid + 1, r, ql, qr, edge)
        
        # Add each edge span to the segment tree
        for start, end, u, v in edge_spans:
            add_to_tree(1, 0, q - 1, start, end, (u, v))
        
        # Initialize DSU and answer array
        dsu = RollbackDSU(n)
        ans = [None] * q
        
        def traverse(node, l, r):
            """DFS through segment tree, maintaining DSU state"""
            # Remember current history length for rollback
            prev_len = len(dsu.history)
            
            # Add all edges for this segment tree node
            for u, v in tree_edges[node]:
                dsu.union(u, v)
            
            if l == r:
                # Leaf node - process query at time l
                if ops[l].type == "ASK":
                    u, v = ops[l].u, ops[l].v
                    if dsu.find(u) == dsu.find(v):
                        ans[l] = "YES"
                    else:
                        ans[l] = "NO"
            else:
                # Internal node - recurse to children
                mid = (l + r) // 2
                traverse(2 * node, l, mid)
                traverse(2 * node + 1, mid + 1, r)
            
            # Rollback all unions made at this level
            dsu.rollback(prev_len)
        
        # Start DFS from root
        if q > 0:
            traverse(1, 0, q - 1)
        
        # Return only the answers to ASK queries
        return [a for a in ans if a is not None]
