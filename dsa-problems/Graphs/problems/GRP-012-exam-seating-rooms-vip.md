---
problem_id: GRP_EXAM_SEATING_VIP__3928
display_id: GRP-012
slug: exam-seating-rooms-vip
title: "Exam Seating Rooms with VIP Isolation"
difficulty: Medium
difficulty_score: 40
topics:
  - Union-Find
  - Connected Components
  - Disjoint Set Union
tags:
  - graph
  - union-find
  - dsu
  - connected-components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-012: Exam Seating Rooms with VIP Isolation

## Problem Statement

You are given an undirected graph where nodes represent students who prefer to sit together (connected by edges). Some students are designated as VIPs.

**Constraint**: No connected component can contain more than one VIP.

Your task is to remove the minimum number of edges such that no component contains more than one VIP, then return the size of the largest remaining connected component.

![Problem Illustration](../images/GRP-012/problem-illustration.png)

## Input Format

- First line: integer `n` (number of students/nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an edge between students `u` and `v`
- Last line: space-separated integers representing VIP student IDs

## Output Format

- Single integer: the size of the largest connected component after edge removals

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- Number of VIPs `<= n`

## Example

**Input:**

```
5
3
0 1
1 2
3 4
2 3
```

**Output:**

```
3
```

**Explanation:**

Edges: (0,1), (1,2), (3,4)
VIPs: {2, 3}

Initial components:

- Component 1: {0, 1, 2} (contains VIP 2)
- Component 2: {3, 4} (contains VIP 3)

Since VIPs 2 and 3 are already in different components, no edges need to be removed.

Final components:

- Component 1: {0, 1, 2} → size 3
- Component 2: {3, 4} → size 2

Largest component size = 3

![Example Visualization](../images/GRP-012/example-1.png)

## Notes

- Use Disjoint Set Union (DSU / Union-Find) to track components
- Track which components contain VIPs
- When processing an edge (u, v):
  - If both components already have a VIP, skip the edge
  - Otherwise, union the components
- After processing all valid edges, find the maximum component size
- Time complexity: O(m × α(n)) where α is the inverse Ackermann function (nearly constant)

## Related Topics

Union-Find, DSU, Connected Components, Graph Constraints, Component Tracking

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int maxSafeComponentSize(int n, int m, List<int[]> edges, Set<Integer> vips) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String[] edge = br.readLine().trim().split("\\s+");
            edges.add(new int[]{Integer.parseInt(edge[0]), Integer.parseInt(edge[1])});
        }

        String vipLine = br.readLine();
        Set<Integer> vips = new HashSet<>();
        if (vipLine != null && !vipLine.trim().isEmpty()) {
            String[] vipsArr = vipLine.trim().split("\\s+");
            for (String s : vipsArr) vips.add(Integer.parseInt(s));
        }

        Solution sol = new Solution();
        System.out.println(sol.maxSafeComponentSize(n, m, edges, vips));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_safe_component_size(self, n, m, edges, vips):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0].strip())
    m = int(input_data[1].strip())

    edges = []
    for i in range(2, 2 + m):
        edges.append(list(map(int, input_data[i].split())))

    vips = set()
    if len(input_data) > 2 + m:
        vips = set(map(int, input_data[2 + m].split()))

    sol = Solution()
    print(sol.max_safe_component_size(n, m, edges, vips))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSafeComponentSize(int n, int m, vector<pair<int, int>>& edges, unordered_set<int>& vips) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    unordered_set<int> vips;
    int v;
    while (cin >> v) {
        vips.insert(v);
    }

    Solution sol;
    cout << sol.maxSafeComponentSize(n, m, edges, vips) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxSafeComponentSize(n, m, edges, vips) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 2) return;

  const n = parseInt(input[0].trim());
  const m = parseInt(input[1].trim());

  const edges = [];
  for (let i = 2; i < 2 + m; i++) {
    edges.push(input[i].trim().split(/\s+/).map(Number));
  }

  let vips = new Set();
  if (input.length > 2 + m) {
    const vipsArr = input[2 + m].trim().split(/\s+/);
    if (vipsArr[0] !== "") {
      vipsArr.forEach((v) => vips.add(parseInt(v)));
    }
  }

  const sol = new Solution();
  console.log(sol.maxSafeComponentSize(n, m, edges, vips));
}

solve();
```
