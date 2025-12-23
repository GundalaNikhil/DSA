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

public class Solution {
    static class Edge {
        int to;
        Edge(int to) {
            this.to = to;
        }
    }

    static List<Edge>[] graph;
    static long[] weight;
    static long[] subtreeWeight;
    static long[] down;
    static long[] up;
    static long totalWeight;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        // Initialize data structures
        // TODO: Implement rerooting DP

        sc.close();
    }

    static void dfsDown(int u, int parent) {
        // TODO: Compute downward DP
    }

    static void dfsUp(int u, int parent) {
        // TODO: Compute upward DP (rerooting)
    }
}
```

### Python

```python
import sys
from collections import defaultdict

def solve():
    n = int(input())
    weight = [0] + list(map(int, input().split()))

    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # TODO: Implement rerooting DP

    print(best_node)

solve()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> graph[MAXN];
long long weight[MAXN];
long long subtreeWeight[MAXN];
long long down[MAXN];
long long up[MAXN];
int n;

void dfsDown(int u, int parent) {
    // TODO: Compute downward DP
}

void dfsUp(int u, int parent) {
    // TODO: Compute upward DP
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    // TODO: Implement rerooting DP

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  solve();
});

function solve() {
  const n = parseInt(lines[0]);
  const weight = [0, ...lines[1].split(" ").map(Number)];

  const graph = Array.from({ length: n + 1 }, () => []);

  for (let i = 2; i < n + 1; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  // TODO: Implement rerooting DP

  console.log(bestNode);
}
```

## Notes

- The problem requires rerooting DP technique to achieve O(n) time complexity
- Naive approach of computing cost for each root separately would be O(n²)
- Be careful with integer overflow - use long/long long for intermediate calculations
- The squared distance means we need special handling in the DP transition
