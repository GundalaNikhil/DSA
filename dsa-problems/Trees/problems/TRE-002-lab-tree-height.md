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
        // Your implementation here
        return 0;
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
        System.out.println(solution.treeHeight(n, left, right));
        sc.close();
    }
}
```

### Python

```python
def tree_height(n: int, left: list[int], right: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
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
    print(tree_height(n, left, right))

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
    int treeHeight(int n, const vector<int>& left, const vector<int>& right) {
        // Your implementation here
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
    cout << solution.treeHeight(n, left, right) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  treeHeight(n, left, right) {
    // Your implementation here
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
