---
problem_id: REC_CAMPUS_TICKET_PACKS__2187
display_id: REC-003
slug: campus-ticket-packs
title: "Campus Ticket Packs"
difficulty: Medium
difficulty_score: 46
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - combinations
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-003: Campus Ticket Packs

## Problem Statement

A ticket system has `n` values `v[i]`. For each value you may take either `0` tickets or exactly `p[i]` tickets (a fixed pack size). List all unique combinations of ticket values that sum exactly to `target`.

Output each combination as a space-separated list of ticket values in nondecreasing order. If no combination exists, output `NONE`.

![Problem Illustration](../images/REC-003/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `v[i]`
- Third line: `n` space-separated integers `p[i]`
- Fourth line: integer `target`

## Output Format

- Each valid combination on its own line (values space-separated)
- Output `NONE` if no solution exists

## Constraints

- `1 <= n <= 15`
- `1 <= target <= 200`
- `1 <= v[i] <= 50`
- `1 <= p[i] <= 10`

## Example

**Input:**

```
2
2 3
2 1
7
```

**Output:**

```
2 2 3
```

**Explanation:**

Choose two 2s and one 3 to reach 7.

![Example Visualization](../images/REC-003/example-1.png)

## Notes

- Decide for each value whether to take its full pack or not
- Sort values to keep combinations ordered
- Prune when current sum exceeds target
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinations, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findCombinations(int n, int[] v, int[] p, int target) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] v = new int[n];
        for (int i = 0; i < n; i++) v[i] = sc.nextInt();
        int[] p = new int[n];
        for (int i = 0; i < n; i++) p[i] = sc.nextInt();
        int target = sc.nextInt();
        Solution sol = new Solution();
        sol.findCombinations(n, v, p, target);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_combinations(self, n, v, p, target):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    v = [int(x) for x in input_data[1:n+1]]
    p = [int(x) for x in input_data[n+1:2*n+1]]
    target = int(input_data[2*n+1])
    sol = Solution()
    sol.find_combinations(n, v, p, target)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void findCombinations(int n, vector<int>& v, vector<int>& p, int target) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> v(n), p(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    for (int i = 0; i < n; i++) cin >> p[i];
    int target;
    cin >> target;
    Solution sol;
    sol.findCombinations(n, v, p, target);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findCombinations(n, v, p, target) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  let idx = 0;
  const n = parseInt(input[idx++]);
  const v = [];
  for (let i = 0; i < n; i++) v.push(parseInt(input[idx++]));
  const p = [];
  for (let i = 0; i < n; i++) p.push(parseInt(input[idx++]));
  const target = parseInt(input[idx++]);
  const sol = new Solution();
  sol.findCombinations(n, v, p, target);
}

solve();
```
