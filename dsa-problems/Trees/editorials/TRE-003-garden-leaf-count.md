---
problem_id: TRE_GARDEN_LEAF_COUNT__2475
display_id: TRE-003
slug: garden-leaf-count
title: "Garden Leaf Count"
difficulty: Easy
difficulty_score: 18
topics:
  - Trees
  - DFS
  - Counting
tags:
  - trees
  - dfs
  - counting
  - easy
premium: true
subscription_tier: basic
---

# TRE-003: Garden Leaf Count

## 📋 Problem Summary

Given a binary tree, count the number of **leaf nodes**. A leaf node is defined as a node that has neither a left child nor a right child.

## 🌍 Real-World Scenario

**Scenario Title:** Network Endpoints

Imagine a computer network structured like a tree, where the root is the main server, intermediate nodes are routers or switches, and leaf nodes are the actual end-user devices (laptops, phones, printers). To estimate the total number of active users or devices connected to the network, you simply need to count the "leaves" of this network tree.

![Real-World Application](../images/TRE-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1
     / \
    2   3
   / \
  4   5
```
**Analysis:**
-   Node 1: Has children (2, 3). Not a leaf.
-   Node 2: Has children (4, 5). Not a leaf.
-   Node 3: No children. **Leaf**.
-   Node 4: No children. **Leaf**.
-   Node 5: No children. **Leaf**.

**Total Leaves:** 3 (Nodes 3, 4, 5).

### Algorithm Steps

1.  Start a traversal (DFS or BFS) from the root.
2.  For each node visited:
    -   Check if `left` child is `-1` (or null).
    -   Check if `right` child is `-1` (or null).
    -   If both are missing, increment the leaf counter.
3.  Continue traversal to children.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Empty Tree:** `n=0`. Leaf count is 0.
-   **Single Node:** `n=1`. Leaf count is 1.
-   **Input Format:** Array of nodes. `left` and `right` are indices.

## Naive Approach

### Intuition

Since we are given the tree as an array of nodes `0..n-1`, we can simply iterate through the array indices from `0` to `n-1` and check the `left` and `right` values for each node. We don't even need to perform a traversal starting from the root!

### Algorithm

1.  Initialize `count = 0`.
2.  Loop `i` from `0` to `n-1`.
3.  If `left[i] == -1` AND `right[i] == -1`, `count++`.
4.  Return `count`.

### Time Complexity

-   **O(N)**: Single pass through the array.

### Space Complexity

-   **O(1)**: No recursion stack or queue needed.

## Optimal Approach (DFS Traversal)

While the array iteration is O(N) and O(1), in many tree problems (and interviews), you are given a reference to the root node, not the full array. Thus, knowing the traversal approach is critical.

### Algorithm

1.  Define `countLeaves(u)`:
    -   If `u == -1`, return 0.
    -   If `left[u] == -1` AND `right[u] == -1`, return 1.
    -   Return `countLeaves(left[u]) + countLeaves(right[u])`.

### Time Complexity

-   **O(N)**: Visit every node.

### Space Complexity

-   **O(H)**: Recursion stack depth.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int countLeaves(int n, int[] left, int[] right) {
        if (n == 0) return 0;
        // Iterative approach since we have the array
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] == -1 && right[i] == -1) {
                count++;
            }
        }
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.countLeaves(n, left, right));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def count_leaves(n: int, left: list[int], right: list[int]) -> int:
    if n == 0:
        return 0
    
    # Iterative approach on array
    count = 0
    for i in range(n):
        if left[i] == -1 and right[i] == -1:
            count += 1
    return count

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    left = [0] * n
    right = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print(count_leaves(n, left, right))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countLeaves(int n, const vector<int>& left, const vector<int>& right) {
        if (n == 0) return 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] == -1 && right[i] == -1) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.countLeaves(n, left, right) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countLeaves(n, left, right) {
    if (n === 0) return 0;
    let count = 0;
    for (let i = 0; i < n; i++) {
      if (left[i] === -1 && right[i] === -1) {
        count++;
      }
    }
    return count;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    idx++; // value
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.countLeaves(n, left, right).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
7 1 2
4 -1 -1
8 -1 -1
```

**Array Data:**
- Index 0: left=1, right=2
- Index 1: left=-1, right=-1
- Index 2: left=-1, right=-1

**Execution:**
1.  `i=0`: `left[0]=1`, `right[0]=2`. Not a leaf.
2.  `i=1`: `left[1]=-1`, `right[1]=-1`. Leaf! `count=1`.
3.  `i=2`: `left[2]=-1`, `right[2]=-1`. Leaf! `count=2`.

**Output:** `2`. Correct.

## ✅ Proof of Correctness

The definition of a leaf node is strictly "a node with no children".
By iterating through every node in the tree (which the array format allows us to do directly), we check this condition for every node exactly once.
This guarantees that we count all leaves and only leaves.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Sum of Left Leaves**
    -   Count only leaves that are the *left* child of their parent. (Requires traversal passing `isLeft` flag).
-   **Extension 2: Leaves at Same Level**
    -   Check if all leaves are at the same depth.
-   **Extension 3: Remove Leaves**
    -   Prune all leaf nodes from the tree.

### Common Mistakes to Avoid

1.  **Null Check:**
    -   ❌ Forgetting to check `n=0`.
    -   ✅ Handle empty tree case.
2.  **Definition Confusion:**
    -   ❌ Counting nodes with 1 child as leaves?
    -   ✅ Leaf must have **zero** children.

## Related Concepts

-   **Tree Traversal**
-   **Internal Nodes** (Nodes that are not leaves).
