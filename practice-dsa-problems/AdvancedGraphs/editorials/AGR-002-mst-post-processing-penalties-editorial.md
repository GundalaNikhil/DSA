# Editorial: Minimum Spanning Tree with Post-Processing Penalties

## 1. Problem

Given a connected, undirected graph with `n` nodes and `m` edges, where each edge has:

- **Base weight** `w`: Used for selecting the MST
- **Penalty** `p`: Additional cost if the edge is selected

Build a minimum spanning tree using **only base weights** (standard Kruskal's algorithm), then calculate the final cost as:

```
Final Cost = (sum of base weights) + (sum of penalties)
```

If the graph is disconnected, output `-1`.

**Constraints:**

- 1 ≤ n ≤ 200,000
- 0 ≤ m ≤ 200,000
- 1 ≤ u, v ≤ n
- -10⁹ ≤ w, p ≤ 10⁹

---

## 2. Explanation with Real-World Analogy

### Real-World Analogy: Building a Road Network

Imagine you're a city planner connecting `n` cities with roads:

- **Base weight (w)**: Construction cost of the road
- **Penalty (p)**: Annual maintenance cost once built

**Your task:**

1. Choose roads to connect all cities (minimum spanning tree)
2. Selection is based ONLY on construction cost
3. Calculate total cost = construction + maintenance

**Example:**

```
Cities: A, B, C

Roads:
A-B: construction=$100, maintenance=$20/year
B-C: construction=$100, maintenance=$5/year
A-C: construction=$200, maintenance=$0/year

MST Selection (by construction cost):
- Choose A-B ($100) ✓
- Choose B-C ($100) ✓
- Skip A-C ($200) (would create cycle)

Total Cost: ($100+$20) + ($100+$5) = $225
```

**Key Insight**: You're forced to use construction cost for selection, but you pay both construction AND maintenance!

### Why This Problem Is Interesting

Unlike standard MST where we minimize total weight, here we have a **two-phase cost model**:

1. **Selection Phase**: Use only base weights
2. **Payment Phase**: Pay both base weights AND penalties

This models real scenarios where initial selection criteria differ from total cost.

---

## 3. Brute Force Approach

### Algorithm

```
1. Generate all possible spanning trees
2. For each spanning tree:
   a. Calculate total cost = sum(w + p) for all edges
   b. Track which tree was selected based on sum(w)
3. Return cost of the tree with minimum sum(w)
```

### Complexity

- **Time**: O(n^(n-2) × n)
  - Cayley's formula: n^(n-2) spanning trees
  - Each tree: O(n) to evaluate
- **Space**: O(n)

### Why It's Impractical

For n = 100, there are ~10^196 spanning trees - impossible to enumerate!

---

## 4. Key Observations

### Observation 1: MST Structure Is Fixed

The MST structure is determined ONLY by base weights. Penalties don't affect which edges are chosen, only the final cost.

### Observation 2: Kruskal's Algorithm Works

Standard Kruskal's algorithm finds the MST:

1. Sort edges by weight
2. Use DSU to avoid cycles
3. Select n-1 edges

### Observation 3: Tie-Breaking Matters

When multiple edges have the same base weight, we should prefer edges with lower penalties for a unique, deterministic answer.

### Observation 4: Disconnected Graph Detection

If we can't select n-1 edges, the graph is disconnected → return -1.

---

## 5. Visual Explanation

### Example Graph

```
    (1,10)
   A -------- B
   |         /|
(2,5)  (3,0)/|(4,10)
   |      /  |
   |  (2,0)  |
   C -------- D
```

Numbers: (weight, penalty)

### Step 1: Sort Edges by (weight, penalty)

```
Edge    Weight  Penalty  Cumulative
A-B     1       10       (select first)
C-D     2       0        (lower penalty wins)
B-C     2       0        (same as above)
B-C     3       0
B-D     4       10
```

### Step 2: Apply Kruskal's

```
DSU state: {A}, {B}, {C}, {D}

Process A-B (w=1, p=10):
  union(A, B) ✓
  DSU: {A-B}, {C}, {D}
  Cost so far: 1 + 10 = 11

Process C-D (w=2, p=0):
  union(C, D) ✓
  DSU: {A-B}, {C-D}
  Cost so far: 11 + 2 + 0 = 13

Process B-C (w=2, p=0):
  union(A-B, C-D) ✓
  DSU: {A-B-C-D}
  Cost so far: 13 + 2 + 0 = 15

Selected 3 edges = n-1 ✓ DONE
```

### Final MST

```
    (1,10)
   A -------- B
              /
         (2,0)/
            /
          C -------- D
              (2,0)
```

**Total Cost**: 15

---

## 6. Dry Run

### Input

```
n = 4, m = 5
Edges:
(1, 2, w=1, p=10)
(2, 3, w=2, p=0)
(3, 4, w=1, p=1)
(1, 4, w=3, p=0)
(2, 4, w=4, p=10)
```

### Step 1: Sort by (w, p)

```
(1,2): w=1, p=10
(3,4): w=1, p=1   (lower penalty, comes first in tie-breaking)
(2,3): w=2, p=0
(1,4): w=3, p=0
(2,4): w=4, p=10
```

After sorting:

```
1. (3,4): w=1, p=1
2. (1,2): w=1, p=10
3. (2,3): w=2, p=0
4. (1,4): w=3, p=0
5. (2,4): w=4, p=10
```

### Step 2: Kruskal's Algorithm

```
DSU: {1}, {2}, {3}, {4}
Edges used: 0, Total cost: 0

Process (3,4):
  find(3) = 3, find(4) = 4 → Different
  union(3, 4) ✓
  Edges used: 1, Total cost: 1 + 1 = 2
  DSU: {1}, {2}, {3-4}

Process (1,2):
  find(1) = 1, find(2) = 2 → Different
  union(1, 2) ✓
  Edges used: 2, Total cost: 2 + 1 + 10 = 13
  DSU: {1-2}, {3-4}

Process (2,3):
  find(2) = 1, find(3) = 3 → Different
  union(1, 3) ✓
  Edges used: 3, Total cost: 13 + 2 + 0 = 15
  DSU: {1-2-3-4}

Edges used = 3 = n-1 ✓ MST complete!
```

**Output**: 15

---

## 7. Optimal Algorithm

### Algorithm Steps

1. **Sort edges** by (base_weight, penalty) - O(m log m)
2. **Initialize DSU** with n nodes - O(n)
3. **Apply Kruskal's**:
   ```
   for each edge (u, v, w, p) in sorted order:
       if union(u, v) succeeds:
           total_cost += w + p
           edges_used += 1
           if edges_used == n-1:
               break  (early termination)
   ```
4. **Check completeness**:
   ```
   if edges_used == n-1:
       return total_cost
   else:
       return -1  (disconnected)
   ```

### Why It Works

**Correctness**: Kruskal's algorithm guarantees the MST based on weights. The penalties are just additive costs that don't affect edge selection.

**Optimality**: Among all spanning trees, we select the one with minimum sum of base weights, which is the MST.

---

## 8. Pseudocode

```
class DSU:
    function __init__(n):
        parent = [0, 1, 2, ..., n]
        rank = [0, 0, 0, ..., 0]

    function find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])  // Path compression
        return parent[i]

    function union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i == root_j:
            return false

        // Union by rank
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            rank[root_i] += 1

        return true

function minSpanningTreeCostWithPenalties(n, m, edges):
    // Sort by (weight, penalty)
    sorted_edges = sort(edges, key = (e.weight, e.penalty))

    dsu = DSU(n)
    total_cost = 0
    edges_used = 0

    for each edge in sorted_edges:
        if dsu.union(edge.u, edge.v):
            total_cost += edge.weight + edge.penalty
            edges_used += 1

            if edges_used == n - 1:
                break  // MST complete

    if edges_used == n - 1:
        return total_cost
    else:
        return -1  // Disconnected graph
```

---

## 9. Code Implementation

```python
from typing import List

class Edge:
    def __init__(self, u: int, v: int, w: int, p: int):
        self.u = u
        self.v = v
        self.w = w
        self.p = p

class DSU:
    """Disjoint Set Union (Union-Find)"""

    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i):
        """Find with path compression"""
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """Union by rank"""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1

        return True

class Solution:
    def minSpanningTreeCostWithPenalties(self, n: int, m: int, edges: List[Edge]) -> int:
        """
        Find MST using base weights, return total cost including penalties.

        Args:
            n: Number of nodes
            m: Number of edges
            edges: List of Edge objects

        Returns:
            Total cost (base + penalties) or -1 if disconnected
        """
        # Sort by (weight, penalty) for tie-breaking
        sorted_edges = sorted(edges, key=lambda e: (e.w, e.p))

        dsu = DSU(n)
        total_cost = 0
        edges_used = 0

        for edge in sorted_edges:
            if dsu.union(edge.u, edge.v):
                # Edge added to MST
                total_cost += edge.w + edge.p
                edges_used += 1

                # Early termination
                if edges_used == n - 1:
                    break

        # Check if we have a spanning tree
        return total_cost if edges_used == n - 1 else -1
```

---

## 10. Complexity Analysis

### Time Complexity: **O(m log m + m α(n))**

**Breakdown:**

1. **Sorting edges**: O(m log m)
2. **Initialize DSU**: O(n)
3. **Kruskal's algorithm**:
   - Process at most m edges
   - Each union/find: O(α(n)) amortized (inverse Ackermann)
   - **O(m α(n))**

**Overall**: O(m log m) dominates

### Space Complexity: **O(n + m)**

- DSU arrays: O(n)
- Sorted edges: O(m)
- **Total**: O(n + m)

### Practical Performance

- For n, m ≤ 200,000: ~2-3 million operations
- Very fast in practice (< 1 second)

---

## 11. Edge Cases

### Case 1: Disconnected Graph

```
n = 3, m = 1
Edge: (1, 2, 10, 5)

Only 1 edge selected, need 2 for spanning tree
→ Return -1
```

### Case 2: Minimum Graph (Tree)

```
n = 3, m = 2
Edges: (1, 2, 5, 5), (2, 3, 5, 5)

Already a tree, select both
→ Return 20
```

### Case 3: Complete Graph

```
n = 3, m = 3 (triangle)
All edges might have same weight

Tie-breaking by penalty ensures deterministic result
```

### Case 4: Single Node

```
n = 1, m = 0

No edges needed for spanning tree
→ Return 0
```

### Case 5: Negative Weights/Penalties

```
Edge: (1, 2, -10, -5)

Total cost: -10 + (-5) = -15 ✓
Algorithm still works!
```

### Case 6: All Edges Same Weight

```
n = 5, m = 10
All edges: weight = 10

Sort by penalty: prefer edges with lower penalties
```

---

## 12. Common Pitfalls

### Pitfall 1: Sorting by Total Cost

❌ **Wrong**:

```python
sorted_edges = sorted(edges, key=lambda e: e.w + e.p)
```

This gives wrong MST! Must sort by weight only (with penalty tie-breaking).

✓ **Correct**:

```python
sorted_edges = sorted(edges, key=lambda e: (e.w, e.p))
```

### Pitfall 2: Forgetting Disconnected Case

❌ **Wrong**:

```python
return total_cost  # Always return cost
```

✓ **Correct**:

```python
return total_cost if edges_used == n - 1 else -1
```

### Pitfall 3: Off-by-One in Edge Count

```python
# Spanning tree has exactly n-1 edges, not n!
if edges_used == n - 1:  # Correct
    return total_cost
```

### Pitfall 4: Not Handling Empty Graph

```python
# If n = 0 or m = 0, handle specially
if n == 0 or n == 1:
    return 0
```

### Pitfall 5: Integer Overflow

For large weights/penalties, use:

```python
total_cost = 0  # Python handles big integers automatically

# In other languages:
long long total_cost = 0;  // C++
```

---

## 13. Alternative Approaches

### Approach 1: Prim's Algorithm

```python
# Instead of Kruskal's, use Prim's MST
# Same result, different algorithm
```

- **Pros**: Better for dense graphs
- **Cons**: Harder to implement with penalty tie-breaking
- **Complexity**: O(m log n) with priority queue

### Approach 2: Borůvka's Algorithm

```python
# Parallel-friendly MST algorithm
```

- **Pros**: Can be parallelized
- **Cons**: More complex, same complexity
- **Use When**: Implementing in parallel/distributed systems

### Approach 3: Dynamic Programming (Wrong Approach!)

```python
# Some might think: "Find minimum cost subset"
# This doesn't work! Must be MST by weight.
```

❌ This violates the problem constraint!

---

## 14. Interview Follow-Ups

### Q1: What if we could choose which edges to use freely?

**A**: Then it becomes a different problem - selecting minimum cost subset that spans the tree. Use DP or brute force on subset selection.

### Q2: What if penalties could be negative (rewards)?

**A**: Algorithm still works! Sort by (w, p) and sum normally. Negative penalties just reduce total cost.

### Q3: How would you handle maximum spanning tree?

**A**: Negate all weights, run Kruskal's, negate result. Or modify comparator in sorting.

### Q4: Can you support edge deletions?

**A**: Need dynamic MST algorithms (Link-Cut Trees). Static Kruskal's won't work.

### Q5: What if there are k types of penalties?

**A**: Sort by (w, p1, p2, ..., pk) and sum all penalties in the final cost calculation.

---

## 15. Pattern Recognition

### When to Use This Pattern

✓ **MST with additional costs** that don't affect selection
✓ **Two-phase optimization** (selection + payment)
✓ **Constrained optimization** where selection criterion differs from cost
✓ **Greedy + Union-Find** problems

### Related Problems

1. **Standard MST** (Kruskal's/Prim's)
2. **Second-best MST** (Find MST with second minimum weight)
3. **Degree-constrained MST** (MST where nodes have max degree)
4. **Capacitated MST** (MST with capacity constraints)
5. **Steiner Tree** (Connect subset of nodes with minimum cost)

### Key Techniques

- **Greedy Selection**: Sort and process in order
- **Union-Find (DSU)**: Efficiently detect cycles
- **Tie-Breaking**: Use secondary criteria for deterministic results
- **Early Termination**: Stop when spanning tree is complete

### Applications

- **Network Design**: Cost + maintenance optimization
- **Supply Chain**: Setup cost + operational cost
- **Infrastructure**: Construction + upkeep
- **Resource Allocation**: Selection cost + usage cost
