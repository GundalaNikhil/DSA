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
        // Your implementation here
        return false;
    }
}

public class Main {
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
        long G = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.validateBSTGap(n, values, left, right, G) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
def validate_bst_gap(n: int, values: list[int], left: list[int], right: list[int], G: int) -> bool:
    # Your implementation here
    return False

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    G = int(data[idx]) if idx < len(data) else 0
    print("true" if validate_bst_gap(n, values, left, right, G) else "false")

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
    bool validateBSTGap(int n, const vector<long long>& values,
                        const vector<int>& left, const vector<int>& right, long long G) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

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
    cout << (solution.validateBSTGap(n, values, left, right, G) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  validateBSTGap(n, values, left, right, G) {
    // Your implementation here
    return false;
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
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const G = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.validateBSTGap(n, values, left, right, G) ? "true" : "false");
});
```
