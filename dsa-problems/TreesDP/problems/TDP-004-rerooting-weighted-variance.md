---
title: Rerooting for Weighted Distance Variance
problem_id: TDP_REROOTING_WEIGHTED_VARIANCE__5927
display_id: TDP-004
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Rerooting Technique
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: rerooting-weighted-variance
---

# Rerooting for Weighted Distance Variance

## Problem Description

You are given a tree with `n` nodes, where each node `i` has a weight `w[i]`. Your task is to find the node that minimizes the **weighted sum of squared distances**:

`cost(i) = sum_j=1^n w[j] x dist(i, j)^2`

where `dist(i, j)` is the number of edges in the shortest path between nodes `i` and `j`.

Return the node number (1-indexed) that minimizes this cost. If there are multiple such nodes, return the smallest node number.

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers representing `w[1], w[2], ..., w[n]`
- Next `n-1` lines: each contains two integers `u v` representing an edge between nodes `u` and `v`

## Output Format

- Single integer: the node number that minimizes the weighted sum of squared distances

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= w[i] <= 10^6`
- `1 <= u, v <= n`
- The graph forms a valid tree (connected, acyclic, n-1 edges)

## Example 1

**Input:**

```
3
1 2 1
1 2
2 3
```

**Output:**

```
2
```

**Explanation:**
Tree structure: 1 -- 2 -- 3

Cost for node 1: w[1]×0² + w[2]×1² + w[3]×2² = 1×0 + 2×1 + 1×4 = 6
Cost for node 2: w[1]×1² + w[2]×0² + w[3]×1² = 1×1 + 2×0 + 1×1 = 2 ✓ (minimum)
Cost for node 3: w[1]×2² + w[2]×1² + w[3]×0² = 1×4 + 2×1 + 1×0 = 6

Node 2 has the minimum cost.

## Example 2

**Input:**

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
```

**Output:**

```
2
```

**Explanation:**
Tree structure:

```
    1
   / \
  2   3
 / \
4   5
```

Cost calculations:

- Node 1: 0 + 20×1 + 30×1 + 40×4 + 50×4 = 470
- Node 2: 10×1 + 0 + 30×4 + 40×1 + 50×1 = 220 ✓ (minimum)
- Node 3: 10×1 + 20×4 + 0 + 40×9 + 50×9 = 900
- Node 4: 10×4 + 20×1 + 30×9 + 0 + 50×4 = 540
- Node 5: 10×4 + 20×1 + 30×9 + 40×4 + 0 = 580

Node 2 minimizes the cost.

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int findBestRoot(int n, long[] weights, int[][] edges) {
        // Implement here
        return -1;
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
        System.out.println(solution.findBestRoot(n, weights, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def find_best_root(self, n: int, weights: List[int], edges: List[List[int]]) -> int:
        # Implement here
        return -1

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
        print(solution.find_best_root(n, weights, edges))
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
    int findBestRoot(int n, const vector<long long>& weights, const vector<vector<int>>& edges) {
        // Implement here
        return -1;
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
    cout << solution.findBestRoot(n, weights, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findBestRoot(n, weights, edges) {
    // Implement here
    return -1;
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
  console.log(solution.findBestRoot(n, weights, edges));
});
```

## Notes

- The problem requires rerooting DP technique to achieve O(n) time complexity
- Naive approach of computing cost for each root separately would be O(n²)
- Be careful with integer overflow - use long/long long for intermediate calculations
- The squared distance means we need special handling in the DP transition
