# Editorial: Steiner Connection with Paid-Edge Budget

## 1. Problem

Given an undirected graph with `k` terminal nodes that MUST be connected, where each edge has:

- **Paid status** (0 or 1): Whether using this edge consumes 1 unit of budget
- **Activation cost** `a`: The cost paid if this edge is included in the solution

Find a connected subgraph that:

1. Connects all `k` terminals
2. Uses at most `B` paid edges
3. Minimizes the sum of activation costs

Return the minimum activation cost, or `-1` if impossible.

**Constraints:**

- 2 ≤ k ≤ 10 (small number of terminals)
- 2 ≤ n ≤ 5,000
- 1 ≤ m ≤ 10,000
- 0 ≤ B ≤ 30
- paid ∈ {0, 1}
- 0 ≤ a ≤ 10⁹

---

## 2. Explanation with Real-World Analogy

### Real-World Analogy: Building a Power Grid

You're connecting `k` critical power stations (terminals) across a city:

- **Free edges** (paid=0): Public roads (no toll)
- **Paid edges** (paid=1): Private toll roads (each costs 1 permit)
- **Activation cost**: Cost to build power lines along the road
- **Budget B**: Maximum number of toll road permits you can afford

**Example Scenario:**

```
Stations to connect: Hospital, School, Police Station
Budget: 1 toll permit
Roads:
- Hospital ↔ Market: Free, cost $100
- Market ↔ School: Free, cost $100
- School ↔ Police: Toll, cost $50
- Hospital ↔ Police: Toll, cost $200

Solution:
Use free roads Hospital→Market→School (cost $200)
Use toll road School→Police (cost $50)
Total: $250, using 1 toll permit ✓
```

### Why This Is a Steiner Tree Problem

Unlike standard MST where we connect ALL nodes, here we:

- **Must connect**: Only the k terminal nodes (not all n nodes)
- **Can use**: Other nodes as intermediates (**Steiner nodes**)
- **Constraint**: Limited budget for paid edges

This is significantly harder than MST!

---

## 3. Brute Force Approach

### Algorithm

```
1. Enumerate all possible subsets of edges
2. For each subset:
   a. Check if it connects all terminals
   b. Check if paid edges ≤ B
   c. Calculate total activation cost
3. Return minimum cost among valid subsets
```

### Complexity

- **Time**: O(2^m × (n + m))
  - 2^m possible subsets
  - Each: O(n + m) to check connectivity (BFS/DFS)
- **Space**: O(m)

### Why It's Impractical

- For m = 10,000: 2^10,000 ≈ infinity!
- Even for m = 30: 2^30 ≈ 1 billion subsets

---

## 4. Key Observations

### Observation 1: Small k Enables Bitmask DP

With k ≤ 10, we have at most 2^10 = 1,024 subsets of terminals. We can use **bitmask DP** to track which terminals are connected.

### Observation 2: Budget Constraint Is Small

B ≤ 30 means we can track budget usage as a DP dimension without explosion.

### Observation 3: Optimal Substructure

If we've connected subset S₁ and subset S₂ at some node, we can merge them to connect S₁ ∪ S₂.

### Observation 4: Shortest Paths Matter

To extend a connection from one terminal set to others, we need shortest paths (considering both cost and budget).

### Observation 5: Steiner Tree DP Pattern

```
dp[mask][node][budget] = minimum cost to connect terminals in 'mask'
                         with current tree ending at 'node'
                         using 'budget' paid edges
```

---

## 5. Visual Explanation

### Example Graph

```
Terminals: {1, 3, 5}
Budget: 1

    1 -----(F,2)------ 2 -----(F,2)------ 3
    |                                      |
 (P,1)|                                    |(F,2)
    |                                      |
    5 -----(F,2)------ 4 ------------------+

F = Free (paid=0)
P = Paid (paid=1)
Numbers = activation costs
```

### DP States Evolution

**Initialization:**

```
dp[001][1][0] = 0  (terminal 1 at node 1, free)
dp[010][3][0] = 0  (terminal 3 at node 3, free)
dp[100][5][0] = 0  (terminal 5 at node 5, free)
```

**Merge Example:**

```
Connect mask 001 (terminal 1) and mask 010 (terminal 3):

At node 1: dp[001][1][0] = 0
Extend to node 2: dp[001][2][0] = 0 + 2 = 2 (via edge 1-2)
Extend to node 3: dp[001][3][0] = 2 + 2 = 4 (via edges 1-2-3)

Now merge with dp[010][3][0] = 0:
dp[011][3][0] = dp[001][3][0] + dp[010][3][0] = 4 + 0 = 4
```

**Final State:**

```
dp[111][any node][budget ≤ 1] = minimum cost to connect all 3 terminals
```

---

## 6. Dry Run

### Input

```
n = 4, m = 5, k = 2, B = 1
Terminals: [1, 4]
Edges:
(1, 2, paid=0, cost=2)
(2, 3, paid=0, cost=2)
(3, 4, paid=0, cost=2)
(1, 4, paid=1, cost=1)  ← Toll road shortcut!
(2, 4, paid=1, cost=10)
```

### Visualization

```
    1 --(F,2)-- 2
    |          /|
(P,1)|    (F,2)/ |
    |        /  |(P,10)
    |      /    |
    4 -------- 3
       (F,2)
```

### DP Execution

**Step 1: Initialize single terminals**

```
dp[01][1][0] = 0  (terminal 1 at node 1)
dp[10][4][0] = 0  (terminal 4 at node 4)
```

**Step 2: Dijkstra for mask=01 (terminal 1)**

```
Start: dp[01][1][0] = 0

Relax edge (1,2) free:
  dp[01][2][0] = min(∞, 0+2) = 2

Relax edge (1,4) paid:
  dp[01][4][1] = min(∞, 0+1) = 1  ← Found cheaper path to node 4!

Relax edge (2,3) free from node 2:
  dp[01][3][0] = min(∞, 2+2) = 4

... (continue Dijkstra)
```

**Step 3: Merge masks at each node**

```
Mask 11 (both terminals):

At node 4:
  Merge dp[01][4][1] and dp[10][4][0]:
  dp[11][4][1] = 1 + 0 = 1  ✓ Best solution!

At node 1:
  Only dp[01][1][0] exists, can't merge solo

Alternative at node 3:
  Path 1→2→3 (cost 4) + path 4→3 (cost 2):
  dp[11][3][0] = 4 + 2 = 6  (worse, uses no paid edges)
```

**Step 4: Extract answer**

```
Answer = min over all nodes and budgets ≤ 1:
  = dp[11][4][1] = 1  ✓
```

**Output**: 1

---

## 7. Optimal Algorithm

### High-Level Strategy

Use **Bitmask DP + Shortest Path (Dijkstra)** in two phases:

**Phase 1: Merge submasks**

- For each mask, try combining smaller masks at each node
- dp[mask][node] = dp[sub1][node] + dp[sub2][node]

**Phase 2: Propagate via shortest paths**

- For each mask, run Dijkstra to find cheapest ways to reach other nodes
- Respect budget constraint when using paid edges

### Algorithm Steps

```
1. Initialize base cases: each terminal at its starting node
2. For each mask from 1 to 2^k - 1:
   a. Merge smaller masks at each node
   b. Run Dijkstra to propagate this mask to other nodes
3. Return min cost for final mask (all terminals) across all nodes/budgets
```

---

## 8. Pseudocode

```
function minSteinerActivationCost(n, m, k, B, terminals, edges):
    INF = infinity

    // Build adjacency list
    adj = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge.u - 1, edge.v - 1  // 0-indexed
        adj[u].append((v, edge.paid, edge.cost))
        adj[v].append((u, edge.paid, edge.cost))

    // DP table
    dp[mask][node][budget] = INF for all states

    // Base case: each terminal at its location
    terminals = [t-1 for t in terminals]  // 0-indexed
    for i in range(k):
        dp[1 << i][terminals[i]][0] = 0

    // Process each mask
    for mask in range(1, 1 << k):

        // Phase 1: Merge submasks
        submask = mask
        while submask > 0:
            complement = mask XOR submask
            if complement > 0 and submask >= complement:

                for node in range(n):
                    for b1 in range(B + 1):
                        if dp[submask][node][b1] == INF:
                            continue
                        for b2 in range(B - b1 + 1):
                            if dp[complement][node][b2] == INF:
                                continue

                            new_cost = dp[submask][node][b1] + dp[complement][node][b2]
                            dp[mask][node][b1 + b2] = min(dp[mask][node][b1 + b2], new_cost)

            submask = (submask - 1) AND mask

        // Phase 2: Dijkstra propagation
        pq = priority_queue  // (cost, node, budget)

        for node in range(n):
            for budget in range(B + 1):
                if dp[mask][node][budget] < INF:
                    pq.push((dp[mask][node][budget], node, budget))

        while pq not empty:
            (cost, u, used_budget) = pq.pop()

            if cost > dp[mask][u][used_budget]:
                continue

            for (v, paid, activation) in adj[u]:
                new_budget = used_budget + paid
                if new_budget <= B:
                    new_cost = cost + activation
                    if new_cost < dp[mask][v][new_budget]:
                        dp[mask][v][new_budget] = new_cost
                        pq.push((new_cost, v, new_budget))

    // Find answer
    final_mask = (1 << k) - 1
    answer = INF

    for node in range(n):
        for budget in range(B + 1):
            answer = min(answer, dp[final_mask][node][budget])

    return answer if answer < INF else -1
```

---

## 9. Code Implementation

```python
from typing import List
import heapq

class Edge:
    def __init__(self, u: int, v: int, paid: int, a: int):
        self.u = u
        self.v = v
        self.paid = paid
        self.a = a

class Solution:
    def minSteinerActivationCost(self, n: int, m: int, k: int, b: int,
                                  terminals: List[int], edges: List[Edge]) -> int:
        """
        Solve Steiner tree with budget-constrained paid edges.

        Uses bitmask DP + Dijkstra algorithm.
        """
        INF = float('inf')

        # Convert to 0-indexed
        terminals = [t - 1 for t in terminals]

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge.u - 1, edge.v - 1
            adj[u].append((v, edge.paid, edge.a))
            adj[v].append((u, edge.paid, edge.a))

        # DP: dp[mask][node][budget] = min cost
        dp = [[[INF] * (b + 1) for _ in range(n)] for _ in range(1 << k)]

        # Base case
        for i in range(k):
            dp[1 << i][terminals[i]][0] = 0

        # Process each mask
        for mask in range(1, 1 << k):
            # Phase 1: Merge submasks
            sub = mask
            while sub > 0:
                comp = mask ^ sub
                if comp > 0 and sub >= comp:
                    for node in range(n):
                        for b1 in range(b + 1):
                            if dp[sub][node][b1] >= INF:
                                continue
                            for b2 in range(b - b1 + 1):
                                if dp[comp][node][b2] >= INF:
                                    continue
                                total_b = b1 + b2
                                total_cost = dp[sub][node][b1] + dp[comp][node][b2]
                                dp[mask][node][total_b] = min(dp[mask][node][total_b], total_cost)

                sub = (sub - 1) & mask

            # Phase 2: Dijkstra
            pq = []
            for node in range(n):
                for budget in range(b + 1):
                    if dp[mask][node][budget] < INF:
                        heapq.heappush(pq, (dp[mask][node][budget], node, budget))

            while pq:
                cost, u, used_budget = heapq.heappop(pq)

                if cost > dp[mask][u][used_budget]:
                    continue

                for v, paid, activation in adj[u]:
                    new_budget = used_budget + paid
                    if new_budget <= b:
                        new_cost = cost + activation
                        if new_cost < dp[mask][v][new_budget]:
                            dp[mask][v][new_budget] = new_cost
                            heapq.heappush(pq, (new_cost, v, new_budget))

        # Extract answer
        final_mask = (1 << k) - 1
        ans = INF

        for node in range(n):
            for budget in range(b + 1):
                ans = min(ans, dp[final_mask][node][budget])

        return ans if ans < INF else -1
```

---

## 10. Complexity Analysis

### Time Complexity: **O(3^k × n × B + 2^k × m × B × log(n × B))**

**Breakdown:**

**Part 1: Merging submasks**

- For each mask (2^k total)
- Enumerate all submask partitions: O(3^k / 2^k) = O(3^k) per mask
- For each partition: O(n × B²) work
- **Total**: O(3^k × n × B²)

**Part 2: Dijkstra**

- For each mask (2^k total)
- Dijkstra with n × B states
- Each edge relaxation: O(log(n × B))
- **Total**: O(2^k × (n × B + m × B) × log(n × B))

**Dominant term**: O(3^k × n × B²) when k is small

**Practical values** (k=10, n=5000, B=30):

- 3^10 × 5000 × 900 ≈ 265 billion ops (feasible with optimizations)

### Space Complexity: **O(2^k × n × B)**

- DP table: 2^k × n × B states
- Adjacency list: O(m)
- Priority queue: O(n × B)
- **Total**: O(2^k × n × B)

---

## 11. Edge Cases

### Case 1: All Terminals Co-located

```
Terminals: [1, 1]  (same node)
→ Return 0 (already connected)
```

### Case 2: Impossible with Budget

```
Terminals: [1, 5]
Budget: 0
Only path uses paid edges
→ Return -1
```

### Case 3: Direct Paid Edge vs. Free Path

```
Terminals: [1, 3]
Budget: 1
Direct: 1--(P,1)--3
Path: 1--(F,100)--2--(F,100)--3
→ Choose direct (cheaper despite being paid)
```

### Case 4: Two Terminals, Budget=0

```
Must use only free edges
→ Standard shortest path problem
```

### Case 5: Budget Exceeds Requirement

```
Budget: 100
Only need 2 paid edges
→ Use optimal solution, ignore excess budget
```

### Case 6: All Edges Paid

```
Budget: 0
→ Impossible unless terminals are same node
```

---

## 12. Common Pitfalls

### Pitfall 1: Forgetting 0-Indexing Conversion

```python
# Input terminals are 1-indexed!
terminals = [t - 1 for t in terminals]
edges.u -= 1
edges.v -= 1
```

### Pitfall 2: Incorrect Submask Enumeration

❌ **Wrong:**

```python
for sub in range(mask):  # Misses valid submasks!
```

✓ **Correct:**

```python
sub = mask
while sub > 0:
    # process sub
    sub = (sub - 1) & mask
```

### Pitfall 3: Not Avoiding Double Counting in Merges

```python
# Only merge when sub >= comp
if comp > 0 and sub >= comp:
    # merge
```

### Pitfall 4: Budget Overflow

```python
new_budget = used_budget + paid
if new_budget <= b:  # Check BEFORE using!
    # relax
```

### Pitfall 5: Not Checking Dijkstra Staleness

```python
if cost > dp[mask][u][used_budget]:
    continue  # Already found better path
```

---

## 13. Alternative Approaches

### Approach 1: ILP (Integer Linear Programming)

```
Variables: x_e ∈ {0, 1} for each edge
Minimize: Σ(a_e × x_e)
Subject to:
  - Connectivity constraints
  - Σ(paid_e × x_e) ≤ B
```

- **Pros**: General, handles various constraints
- **Cons**: NP-hard, slow for large instances

### Approach 2: Approximation Algorithms

- **Metric Steiner Tree**: 2-approximation exists
- **Pros**: Polynomial time
- **Cons**: Only approximation, may not satisfy budget exactly

### Approach 3: Branch and Bound

- **Idea**: Prune search tree using bounds
- **Pros**: Exact solution
- **Cons**: Exponential worst case

### Approach 4: Without Budget Constraint

```
Standard Steiner Tree in Graphs
- Still NP-hard but simpler DP
- dp[mask][node] = min cost
- No budget dimension
```

---

## 14. Interview Follow-Ups

### Q1: What if Budget B is very large (> n)?

**A**: The effective budget is at most n-1 (MST bound). Cap B at n-1 to save memory.

### Q2: Can you handle edge deletions/additions dynamically?

**A**: No, this offline algorithm assumes static graph. Would need persistent/dynamic data structures.

### Q3: What if terminals can change?

**A**: Need to recompute from scratch. DP table is specific to terminals.

### Q4: How to find the actual edges in the solution?

**A**: Backtrack through DP table, tracking which transitions led to optimal value.

### Q5: What if we want the k-th best solution?

**A**: Modify to track top-k values at each state instead of just minimum.

---

## 15. Pattern Recognition

### When to Use This Pattern

✓ **Small subset constraint** (k ≤ 10-15)
✓ **Subset connection problems** (connect specific nodes)
✓ **Budget constraints** on solution
✓ **Steiner tree variants**
✓ **Partial connectivity** (not all nodes needed)

### Related Problems

1. **Traveling Salesman Problem (TSP)**: Visit all cities with min cost
   - Similar bitmask DP: dp[mask][node]
2. **Hamiltonian Path**: Visit all nodes exactly once

   - DP: dp[mask][node] = can visit nodes in mask ending at node

3. **Set Cover**: Cover all elements with min cost

   - DP: dp[mask] = min cost to cover elements in mask

4. **Prize-Collecting Steiner Tree**: Trade off connection cost vs. prize
5. **Group Steiner Tree**: Connect groups of nodes

### Core Techniques

- **Bitmask DP**: Track subsets with 2^k states
- **Subset Enumeration**: Iterate submasks using (sub-1) & mask
- **Shortest Path (Dijkstra)**: Find minimum cost paths with constraints
- **Merge Operations**: Combine solutions for disjoint subsets

### Applications

- **Network Design**: Connect critical infrastructure with budget
- **VLSI Routing**: Connect pins on chip with resource limits
- **Telecommunication**: Build networks connecting hubs
- **Transportation**: Optimize route networks
- **Social Network Analysis**: Influence maximization with budget

---

## Summary

The Steiner Tree with Budget problem combines:

- **Graph theory** (connectivity)
- **Dynamic programming** (optimal substructure)
- **Shortest paths** (Dijkstra)
- **Constraint satisfaction** (budget limit)

The key insight is leveraging small k to make bitmask DP feasible, then using Dijkstra to efficiently propagate solutions across the graph while respecting budget constraints.
