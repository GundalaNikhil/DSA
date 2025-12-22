---
problem_id: TRE_SHUTTLE_BST_KTH_SMALLEST_RANGE__4916
display_id: TRE-015
slug: shuttle-bst-kth-smallest-range
title: "Shuttle BST Kth Smallest in Range"
difficulty: Medium
difficulty_score: 52
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - kth-smallest
  - medium
premium: true
subscription_tier: basic
---

# TRE-015: Shuttle BST Kth Smallest in Range

## 📋 Problem Summary

1.  **Build a BST** from a given sequence of numbers.
2.  Consider only the values that fall within the inclusive range `[L, R]`.
3.  Find the **k-th smallest** value among these filtered numbers.
4.  If there are fewer than `k` numbers in the range, return `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** Shuttle Bus Scheduling

Imagine a shuttle service with buses departing at various times (represented by BST nodes).
-   **Range [L, R]:** A passenger can only catch a bus between 8:00 AM (`L`) and 10:00 AM (`R`).
-   **k-th Smallest:** The passenger wants to catch the `k`-th available bus in that window (e.g., the 2nd bus, to grab coffee before the first one leaves).
-   **Goal:** Find the departure time of that specific bus.

![Real-World Application](../images/TRE-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Input:** `2, 4, 5, 7, 9`. Range `[4, 8]`. `k=2`.

**Tree:**
```
      2
       \
        4
         \
          5
           \
            7
             \
              9
```
**Inorder Traversal:** `2, 4, 5, 7, 9`

**Filtering [4, 8]:**
-   2 < 4 (Skip)
-   4 (Keep, count=1)
-   5 (Keep, count=2) -> **Target Found!**
-   7 (Keep)
-   9 > 8 (Skip)

**Result:** 5.

### Algorithm Steps

1.  **Build BST:** Insert elements sequentially.
2.  **Inorder Traversal:** Traverse the tree (Left -> Node -> Right).
3.  **Filter & Count:**
    -   If `node.val < L`: Ignore, but right subtree might have valid nodes.
    -   If `node.val > R`: Ignore, and right subtree definitely has invalid nodes (pruning optimization).
    -   If `L <= node.val <= R`: Increment counter. If counter equals `k`, return `node.val`.
4.  **Result:** If traversal finishes without count reaching `k`, return `-1`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Duplicates:** Problem says duplicates go right. They are valid values.
-   **Pruning:**
    -   If `node.val < L`, left subtree is all `< L`, so skip left. Go right.
    -   If `node.val > R`, right subtree is all `> R`, so skip right. Go left.
    -   This optimizes the search to `O(h + k)`.

## Naive Approach

### Intuition

Store all nodes in a list, sort them (or just use the BST property), filter the list, and pick the k-th element.

### Algorithm

1.  Build BST.
2.  Get full inorder list.
3.  Filter list for `x` where `L <= x <= R`.
4.  If `len(filtered) >= k`, return `filtered[k-1]`. Else `-1`.

### Time Complexity

-   **O(N)**: Visit all nodes.

## Optimal Approach (Pruned Inorder)

We can optimize the traversal by pruning subtrees that can't possibly contain values in `[L, R]`.

### Algorithm

1.  `count = 0`, `result = -1`.
2.  `dfs(node)`:
    -   If `node` is null or `result` found, return.
    -   If `node.val > L`: `dfs(node.left)` (Only go left if current is not too small).
    -   If `L <= node.val <= R`:
        -   `count++`
        -   If `count == k`: `result = node.val`, return.
    -   If `node.val < R`: `dfs(node.right)` (Only go right if current is not too large).

### Time Complexity

-   **O(N)** worst case, but effectively visits only relevant nodes.

### Space Complexity

-   **O(H)**: Recursion stack.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class TreeNode {
        long val;
        TreeNode left, right;
        TreeNode(long val) { this.val = val; }
    }

    private int count;
    private long result;

    public long kthInRange(long[] values, long L, long R, int k) {
        TreeNode root = null;
        for (long v : values) {
            root = insert(root, v);
        }

        count = 0;
        result = -1;
        inorder(root, L, R, k);
        return result;
    }

    private TreeNode insert(TreeNode node, long val) {
        if (node == null) return new TreeNode(val);
        if (val < node.val) {
            node.left = insert(node.left, val);
        } else {
            node.right = insert(node.right, val);
        }
        return node;
    }

    private void inorder(TreeNode node, long L, long R, int k) {
        if (node == null || result != -1) return;

        // Pruning: if node.val < L, left subtree is useless (all < L)
        // Correct logic: Visit left if it COULD contain values >= L.
        // Left child values are < node.val.
        // If node.val <= L, then left child < L. Useless.
        // So visit left only if node.val > L.
        
        if (node.val > L) {
            inorder(node.left, L, R, k);
        }

        if (result != -1) return; // Check again after returning from left

        if (node.val >= L && node.val <= R) {
            count++;
            if (count == k) {
                result = node.val;
                return;
            }
        }

        // Pruning: Visit right only if node.val < R.
        // If node.val >= R, right child > R. Useless.
        if (node.val < R) {
            inorder(node.right, L, R, k);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextLong();
        long L = 0, R = 0;
        if (sc.hasNextLong()) L = sc.nextLong();
        if (sc.hasNextLong()) R = sc.nextLong();
        int k = 0;
        if (sc.hasNextInt()) k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.kthInRange(values, L, R, k));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, val):
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def kth_in_range(values: list[int], L: int, R: int, k: int) -> int:
    root = None
    for v in values:
        root = insert(root, v)
        
    count = 0
    result = -1
    
    def inorder(node):
        nonlocal count, result
        if node is None or result != -1:
            return
            
        # Visit left if potentially valid
        if node.val > L:
            inorder(node.left)
            
        if result != -1: return
        
        if L <= node.val <= R:
            count += 1
            if count == k:
                result = node.val
                return
                
        # Visit right if potentially valid
        if node.val < R:
            inorder(node.right)

    inorder(root)
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [int(data[idx + i]) for i in range(n)]
    idx += n
    L = int(data[idx]); idx += 1
    R = int(data[idx]); idx += 1
    k = int(data[idx]) if idx < len(data) else 1
    
    print(kth_in_range(values, L, R, k))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    long long val;
    TreeNode *left, *right;
    TreeNode(long long x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    TreeNode* insert(TreeNode* node, long long val) {
        if (!node) return new TreeNode(val);
        if (val < node->val) {
            node->left = insert(node->left, val);
        } else {
            node->right = insert(node->right, val);
        }
        return node;
    }

    int count;
    long long result;

    void inorder(TreeNode* node, long long L, long long R, int k) {
        if (!node || result != -1) return;

        if (node->val > L) {
            inorder(node->left, L, R, k);
        }

        if (result != -1) return;

        if (node->val >= L && node->val <= R) {
            count++;
            if (count == k) {
                result = node->val;
                return;
            }
        }

        if (node->val < R) {
            inorder(node->right, L, R, k);
        }
    }

public:
    long long kthInRange(const vector<long long>& values, long long L, long long R, int k) {
        TreeNode* root = nullptr;
        for (long long v : values) {
            root = insert(root, v);
        }

        count = 0;
        result = -1;
        inorder(root, L, R, k);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    long long L, R;
    cin >> L >> R;
    int k;
    cin >> k;

    Solution solution;
    cout << solution.kthInRange(values, L, R, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class Solution {
  insert(node, val) {
    if (!node) return new TreeNode(val);
    if (val < node.val) {
      node.left = this.insert(node.left, val);
    } else {
      node.right = this.insert(node.right, val);
    }
    return node;
  }

  kthInRange(values, L, R, k) {
    let root = null;
    for (const v of values) {
      root = this.insert(root, v);
    }

    let count = 0;
    let result = -1;
    const lVal = BigInt(L);
    const rVal = BigInt(R);

    const inorder = (node) => {
      if (!node || result !== -1) return;

      const val = BigInt(node.val);

      if (val > lVal) {
        inorder(node.left);
      }

      if (result !== -1) return;

      if (val >= lVal && val <= rVal) {
        count++;
        if (count === k) {
          result = node.val;
          return;
        }
      }

      if (val < rVal) {
        inorder(node.right);
      }
    };

    inorder(root);
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  for (let i = 0; i < n; i++) values[i] = parseInt(data[idx++], 10);
  const L = parseInt(data[idx++], 10);
  const R = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.kthInRange(values, L, R, k).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
2 4 5 7 9
4 8
2
```
**Tree:** `2 -> R:4 -> R:5 -> R:7 -> R:9` (Skewed right)
**Range:** `[4, 8]`
**k:** 2

**Traversal:**
1.  Root 2. `2 < 4`. Don't go left. Go right.
2.  Node 4. `4 >= 4`. Go left (null).
3.  Process 4. In range? Yes. `count=1`.
4.  `4 < 8`. Go right.
5.  Node 5. `5 >= 4`. Go left (null).
6.  Process 5. In range? Yes. `count=2`.
7.  `count == k`. **Found 5**. Return.

**Result:** 5.

## ✅ Proof of Correctness

Inorder traversal visits nodes in ascending order.
-   By filtering `L <= val <= R`, we only count nodes in the range.
-   Since we visit them in ascending order, the `k`-th node we count is the `k`-th smallest in that range.
-   Pruning logic (`val > L` to go left, `val < R` to go right) ensures we don't visit subtrees that are strictly outside the range, optimizing performance while maintaining correctness.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Reverse Order**
    -   Find k-th *largest* in range (Reverse Inorder).
-   **Extension 2: Sum in Range**
    -   Calculate sum of all nodes in `[L, R]` (LeetCode 938).
-   **Extension 3: Count in Range**
    -   Count how many nodes are in `[L, R]`.

### C++ommon Mistakes to Avoid

1.  **Pruning Logic:**
    -   ❌ `if (val < L) return;` (Wrong, right child could be valid).
    -   ✅ Only skip the *specific* child direction that is invalid.
2.  **K-th Logic:**
    -   ❌ Counting all nodes then checking index.
    -   ✅ Increment count only for valid nodes.

## Related Concepts

-   **BST Range Sum**
-   **Inorder Traversal**
-   **Pruning**
