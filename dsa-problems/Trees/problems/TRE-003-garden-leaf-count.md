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
        // Implement here
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
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def count_leaves(self, n: int, left: List[int], right: List[int]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            val = next(iterator)
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))

        solution = Solution()
        print(solution.count_leaves(n, left, right))
    except StopIteration:
        pass

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
public:
    int countLeaves(int n, const vector<int>& left, const vector<int>& right) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.countLeaves(n, left, right) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countLeaves(n, left, right) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const n = parseInt(tokens[idx++]);
  const left = Array(n).fill(-1);
  const right = Array(n).fill(-1);
  for (let i = 0; i < n; i++) {
    const val = tokens[idx++];
    left[i] = parseInt(tokens[idx++]);
    right[i] = parseInt(tokens[idx++]);
  }

  const solution = new Solution();
  console.log(solution.countLeaves(n, left, right));
});
```
