---
problem_id: HEP_PROJECT_SELECTION_RISK_BUDGET__2917
display_id: HEP-013
slug: project-selection-risk-budget
title: "Project Selection with Risk Budget"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Greedy
  - Finance
tags:
  - heaps
  - greedy
  - risk-budget
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-013: Project Selection with Risk Budget

## Problem Statement

You have `n` projects. Project `i` has cost `c_i`, profit `p_i`, and risk `r_i`. You start with capital `C` and risk budget `R`. You may select at most `k` projects. A project can be selected only if:

- `c_i <= current capital`
- `current risk + r_i <= R`

When you select a project, your capital increases by `p_i` and your risk increases by `r_i`.

Return the maximum final capital you can achieve.

![Problem Illustration](../images/HEP-013/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, `C`, `R`
- Next `n` lines: `c_i p_i r_i`

## Output Format

- Single integer: maximum final capital

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- `0 <= C, R <= 10^12`
- `1 <= c_i, p_i, r_i <= 10^9`

## Example

**Input:**

```
3 2 1 3
1 2 1
2 2 2
3 5 2
```

**Output:**

```
5
```

**Explanation:**

Pick projects 1 and 2:

- Start: capital=1, risk=0
- Project 1: capital=3, risk=1
- Project 2: capital=5, risk=3

Final capital is 5.

![Example Visualization](../images/HEP-013/example-1.png)

## Notes

- Sort projects by cost to unlock affordable options
- Use a max-heap of profits among projects within risk budget
- Greedily pick the most profitable affordable project each step
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Greedy, Resource Allocation, Scheduling

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxFinalCapital(int n, int k, long c, long r, long[][] projects) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        long c = Long.parseLong(parts[2]);
        long r = Long.parseLong(parts[3]);

        long[][] projects = new long[n][3];
        for (int i = 0; i < n; i++) {
            String[] pParts = br.readLine().trim().split("\\s+");
            projects[i][0] = Long.parseLong(pParts[0]);
            projects[i][1] = Long.parseLong(pParts[1]);
            projects[i][2] = Long.parseLong(pParts[2]);
        }

        Solution sol = new Solution();
        System.out.println(sol.maxFinalCapital(n, k, c, r, projects));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_final_capital(self, n, k, c, r, projects):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    k = int(input_data[idx++])
    c = int(input_data[idx++])
    r = int(input_data[idx++])

    projects = []
    for _ in range(n):
        cost = int(input_data[idx++])
        profit = int(input_data[idx++])
        risk = int(input_data[idx++])
        projects.append([cost, profit, risk])

    sol = Solution()
    print(sol.max_final_capital(n, k, c, r, projects))

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
    long long maxFinalCapital(int n, int k, long long c, long long r, vector<vector<long long>>& projects) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    long long c, r;
    if (!(cin >> n >> k >> c >> r)) return 0;

    vector<vector<long long>> projects(n, vector<long long>(3));
    for (int i = 0; i < n; i++) {
        cin >> projects[i][0] >> projects[i][1] >> projects[i][2];
    }

    Solution sol;
    cout << sol.maxFinalCapital(n, k, c, r, projects) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxFinalCapital(n, k, c, r, projects) {
    // Implement here
    return 0n;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const c = BigInt(input[idx++]);
  const r = BigInt(input[idx++]);

  const projects = [];
  for (let i = 0; i < n; i++) {
    const cost = BigInt(input[idx++]);
    const profit = BigInt(input[idx++]);
    const risk = BigInt(input[idx++]);
    projects.push([cost, profit, risk]);
  }

  const sol = new Solution();
  console.log(sol.maxFinalCapital(n, k, c, r, projects).toString());
}

solve();
```
