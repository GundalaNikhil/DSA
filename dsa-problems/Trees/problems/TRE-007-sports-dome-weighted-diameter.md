---
problem_id: TRE_SPORTS_DOME_WEIGHTED_DIAMETER__9532
display_id: TRE-007
slug: sports-dome-weighted-diameter
title: "Sports Dome Weighted Diameter"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - DFS
  - Tree Diameter
tags:
  - trees
  - diameter
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-007: Sports Dome Weighted Diameter

## Problem Statement

Edges of the binary tree have non-negative weights. Find the maximum total edge weight along any path between two nodes.

This value is the weighted diameter of the tree.

![Problem Illustration](../images/TRE-007/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right leftWeight rightWeight` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The corresponding weight is ignored when the child is `-1`. The root is node `0` when `n > 0`.

## Output Format

- Single integer: weighted diameter of the tree

## Constraints

- `0 <= n <= 100000`
- Edge weights are integers in `[0, 10^9]`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
1 1 2 3 1
2 3 -1 2 0
3 -1 -1 0 0
4 -1 -1 0 0
```

**Output:**

```
6
```

**Explanation:**

The path `4 -> 2 -> 1 -> 3` has total weight `2 + 3 + 1 = 6`, which is the maximum.

![Example Visualization](../images/TRE-007/example-1.png)

## Notes

- The diameter can pass through or avoid the root.
- Use DFS to compute the best downward path at each node.
- The answer fits in 64-bit signed integers.

## Related Topics

Tree Diameter, DFS, Weighted Trees

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long weightedDiameter(int n, int[] left, int[] right, long[] lw, long[] rw) {
        //Implement here
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
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            left[i] = Integer.parseInt(parts[1]);
            right[i] = Integer.parseInt(parts[2]);
            if (parts.length >= 5) {
                lw[i] = Long.parseLong(parts[3]);
                rw[i] = Long.parseLong(parts[4]);
            } else {
                lw[i] = 1;
                rw[i] = 1;
            }
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def weighted_diameter(n: int, left: list[int], right: list[int], lw: list[int], rw: list[int]) -> int:
    # //Implement here
    return 0
def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        left = [0] * n
        right = [0] * n
        lw = [0] * n
        rw = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            left[i] = parts[1]
            right[i] = parts[2]
            if len(parts) >= 5:
                lw[i] = parts[3]
                rw[i] = parts[4]
            else:
                lw[i] = 1
                rw[i] = 1
                
        print(weighted_diameter(n, left, right, lw, rw))
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

using namespace std;

class Solution {
public:
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right,
                               const vector<long long>& lw, const vector<long long>& rw) {
        //Implement here
        return 0;
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
    vector<int> left(n, -1), right(n, -1);
    vector<long long> lw(n, 1), rw(n, 1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        left[i] = (int)parts[1];
        right[i] = (int)parts[2];
        if (parts.size() >= 5) {
            lw[i] = parts[3];
            rw[i] = parts[4];
        }
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function weightedDiameter(n, left, right, lw, rw) {
  //Implement here
  return 0;
}

const lines = fs
  .readFileSync(0, "utf8")
  .split(/\r?\n/)
  .map((line) => line.trim())
  .filter((line) => line.length > 0);

if (lines.length === 0) {
  process.exit(0);
}

const n = parseInt(lines[0], 10);
const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);
const lw = new Array(n).fill(1);
const rw = new Array(n).fill(1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  left[i] = parts[1];
  right[i] = parts[2];
  if (parts.length >= 5) {
    lw[i] = parts[3];
    rw[i] = parts[4];
  }
}

const result = weightedDiameter(n, left, right, lw, rw);
console.log(result.toString());
```
