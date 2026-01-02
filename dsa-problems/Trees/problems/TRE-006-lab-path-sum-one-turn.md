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
        // Implementation here
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
        System.out.println(solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys

def has_one_turn_path(n: int, values: list[int], left: list[int], right: list[int], target: int) -> bool:
    # Implementation here
    return False

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
    target = int(data[idx]) if idx < len(data) else 0
    
    print("true" if has_one_turn_path(n, values, left, right, target) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool hasOneTurnPath(int n, const vector<long long>& values,
                        const vector<int>& left, const vector<int>& right, long long target) {
        // Implementation here
        return {};
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
    long long target;
    cin >> target;

    Solution solution;
    cout << (solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    // Implementation here
    return null;
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
  const target = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false");
});
```
