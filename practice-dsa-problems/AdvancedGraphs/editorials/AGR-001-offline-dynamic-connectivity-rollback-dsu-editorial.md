# Editorial: Offline Dynamic Connectivity with Rollback DSU

## 1. Problem

Given an undirected graph with `n` nodes and a sequence of `q` operations that modify the graph over time, answer connectivity queries efficiently. Operations include:

- `ADD u v`: Add edge (u, v) to the graph
- `REM u v`: Remove edge (u, v) from the graph
- `ASK u v`: Check if nodes u and v are connected in the current graph state

You must process all operations in order and output "YES" or "NO" for each ASK query.

**Constraints:**

- 1 ≤ n, q ≤ 200,000
- Edges are uniquely identified and won't be added twice without removal
- All REM operations refer to currently active edges

---

## 2. Explanation with Real-World Analogy

### Real-World Analogy: Social Network Groups

Imagine you're managing a social network where people can join and leave groups over time:

- **ADD operation**: Two people become friends
- **REM operation**: Two people stop being friends
- **ASK operation**: Check if two people are connected through mutual friends

**Example scenario:**

```
Day 1: Alice ←→ Bob (they become friends)
Day 2: Bob ←→ Carol (Bob and Carol become friends)
Day 3: ASK: Are Alice and Carol connected? → YES (through Bob)
Day 4: Bob and Carol end their friendship
Day 5: ASK: Are Alice and Carol connected? → NO (link broken)
```

The challenge is that we want to answer ALL queries AFTER seeing all operations (offline), which lets us use smarter algorithms than processing them one-by-one (online).

### Why This Problem is Hard

The naive approach of maintaining the graph and running BFS/DFS for each query is too slow (O(q²) time). We need a data structure that:

1. Supports union operations (adding edges)
2. Supports **undo** operations (removing edges)
3. Answers connectivity queries quickly

---

## 3. Brute Force Approach

### Algorithm

```
1. Maintain an adjacency list representation of the graph
2. For each operation:
   - If ADD: Add edge to adjacency list
   - If REM: Remove edge from adjacency list
   - If ASK: Run BFS/DFS to check if nodes are connected
```

### Complexity

- **Time**: O(q × (n + m)) where m is the number of edges
  - Each BFS/DFS: O(n + m)
  - q operations total
- **Space**: O(n + m)

### Why It's Too Slow

For q = 200,000 and n = 200,000, this gives ~40 billion operations - far too slow!

---

## 4. Key Observations

### Observation 1: Offline Nature

We can read ALL operations before answering ANY query. This lets us:

- Know the entire "lifespan" of each edge
- Process queries in a clever order

### Observation 2: Edge Lifespans

Each edge exists during a specific time interval `[start, end]`:

```
Time:     0   1   2   3   4   5   6
Edge(1,2): [===ADD=======REM===]
Edge(2,3):     [===ADD=============]
```

### Observation 3: Segment Tree Over Time

We can build a **segment tree** where:

- Each leaf represents one operation (time point)
- Each edge is assigned to O(log q) nodes covering its lifespan
- We traverse the tree with a DSU that can **rollback**

### Observation 4: Rollback DSU

Standard DSU with path compression can't undo operations easily. But if we:

- Skip path compression
- Track changes in a stack
- We can rollback to any previous state!

---

## 5. Visual Explanation

### Step 1: Build Edge Intervals

```
Operations: ADD(1,2), ADD(2,3), ASK(1,3), REM(2,3), ASK(1,3)
Time:       0         1         2         3         4

Edge (1,2): [0, ∞)  (never removed)
Edge (2,3): [1, 2]  (added at 1, removed before 3)
```

### Step 2: Build Segment Tree Over Time

```
Time Points: [0, 1, 2, 3, 4]

Segment Tree:
                 [0,4]
                /      \
           [0,2]        [3,4]
          /    \        /    \
      [0,1]  [2,2]  [3,3]  [4,4]
```

### Step 3: Assign Edges to Tree Nodes

Edge (1,2) spans [0,4] → assign to root  
Edge (2,3) spans [1,2] → assign to nodes [1,1] and [2,2]

### Step 4: DFS Traversal with Rollback

```
DFS(node, l, r):
  1. Remember current DSU state
  2. Add all edges assigned to this node
  3. If leaf: answer query at this time
  4. Else: recurse to children
  5. Rollback DSU to remembered state
```

---

## 6. Dry Run

### Input

```
n=4, q=5
Operations:
0: ADD 1 2
1: ADD 2 3
2: ASK 1 3
3: REM 2 3
4: ASK 1 3
```

### Step 1: Edge Intervals

- Edge (1,2): [0, 4]
- Edge (2,3): [1, 2]

### Step 2: Build Segment Tree

```
        [0,4]
       /      \
    [0,2]    [3,4]
   /    \    /    \
 [0,1] [2] [3]   [4]
```

### Step 3: Assign Edges

- Edge (1,2) → node [0,4]
- Edge (2,3) → nodes [1,1] and [2,2]

### Step 4: DFS Traversal

```
Traverse([0,4]):
  Add edge (1,2), DSU: {1-2, 3, 4}

  Traverse([0,2]):
    Traverse([0,1]):
      Add edge (2,3), DSU: {1-2-3, 4}
      Process time 0: (no query)
      Process time 1: (no query)
      Rollback: DSU: {1-2, 3, 4}

    Traverse([2,2]):
      Add edge (2,3), DSU: {1-2-3, 4}
      Process time 2: ASK(1,3) → find(1)==find(3)? YES ✓
      Rollback: DSU: {1-2, 3, 4}

  Traverse([3,4]):
    Process time 3: (no query)
    Process time 4: ASK(1,3) → find(1)==find(3)? NO ✓

  Rollback: DSU: {1, 2, 3, 4}
```

**Output**: `["YES", "NO"]`

---

## 7. Optimal Algorithm

### High-Level Steps

1. **Parse Operations**: Separate ADDs, REMs, and ASKs
2. **Build Edge Lifespans**: Track when each edge exists
3. **Build Segment Tree**: Create tree over time points [0, q-1]
4. **Assign Edges**: For each edge's lifespan, assign to O(log q) tree nodes
5. **Initialize Rollback DSU**: DSU without path compression + history stack
6. **DFS Traversal**:
   - At each node: apply edges, recurse, rollback
   - At each leaf: answer query if present
7. **Return Answers**: Collect all ASK query results

### Rollback DSU Implementation

**Key Differences from Standard DSU:**

- **No path compression** in find() - just follow parent pointers
- **Track history** of all parent/size changes
- **Rollback function** to undo changes

---

## 8. Pseudocode

```
class RollbackDSU:
    function __init__(n):
        parent = [0, 1, 2, ..., n]
        size = [1, 1, 1, ..., 1]
        history = []

    function find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    function union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i == root_j:
            return false

        // Union by size
        if size[root_i] < size[root_j]:
            swap(root_i, root_j)

        // Record change
        history.append((root_j, root_i))
        parent[root_j] = root_i
        size[root_i] += size[root_j]
        return true

    function rollback(target_len):
        while len(history) > target_len:
            (child, parent_node) = history.pop()
            size[parent_node] -= size[child]
            parent[child] = child

function solveDynamicConnectivity(n, q, ops):
    // 1. Build edge intervals
    edge_intervals = {}
    edge_spans = []

    for t = 0 to q-1:
        op = ops[t]
        edge = (min(op.u, op.v), max(op.u, op.v))

        if op.type == "ADD":
            edge_intervals[edge] = t
        elif op.type == "REM":
            start = edge_intervals.remove(edge)
           edge_spans.append((start, t-1, edge.u, edge.v))

    // Edges active till end
    for (edge, start) in edge_intervals:
        edge_spans.append((start, q-1, edge.u, edge.v))

    // 2. Build segment tree
    tree_edges = array of lists, size 4*q

    function add_to_tree(node, l, r, ql, qr, edge):
        if ql <= l and r <= qr:
            tree_edges[node].append(edge)
            return

        mid = (l + r) / 2
        if ql <= mid:
            add_to_tree(2*node, l, mid, ql, qr, edge)
        if qr > mid:
            add_to_tree(2*node+1, mid+1, r, ql, qr, edge)

    for (start, end, u, v) in edge_spans:
        add_to_tree(1, 0, q-1, start, end, (u, v))

    // 3. DFS with rollback
    dsu = RollbackDSU(n)
    ans = array of size q, initialized to null

    function traverse(node, l, r):
        prev_len = len(dsu.history)

        // Add all edges for this node
        for (u, v) in tree_edges[node]:
            dsu.union(u, v)

        if l == r:
            // Leaf: process query
            if ops[l].type == "ASK":
                u, v = ops[l].u, ops[l].v
                if dsu.find(u) == dsu.find(v):
                    ans[l] = "YES"
                else:
                    ans[l] = "NO"
        else:
            // Internal: recurse
            mid = (l + r) / 2
            traverse(2*node, l, mid)
            traverse(2*node+1, mid+1, r)

        // Rollback
        dsu.rollback(prev_len)

    traverse(1, 0, q-1)

    // 4. Return only ASK answers
    return [a for a in ans if a != null]
```

---

## 9. Code Implementation

```python
from typing import List

class GraphOp:
    def __init__(self, type: str, u: int, v: int):
        self.type = type
        self.u = u
        self.v = v

class RollbackDSU:
    """Union-Find with rollback capability"""

    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.history = []

    def find(self, i):
        """Find without path compression"""
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, i, j):
        """Union by size with history tracking"""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        # Attach smaller to larger
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i

        # Record change
        self.history.append((root_j, root_i))
        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        return True

    def rollback(self, target_len):
        """Rollback to previous state"""
        while len(self.history) > target_len:
            child, parent = self.history.pop()
            self.size[parent] -= self.size[child]
            self.parent[child] = child

class Solution:
    def solveDynamicConnectivity(self, n: int, q: int, ops: List[GraphOp]) -> List[str]:
        # Build edge intervals
        edge_intervals = {}
        edge_spans = []

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

        # Edges active till end
        for edge, start in edge_intervals.items():
            u, v = edge
            edge_spans.append((start, q - 1, u, v))

        # Build segment tree
        tree_edges = [[] for _ in range(4 * q)]

        def add_to_tree(node, l, r, ql, qr, edge):
            if qr < l or ql > r:
                return
            if ql <= l and r <= qr:
                tree_edges[node].append(edge)
                return

            mid = (l + r) // 2
            add_to_tree(2 * node, l, mid, ql, qr, edge)
            add_to_tree(2 * node + 1, mid + 1, r, ql, qr, edge)

        for start, end, u, v in edge_spans:
            add_to_tree(1, 0, q - 1, start, end, (u, v))

        # DFS with rollback
        dsu = RollbackDSU(n)
        ans = [None] * q

        def traverse(node, l, r):
            prev_len = len(dsu.history)

            for u, v in tree_edges[node]:
                dsu.union(u, v)

            if l == r:
                if ops[l].type == "ASK":
                    u, v = ops[l].u, ops[l].v
                    ans[l] = "YES" if dsu.find(u) == dsu.find(v) else "NO"
            else:
                mid = (l + r) // 2
                traverse(2 * node, l, mid)
                traverse(2 * node + 1, mid + 1, r)

            dsu.rollback(prev_len)

        if q > 0:
            traverse(1, 0, q - 1)

        return [a for a in ans if a is not None]
```

---

## 10. Complexity Analysis

### Time Complexity: **O(q log² q)**

**Breakdown:**

1. **Building edge intervals**: O(q)
2. **Building segment tree**:
   - Each edge assigned to O(log q) nodes
   - q edges total
   - **O(q log q)**
3. **DFS traversal**:
   - Visit O(q) tree nodes
   - Each node processes O(log q) edges on average
   - Each union/find: O(log n) without path compression
   - **O(q log q × log n) ≈ O(q log² q)** when n ≈ q

### Space Complexity: **O(q log q)**

- Segment tree: O(q) nodes
- Edges stored across tree: O(q log q) total
- DSU: O(n)
- History stack: O(log q) depth
- **Total: O(q log q)**

---

## 11. Edge Cases

### Case 1: Self-Loops

```
ASK 1 1 → Always "YES" (node connected to itself)
```

### Case 2: Disconnected Components

```
ADD 1 2
ADD 3 4
ASK 1 3 → "NO"
```

### Case 3: No Operations

```
q = 0 → return []
```

### Case 4: Only Queries, No Edges

```
ASK 1 2 → "NO"
ASK 3 3 → "YES"
```

### Case 5: Edge Added and Removed Multiple Times

```
ADD 1 2
REM 1 2
ADD 1 2  ✓ Valid
```

### Case 6: Complex Cycle

```
ADD 1 2
ADD 2 3
ADD 3 4
ADD 4 1  (creates cycle)
REM 1 2  (breaks cycle but still connected)
ASK 1 2 → "YES" (via 1→4→3→2)
```

---

## 12. Common Pitfalls

### Pitfall 1: Using Path Compression

❌ **Wrong**: Standard DSU with path compression can't rollback easily
✓ **Correct**: Skip path compression, use union by size only

### Pitfall 2: Forgetting to Normalize Edges

```python
# Edge (2,1) and (1,2) are the same!
if u > v:
    u, v = v, u  # Always store as (smaller, larger)
```

### Pitfall 3: Incorrect Segment Tree Assignment

❌ **Wrong**: Assigning edge to all nodes in range
✓ **Correct**: Assign to O(log q) nodes that exactly cover the range

### Pitfall 4: Not Handling Edges Active Till End

```python
# After processing all REMs, some edges are still active
for edge, start in edge_intervals.items():
    edge_spans.append((start, q - 1, edge[0], edge[1]))
```

### Pitfall 5: Rollback After Leaf Processing

```python
# Must rollback even at leaf nodes!
def traverse(node, l, r):
    prev_len = len(dsu.history)
    # ... process ...
    dsu.rollback(prev_len)  # Essential!
```

---

## 13. Alternative Approaches

### Approach 1: Link-Cut Trees

- **Idea**: Dynamic tree data structure supporting link/cut/query
- **Pros**: Truly online, handles insertions and deletions
- **Cons**: Complex implementation, O(log n) per operation
- **When to use**: When operations must be processed online

### Approach 2: Sqrt Decomposition

- **Idea**: Divide time into √q blocks, rebuild DSU at each block
- **Complexity**: O(q√q)
- **Pros**: Simpler than segment tree
- **Cons**: Slower asymptotic complexity

### Approach 3: Persistent DSU

- **Idea**: Create persistent version of DSU, store snapshot at each time
- **Complexity**: O(q log q) time, O(q² ) space
- **Cons**: Excessive space usage

---

## 14. Interview Follow-Ups

### Q1: What if we need to support weights on edges?

**A**: Add weight tracking to DSU. For MST queries, use persistent Kruskal's.

### Q2: Can this be adapted for directed graphs?

**A**: Yes, but connectivity becomes more complex (strongly connected components). Would need different approach.

### Q3: What if ADD can add an already-existing edge?

**A**: Track edge count instead of binary existence. Remove when count reaches 0.

### Q4: How would you make this fully online?

**A**: Use Link-Cut Trees or Euler Tour Trees for O(log n) per operation.

### Q5: Can you support counting connected components?

**A**: Yes! Track component count in DSU, update on union/rollback.

---

## 15. Pattern Recognition

### When to Use This Pattern

✓ **Offline queries** on dynamic graphs
✓ **Temporal edge existence** (edges have lifespans)
✓ **Undo requirements** (need to revert state)
✓ **Multiple queries** about historical states

### Related Techniques

1. **Offline Query Processing**: Process all queries together for optimization
2. **Segment Tree**: Divide time/space into logarithmic ranges
3. **Rollback/Undo Stacks**: Maintain history of changes
4. **Union-Find**: Efficiently track connected components

### Similar Problems

- **Range Queries with Updates**: Segment tree with lazy propagation
- **Temporal Databases**: Querying data at different timestamps
- **Version Control**: Maintaining history with rollback capability
- **Undo/Redo Systems**: Stack-based state management

This pattern appears in:

- Competitive programming (Codeforces, ICPC)
- Database temporal queries
- Version control systems
- Network topology analysis
