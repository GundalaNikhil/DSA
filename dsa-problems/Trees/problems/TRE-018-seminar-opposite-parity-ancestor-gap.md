---
problem_id: TRE_SEMINAR_OPPOSITE_PARITY_ANCESTOR_GAP__9157
display_id: TRE-018
slug: seminar-opposite-parity-ancestor-gap
title: "Seminar Opposite-Parity Ancestor Gap"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - DFS
  - Prefix Min/Max
tags:
  - trees
  - dfs
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-018: Seminar Opposite-Parity Ancestor Gap

## Problem Statement

For each node, consider only ancestors whose depth parity is different from the node (one even, one odd). Compute the maximum absolute difference between a node's value and any such opposite-parity ancestor value.

Return the maximum difference over all nodes.

![Problem Illustration](../images/TRE-018/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: maximum absolute difference

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
5
8 1 2
3 3 -1
10 -1 4
1 -1 -1
14 -1 -1
```

**Output:**

```
5
```

**Explanation:**

At node `3` (odd depth), the opposite-parity ancestor is `8` (even depth) with difference 5, which is the maximum.

![Example Visualization](../images/TRE-018/example-1.png)

## Notes

- If a node has no opposite-parity ancestors, it contributes nothing.
- Track min and max values for each parity along the root-to-node path.
- An empty tree outputs 0.

## Related Topics

Tree DFS, Parity, Prefix Min/Max

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxOppositeParityGap(int n, int[] values, int[] left, int[] right) {
        // Implement here
        return 0;
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
        System.out.println(solution.maxOppositeParityGap(n, values, left, right));
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
    def max_opposite_parity_gap(self, n: int, values: List[int], left: List[int], right: List[int]) -> int:
        # Implement here
        return 0

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

        solution = Solution()
        print(solution.max_opposite_parity_gap(n, values, left, right))
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
    long long maxOppositeParityGap(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.maxOppositeParityGap(n, values, left, right) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxOppositeParityGap(n, values, left, right) {
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
  const values = [],
    left = [],
    right = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
  }

  const solution = new Solution();
  console.log(solution.maxOppositeParityGap(n, values, left, right).toString());
});
```
