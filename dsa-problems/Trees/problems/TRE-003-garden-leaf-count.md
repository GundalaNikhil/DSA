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
time_limit: 2000
memory_limit: 256
---
# TRE-003: Garden Leaf Count

## Problem Statement

Count the number of leaf nodes in a binary tree. A leaf node has no left or right child.

![Problem Illustration](../images/TRE-003/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: number of leaf nodes

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
3
7 1 2
4 -1 -1
8 -1 -1
```

**Output:**

```
2
```

**Explanation:**

Nodes `4` and `8` have no children, so the leaf count is 2.

![Example Visualization](../images/TRE-003/example-1.png)

## Notes

- An empty tree has 0 leaves.
- A single-node tree has 1 leaf.
- Use DFS or BFS to count nodes with both children absent.

## Related Topics

Binary Trees, DFS, Tree Traversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countLeaves(int n, int[] left, int[] right) {
        return 0;
    }
}

class Main {
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
    return 0
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
        return 0;
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
    return 0;
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

