---
problem_id: TRE_CAMPUS_BST_INSERT_SEARCH__2824
display_id: TRE-014
slug: campus-bst-insert-search
title: "Campus BST Insert & Search"
difficulty: Easy
difficulty_score: 30
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - insertion
  - easy
premium: true
subscription_tier: basic
---

# TRE-014: Campus BST Insert & Search

## 📋 Problem Summary

You are given a sequence of numbers.
1.  **Build a Binary Search Tree (BST)** by inserting these numbers one by one in the given order.
2.  **Search** for a specific target value `x` in the constructed BST.
3.  Output the **Inorder Traversal** of the tree (which should be sorted) and the result of the search (`true` or `false`).

## 🌍 Real-World Scenario

**Scenario Title:** Library Book Cataloging

Imagine a librarian receiving a shipment of new books.
-   **Insertion:** As each book arrives, the librarian places it on the shelf. If the book's ID is smaller than the current one, they go left; if larger, they go right. This builds a structured organization (BST).
-   **Search:** A student asks for a specific book ID. The librarian uses the structure to quickly find it or confirm it's missing.
-   **Inorder:** Reading the shelf from left to right lists all book IDs in sorted order.

![Real-World Application](../images/TRE-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Input:** `4, 2, 6, 1, 3`

1.  **Insert 4:** Root is 4.
2.  **Insert 2:** 2 < 4. Left child of 4.
3.  **Insert 6:** 6 > 4. Right child of 4.
4.  **Insert 1:** 1 < 4 -> 1 < 2. Left child of 2.
5.  **Insert 3:** 3 < 4 -> 3 > 2. Right child of 2.

**Tree:**
```
      4
     / \
    2   6
   / \
  1   3
```

**Inorder:** `1 2 3 4 6` (Sorted).

**Search 5:**
-   5 > 4 (Go Right).
-   5 < 6 (Go Left).
-   Left of 6 is null. **Not Found**.

### Algorithm Steps

1.  **Node Class:** Define a simple `TreeNode` with `val`, `left`, `right`.
2.  **Insertion:**
    -   Start at root.
    -   If value < current.val, go left. If left is null, insert here.
    -   If value >= current.val, go right. If right is null, insert here. (Problem says duplicates to right).
3.  **Search:**
    -   Start at root.
    -   If current is null, return `false`.
    -   If val == target, return `true`.
    -   If target < val, recurse left.
    -   If target > val, recurse right.
4.  **Inorder:**
    -   Recurse left -> Visit node -> Recurse right.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Duplicates:** Problem statement says "Duplicates, if any, must be inserted into the right subtree." This implies `val >= node.val` goes right.
-   **Empty Input:** If `n=0`, output empty line and `false`.
-   **Output Format:** Space-separated integers for inorder.

## Naive Approach

### Intuition

Since the problem asks to simulate BST insertion, the "naive" approach is simply the standard iterative or recursive insertion. There isn't really a "worse" way unless you sort the array first (which changes the tree structure) or use an unbalanced structure when a balanced one isn't asked for.

### Time Complexity

-   **Insertion:** O(N) worst case (skewed tree), O(log N) average. Total for N nodes: O(N^2) worst case.
-   **Search:** O(N) worst case.

## Optimal Approach (Standard BST Operations)

We implement the standard recursive or iterative BST logic. Since the problem requires the specific tree structure resulting from the insertion order, we **cannot** balance the tree (e.g., AVL/Red-Black) as that would change the structure.

### Algorithm

1.  `root = null`.
2.  For each value `v`: `root = insert(root, v)`.
3.  `inorder(root)` -> print.
4.  `found = search(root, x)` -> print.

### Time Complexity

-   **O(N^2)** worst case (if input is sorted).
-   **O(N log N)** average case.

### Space Complexity

-   **O(N)** to store nodes.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    private TreeNode root;

    public List<Integer> buildInorder(int[] values) {
        root = null;
        for (int v : values) {
            root = insert(root, v);
        }
        List<Integer> result = new ArrayList<>();
        inorder(root, result);
        return result;
    }

    public boolean searchValue(int[] values, int x) {
        // Note: We reuse the root built in buildInorder if called sequentially,
        // but for safety/independence, we can rebuild or assume state.
        // The template implies independent calls or stateful object.
        // Let's assume buildInorder is called first or we rebuild.
        // Given the template structure, it's safer to rebuild if root is null.
        if (root == null && values.length > 0) {
            buildInorder(values);
        }
        return search(root, x);
    }

    private TreeNode insert(TreeNode node, int val) {
        if (node == null) return new TreeNode(val);
        if (val < node.val) {
            node.left = insert(node.left, val);
        } else {
            // Duplicates to the right
            node.right = insert(node.right, val);
        }
        return node;
    }

    private void inorder(TreeNode node, List<Integer> result) {
        if (node == null) return;
        inorder(node.left, result);
        result.add(node.val);
        inorder(node.right, result);
    }

    private boolean search(TreeNode node, int x) {
        if (node == null) return false;
        if (node.val == x) return true;
        if (x < node.val) return search(node.left, x);
        return search(node.right, x);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextInt();
        int x = 0;
        if (sc.hasNextInt()) x = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> inorder = solution.buildInorder(values);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < inorder.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(inorder.get(i));
        }
        System.out.println(sb.toString());
        System.out.println(solution.searchValue(values, x) ? "true" : "false");
        sc.close();
    }
}
```

### Python
```python
import sys

# Increase recursion depth just in case
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

def get_inorder(node, result):
    if node is None:
        return
    get_inorder(node.left, result)
    result.append(node.val)
    get_inorder(node.right, result)

def search(node, x):
    if node is None:
        return False
    if node.val == x:
        return True
    if x < node.val:
        return search(node.left, x)
    return search(node.right, x)

# Global root for simplicity in functional style
root = None

def build_inorder(values: list[int]) -> list[int]:
    global root
    root = None
    for v in values:
        root = insert(root, v)
    result = []
    get_inorder(root, result)
    return result

def search_value(values: list[int], x: int) -> bool:
    global root
    # If root is not built (e.g. direct call), rebuild
    if root is None and values:
        for v in values:
            root = insert(root, v)
    return search(root, x)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [int(data[idx + i]) for i in range(n)]
    idx += n
    x = int(data[idx]) if idx < len(data) else 0
    
    inorder = build_inorder(values)
    print(" ".join(str(v) for v in inorder))
    print("true" if search_value(values, x) else "false")

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    TreeNode* root = nullptr;

    TreeNode* insert(TreeNode* node, int val) {
        if (!node) return new TreeNode(val);
        if (val < node->val) {
            node->left = insert(node->left, val);
        } else {
            node->right = insert(node->right, val);
        }
        return node;
    }

    void inorder(TreeNode* node, vector<int>& res) {
        if (!node) return;
        inorder(node->left, res);
        res.push_back(node->val);
        inorder(node->right, res);
    }

    bool search(TreeNode* node, int x) {
        if (!node) return false;
        if (node->val == x) return true;
        if (x < node->val) return search(node->left, x);
        return search(node->right, x);
    }

public:
    vector<int> buildInorder(const vector<int>& values) {
        root = nullptr; // Reset for fresh build
        for (int v : values) {
            root = insert(root, v);
        }
        vector<int> res;
        inorder(root, res);
        return res;
    }

    bool searchValue(const vector<int>& values, int x) {
        if (!root && !values.empty()) buildInorder(values);
        return search(root, x);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    int x;
    cin >> x;

    Solution solution;
    vector<int> inorder = solution.buildInorder(values);
    for (int i = 0; i < (int)inorder.size(); i++) {
        if (i) cout << ' ';
        cout << inorder[i];
    }
    cout << "\n" << (solution.searchValue(values, x) ? "true" : "false") << "\n";
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
  constructor() {
    this.root = null;
  }

  insert(node, val) {
    if (!node) return new TreeNode(val);
    if (val < node.val) {
      node.left = this.insert(node.left, val);
    } else {
      node.right = this.insert(node.right, val);
    }
    return node;
  }

  inorder(node, res) {
    if (!node) return;
    this.inorder(node.left, res);
    res.push(node.val);
    this.inorder(node.right, res);
  }

  search(node, x) {
    if (!node) return false;
    if (node.val === x) return true;
    if (x < node.val) return this.search(node.left, x);
    return this.search(node.right, x);
  }

  buildInorder(values) {
    this.root = null;
    for (const v of values) {
      this.root = this.insert(this.root, v);
    }
    const res = [];
    this.inorder(this.root, res);
    return res;
  }

  searchValue(values, x) {
    if (!this.root && values.length > 0) {
      this.buildInorder(values);
    }
    return this.search(this.root, x);
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
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
  }
  const x = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const inorder = solution.buildInorder(values);
  console.log(inorder.join(" "));
  console.log(solution.searchValue(values, x) ? "true" : "false");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
4 2 6 1 3
5
```

**Insertion:**
1.  **4**: Root.
2.  **2**: Left of 4.
3.  **6**: Right of 4.
4.  **1**: Left of 2.
5.  **3**: Right of 2.

**Inorder Traversal:**
-   Left of 4 -> (Left of 2 -> 1, Node 2, Right of 2 -> 3) -> `1 2 3`
-   Node 4
-   Right of 4 -> (6)
-   Result: `1 2 3 4 6`

**Search 5:**
-   Start 4. 5 > 4 -> Right.
-   Curr 6. 5 < 6 -> Left.
-   Left of 6 is null. Return `false`.

## ✅ Proof of Correctness

The algorithm directly implements the definition of BST insertion and search.
-   **Insertion:** Maintains the invariant `left < node <= right` at every step.
-   **Inorder:** By definition, inorder traversal of a BST yields sorted values.
-   **Search:** Uses the BST property to eliminate half the search space (ideally) at each step, guaranteeing correctness if the element exists.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Delete Node**
    -   Implement deletion (handling 0, 1, 2 children).
-   **Extension 2: Balance Tree**
    -   Convert the BST to a balanced AVL/Red-Black tree.
-   **Extension 3: LCA in BST**
    -   Find LCA (much easier in BST than generic tree).

### Common Mistakes to Avoid

1.  **Duplicate Handling:**
    -   ❌ Ignoring duplicates or putting them left.
    -   ✅ Problem specifies duplicates go to the right.
2.  **State Management:**
    -   ❌ Forgetting to reset root between test cases (if static).
3.  **Recursion Depth:**
    -   ❌ Stack overflow on sorted input (skewed tree) for large N. Iterative approach avoids this.

## Related Concepts

-   **BST Properties**
-   **Recursion vs Iteration**
-   **Tree Traversal**
