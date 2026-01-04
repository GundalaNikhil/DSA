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
time_limit: 2000
memory_limit: 256
---

# TRE-002: Lab Tree Height

## Problem Statement

Compute the height of a binary tree. The height is defined as the number of edges on the longest path from the root to any leaf.

If the tree is empty, output `-1`.

![Problem Illustration](../images/TRE-002/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: height of the tree

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
5 1 2
3 3 -1
9 -1 -1
1 -1 -1
```

**Output:**

```
2
```

**Explanation:**

The longest root-to-leaf path is `5 -> 3 -> 1`, which has 2 edges.

![Example Visualization](../images/TRE-002/example-1.png)

## Notes

- Height is measured in edges, not nodes.
- Return `-1` for an empty tree.
- A single-node tree has height 0.

## Related Topics

Binary Trees, DFS, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int treeHeight(int n, int[] left, int[] right) {
        // Implement here
        return -1;
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
            int val = sc.nextInt(); // val is unused
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
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def tree_height(self, n: int, left: List[int], right: List[int]) -> int:
        # Implement here
        return -1

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
            val = next(iterator) # unused
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))

        solution = Solution()
        print(solution.tree_height(n, left, right))
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
    int treeHeight(int n, const vector<int>& left, const vector<int>& right) {
        // Implement here
        return -1;
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
    cout << solution.treeHeight(n, left, right) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  treeHeight(n, left, right) {
    // Implement here
    return -1;
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
    const val = tokens[idx++]; // unused
    left[i] = parseInt(tokens[idx++]);
    right[i] = parseInt(tokens[idx++]);
  }

  const solution = new Solution();
  console.log(solution.treeHeight(n, left, right));
});
```
