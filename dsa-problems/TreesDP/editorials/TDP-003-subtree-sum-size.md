---
problem_id: TDP_SUBTREE_SUM_SIZE__3184
display_id: TDP-003
slug: subtree-sum-size
title: "Subtree Sum and Size"
difficulty: Easy
difficulty_score: 25
topics:
  - Tree DP
  - DFS
  - Subtree Queries
tags:
  - tree-traversal
  - aggregation
  - subtree-properties
premium: true
subscription_tier: basic
---

# TDP-003: Subtree Sum and Size

## 📋 Problem Summary

For each node in a rooted tree with weighted nodes, compute the sum and size (number of nodes) of its subtree using DFS and dynamic programming.

## 🌍 Real-World Scenario

**Scenario Title:** Corporate Budget Management System

A large enterprise has a hierarchical organizational structure where each department is a node in the tree, and the CEO's office is the root. Each department has an annual budget (the node value). The CFO needs to quickly answer queries like: "What is the total budget allocated to the Engineering division and all its sub-departments?" or "How many teams report under the VP of Sales (directly or indirectly)?"

By preprocessing the tree to compute subtree sums and sizes, the system can instantly provide these aggregated metrics without recalculating each time. This is essential for budget planning, resource allocation, and organizational analysis. When departments are added or restructured, the preprocessing can be rerun efficiently.

This technique is also used in file systems (computing directory sizes), comment threads (counting replies), and biological taxonomy (species counts in phylogenetic clades).

**Why This Problem Matters:**

- **Efficient Aggregation:** O(n) preprocessing enables O(1) subtree queries
- **Foundation for Advanced DP:** Building block for complex tree DP problems
- **Practical Applications:** Directory sizes, organizational metrics, nested data analysis

![Real-World Application](../images/TDP-003/real-world-scenario.png)

## Detailed Explanation

Given a rooted tree where each node has a value, we need to compute:

1. **Subtree Size:** Number of nodes in the subtree rooted at each node (including itself)
2. **Subtree Sum:** Sum of all node values in the subtree

The key insight is that a node's subtree sum/size equals its own value/1 plus the sum/size of all its children's subtrees. This recursive relationship makes DFS with DP ideal.

**Algorithm Intuition:**

- Perform DFS from the root
- For each node, first recursively process all children
- Then aggregate: `subtree_sum[node] = value[node] + Σ subtree_sum[child]`
- Similarly: `subtree_size[node] = 1 + Σ subtree_size[child]`

## Naive Approach

**Intuition:**
For each node, run a separate DFS/BFS to count all nodes and sum all values in its subtree.

### Algorithm

```
function compute_subtrees_naive():
    size = array of n+1
    sum = array of n+1

    for v from 1 to n:
        // Run separate DFS for each node
        size[v], sum[v] = dfs_subtree(v, parent_of_v)

    return size, sum

function dfs_subtree(node, parent):
    count = 1
    total = value[node]

    for child in adj[node]:
        if child != parent and child is in subtree of node:
            c, s = dfs_subtree(child, node)
            count += c
            total += s

    return count, total
```

### Complexity Analysis

| Phase           | Time            | Space    | Explanation                      |
| --------------- | --------------- | -------- | -------------------------------- |
| Outer loop      | O(n)            | O(1)     | Iterate all nodes                |
| DFS per node    | O(subtree size) | O(h)     | Average n/2 nodes                |
| **Naive Total** | **O(n²)**       | **O(h)** | Each node visited multiple times |

**Why This Complexity:**

- Worst case: root's DFS visits n nodes, its child visits n-1, etc.
- Sum: n + (n-1) + ... + 1 = O(n²)
- For n = 200,000: ~20B operations (too slow)

**Limitations:**

- Extremely inefficient with redundant traversals
- Each subtree is visited multiple times
- Doesn't leverage the tree structure

## Optimal Approach

**Key Insight:**
Use a single DFS traversal where each node's subtree metrics are computed from its children's metrics using dynamic programming (post-order traversal).

### Algorithm

```
function compute_subtrees_optimal():
    size = array of n+1
    sum = array of n+1

    function dfs(node, parent):
        // Base case: leaf contributes just itself
        size[node] = 1
        sum[node] = value[node]

        // Aggregate children's subtrees
        for child in adj[node]:
            if child != parent:
                dfs(child, node)  // Process child first (post-order)
                size[node] += size[child]
                sum[node] += sum[child]

    dfs(root, -1)
    return size, sum
```

### Complexity Analysis

| Phase             | Time                | Space    | Explanation                  |
| ----------------- | ------------------- | -------- | ---------------------------- |
| DFS traversal     | O(n)                | O(h)     | Visit each node exactly once |
| Aggregation       | O(degree) per node  | O(1)     | Sum over children            |
| Result arrays     | O(1) write per node | O(n)     | Store n values               |
| **Optimal Total** | **O(n)**            | **O(n)** | Linear in tree size          |

**Why This Is Optimal:**

- Each edge traversed exactly once (down and up)
- Bottom-up DP ensures no redundant computation
- Linear time is optimal since all nodes must be visited
- For n = 200,000: ~400K operations vs ~20B naive

![Algorithm Visualization](../images/TDP-003/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


---

## 🧪 Test Case Walkthrough (Dry Run)

### Input

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
```

### Visual Representation

```
Tree with values:
       1 (10)
      / \
   2(20) 3(30)
   / \
4(40) 5(50)
```

### DFS Walkthrough (post-order)

| Node | Own Value | Children | Child Sums | Subtree Sum | Subtree Size |
| ---- | --------- | -------- | ---------- | ----------- | ------------ |
| 4    | 40        | none     | 0          | **40**      | 1            |
| 5    | 50        | none     | 0          | **50**      | 1            |
| 2    | 20        | 4, 5     | 40+50=90   | **110**     | 3            |
| 3    | 30        | none     | 0          | **30**      | 1            |
| 1    | 10        | 2, 3     | 110+30=140 | **150**     | 5            |

**Output:**

```
150
110
30
40
50
```

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                  | ❌ Wrong                | ✅ Correct                        |
| --- | ------------------------ | ----------------------- | --------------------------------- |
| 1   | **Forget own value**     | `sum[u] = Σ sum[child]` | `sum[u] = val[u] + Σ sum[child]`  |
| 2   | **Integer overflow**     | `int sum[]`             | `long sum[]` for large values     |
| 3   | **Visit parent**         | No parent check         | `if (child == parent) continue`   |
| 4   | **Wrong initialization** | `subtreeSize[u] = 0`    | `subtreeSize[u] = 1` (count self) |

### Detailed Example:

**Mistake 1: Forgetting Node's Own Value**


---

## Related Concepts

- **Prefix Sums:** Similar aggregation technique for arrays
- **Rerooting DP:** Computing metrics for all possible roots
- **Heavy-Light Decomposition:** Advanced subtree query techniques
- **Lazy Propagation:** Handling subtree updates efficiently


## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `-10^9 ≤ value[i] ≤ 10^9`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree