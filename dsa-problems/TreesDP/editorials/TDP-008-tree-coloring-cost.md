---
title: Tree Coloring with Color Costs
problem_id: TDP_TREE_COLORING_COST__5821
display_id: TDP-008
difficulty: Medium
tags:
- tree-dp
- coloring
- optimization
- dynamic-programming
editorial_categories:
- Tree DP
- Optimization DP
slug: tree-coloring-cost
---
## 📝 Problem Summary

Given a tree with N nodes where each node must be colored with one of K colors, and each node has a cost associated with each possible color, find the minimum total cost to color all nodes such that no two adjacent nodes share the same color. This is a tree coloring optimization problem that combines the classic graph coloring constraint with cost minimization.

---

## 🔍 Approach: Tree DP with Color States

### Key Insight

On a tree, we can solve the coloring problem optimally using dynamic programming. For each node, we track the minimum cost to color its subtree for each possible color assignment to that node. Since adjacent nodes cannot share colors, when a node is assigned color c, all its children must be assigned colors different from c.

### Algorithm Overview

1. Root the tree at any node (typically node 1)
2. For each node u and each color c: compute dp[u][c] = cost of coloring subtree rooted at u, where u has color c
3. The recurrence: dp[u][c] = cost[u][c] + Σ min(dp[child][c']) for all c' ≠ c
4. Answer: min(dp[root][c]) for all colors c

### Optimization for Large K

When K is large, the naive O(N × K²) approach may be too slow. We can optimize using a trick:

- For each node's children, precompute the minimum and second minimum dp values across all colors
- When computing dp[u][c], if the minimum comes from color c, use second minimum; otherwise use minimum

This reduces complexity to O(N × K).

---

## 🧠 Intuition Builder

### 💡 Visual Intuition

Imagine painting a hierarchical organization chart where managers cannot have the same office color as their direct reports. Each color has a different cost per office based on size, availability, etc. We want to find the cheapest way to paint all offices while respecting the adjacency constraint.

### 🌍 Real-World Analogy

**Frequency Assignment in Communication Networks:**
Consider assigning radio frequencies to relay stations in a tree-structured network. Adjacent stations must use different frequencies to avoid interference. Each station has different equipment costs for different frequencies. We want to minimize total equipment cost while ensuring no interference.

### 🔗 Pattern Recognition

This problem combines:

- **Graph Coloring**: Adjacent nodes have different colors
- **Tree DP**: Optimal substructure on tree
- **Optimization**: Minimize total cost
- **State Compression**: Track color per node

---

## ✅ Solution: Tree Coloring DP

### Detailed Solution Steps

1. **Parse input and build adjacency list**
2. **Root the tree using DFS/BFS**
3. **Post-order traversal to compute DP values**
4. **For each node, compute minimum cost for each color**
5. **Return minimum of root's DP values**

### Implementation Notes

- Use post-order traversal so children are processed before parent
- For optimization, track min and second-min for each child
- Handle single-node tree as edge case

---

## 💻 Implementation

### Java


### Python


### C++


### JavaScript


---

## ⏱️ Complexity Analysis

### Detailed Breakdown

| Phase               | Naive O(N×K²)  | Optimized O(N×K) | Explanation                     |
| ------------------- | -------------- | ---------------- | ------------------------------- |
| DFS traversal       | O(N)           | O(N)             | Visit each node once            |
| Per-node processing | O(K²)          | O(K)             | Sum over children's colors      |
| Child aggregation   | O(K) per child | O(1) per child   | Use min/second-min trick        |
| **Total Time**      | **O(N×K²)**    | **O(N×K)**       | Optimized with precomputed mins |
| **Space**           | **O(N×K)**     | **O(N×K)**       | DP table + adjacency list       |

### Why This Complexity:

**Naive Approach:**

- For each node (N nodes) and each color (K colors): O(N×K) states
- For each state, sum over all children's K colors: O(K) per child
- With d children: O(d×K) = O(K²) worst case (sum of degrees = 2N-2)
- Total: O(N×K²)

**Optimized Approach:**

- Precompute for each child: minCost and secondMinCost across all K colors
- When computing dp[u][c]:
  - If child's minimum is at color c: use secondMinCost
  - Otherwise: use minCost
- This reduces per-child work from O(K) to O(1)
- Total: O(N×K)

**For N = 200K, K = 100:**

- Naive: ~4 billion operations
- Optimized: ~20 million operations (200× faster)

---

## 🧪 Test Case Walkthrough (Dry Run)

### Input

```
4 3
10 20 30
15 25 5
20 10 25
5 30 15
1 2
1 3
2 4
```

### Visual Representation

```
Tree with K=3 colors:
Node costs: [R, G, B]

       1 [10,20,30]
      / \
   2[15,25,5]  3[20,10,25]
    |
   4[5,30,15]

Constraint: Adjacent nodes different colors
```

### DP Walkthrough

| Node | Color R (0)                 | Color G (1)                 | Color B (2)                 | Explanation                |
| ---- | --------------------------- | --------------------------- | --------------------------- | -------------------------- |
| 4    | 5                           | 30                          | 15                          | Leaf: just own cost        |
| 2    | 15+min(30,15)=30            | 25+min(5,15)=30             | 5+min(5,30)=10              | Add best child ≠ own color |
| 3    | 20                          | 10                          | 25                          | Leaf                       |
| 1    | 10+min(30,10)+min(10,25)=30 | 20+min(30,10)+min(20,25)=50 | 30+min(30,30)+min(20,10)=70 | Sum from both children     |

**Answer: min(30, 50, 70) = 30**

Optimal: 1=R(10), 2=B(5), 3=G(10), 4=R(5) = 30

**Output:** `30`

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                | ❌ Wrong                         | ✅ Correct                            |
| --- | ---------------------- | -------------------------------- | ------------------------------------- |
| 1   | **Same color allowed** | `dp[u][c] += min(dp[v])`         | `dp[u][c] += min(dp[v][c'] for c'≠c)` |
| 2   | **O(K²) per node**     | Loop all K colors for each child | Use min/second-min optimization       |
| 3   | **Forget own cost**    | `dp[u][c] = sum of children`     | `dp[u][c] = cost[u][c] + sum`         |
| 4   | **Int overflow**       | `int dp[][]` with large costs    | Use `long` for sums                   |

### Detailed Example:

**Min/Second-Min Optimization**


---

## ✅ Correctness Proof

### Invariant

After DFS on node u, dp[u][c] contains the minimum cost to color the subtree rooted at u where u is colored with color c.

### Proof by Induction

1. **Base case (leaf):** dp[leaf][c] = cost[leaf][c], which is correct.
2. **Inductive step:** Assuming dp values for all children are correct, for node u with color c, we need the sum of (cost[u][c] + min cost for each child with a different color). Since we can choose any color ≠ c for each child independently, we take the minimum over all valid colors.

---

## 🧪 Edge Cases

| Case           | Input                   | Expected Output           |
| -------------- | ----------------------- | ------------------------- |
| Single node    | n=1, k=3, costs=[5,2,8] | 2                         |
| Two nodes      | n=2, k=2                | Minimum valid assignment  |
| All same costs | All costs equal         | Sum of any valid coloring |
| Large costs    | costs up to 10^9        | Handle long overflow      |

---

## 🔗 Related Problems

1. **House Painting Problem** - Similar DP with limited colors
2. **Graph Coloring** - NP-complete for general graphs, polynomial for trees
3. **Chromatic Number** - Minimum colors needed (always 2 for trees)
4. **Weighted Graph Coloring** - Optimization version

---

## 💡 Key Takeaways

1. **Tree structure enables polynomial solution** for otherwise NP-complete problems
2. **Min/second-min optimization** reduces K² to K factor
3. **Post-order traversal** ensures children processed before parent
4. **State = color assignment** gives us complete information for DP
5. **Adjacency constraint** handled by excluding same color in transitions


## Constraints

- 1 ≤ N ≤ 200,000
- 2 ≤ K ≤ 200
- 1 ≤ c[i][j] ≤ 10^9
- The graph is guaranteed to be a tree
- Answer fits in 64-bit signed integer

---