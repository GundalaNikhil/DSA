---
problem_id: TRE_SEMINAR_LEVEL_ORDER_ODD__5168
display_id: TRE-004
slug: seminar-level-order-odd
title: "Seminar Level Order Odd-Depth Only"
difficulty: Easy
difficulty_score: 26
topics:
  - Trees
  - BFS
  - Level Order
tags:
  - trees
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-004: Seminar Level Order Odd-Depth Only

## Problem Statement

Return the level-order traversal of a binary tree, but include only nodes at odd depths. The root is at depth 0.

For each odd depth that exists, output the node values in left-to-right order.

![Problem Illustration](../images/TRE-004/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- For each odd depth that has nodes, print one line with the values in left-to-right order
- If there are no odd-depth nodes, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
5 3 -1
12 -1 -1
7 -1 -1
```

**Output:**

```
5 12
```

**Explanation:**

Depth 1 nodes are `5` and `12`. Depth 3 does not exist, so only one line is printed.

![Example Visualization](../images/TRE-004/example-1.png)

## Notes

- Traverse all levels, but only output odd depths.
- Preserve left-to-right order within each level.
- An empty tree produces a single empty line.

## Related Topics

Level Order Traversal, BFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> oddDepthLevels(int n, int[] left, int[] right, int[] values) {
        return null;
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
        List<List<Integer>> levels = solution.oddDepthLevels(n, left, right, values);
        if (levels.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < levels.size(); i++) {
                List<Integer> lvl = levels.get(i);
                for (int j = 0; j < lvl.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(lvl.get(j));
                }
                if (i + 1 < levels.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(200000)
from collections import deque

def odd_depth_levels(n: int, left: list[int], right: list[int], values: list[int]) -> list[list[int]]:
    return []
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    if n == 0:
        print()
        return

    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    levels = odd_depth_levels(n, left, right, values)
    if not levels:
        print()
    else:
        print("\n".join(" ".join(str(x) for x in lvl) for lvl in levels))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<vector<int>> oddDepthLevels(int n, const vector<int>& left,
                                       const vector<int>& right, const vector<int>& values) {
        vector<vector<int>> result;
        if (n == 0) return result;
        
        queue<int> q;
        q.push(0);
        int depth = 0;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> currentLevel;
            bool isOdd = (depth % 2 != 0);
            
            for (int i = 0; i < size; i++) {
                int u = q.front();
                q.pop();
                
                if (isOdd) {
                    currentLevel.push_back(values[u]);
                }
                
                if (left[u] != -1) q.push(left[u]);
                if (right[u] != -1) q.push(right[u]);
            }
            
            if (isOdd) {
                result.push_back(currentLevel);
            }
            depth++;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    if (n == 0) {
        cout << "\n";
        return 0;
    }

    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<vector<int>> levels = solution.oddDepthLevels(n, left, right, values);
    if (levels.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)levels.size(); i++) {
            for (int j = 0; j < (int)levels[i].size(); j++) {
                if (j) cout << ' ';
                cout << levels[i][j];
            }
            if (i + 1 < (int)levels.size()) cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  oddDepthLevels(n, left, right, values) {
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
  
  if (n === 0) {
      console.log("");
      return;
  }
  
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const levels = solution.oddDepthLevels(n, left, right, values);
  if (levels.length === 0) {
    console.log("");
  } else {
    console.log(levels.map((lvl) => lvl.join(" ")).join("\n"));
  }
});
```

