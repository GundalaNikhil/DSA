---
problem_id: TRE_LAB_TREE_HEIGHT__1934
display_id: TRE-002
slug: lab-tree-height
title: "Lab Tree Height"
difficulty: Easy
difficulty_score: 20
topics:
  - Trees
  - DFS
  - Recursion
tags:
  - trees
  - dfs
  - recursion
  - easy
premium: true
subscription_tier: basic
---

# TRE-002: Lab Tree Height

## 📋 Problem Summary

Given a binary tree, calculate its **height**. The height is defined as the number of edges on the longest path from the root node to any leaf node. If the tree is empty, the height is `-1`. A tree with a single node has a height of `0`.

## 🌍 Real-World Scenario

**Scenario Title:** Corporate Hierarchy Levels

Consider a corporate organizational chart where the CEO is at the top. You want to determine the "depth" of the organization—that is, the maximum number of reporting levels between the CEO and an entry-level employee.
-   **CEO:** Level 0.
-   **VP:** Level 1 (1 edge from CEO).
-   **Manager:** Level 2 (2 edges from CEO).
-   **Intern:** Level 3 (3 edges from CEO).

Knowing the height of this tree helps in understanding the organizational structure's complexity and communication distance.

![Real-World Application](../images/TRE-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      5 (Root)
     / \
    3   9
   /
  1
```
**Paths:**
-   5 -> 9: 1 edge.
-   5 -> 3 -> 1: 2 edges.

**Height:** Max(1, 2) = 2.

### Algorithm Steps

1.  **Base Case:** If the node is empty (or index is `-1`), return `-1`.
2.  **Recursive Step:**
    -   Compute the height of the left subtree.
    -   Compute the height of the right subtree.
    -   The height of the current node is `1 + max(left_height, right_height)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Height Definition:** Number of edges. Some definitions use number of nodes (where single node = 1). Here, single node = 0.
-   **Empty Tree:** `n=0`. Return `-1`.
-   **Input Format:** Array of nodes. `left` and `right` are indices.

## Naive Approach

### Intuition

We can perform a Level Order Traversal (BFS). The number of levels minus 1 is the height.

### Algorithm

1.  If root is null, return -1.
2.  Queue `q`, add root. `levels = 0`.
3.  While `q` is not empty:
    -   `size = q.size()`.
    -   Process `size` nodes (add their children).
    -   `levels++`.
4.  Return `levels - 1`.

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(W)**: Max width of the tree (can be N/2).

## Optimal Approach (Recursive DFS)

### Key Insight

The height of a tree is defined recursively. The height of a node is simply 1 plus the maximum height of its children. This maps perfectly to a Depth First Search (DFS).

### Algorithm

1.  Define `height(u)`:
    -   If `u == -1`, return `-1`.
    -   Return `1 + max(height(left[u]), height(right[u]))`.
2.  Call `height(0)` (if `n > 0`).

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(H)**: Recursion stack depth. Best case O(log N), worst case O(N).

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int treeHeight(int n, int[] left, int[] right) {
        if (n == 0) return -1;
        return dfs(0, left, right);
    }

    private int dfs(int u, int[] left, int[] right) {
        if (u == -1) return -1;
        int lHeight = dfs(left[u], left, right);
        int rHeight = dfs(right[u], left, right);
        return 1 + Math.max(lHeight, rHeight);
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
            int val = sc.nextInt(); // Value is unused for height
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.treeHeight(n, left, right));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def tree_height(n: int, left: list[int], right: list[int]) -> int:
    if n == 0:
        return -1
        
    def dfs(u):
        if u == -1:
            return -1
        l_height = dfs(left[u])
        r_height = dfs(right[u])
        return 1 + max(l_height, r_height)
        
    return dfs(0)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    if n == 0:
        print("-1")
        return

    left = [0] * n
    right = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1 # Skip value
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print(tree_height(n, left, right))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int dfs(int u, const vector<int>& left, const vector<int>& right) {
        if (u == -1) return -1;
        int lHeight = dfs(left[u], left, right);
        int rHeight = dfs(right[u], left, right);
        return 1 + max(lHeight, rHeight);
    }

public:
    int treeHeight(int n, const vector<int>& left, const vector<int>& right) {
        if (n == 0) return -1;
        return dfs(0, left, right);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    if (n == 0) {
        cout << "-1\n";
        return 0;
    }

    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.treeHeight(n, left, right) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  treeHeight(n, left, right) {
    if (n === 0) return -1;
    
    const dfs = (u) => {
      if (u === -1) return -1;
      const lHeight = dfs(left[u]);
      const rHeight = dfs(right[u]);
      return 1 + Math.max(lHeight, rHeight);
    };
    
    return dfs(0);
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
  
  if (n === 0) {
      console.log("-1");
      return;
  }
  
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    idx++; // value
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.treeHeight(n, left, right).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
5 1 2
3 3 -1
9 -1 -1
1 -1 -1
```

**Tree Structure:**
- Node 0 (5): Left -> 1, Right -> 2
- Node 1 (3): Left -> 3, Right -> -1
- Node 2 (9): Leaf
- Node 3 (1): Leaf

**Execution:**
1.  `dfs(0)` called.
2.  `dfs(1)` called (Left of 0).
    -   `dfs(3)` called (Left of 1).
        -   `dfs(-1)` returns -1.
        -   `dfs(-1)` returns -1.
        -   Returns `1 + max(-1, -1) = 0`. (Node 3 height is 0)
    -   `dfs(-1)` called (Right of 1). Returns -1.
    -   Returns `1 + max(0, -1) = 1`. (Node 1 height is 1)
3.  `dfs(2)` called (Right of 0).
    -   Returns `1 + max(-1, -1) = 0`. (Node 2 height is 0)
4.  `dfs(0)` returns `1 + max(1, 0) = 2`.

**Output:** `2`. Correct.

## ✅ Proof of Correctness

The algorithm relies on the inductive definition of tree height.
-   **Base Case:** An empty tree (null node) has height -1. This is correct by definition (single node is 0, so empty must be -1 to make `1 + (-1) = 0`).
-   **Inductive Step:** Assuming `dfs` correctly computes the height for subtrees, `1 + max(left, right)` correctly adds the edge connecting the current node to its children.
Since the tree is finite and acyclic, the recursion terminates and propagates the correct values up to the root.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Diameter of Tree**
    -   Find the longest path between *any* two nodes. (Often uses height calculation as a subroutine: `diam = lHeight + rHeight + 2`).
-   **Extension 2: Balanced Tree Check**
    -   Check if for every node, `abs(lHeight - rHeight) <= 1`.
-   **Extension 3: N-ary Tree Height**
    -   `1 + max(height(child) for child in children)`.

### Common Mistakes to Avoid

1.  **Base Case Value:**
    -   ❌ Returning `0` for null nodes. This would make a single node height `1`.
    -   ✅ Return `-1` for null nodes if height is edge-based.
2.  **Stack Overflow:**
    -   ❌ Deep recursion on skewed trees (e.g., linked list shape) in languages with small stack limits (Python).
    -   ✅ Use `sys.setrecursionlimit` or iterative approach if N is very large (though N=10^5 usually fits in standard C++/Java stacks).

## Related Concepts

-   **Tree Diameter**
-   **Balanced Binary Tree**
-   **Depth vs Height** (Depth is from root down, Height is from leaf up).
