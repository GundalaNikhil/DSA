---
problem_id: TRE_LAB_PATH_SUM_ONE_TURN__8046
display_id: TRE-006
slug: lab-path-sum-one-turn
title: "Lab Path Sum with Exactly One Turn"
difficulty: Medium
difficulty_score: 52
topics:
  - Trees
  - DFS
  - Prefix Sums
tags:
  - trees
  - dfs
  - path-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-006: Lab Path Sum with Exactly One Turn

## Problem Statement

Given a binary tree and a target sum `T`, determine whether there exists a downward path that starts at any node and moves only left, then only right (exactly one direction change). The path can end at any node and does not need to reach a leaf.

Return `true` if such a path exists, otherwise `false`.

![Problem Illustration](../images/TRE-006/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`
- Last line: integer `T`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if a valid path exists, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- `-10^9 <= value <= 10^9`
- `-10^14 <= T <= 10^14`

## Example

**Input:**

```
5
5 1 2
3 3 4
8 -1 -1
2 -1 -1
1 -1 -1
9
```

**Output:**

```
true
```

**Explanation:**

Path `3 -> 2 -> 1` goes left then right and sums to 6. Another valid path is `5 -> 3 -> 1` which sums to 9, so the answer is true.

![Example Visualization](../images/TRE-006/example-1.png)

## Notes

- The path must move downward and change direction exactly once.
- The path can start at any node, not necessarily the root.
- Use 64-bit integers for sums.

## Related Topics

Tree Paths, DFS, Prefix Sums

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean hasOneTurnPath(int n, long[] values, int[] left, int[] right, long target) {
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
        long target = 0;
        if (sc.hasNextLong()) target = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.hasOneTurnPath(n, values, left, right, target));
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
    def has_one_turn_path(self, n: int, values: List[int], left: List[int], right: List[int], target: int) -> bool:
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

        target = 0
        try:
            target = int(next(iterator))
        except StopIteration:
            pass

        solution = Solution()
        print(str(solution.has_one_turn_path(n, values, left, right, target)).lower())
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
    bool hasOneTurnPath(int n, const vector<long long>& values, const vector<int>& left, const vector<int>& right, long long target) {
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
    long long target = 0;
    cin >> target;

    Solution solution;
    cout << (solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasOneTurnPath(n, values, left, right, target) {
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
  const values = [];
  const left = [];
  const right = [];
  for (let i = 0; i < n; i++) {
    values.push(BigInt(tokens[idx++]));
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
  }
  let target = 0n;
  if (idx < tokens.length) target = BigInt(tokens[idx++]);

  const solution = new Solution();
  console.log(solution.hasOneTurnPath(n, values, left, right, target));
});
```
