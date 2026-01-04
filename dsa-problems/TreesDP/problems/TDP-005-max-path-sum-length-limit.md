---
title: Max Path Sum with Length Limit
problem_id: TDP_MAX_PATH_SUM_LENGTH_LIMIT__6382
display_id: TDP-005
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Path Algorithms
  - Constrained Optimization
categories:
  - Algorithms
  - Data Structures
slug: max-path-sum-length-limit
---

# Max Path Sum with Length Limit

## Problem Description

You are given a tree with `n` nodes where each node has a value (possibly negative). Find the maximum path sum where the path uses **at most `L` edges**.

A path is a sequence of distinct nodes where consecutive nodes are connected by an edge. The path sum is the sum of all node values in the path.

## Input Format

- First line: two integers `n` and `L` (number of nodes and maximum path length in edges)
- Second line: `n` space-separated integers representing node values `value[1], value[2], ..., value[n]`
- Next `n-1` lines: each contains two integers `u v` representing an edge between nodes `u` and `v`

## Output Format

- Single integer: the maximum path sum using at most `L` edges

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= L <= n-1`
- `-10^9 <= value[i] <= 10^9`
- The graph forms a valid tree

## Example 1

**Input:**

```
3 2
1 -2 3
1 2
1 3
```

**Output:**

```
4
```

**Explanation:**
Tree structure:

```
    1 (val=1)
   / \
  2   3
(val=-2) (val=3)
```

Possible paths with at most 2 edges:

- Single nodes: 1, -2, 3 → max = 3
- Path 1-2: 1 + (-2) = -1
- Path 1-3: 1 + 3 = 4 ✓ (maximum)
- Path 2-1-3: -2 + 1 + 3 = 2 (uses 2 edges)

Maximum sum is 4 (path from node 1 to node 3).

## Example 2

**Input:**

```
5 3
10 -5 20 -10 30
1 2
1 3
2 4
2 5
```

**Output:**

```
45
```

**Explanation:**
Tree structure:

```
      1(10)
     / \
  2(-5) 3(20)
   / \
4(-10) 5(30)
```

Best path with at most 3 edges:

Possible paths:

- Just node 5: 30
- Path 1-3: 10 + 20 = 30
- Path 5-2-1: 30 + (-5) + 10 = 35
- Path 5-2-1-3: 30 + (-5) + 10 + 20 = 55 (uses 3 edges) ✓

Maximum is 55 (path from node 5 through nodes 2, 1, to node 3).

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxPathSum(int n, int L, long[] values, int[][] edges) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int L = sc.nextInt();

        long[] values = new long[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextLong();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxPathSum(n, L, values, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def max_path_sum(self, n: int, L: int, values: List[int], edges: List[List[int]]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        L = int(next(iterator))

        values = []
        for _ in range(n):
            values.append(int(next(iterator)))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        print(solution.max_path_sum(n, L, values, edges))
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
    long long maxPathSum(int n, int L, const vector<long long>& values, const vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, L;
    if (!(cin >> n >> L)) return 0;

    vector<long long> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    cout << solution.maxPathSum(n, L, values, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxPathSum(n, L, values, edges) {
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
  const L = parseInt(tokens[idx++]);

  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
  }

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxPathSum(n, L, values, edges));
});
```

## Notes

- Path length is measured in edges, not nodes
- Values can be negative - don't prematurely optimize by ignoring negative paths
- A single node is a valid path (0 edges)
- Use long/long long to avoid overflow
- DP state: dp[node][length] = max sum using exactly 'length' edges from this node downward
