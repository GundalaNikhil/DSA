---
problem_id: TRE_ROBOTICS_MIRROR_CHECK_COLORS__6729
display_id: TRE-005
slug: robotics-mirror-check-colors
title: "Robotics Mirror Check with Colors"
difficulty: Easy
difficulty_score: 32
topics:
  - Trees
  - Symmetry
  - BFS
tags:
  - trees
  - symmetry
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-005: Robotics Mirror Check with Colors

## Problem Statement

Each node has a value and a color bit (0 or 1). Determine whether the tree is symmetric in both structure and values, and also whether the multiset of colors on each mirrored level matches.

Colors do not need to match node-for-node across the mirror, but the multiset of colors on each level in the left subtree must equal the multiset on the corresponding level in the right subtree.

![Problem Illustration](../images/TRE-005/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value color left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if the tree passes both checks, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers
- `color` is `0` or `1`

## Example

**Input:**

```
7
4 0 1 2
2 1 3 4
2 1 5 6
1 0 -1 -1
3 1 -1 -1
3 1 -1 -1
1 0 -1 -1
```

**Output:**

```
true
```

**Explanation:**

The tree is structurally symmetric with equal values. At each depth, the multiset of colors in the left subtree matches the right subtree.

![Example Visualization](../images/TRE-005/example-1.png)

## Notes

- If the tree is empty, return `true`.
- You must check both structural/value symmetry and color multiset balance.
- BFS by levels or a mirrored DFS can be used.

## Related Topics

Binary Trees, Symmetry, BFS

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean mirrorCheck(int n, int[] values, int[] colors, int[] left, int[] right) {
        return false;
    }
    
    private boolean isSymmetric(int root, int[] values, int[] left, int[] right) {
        return false;
    }
    
    private boolean checkMirror(int u, int v, int[] values, int[] left, int[] right) {
        return false;
    }
    
    private boolean checkColorBalance(int rootLeft, int rootRight, int[] colors, int[] left, int[] right) {
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] colors = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            colors[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

# Increase recursion depth
sys.setrecursionlimit(200000)

def mirror_check(n: int, values: list[int], colors: list[int], left: list[int], right: list[int]) -> bool:
    return False
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    values = [0] * n
    colors = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        colors[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print("true" if mirror_check(n, values, colors, left, right) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
    bool checkMirror(int u, int v, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        return false;
    }

public:
    bool mirrorCheck(int n, const vector<int>& values, const vector<int>& colors,
                     const vector<int>& left, const vector<int>& right) {
        if (n == 0) return true;
        
        if (left[0] == -1 && right[0] == -1) return true;
        if (!checkMirror(left[0], right[0], values, left, right)) return false;
        
        // Color Check
        queue<int> qL, qR;
        qL.push(left[0]);
        qR.push(right[0]);
        
        while (!qL.empty() && !qR.empty()) {
            if (qL.size() != qR.size()) return false;
            
            int size = qL.size();
            long long sumL = 0;
            for (int i = 0; i < size; i++) {
                int u = qL.front(); qL.pop();
                sumL += colors[u];
                if (left[u] != -1) qL.push(left[u]);
                if (right[u] != -1) qL.push(right[u]);
            }
            
            long long sumR = 0;
            for (int i = 0; i < size; i++) {
                int v = qR.front(); qR.pop();
                sumR += colors[v];
                if (left[v] != -1) qR.push(left[v]);
                if (right[v] != -1) qR.push(right[v]);
            }
            
            if (sumL != sumR) return false;
        }
        
        return qL.empty() && qR.empty();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), colors(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> colors[i] >> left[i] >> right[i];
    }

    Solution solution;
    cout << (solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mirrorCheck(n, values, colors, left, right) {
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
  const colors = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    colors[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false");
});
```

