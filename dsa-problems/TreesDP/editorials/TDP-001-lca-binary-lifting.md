---
problem_id: TDP_LCA_BINARY_LIFTING__7291
display_id: TDP-001
slug: lca-binary-lifting
title: "Lowest Common Ancestor (Binary Lifting)"
difficulty: Medium
difficulty_score: 45
topics:
  - Tree DP
  - Binary Lifting
  - LCA
tags:
  - preprocessing
  - tree-traversal
  - ancestors
premium: true
subscription_tier: basic
---

# TDP-001: Lowest Common Ancestor (Binary Lifting)

## 📋 Problem Summary

Given a rooted tree with n nodes, preprocess it to answer queries for the Lowest Common Ancestor (LCA) of any two nodes in O(log n) time using binary lifting technique.

## 🌍 Real-World Scenario

**Scenario Title:** Corporate Organizational Hierarchy Analysis

In a large multinational corporation with thousands of employees, the organizational structure forms a tree where the CEO is the root, and each employee reports to exactly one manager. The HR department needs to efficiently answer questions like: "Who is the lowest-level manager that oversees both the Sales Director of Region A and the Marketing Manager of Region B?" This is essentially finding the LCA of two nodes in the organizational tree.

Traditional methods of traversing from each employee up to the root would be too slow when handling hundreds of thousands of queries per day. Binary lifting allows the system to preprocess the organizational chart once (whenever there's a restructuring) and then answer any managerial relationship query in logarithmic time, making real-time organizational analysis feasible.

This technique is also used in version control systems like Git to find the common ancestor of two commits, in file system hierarchies to determine the closest common parent directory, and in biological taxonomy to find the most recent common ancestor of two species.

**Why This Problem Matters:**

- **Efficient Query Processing:** Reduces query time from O(n) to O(log n), crucial for real-time systems
- **Preprocessing Investment:** One-time O(n log n) preprocessing enables unlimited fast queries
- **Versatile Applications:** Used in databases, compilers, bioinformatics, and network routing

![Real-World Application](../images/TDP-001/real-world-scenario.png)

## Detailed Explanation

The Lowest Common Ancestor (LCA) of two nodes u and v in a rooted tree is the deepest node that is an ancestor of both u and v. Binary lifting is a preprocessing technique that allows us to answer LCA queries efficiently.

**Key Insight:** Instead of storing just the immediate parent of each node, we store the ancestor at distances 2^0, 2^1, 2^2, ..., 2^k where k = log₂(n). This allows us to "jump" exponentially up the tree.

The preprocessing involves:

1. Computing the depth of each node via DFS
2. Building a 2D array `up[node][j]` where `up[node][j]` is the 2^j-th ancestor of node
3. Using dynamic programming: `up[node][j] = up[up[node][j-1]][j-1]`

For LCA queries:

1. First, bring both nodes to the same depth using binary jumps
2. Then, simultaneously lift both nodes upward, ensuring they don't meet, until their parents are the same
3. The parent is the LCA

## Naive Approach

**Intuition:**
For each LCA query, traverse from both nodes upward toward the root until they meet at a common ancestor.

### Algorithm

```
function lca_naive(u, v):
    ancestors_u = empty set

    // Step 1: Collect all ancestors of u
    current = u
    while current != null:
        ancestors_u.add(current)
        current = parent[current]

    // Step 2: Traverse from v upward until hitting an ancestor of u
    current = v
    while current not in ancestors_u:
        current = parent[current]

    return current  // This is the LCA
```

### Complexity Analysis

| Phase                  | Time       | Space    | Explanation                           |
| ---------------------- | ---------- | -------- | ------------------------------------- |
| Collect ancestors of u | O(h)       | O(h)     | Traverse from u to root, store in set |
| Find LCA from v        | O(h)       | O(1)     | Traverse from v until match found     |
| **Per Query**          | **O(h)**   | **O(h)** | h = height of tree                    |
| **Total (q queries)**  | **O(q·h)** | **O(h)** | Worst case h = n (skewed tree)        |

**Why This Complexity:**

- In a balanced tree: h = O(log n), so O(q log n) per query
- In a skewed tree (linked list): h = O(n), so O(qn) total
- No preprocessing benefit - each query starts fresh

**Limitations:**

- Too slow for large trees with many queries
- Each query requires potentially scanning the entire path to root
- No benefit from preprocessing

## Optimal Approach

**Key Insight:**
By preprocessing ancestors at exponential distances (2^0, 2^1, 2^2, ...), we can jump to any ancestor in O(log n) jumps using binary representation of distances.

### Algorithm

**Phase 1: Preprocessing (Build Jump Table)**

```
function preprocess(root):
    // Step 1: DFS to compute depths and immediate parents
    dfs(root, null, depth=0)

    // Step 2: Build binary lifting table
    // up[node][j] = ancestor at distance 2^j
    for j from 1 to LOG:
        for each node:
            if up[node][j-1] exists:
                up[node][j] = up[up[node][j-1]][j-1]
            // Jump 2^j = jump 2^(j-1) twice
```

**Phase 2: LCA Query**

```
function lca(u, v):
    // Step 1: Ensure u is deeper
    if depth[u] < depth[v]: swap(u, v)

    // Step 2: Lift u to same depth as v
    diff = depth[u] - depth[v]
    for j from LOG-1 down to 0:
        if (diff >> j) & 1:  // If j-th bit is set
            u = up[u][j]

    // Step 3: If same node, v was ancestor of u
    if u == v: return u

    // Step 4: Binary search for LCA
    for j from LOG-1 down to 0:
        if up[u][j] != up[v][j]:
            u = up[u][j]
            v = up[v][j]

    return up[u][0]  // Parent is LCA
```

### Complexity Analysis

| Phase                   | Time                     | Space          | Explanation                       |
| ----------------------- | ------------------------ | -------------- | --------------------------------- |
| DFS traversal           | O(n)                     | O(n)           | Visit each node once, store depth |
| Build jump table        | O(n log n)               | O(n log n)     | n nodes × log n ancestors each    |
| **Preprocessing Total** | **O(n log n)**           | **O(n log n)** | One-time cost                     |
| Equalize depths         | O(log n)                 | O(1)           | At most log n jumps               |
| Binary search LCA       | O(log n)                 | O(1)           | At most log n iterations          |
| **Per Query**           | **O(log n)**             | **O(1)**       | Constant per query                |
| **Total (q queries)**   | **O(n log n + q log n)** | **O(n log n)** | Amortized                         |

**Why This Is Optimal:**

- Each query requires at most log₂(n) jumps
- Preprocessing is done once and amortized over many queries
- Binary representation allows reaching any distance efficiently
- For n = 200,000 and q = 200,000: ~7M operations vs ~40B naive

![Algorithm Visualization](../images/TDP-001/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


---

## 🧪 Test Case Walkthrough (Dry Run)

### Input

```
7 3
1 2
1 3
2 4
2 5
3 6
3 7
4 5
4 7
6 7
```

### Visual Representation

```
Tree Structure:
        1
       / \
      2   3
     / \ / \
    4  5 6  7

Depths: 1→0, 2→1, 3→1, 4→2, 5→2, 6→2, 7→2
```

### Query Walkthrough

| Query | u   | v   | Process                            | LCA   |
| ----- | --- | --- | ---------------------------------- | ----- |
| 1     | 4   | 5   | Same parent (2), depth equal       | **2** |
| 2     | 4   | 7   | Lift to same depth, then lift both | **1** |
| 3     | 6   | 7   | Same parent (3), depth equal       | **3** |

### Step-by-Step for Query (4, 7):

1. `depth[4]=2, depth[7]=2` → same depth
2. `up[4][0]=2, up[7][0]=3` → different, don't jump
3. Since `up[4][0] != up[7][0]`, answer is `up[up[4][0]][0] = up[2][0] = 1`

**Output:** `2 1 3`

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                   | ❌ Wrong                              | ✅ Correct                                          |
| --- | ------------------------- | ------------------------------------- | --------------------------------------------------- |
| 1   | **LOG too small**         | `LOG = (int)(log(n)/log(2))`          | `LOG = 20` (safe upper bound)                       |
| 2   | **Skip same-level check** | Always run lifting loop               | Check `if (u == v) return u` after equalizing depth |
| 3   | **Wrong comparison**      | `if (up[u][j] == up[v][j])` then jump | `if (up[u][j] != up[v][j])` then jump               |
| 4   | **Return wrong node**     | `return u` after lifting              | `return up[u][0]` (parent is LCA)                   |
| 5   | **Forget -1 check**       | Access `up[up[u][j]][...]`            | Check `up[u][j] != -1` first                        |

### Detailed Examples:

**Mistake 1: LOG Calculation**


**Mistake 3: Wrong Comparison Direction**


---

## Related Concepts

- **Sparse Table:** Similar preprocessing for range queries
- **Euler Tour + RMQ:** Alternative LCA approach with different trade-offs
- **Heavy-Light Decomposition:** Advanced tree path queries
- **Link-Cut Trees:** Dynamic tree structures with path queries


## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `1 ≤ q ≤ 2 × 10^5`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree
- All queries are independent