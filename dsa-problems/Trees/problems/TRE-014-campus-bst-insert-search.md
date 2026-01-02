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
time_limit: 2000
memory_limit: 256
---
# TRE-014: Campus BST Insert & Search

## Problem Statement

Build a binary search tree (BST) by inserting values in the given order. Then search for a target value.

Output the inorder traversal of the final BST and the result of the search.

![Problem Illustration](../images/TRE-014/problem-illustration.png)

## Input Format

- First line: integer `n`, number of values to insert
- Second line: `n` integers, the insertion order
- Third line: integer `x`, the value to search

Duplicates, if any, must be inserted into the right subtree.

## Output Format

- Line 1: inorder traversal of the BST (space-separated)
- Line 2: `true` if `x` exists in the BST, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Values fit in 32-bit signed integers

## Example

**Input:**

```
5
4 2 6 1 3
5
```

**Output:**

```
1 2 3 4 6
false
```

**Explanation:**

After insertion, the BST inorder traversal is sorted. The value `5` is not present.

![Example Visualization](../images/TRE-014/example-1.png)

## Notes

- If `n=0`, the inorder traversal is empty and search is `false`.
- Inorder traversal of a BST is non-decreasing.
- Insertion uses standard BST rules with duplicates to the right.

## Related Topics

Binary Search Trees, Insertion, Traversal

---

## Solution Template

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
        return null;
    }

    public boolean searchValue(int[] values, int x) {
        return false;
    }

    private TreeNode insert(TreeNode node, int val) {
        return 0;
    }

    private void inorder(TreeNode node, List<Integer> result) {
    }

    private boolean search(TreeNode node, int x) {
        return false;
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
        return 0
def insert(node, val):
    return 0
def get_inorder(node, result):
    return 0
def search(node, x):
    return 0
root = None

def build_inorder(values: list[int]) -> list[int]:
    return []
def search_value(values: list[int], x: int) -> bool:
    return False
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
    }

    bool search(TreeNode* node, int x) {
        return false;
    }

public:
    vector<int> buildInorder(const vector<int>& values) {
        return {};
    }

    bool searchValue(const vector<int>& values, int x) {
        return false;
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
    return 0;
  }

  inorder(node, res) {
    return 0;
  }

  search(node, x) {
    return 0;
  }

  buildInorder(values) {
    return 0;
  }

  searchValue(values, x) {
    return 0;
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

