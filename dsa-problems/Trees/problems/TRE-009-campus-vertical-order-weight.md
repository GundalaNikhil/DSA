---
problem_id: TRE_CAMPUS_VERTICAL_ORDER_WEIGHT__4502
display_id: TRE-009
slug: campus-vertical-order-weight
title: "Campus Vertical Order With Weight Priority"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - BFS
  - Sorting
tags:
  - trees
  - vertical-order
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-009: Campus Vertical Order With Weight Priority

## Problem Statement

Each node has a value and a weight. Return the vertical order traversal of the tree with custom ordering rules inside each column:

1. Depth ascending
2. Weight descending
3. Value ascending

Only include columns whose total weight is at least `W`.

![Problem Illustration](../images/TRE-009/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value weight left right` for nodes `0..n-1`
- Last line: integer `W`, the minimum column weight

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print columns from left to right
- Each column is one line with its values in the required order
- If no column meets the threshold, print an empty line

## Constraints

- `0 <= n <= 100000`
- `1 <= weight <= 1000000`
- `0 <= W <= 10^12`

## Example

**Input:**

```
5
3 5 1 2
9 2 -1 -1
8 3 3 4
4 1 -1 -1
7 4 -1 -1
3
```

**Output:**

```
3 4
8
7
```

**Explanation:**

Column weights are: col -1 = 2, col 0 = 6, col 1 = 3, col 2 = 4. Columns with weight >= 3 are col 0, 1, and 2.

![Example Visualization](../images/TRE-009/example-1.png)

## Notes

- Columns are indexed by horizontal distance from the root.
- Stable ordering is not required; use the specified sort keys.
- Use 64-bit integers for column weight sums.

## Related Topics

Vertical Traversal, BFS, Sorting

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    static class NodeInfo {
        int val;
        int weight;
        int depth;
        NodeInfo(int val, int weight, int depth) {
            this.val = val;
            this.weight = weight;
            this.depth = depth;
        }
    }

    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights,
                                                       int[] left, int[] right, int W) {
        if (n == 0) return new ArrayList<>();

        boolean[] hasParent = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        Map<Integer, List<NodeInfo>> cols = new HashMap<>();
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{root, 0, 0});
        boolean[] visited = new boolean[n];
        visited[root] = true;

        int minCol = 0;
        int maxCol = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            cols.computeIfAbsent(c, k -> new ArrayList<>()).add(new NodeInfo(values[u], weights[u], d));
            minCol = Math.min(minCol, c);
            maxCol = Math.max(maxCol, c);

            if (left[u] != -1 && !visited[left[u]]) {
                visited[left[u]] = true;
                q.add(new int[]{left[u], c - 1, d + 1});
            }
            if (right[u] != -1 && !visited[right[u]]) {
                visited[right[u]] = true;
                q.add(new int[]{right[u], c + 1, d + 1});
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int c = minCol; c <= maxCol; c++) {
            List<NodeInfo> list = cols.get(c);
            if (list == null) continue;
            long totalWeight = 0;
            for (NodeInfo node : list) totalWeight += node.weight;
            if (totalWeight >= W) {
                list.sort((a, b) -> {
                    if (a.depth != b.depth) return a.depth - b.depth;
                    if (a.weight != b.weight) return b.weight - a.weight;
                    return a.val - b.val;
                });
                List<Integer> colValues = new ArrayList<>();
                for (NodeInfo node : list) colValues.add(node.val);
                result.add(colValues);
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (!line.isEmpty()) lines.add(line);
        }
        if (lines.isEmpty()) return;

        int n = Integer.parseInt(lines.get(0));
        int[] values = new int[n];
        int[] weights = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            values[i] = Integer.parseInt(parts[0]);
            if (parts.length >= 4) {
                weights[i] = Integer.parseInt(parts[1]);
                left[i] = Integer.parseInt(parts[2]);
                right[i] = Integer.parseInt(parts[3]);
            } else {
                weights[i] = 1;
                left[i] = Integer.parseInt(parts[1]);
                right[i] = Integer.parseInt(parts[2]);
            }
        }

        int W = 0;
        if (lines.size() > n + 1) {
            W = Integer.parseInt(lines.get(n + 1));
        }

        Solution solution = new Solution();
        List<List<Integer>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
        if (cols.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < cols.size(); i++) {
                List<Integer> col = cols.get(i);
                for (int j = 0; j < col.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(col.get(j));
                }
                if (i + 1 < cols.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(200000)
from collections import deque, defaultdict

def vertical_order_with_weights(n: int, values: list[int], weights: list[int],
    return 0
def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        values = [0] * n
        weights = [0] * n
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            # 4 tokens: val weight left right
            # 3 tokens: val left right (default weight 1)
            
            values[i] = parts[0]
            if len(parts) >= 4:
                weights[i] = parts[1]
                left[i] = parts[2]
                right[i] = parts[3]
            else:
                weights[i] = 1
                left[i] = parts[1]
                right[i] = parts[2]
                
        # W might be on next line
        try:
            line = next(iterator)
            W = int(line)
        except StopIteration:
            W = 0
            
        cols = vertical_order_with_weights(n, values, weights, left, right, W)
        if not cols:
            print()
        else:
            print("\n".join(" ".join(str(x) for x in col) for col in cols))
            
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

struct NodeInfo {
    int val;
    int weight;
    int depth;
};

class Solution {
public:
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values,
                                                 const vector<int>& weights, const vector<int>& left,
                                                 const vector<int>& right, int W) {
        if (n == 0) return {};

        vector<bool> hasParent(n, false);
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        unordered_map<int, vector<NodeInfo>> cols;
        queue<pair<int, pair<int, int>>> q;
        vector<bool> visited(n, false);
        q.push({root, {0, 0}});
        visited[root] = true;

        int minCol = 0;
        int maxCol = 0;

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            cols[c].push_back({values[u], weights[u], d});
            minCol = min(minCol, c);
            maxCol = max(maxCol, c);

            if (left[u] != -1 && !visited[left[u]]) {
                visited[left[u]] = true;
                q.push({left[u], {c - 1, d + 1}});
            }
            if (right[u] != -1 && !visited[right[u]]) {
                visited[right[u]] = true;
                q.push({right[u], {c + 1, d + 1}});
            }
        }

        vector<vector<int>> result;
        for (int c = minCol; c <= maxCol; c++) {
            auto it = cols.find(c);
            if (it == cols.end()) continue;
            auto& list = it->second;
            long long totalWeight = 0;
            for (const auto& node : list) totalWeight += node.weight;
            if (totalWeight >= W) {
                sort(list.begin(), list.end(), [](const NodeInfo& a, const NodeInfo& b) {
        return 0;
    }
                vector<int> colValues;
                for (const auto& node : list) colValues.push_back(node.val);
                result.push_back(colValues);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty()) {
            bool allSpace = true;
            for (char ch : line) {
                if (ch > ' ') {
                    allSpace = false;
                    break;
                }
            }
            if (!allSpace) lines.push_back(line);
        }
    }
    if (lines.empty()) return 0;

    int n = stoi(lines[0]);
    vector<int> values(n, 0), weights(n, 1), left(n, -1), right(n, -1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        values[i] = (int)parts[0];
        if (parts.size() >= 4) {
            weights[i] = (int)parts[1];
            left[i] = (int)parts[2];
            right[i] = (int)parts[3];
        } else {
            weights[i] = 1;
            left[i] = (int)parts[1];
            right[i] = (int)parts[2];
        }
    }

    int W = 0;
    if ((int)lines.size() > n + 1) {
        W = stoi(lines[n + 1]);
    }

    Solution solution;
    vector<vector<int>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
    if (cols.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)cols.size(); i++) {
            for (int j = 0; j < (int)cols[i].size(); j++) {
                if (j) cout << ' ';
                cout << cols[i][j];
            }
            if (i + 1 < (int)cols.size()) cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

const lines = fs
  .readFileSync(0, "utf8")
  .split(/\r?\n/)
  .map((line) => line.trim())
  .filter((line) => line.length > 0);

if (lines.length === 0) {
  process.exit(0);
}

const n = parseInt(lines[0], 10);
const values = new Array(n).fill(0);
const weights = new Array(n).fill(1);
const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  values[i] = parts[0];
  if (parts.length >= 4) {
    weights[i] = parts[1];
    left[i] = parts[2];
    right[i] = parts[3];
  } else {
    weights[i] = 1;
    left[i] = parts[1];
    right[i] = parts[2];
  }
}

let W = 0;
if (lines.length > n + 1) {
  W = parseInt(lines[n + 1], 10);
}

if (n === 0) {
  console.log("");
  process.exit(0);
}

const hasParent = new Array(n).fill(false);
for (let i = 0; i < n; i++) {
  if (left[i] !== -1) hasParent[left[i]] = true;
  if (right[i] !== -1) hasParent[right[i]] = true;
}
let root = 0;
for (let i = 0; i < n; i++) {
  if (!hasParent[i]) {
    root = i;
    break;
  }
}

const cols = new Map();
const queue = [[root, 0, 0]];
let head = 0;
const visited = new Array(n).fill(false);
visited[root] = true;
let minCol = 0;
let maxCol = 0;

while (head < queue.length) {
  const [u, c, d] = queue[head++];
  if (!cols.has(c)) cols.set(c, []);
  cols.get(c).push({ val: values[u], weight: weights[u], depth: d });
  if (c < minCol) minCol = c;
  if (c > maxCol) maxCol = c;

  if (left[u] !== -1 && !visited[left[u]]) {
    visited[left[u]] = true;
    queue.push([left[u], c - 1, d + 1]);
  }
  if (right[u] !== -1 && !visited[right[u]]) {
    visited[right[u]] = true;
    queue.push([right[u], c + 1, d + 1]);
  }
}

const result = [];
for (let c = minCol; c <= maxCol; c++) {
  if (!cols.has(c)) continue;
  const list = cols.get(c);
  let totalWeight = 0;
  for (const node of list) totalWeight += node.weight;
  if (totalWeight >= W) {
    list.sort((a, b) => {
      if (a.depth !== b.depth) return a.depth - b.depth;
      if (a.weight !== b.weight) return b.weight - a.weight;
      return a.val - b.val;
    });
    result.push(list.map((node) => node.val));
  }
}

if (result.length === 0) {
  console.log("");
} else {
  console.log(result.map((col) => col.join(" ")).join("\n"));
}
```

