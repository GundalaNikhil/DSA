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
    boolean found = false;

    public boolean hasOneTurnPath(int n, long[] values, int[] left, int[] right, long target) {
        return false;
    }

    // isStart: true if 'u' is the start of a new Left-chain (root or right child)
    private void dfs(int u, long currentLeftSum, Set<Long> prefixes, 
                     long[] values, int[] left, int[] right, long target, boolean isStart) {
        if (u == -1 || found) return;

        long val = values[u];
        long nextSum = currentLeftSum + val;

        // If we are not the start, we have incoming Left edges. We can Turn Right.
        if (!isStart) {
            checkRightChain(right[u], val, nextSum, prefixes, values, left, right, target);
        }

        // Add current prefix to set for children
        prefixes.add(currentLeftSum);

        // 1. Continue Left
        dfs(left[u], nextSum, prefixes, values, left, right, target, false);

        // Backtrack for this chain
        prefixes.remove(currentLeftSum);

        // 2. Go Right (Starts a NEW Left-chain logic for the subtree)
        // We pass a NEW empty set because the Left-chain breaks here.
        dfs(right[u], 0, new HashSet<>(), values, left, right, target, true);
    }

    private void checkRightChain(int u, long turnVal, long turnLeftSum, Set<Long> prefixes,
                                 long[] values, int[] left, int[] right, long target) {
        long currentRightSum = 0;
        int curr = u;
        while (curr != -1 && !found) {
            currentRightSum += values[curr];
            // Total = SuffixLeft + RightChainSum
            // SuffixLeft = turnLeftSum - somePrefix
            // Total = (turnLeftSum - somePrefix) + currentRightSum = T
            // somePrefix = turnLeftSum + currentRightSum - T
            long neededPrefix = turnLeftSum + currentRightSum - target;
            if (prefixes.contains(neededPrefix)) {
                found = true;
                return;
            }
            curr = right[curr];
        }
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

# Increase recursion depth
sys.setrecursionlimit(200000)

def has_one_turn_path(n: int, values: list[int], left: list[int], right: list[int], target: int) -> bool:
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
    bool found = false;

    void checkRightChain(int u, long long turnLeftSum, const unordered_set<long long>& prefixes,
                         const vector<long long>& values, const vector<int>& right, long long target) {
        long long currentRightSum = 0;
        int curr = u;
        while (curr != -1 && !found) {
            currentRightSum += values[curr];
            long long needed = turnLeftSum + currentRightSum - target;
            if (prefixes.count(needed)) {
                found = true;
                return;
            }
            curr = right[curr];
        }
    }

    void dfs(int u, long long currentLeftSum, unordered_set<long long>& prefixes,
             const vector<long long>& values, const vector<int>& left, const vector<int>& right,
             long long target, bool isStart) {
        if (u == -1 || found) return;

        long long val = values[u];
        long long nextSum = currentLeftSum + val;

        if (!isStart) {
            checkRightChain(right[u], nextSum, prefixes, values, right, target);
        }
        if (found) return;

        prefixes.insert(currentLeftSum);
        dfs(left[u], nextSum, prefixes, values, left, right, target, false);
        prefixes.erase(currentLeftSum);

        if (found) return;

        // Start new chain for right child
        unordered_set<long long> newPrefixes;
        dfs(right[u], 0, newPrefixes, values, left, right, target, true);
    }

public:
    bool hasOneTurnPath(int n, const vector<long long>& values,
                        const vector<int>& left, const vector<int>& right, long long target) {
        if (n == 0) return false;
        found = false;
        unordered_set<long long> prefixes;
        dfs(0, 0, prefixes, values, left, right, target, true);
        return found;
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
    this.found = false;
  }

  hasOneTurnPath(n, values, left, right, target) {
    return 0;
  }

  dfs(u, currentLeftSum, prefixes, values, left, right, target, isStart) {
    return 0;
  }

  checkRightChain(u, turnLeftSum, prefixes, values, right, target) {
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
  const target = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false");
});
```

