---
title: Longest Increasing Subarray After Updates
slug: longest-increasing-subarray-updates
difficulty: Medium
difficulty_score: 55
tags:
- Segment Tree
- Range Merge
- Dynamic Updates
problem_id: SEG_LONGEST_INCREASING_SUBARRAY_UPDATES__2654
display_id: SEG-008
topics:
- Segment Tree
- Dynamic Arrays
- Monotonicity
---
# Longest Increasing Subarray After Updates - Editorial

## Problem Summary

You are given an array `a`. You need to handle point updates `SET i x` and after each update, output the length of the longest **strictly increasing contiguous subarray**.

## Real-World Scenario

Imagine a **Stock Market Analysis Tool**.
-   You track the price of a stock over time.
-   A "bull run" is a period where the price strictly increases every day.
-   As historical data is corrected or new data comes in, you want to know the duration of the longest bull run ever recorded in the dataset.

## Problem Exploration

### 1. Contiguous vs. Subsequence
The problem asks for a **subarray** (contiguous), not a subsequence. This simplifies things greatly.
-   Subsequence: LIS problem ($O(N \log N)$). Dynamic LIS is hard.
-   Subarray: Can be solved by checking adjacent elements.

### 2. Segment Tree Approach
We can use a Segment Tree to maintain information about increasing subarrays in each range.
For a range `[L, R]`, what do we need to know to merge it with a neighbor?
-   `maxLen`: The length of the longest increasing subarray fully inside this range.
-   `prefLen`: The length of the increasing subarray starting at `L` and extending into the range.
-   `suffLen`: The length of the increasing subarray ending at `R` and extending backwards.
-   `len`: Total length of the range (constant `R - L + 1`).
-   `leftVal`: Value at `a[L]`.
-   `rightVal`: Value at `a[R]`.

### 3. Merge Logic
When merging left child `left` and right child `right`:
-   **New `maxLen`**: Max of:
    -   `left.maxLen`
    -   `right.maxLen`
    -   If `left.rightVal < right.leftVal`: `left.suffLen + right.prefLen` (crossing boundary).
-   **New `prefLen`**:
    -   `left.prefLen`
    -   If `left.prefLen == left.len` (entire left is increasing) AND `left.rightVal < right.leftVal`: `left.len + right.prefLen`.
-   **New `suffLen`**:
    -   `right.suffLen`
    -   If `right.suffLen == right.len` (entire right is increasing) AND `left.rightVal < right.leftVal`: `right.len + left.suffLen`.
-   **New `leftVal`**: `left.leftVal`.
-   **New `rightVal`**: `right.rightVal`.

## Approaches

### Approach 1: Segment Tree
-   **Build**: $O(N)$.
-   **Update**: $O(\log N)$.
-   **Query**: Root node's `maxLen`.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        int maxLen;
        int prefLen;
        int suffLen;
        int len;
        int leftVal;
        int rightVal;
        
        Node(int val) {
            maxLen = prefLen = suffLen = len = 1;
            leftVal = rightVal = val;
        }
        
        Node() {}
    }
    
    private Node[] tree;
    private int n;

    public int[] process(int[] arr, int[][] updates) {
        n = arr.length;
        tree = new Node[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        int[] results = new int[updates.length];
        for (int i = 0; i < updates.length; i++) {
            int idx = updates[i][0];
            int val = updates[i][1];
            update(0, 0, n - 1, idx, val);
            results[i] = tree[0].maxLen;
        }
        return results;
    }

    private Node merge(Node left, Node right) {
        Node res = new Node();
        res.len = left.len + right.len;
        res.leftVal = left.leftVal;
        res.rightVal = right.rightVal;
        
        res.maxLen = Math.max(left.maxLen, right.maxLen);
        res.prefLen = left.prefLen;
        res.suffLen = right.suffLen;
        
        if (left.rightVal < right.leftVal) {
            res.maxLen = Math.max(res.maxLen, left.suffLen + right.prefLen);
            if (left.prefLen == left.len) {
                res.prefLen = left.len + right.prefLen;
            }
            if (right.suffLen == right.len) {
                res.suffLen = right.len + left.suffLen;
            }
        }
        return res;
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = new Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }
}
```

### Python

```python
import sys

class Node:
    def __init__(self, val=None):
        if val is not None:
            self.max_len = 1
            self.pref_len = 1
            self.suff_len = 1
            self.length = 1
            self.left_val = val
            self.right_val = val
        else:
            self.max_len = 0
            self.pref_len = 0
            self.suff_len = 0
            self.length = 0
            self.left_val = 0
            self.right_val = 0

def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
    n = len(arr)
    tree = [None] * (4 * n)
    
    def merge(left, right):
        res = Node()
        res.length = left.length + right.length
        res.left_val = left.left_val
        res.right_val = right.right_val
        
        res.max_len = max(left.max_len, right.max_len)
        res.pref_len = left.pref_len
        res.suff_len = right.suff_len
        
        if left.right_val < right.left_val:
            res.max_len = max(res.max_len, left.suff_len + right.pref_len)
            if left.pref_len == left.length:
                res.pref_len = left.length + right.pref_len
            if right.suff_len == right.length:
                res.suff_len = right.length + left.suff_len
                
        return res

    def build(node, start, end):
        if start == end:
            tree[node] = Node(arr[start])
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = Node(val)
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

    build(0, 0, n - 1)
    results = []
    
    for idx, val in updates:
        update(0, 0, n - 1, idx, val)
        results.append(tree[0].max_len)
        
    return results
```

### C++

```cpp
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int maxLen;
    int prefLen;
    int suffLen;
    int len;
    int leftVal;
    int rightVal;
    
    Node() : maxLen(0), prefLen(0), suffLen(0), len(0), leftVal(0), rightVal(0) {}
    Node(int val) : maxLen(1), prefLen(1), suffLen(1), len(1), leftVal(val), rightVal(val) {}
};

class Solution {
    vector<Node> tree;
    int n;

    Node merge(const Node& left, const Node& right) {
        Node res;
        res.len = left.len + right.len;
        res.leftVal = left.leftVal;
        res.rightVal = right.rightVal;
        
        res.maxLen = max(left.maxLen, right.maxLen);
        res.prefLen = left.prefLen;
        res.suffLen = right.suffLen;
        
        if (left.rightVal < right.leftVal) {
            res.maxLen = max(res.maxLen, left.suffLen + right.prefLen);
            if (left.prefLen == left.len) {
                res.prefLen = left.len + right.prefLen;
            }
            if (right.suffLen == right.len) {
                res.suffLen = right.len + left.suffLen;
            }
        }
        return res;
    }

    void build(const vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

public:
    vector<int> process(const vector<int>& arr, const vector<pair<int,int>>& updates) {
        n = arr.size();
        tree.resize(4 * n);
        
        build(arr, 0, 0, n - 1);
        
        vector<int> results;
        results.reserve(updates.size());
        for (const auto& up : updates) {
            update(0, 0, n - 1, up.first, up.second);
            results.push_back(tree[0].maxLen);
        }
        return results;
    }
};
```

### JavaScript

```javascript
class Solution {
  process(arr, updates) {
    class Node {
      constructor(val) {
        if (val !== undefined) {
          this.maxLen = 1;
          this.prefLen = 1;
          this.suffLen = 1;
          this.len = 1;
          this.leftVal = val;
          this.rightVal = val;
        } else {
          this.maxLen = 0;
          this.prefLen = 0;
          this.suffLen = 0;
          this.len = 0;
          this.leftVal = 0;
          this.rightVal = 0;
        }
      }
    }

    const n = arr.length;
    const tree = new Array(4 * n);

    const merge = (left, right) => {
      const res = new Node();
      res.len = left.len + right.len;
      res.leftVal = left.leftVal;
      res.rightVal = right.rightVal;
      
      res.maxLen = Math.max(left.maxLen, right.maxLen);
      res.prefLen = left.prefLen;
      res.suffLen = right.suffLen;
      
      if (left.rightVal < right.leftVal) {
        res.maxLen = Math.max(res.maxLen, left.suffLen + right.prefLen);
        if (left.prefLen === left.len) {
          res.prefLen = left.len + right.prefLen;
        }
        if (right.suffLen === right.len) {
          res.suffLen = right.len + left.suffLen;
        }
      }
      return res;
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = new Node(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = new Node(val);
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    build(0, 0, n - 1);
    const results = [];

    for (const [idx, val] of updates) {
      update(0, 0, n - 1, idx, val);
      results.push(tree[0].maxLen);
    }
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`3 1`
`1 2 1`
`SET 2 3`

1.  **Initial**: `[1, 2, 1]`.
    -   Root merges `[1, 2]` and `[1]`.
    -   Left `[1, 2]`: maxLen 2, suffLen 2, rightVal 2.
    -   Right `[1]`: maxLen 1, prefLen 1, leftVal 1.
    -   `2 < 1` is False. No merge across boundary.
    -   Root maxLen = max(2, 1) = 2.
2.  **Update**: `a[2] = 3`. Array `[1, 2, 3]`.
    -   Right leaf `[3]`: maxLen 1, prefLen 1, leftVal 3.
    -   Left child `[1, 2]`: rightVal 2.
    -   `2 < 3` is True.
    -   Merge: `maxLen = max(2, 1, 2+1) = 3`.
3.  **Result**: 3.

## Proof of Correctness

-   **Merge Logic**: Covers all cases:
    1.  Longest subarray is entirely in left child.
    2.  Longest subarray is entirely in right child.
    3.  Longest subarray crosses the midpoint (requires `left.rightVal < right.leftVal`).
-   **Prefix/Suffix**: Correctly maintained to support case 3 for the parent node.

## Interview Extensions

1.  **Longest Non-Decreasing?**
    -   Change `<` to `<=`.
2.  **Number of Increasing Subarrays?**
    -   Different problem. Just sum lengths? No, combinatorial.
3.  **Query Range [L, R]?**
    -   Return `Node` from query function and check `maxLen`.

### Common Mistakes

-   **Empty Range**: Base cases for recursion.
-   **Boundary Check**: `left.rightVal < right.leftVal` is the only condition for merging across boundary.
-   **Prefix/Suffix Update**: Only extend prefix if the *entire* left side is increasing. Similarly for suffix.
