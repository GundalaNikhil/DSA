---
problem_id: TRE_ROBOTICS_LCA_BLOCKED__7104
display_id: TRE-012
slug: robotics-lca-blocked
title: "Robotics LCA with Blocked Nodes"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - LCA
  - DFS
tags:
  - trees
  - lca
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-012: Robotics LCA with Blocked Nodes

## Problem Statement

Some nodes in the tree are blocked and cannot be used as part of any path. Given two target nodes that are not blocked, find their lowest common ancestor (LCA) that is also not blocked.

If all common ancestors are blocked, output `-1`.

![Problem Illustration](../images/TRE-012/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value blocked left right` for nodes `0..n-1`
- Last line: two integers `u` and `v`, the node indices of the targets

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: value of the lowest unblocked common ancestor, or `-1` if none

## Constraints

- `1 <= n <= 100000`
- `blocked` is `0` or `1`
- Node values are distinct and fit in 32-bit signed integers
- Target nodes are unblocked

## Example

**Input:**

```
5
6 1 1 2
2 0 3 4
8 0 -1 -1
1 0 -1 -1
4 0 -1 -1
3 4
```

**Output:**

```
2
```

**Explanation:**

The LCA of nodes 3 and 4 is node 1 (value 2). The root is blocked, but the LCA node itself is unblocked.

![Example Visualization](../images/TRE-012/example-1.png)

## Notes

- If the LCA is blocked, climb to the nearest unblocked ancestor.
- Use DFS to detect presence of targets in subtrees.
- Output `-1` if no unblocked common ancestor exists.

## Related Topics

LCA, DFS, Binary Trees

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public int lcaBlocked(int n, int[] values, int[] blocked, int[] left, int[] right, int u, int v) {
        // Implementation here
        return 0;
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
        int[] blocked = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            values[i] = Integer.parseInt(parts[0]);
            if (parts.length >= 4) {
                blocked[i] = Integer.parseInt(parts[1]);
                left[i] = Integer.parseInt(parts[2]);
                right[i] = Integer.parseInt(parts[3]);
            } else {
                blocked[i] = 0;
                left[i] = Integer.parseInt(parts[1]);
                right[i] = Integer.parseInt(parts[2]);
            }
        }

        if (lines.size() <= n + 1) return;
        String[] uv = lines.get(n + 1).split("\\s+");
        if (uv.length < 2) return;
        int u = Integer.parseInt(uv[0]);
        int v = Integer.parseInt(uv[1]);

        Solution solution = new Solution();
        System.out.println(solution.lcaBlocked(n, values, blocked, left, right, u, v));
    }
}
```

### Python

```python
import sys

def lca_blocked(n: int, values: list[int], blocked: list[int], left: list[int], right: list[int], u: int, v: int) -> int:
    # Implementation here
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
        blocked = [0] * n
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            # 4 tokens: val blocked left right
            # 3 tokens: val left right
            
            values[i] = parts[0]
            if len(parts) >= 4:
                blocked[i] = parts[1]
                left[i] = parts[2]
                right[i] = parts[3]
            else:
                blocked[i] = 0
                left[i] = parts[1]
                right[i] = parts[2]
                
        line = next(iterator)
        u, v = map(int, line.split())
        
        # u and v are indices in this problem context? 
        # Test cases seem to implies indices.
        # But if they are values, we need a map. 
        # Given "lca of u and v", and previous tre012 failure, let's assume indices.
        # If they are values, we need value_to_index map.
        # Let's add robustness: if u or v >= n, try to look up index by value?
        # But values might not be unique.
        # Standard assumption for "u and v" in LCA is node indices.
        
        print(lca_blocked(n, values, blocked, left, right, u, v))
        
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
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lcaBlocked(int n, const vector<int>& values, const vector<int>& blocked,
                   const vector<int>& left, const vector<int>& right, int u, int v) {
        // Implementation here
        return {};
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
    vector<int> values(n, 0), blocked(n, 0), left(n, -1), right(n, -1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        values[i] = (int)parts[0];
        if (parts.size() >= 4) {
            blocked[i] = (int)parts[1];
            left[i] = (int)parts[2];
            right[i] = (int)parts[3];
        } else {
            blocked[i] = 0;
            left[i] = (int)parts[1];
            right[i] = (int)parts[2];
        }
    }

    if ((int)lines.size() <= n + 1) return 0;
    stringstream uv(lines[n + 1]);
    int u = 0, v = 0;
    if (!(uv >> u >> v)) return 0;

    Solution solution;
    cout << solution.lcaBlocked(n, values, blocked, left, right, u, v) << "\n";
    return 0;
}
```

### JavaScript

```
// No template available
```
