---
problem_id: TRE_HOSTEL_BOUNDARY_WALK_GAPS__3187
display_id: TRE-008
slug: hostel-boundary-walk-gaps
title: "Hostel Boundary Walk with Gaps"
difficulty: Medium
difficulty_score: 44
topics:
  - Trees
  - Boundary Traversal
  - DFS
tags:
  - trees
  - traversal
  - boundary
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-008: Hostel Boundary Walk with Gaps

## Problem Statement

Return the boundary traversal of a binary tree but skip any boundary node whose value is negative. The boundary traversal includes:

1. Root
2. Left boundary (excluding leaves)
3. All leaves (left to right)
4. Right boundary (excluding leaves) in reverse

Preserve order while skipping negative-valued nodes.

![Problem Illustration](../images/TRE-008/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: boundary traversal values separated by spaces
- If the tree is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
-5 3 -1
15 -1 -1
2 -1 -1
```

**Output:**

```
10 2 15
```

**Explanation:**

Boundary nodes are `10`, `-5`, `2`, and `15`. Skipping the negative value `-5` yields `10 2 15`.

![Example Visualization](../images/TRE-008/example-1.png)

## Notes

- Avoid duplicates when root or leaves appear in multiple boundary parts.
- Skipping applies only to boundary nodes, not to traversal structure.
- Use DFS to collect left boundary, leaves, and right boundary.

## Related Topics

Boundary Traversal, DFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> boundaryWithGaps(int n, int[] values, int[] left, int[] right) {
        return null;
    }

    private void addLeaves(int u, int[] values, int[] left, int[] right, List<Integer> result) {
        if (u == -1) return;
        if (left[u] == -1 && right[u] == -1) {
            if (values[u] >= 0) result.add(values[u]);
            return;
        }
        addLeaves(left[u], values, left, right, result);
        addLeaves(right[u], values, left, right, result);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Integer> ans = solution.boundaryWithGaps(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def boundary_with_gaps(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    return []
def main():
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
    ans = boundary_with_gaps(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

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
    void addLeaves(int u, const vector<int>& values, const vector<int>& left, const vector<int>& right, vector<int>& result) {
    }

public:
    vector<int> boundaryWithGaps(int n, const vector<int>& values,
                                 const vector<int>& left, const vector<int>& right) {
        vector<int> result;
        if (n == 0) return result;

        if (values[0] >= 0) result.push_back(values[0]);
        if (left[0] == -1 && right[0] == -1) return result;

        // Left Boundary
        int curr = left[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break;
            if (values[curr] >= 0) result.push_back(values[curr]);
            if (left[curr] != -1) curr = left[curr];
            else curr = right[curr];
        }

        // Leaves
        addLeaves(0, values, left, right, result);

        // Right Boundary
        vector<int> rightBound;
        curr = right[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break;
            if (values[curr] >= 0) rightBound.push_back(values[curr]);
            if (right[curr] != -1) curr = right[curr];
            else curr = left[curr];
        }
        reverse(rightBound.begin(), rightBound.end());
        result.insert(result.end(), rightBound.begin(), rightBound.end());

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.boundaryWithGaps(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  boundaryWithGaps(n, values, left, right) {
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
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const ans = solution.boundaryWithGaps(n, values, left, right);
  console.log(ans.join(" "));
});
```

