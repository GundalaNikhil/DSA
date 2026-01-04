---
problem_id: REC_CAMPUS_COURSE_ORDERING__5184
display_id: REC-011
slug: campus-course-ordering
title: "Campus Course Ordering"
difficulty: Medium
difficulty_score: 55
topics:
  - Recursion
  - Backtracking
  - Graphs
tags:
  - recursion
  - topological-sort
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-011: Campus Course Ordering

## Problem Statement

A student must take `n` courses labeled `0` to `n-1`. You are given prerequisite pairs `(u, v)` meaning course `u` must be taken before course `v`.

List all possible valid course orderings.

![Problem Illustration](../images/REC-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: two integers `u` and `v`

## Output Format

- Each valid ordering on its own line as space-separated course IDs
- Output `NONE` if no ordering exists

## Constraints

- `1 <= n <= 8`
- `0 <= m <= 15`
- Course IDs are in `[0, n-1]`

## Example

**Input:**

```
3 2
0 1
0 2
```

**Output:**

```
0 1 2
0 2 1
```

**Explanation:**

Course 0 must come before both 1 and 2, so both orders are valid.

![Example Visualization](../images/REC-011/example-1.png)

## Notes

- Use backtracking with indegree counts
- Choose any zero-indegree node at each step
- Prune if no available node exists
- Time complexity can be O(n!) in worst case

## Related Topics

Topological Sort, Backtracking, Graphs

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findOrderings(int n, int m, List<int[]> prerequisites) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<int[]> prerequisites = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            prerequisites.add(new int[]{sc.nextInt(), sc.nextInt()});
        }
        Solution sol = new Solution();
        sol.findOrderings(n, m, prerequisites);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_orderings(self, n, m, prerequisites):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    prerequisites = []
    idx = 2
    for i in range(m):
        prerequisites.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
    sol = Solution()
    sol.find_orderings(n, m, prerequisites)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void findOrderings(int n, int m, const vector<pair<int, int>>& prerequisites) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> prerequisites(m);
    for (int i = 0; i < m; i++) cin >> prerequisites[i].first >> prerequisites[i].second;
    Solution sol;
    sol.findOrderings(n, m, prerequisites);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findOrderings(n, m, prerequisites) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const m = parseInt(input[1]);
  const prerequisites = [];
  let idx = 2;
  for (let i = 0; i < m; i++) {
    prerequisites.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }
  const sol = new Solution();
  sol.findOrderings(n, m, prerequisites);
}

solve();
```
