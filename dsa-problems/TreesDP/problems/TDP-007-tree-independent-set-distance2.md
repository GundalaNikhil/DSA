---
title: Distance-2 Independent Set on Tree
problem_id: TDP_DISTANCE2_INDEPENDENT_SET__8395
display_id: TDP-007
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Independent Set
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: tree-independent-set-distance2
---

# Distance-2 Independent Set on Tree

## Problem Description

Given a tree with `n` nodes where each node `i` has a weight `w[i]`, find the maximum total weight of a subset of nodes such that any two chosen nodes are at distance **at least 3**.

Two nodes are at distance at least 3 if they are not adjacent AND do not share a common neighbor.

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `w[1], w[2], ..., w[n]`
- Next `n-1` lines: edges `u v`

## Output Format

- Single integer: maximum total weight

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= w[i] <= 10^9`

## Example 1

**Input:**

```
3
1 2 3
1 2
1 3
```

**Output:**

```
3
```

**Explanation:** Can only pick node 3 (or any single node). Nodes 2 and 3 share neighbor 1, so can't pick both.

## Example 2

**Input:**

```
5
10 20 30 40 50
1 2
2 3
3 4
4 5
```

**Output:**

```
60
```

**Explanation:** Pick nodes 1 and 4 (or 2 and 5): 10+50=60 or 20+40=60.

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxIndependentSet(int n, long[] weights, int[][] edges) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        long[] weights = new long[n];
        for (int i = 0; i < n; i++) {
            weights[i] = sc.nextLong();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxIndependentSet(n, weights, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def max_independent_set(self, n: int, weights: List[int], edges: List[List[int]]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))

        weights = []
        for _ in range(n):
            weights.append(int(next(iterator)))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        print(solution.max_independent_set(n, weights, edges))
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
    long long maxIndependentSet(int n, const vector<long long>& weights, const vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;

    vector<long long> weights(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    cout << solution.maxIndependentSet(n, weights, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxIndependentSet(n, weights, edges) {
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

  const weights = [];
  for (let i = 0; i < n; i++) {
    weights.push(parseInt(tokens[idx++]));
  }

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxIndependentSet(n, weights, edges));
});
```

## Notes

- dp[u][0] = u not selected, no child selected
- dp[u][1] = u not selected, some child selected
- dp[u][2] = u selected (all children must be in state 0)
