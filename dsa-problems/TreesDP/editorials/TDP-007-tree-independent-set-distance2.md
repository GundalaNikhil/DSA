---

title: Distance-2 Independent Set on Tree
problem_id: TDP_DISTANCE2_INDEPENDENT_SET__8395
display_id: TDP-007
difficulty: Medium
tags:
  - Tree DP
  - Independent Set
  - Optimization
editorial_categories:
  - Algorithms
  - Data Structures
slug: tree-independent-set-distance2
---


# Distance-2 Independent Set on Tree

## 📋 Problem Summary

Given a tree with `n` nodes where each node has a weight, find the **maximum total weight** of a subset of nodes such that any two chosen nodes are at distance **at least 3** (no adjacency and no common neighbor).

### Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= w[i] <= 10^9`

## 🌍 Real-World Scenario

**Cell Tower Placement:**

- Each location has a value (population coverage potential)
- Towers must be placed far apart to avoid interference
- Distance-2 constraint: no adjacent towers, no towers sharing a common junction
- Goal: Maximize total population coverage

## 🔍 Naive Approach

### Algorithm

```
function max_independent_set_d2_naive():
    max_value = 0

    // Step 1: Try all subsets
    for subset in all_subsets(vertices):
        // Step 2: Check distance-2 constraint
        valid = true
        for u in subset:
            for v in subset:
                if u != v and distance(u, v) <= 2:
                    valid = false
                    break

        // Step 3: Calculate value
        if valid:
            value = sum of weights in subset
            max_value = max(max_value, value)

    return max_value
```

### Complexity Analysis

| Phase            | Time             | Space    | Explanation         |
| ---------------- | ---------------- | -------- | ------------------- |
| Generate subsets | O(2^n)           | O(n)     | All 2^n subsets     |
| Distance check   | O(n²) per subset | O(n)     | All pairs in subset |
| **Naive Total**  | **O(2^n · n²)**  | **O(n)** | Exponential         |

**Why This Complexity:**

- 2^n subsets, each requires O(n²) distance checks
- For n = 20: billions of operations
- Completely infeasible for n = 200K

## 💡 Optimal Approach: Extended State DP

### DP States

For each node `u`, track three states based on its relationship to selected nodes:

- `dp[u][0]` = u NOT selected, and no child is selected
- `dp[u][1]` = u NOT selected, but at least one child is selected
- `dp[u][2]` = u IS selected

### Recurrence

**dp[u][2] (u selected):**

- All children must be in state 0 (not selected, no grandchild selected)

```
dp[u][2] = w[u] + Σ dp[child][0]
```

**dp[u][0] (u not selected, no child selected):**

- All children in state 0 or 1, but none in state 2

```
dp[u][0] = Σ max(dp[child][0], dp[child][1])
```

**dp[u][1] (u not selected, at least one child selected):**

- At least one child must be in state 2
- Others can be in state 0, 1, or 2

```
dp[u][1] = max over configurations where at least one child is in state 2
```

### Algorithm

```
function max_independent_set_d2_dp():
    function dfs(u, parent):
        dp[u][0] = 0  // u not selected, no child selected
        dp[u][1] = 0  // u not selected, ≥1 child selected
        dp[u][2] = w[u]  // u selected

        sum_no_child = 0
        max_with_child = 0

        for child in adj[u]:
            if child != parent:
                dfs(child, u)

                dp[u][2] += dp[child][0]  // u selected → child state 0
                sum_no_child += max(dp[child][0], dp[child][1])
                max_with_child = max(max_with_child,
                                     dp[child][2] - max(dp[child][0], dp[child][1]))

        dp[u][0] = sum_no_child
        dp[u][1] = sum_no_child + max_with_child

    dfs(1, -1)
    return max(dp[1][0], dp[1][1], dp[1][2])
```

### Complexity Analysis

| Phase             | Time          | Space    | Explanation          |
| ----------------- | ------------- | -------- | -------------------- |
| DFS traversal     | O(n)          | O(h)     | Visit each node once |
| Process children  | O(d) per node | O(1)     | d = degree           |
| DP storage        | -             | O(n)     | 3 states × n nodes   |
| **Optimal Total** | **O(n)**      | **O(n)** | Linear               |

**Why This Is Optimal:**

- Each node visited once in post-order DFS
- 3 states sufficient to capture all constraints
- For n = 200K: ~600K operations vs ~10^60K naive

## 💻 Implementation

### Java


### Python


### C++


### JavaScript


---

## 🧪 Test Case Walkthrough (Dry Run)

### Input

```
7
10 20 30 40 50 60 70
1 2
1 3
2 4
2 5
3 6
3 7
```

### Visual Representation

```
Tree with weights:
        1 (10)
       / \
   2(20) 3(30)
   / \   / \
4(40)5(50)6(60)7(70)

Constraint: Selected nodes must be at distance ≥ 3
(at least 2 nodes between any two selected)
```

### Valid Selections

| Selection    | Distance Check | Total Weight  |
| ------------ | -------------- | ------------- |
| {4, 6}       | d(4,6)=4 ✓     | 40+60=100     |
| {4, 7}       | d(4,7)=4 ✓     | 40+70=110     |
| {5, 6}       | d(5,6)=4 ✓     | 50+60=110     |
| {5, 7}       | d(5,7)=4 ✓     | 50+70=**120** |
| {4, 5, 6, 7} | d(4,5)=2 ❌    | Invalid       |

**Answer: 120** (select nodes 5 and 7)

**Output:** `120`

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake            | ❌ Wrong                         | ✅ Correct                         |
| --- | ------------------ | -------------------------------- | ---------------------------------- |
| 1   | **Use 2 states**   | dp[u][0/1] like regular IS       | Need 3 states for dist-2           |
| 2   | **Wrong distance** | Adjacent = distance 2            | Adjacent = distance 1              |
| 3   | **Miss max gain**  | Don't track best child to select | Track `maxGain` over children      |
| 4   | **Init maxGain**   | `maxGain = 0`                    | `maxGain = -INF` (may be negative) |

### State Explanation:

```
dp[u][0] = u not selected, no child selected
dp[u][1] = u not selected, some child selected
dp[u][2] = u IS selected

When u is selected (dp[u][2]):
- All children must be in state 0 (not selected, no grandchild selected)
- Because distance(u, grandchild) = 2 < 3
```

---

## 🔗 Related Concepts

- **Maximum Independent Set:** Distance-1 constraint (no adjacent)
- **Dominating Set:** Every node covered or adjacent to selected
- **Tree Matching:** Pairing adjacent nodes
