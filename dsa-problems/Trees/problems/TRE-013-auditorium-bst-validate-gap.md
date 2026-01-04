---
problem_id: TRE_AUDITORIUM_BST_VALIDATE_GAP__6370
display_id: TRE-013
slug: auditorium-bst-validate-gap
title: "Auditorium BST Validate with Gap"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - BST
  - Validation
tags:
  - trees
  - bst
  - validation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-013: Auditorium BST Validate with Gap

## Problem Statement

Validate that a binary tree is a binary search tree (BST) and that every parent-child edge also satisfies a strict gap rule:

`|parent.value - child.value| >= G`

Return `true` if both conditions hold, otherwise `false`.

![Problem Illustration](../images/TRE-013/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`
- Last line: integer `G`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if the tree is a valid BST with the gap rule, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Node values fit in 64-bit signed integers
- `0 <= G <= 10^12`

## Example

**Input:**

```
3
5 1 2
1 -1 -1
7 -1 -1
2
```

**Output:**

```
true
```

**Explanation:**

The tree is a BST, and both edges have gaps at least 2.

![Example Visualization](../images/TRE-013/example-1.png)

## Notes

- The BST property uses strict ordering (`left < node < right`).
- Gap rule applies only to parent-child edges.
- Use DFS with min/max bounds for validation.

## Related Topics

Binary Search Trees, Validation, DFS

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean validateBSTGap(int n, long[] values, int[] left, int[] right, long G) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long G = sc.hasNextLong() ? sc.nextLong() : 0;

        Solution solution = new Solution();
        System.out.println(solution.validateBSTGap(n, values, left, right, G));
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
    def validate_bst_gap(self, n: int, values: List[int], left: List[int], right: List[int], G: int) -> bool:
        # Implement here
        return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [0] * n
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            values[i] = int(next(iterator))
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))

        G = 0
        try:
            G = int(next(iterator))
        except StopIteration:
            pass

        solution = Solution()
        print(str(solution.validate_bst_gap(n, values, left, right, G)).lower())
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
    bool validateBSTGap(int n, const vector<long long>& values, const vector<int>& left, const vector<int>& right, long long G) {
        // Implement here
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }
    long long G;
    cin >> G;

    Solution solution;
    cout << (solution.validateBSTGap(n, values, left, right, G) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  validateBSTGap(n, values, left, right, G) {
    // Implement here
    return false;
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
  const values = [],
    left = [],
    right = [];
  for (let i = 0; i < n; i++) {
    values.push(BigInt(tokens[idx++]));
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
  }
  let G = 0n;
  if (idx < tokens.length) G = BigInt(tokens[idx++]);

  const solution = new Solution();
  console.log(solution.validateBSTGap(n, values, left, right, G));
});
```
