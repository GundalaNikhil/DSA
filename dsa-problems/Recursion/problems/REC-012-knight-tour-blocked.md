---
problem_id: REC_KNIGHT_TOUR_BLOCKED__7742
display_id: REC-012
slug: knight-tour-blocked
title: "Knight Tour With Blocked Cells"
difficulty: Medium
difficulty_score: 60
topics:
  - Recursion
  - Backtracking
  - Chess
tags:
  - recursion
  - backtracking
  - knight-tour
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-012: Knight Tour With Blocked Cells

## Problem Statement

On an `n x n` board, a knight starts at `(0,0)` and must visit every unblocked cell exactly once using standard knight moves.

Some cells are blocked and cannot be visited. Output any valid path that visits all unblocked cells, or `NONE` if impossible.

![Problem Illustration](../images/REC-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: integer `b` (number of blocked cells)
- Next `b` lines: two integers `r` and `c` for each blocked cell

## Output Format

- One line with the path as `row,col` coordinates separated by spaces
- Output `NONE` if no tour exists

## Constraints

- `1 <= n <= 5`
- `0 <= b < n * n`
- `(0,0)` is guaranteed to be unblocked

## Example

**Input:**

```
2
3
0 1
1 0
1 1
```

**Output:**

```
0,0
```

**Explanation:**

Only the start cell is unblocked, so the tour is just `(0,0)`.

![Example Visualization](../images/REC-012/example-1.png)

## Notes

- Track visited cells and remaining unblocked count
- Knight moves are (±2, ±1) and (±1, ±2)
- Backtracking is required due to branching
- Any valid tour is acceptable

## Related Topics

Backtracking, Graph Traversal, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findKnightTour(int n, int b, int[][] blocked) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int b = sc.nextInt();
        int[][] blocked = new int[b][2];
        for (int i = 0; i < b; i++) {
            blocked[i][0] = sc.nextInt();
            blocked[i][1] = sc.nextInt();
        }
        Solution sol = new Solution();
        sol.findKnightTour(n, b, blocked);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_knight_tour(self, n, b, blocked):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    b = int(input_data[1])
    blocked = []
    idx = 2
    for i in range(b):
        blocked.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
    sol = Solution()
    sol.find_knight_tour(n, b, blocked)

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
    void findKnightTour(int n, int b, const vector<pair<int, int>>& blocked) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, b;
    if (!(cin >> n >> b)) return 0;
    vector<pair<int, int>> blocked(b);
    for (int i = 0; i < b; i++) cin >> blocked[i].first >> blocked[i].second;
    Solution sol;
    sol.findKnightTour(n, b, blocked);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findKnightTour(n, b, blocked) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const b = parseInt(input[1]);
  const blocked = [];
  let idx = 2;
  for (let i = 0; i < b; i++) {
    blocked.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }
  const sol = new Solution();
  sol.findKnightTour(n, b, blocked);
}

solve();
```
