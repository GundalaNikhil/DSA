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
time_limit: 2000
memory_limit: 256
---
# TRE-015: Shuttle BST Kth Smallest in Range

## Problem Statement

Build a BST by inserting values in the given order. Given a range `[L, R]` and an integer `k`, return the k-th smallest value within the range (1-indexed among in-range values).

If fewer than `k` values fall in the range, output `-1`.

![Problem Illustration](../images/TRE-015/problem-illustration.png)

## Input Format

- First line: integer `n`, number of values to insert
- Second line: `n` integers, the insertion order
- Third line: integers `L` and `R`
- Fourth line: integer `k`

Duplicates, if any, must be inserted into the right subtree.

## Output Format

- Single integer: the k-th smallest value in `[L, R]`, or `-1` if not enough values

## Constraints

- `1 <= n <= 100000`
- Values fit in 64-bit signed integers
- `1 <= k <= n`

## Example

**Input:**

```
5
2 4 5 7 9
4 8
2
```

**Output:**

```
5
```

**Explanation:**

Values in the range `[4, 8]` are `[4, 5, 7]`. The 2nd smallest is 5.

![Example Visualization](../images/TRE-015/example-1.png)

## Notes

- Use inorder traversal and skip values outside the range.
- Stop early once `k` elements are counted.
- If `n=0`, output `-1`.

## Related Topics

BST, Inorder Traversal, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long kthInRange(long[] values, long L, long R, int k) {
        //Implement here
        return 0;
    }
}

class Main {
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
    # //Implement here
    return 0
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
public:
    long long kthInRange(const vector<long long>& values, long long L, long long R, int k) {
        //Implement here
        return 0;
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
  kthInRange(values, L, R, k) {
    //Implement here
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
  for (let i = 0; i < n; i++) values[i] = parseInt(data[idx++], 10);
  const L = parseInt(data[idx++], 10);
  const R = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.kthInRange(values, L, R, k).toString());
});
```
