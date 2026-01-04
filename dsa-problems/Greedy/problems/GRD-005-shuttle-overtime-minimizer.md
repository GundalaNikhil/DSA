---
problem_id: GRD_SHUTTLE_OVERTIME_MINIMIZER__6381
display_id: GRD-005
slug: shuttle-overtime-minimizer
title: "Shuttle Overtime Minimizer"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-005: Shuttle Overtime Minimizer

## Problem Statement

You manage shuttle driver shifts where each shift `i` has:

- A standard length `l[i]` hours (no overtime cost for these hours)
- An overtime cost `p[i]` per hour beyond the standard length

You must cover a total of `H` hours using these shifts. Shifts can be partially used, but any hours beyond the standard length incur overtime costs at rate `p[i]`.

Your goal is to minimize the total overtime cost while covering all `H` hours.

![Problem Illustration](../images/GRD-005/problem-illustration.png)

## Input Format

- First line: two integers `n H` (number of shifts and total hours needed)
- Next `n` lines: two integers `l p` representing standard length and overtime cost per hour for each shift

## Output Format

- Single integer: minimum total overtime cost

## Constraints

- `1 <= n <= 10^5`
- `0 <= l[i], p[i] <= 10^9`
- `1 <= H <= 10^12`
- Total standard hours (sum of all `l[i]`) may be less than, equal to, or greater than `H`

## Example

**Input:**

```
2 8
4 3
2 1
```

**Output:**

```
4
```

**Explanation:**

Shifts:

- Shift 1: 4 standard hours, overtime costs 3 per hour
- Shift 2: 2 standard hours, overtime costs 1 per hour

Total hours needed: 8

Strategy:

Strategy to minimize cost:

1. Use all standard hours first: 4 + 2 = 6 hours (no overtime cost)
2. Need 2 more hours (8 - 6 = 2)
3. For overtime, choose the cheaper rate (shift 2 at cost 1 per hour)
4. Overtime cost: 2 × 1 = 2

Total minimum cost: 2

![Example Visualization](../images/GRD-005/example-1.png)

## Notes

- First use all standard hours from all shifts (these are free)
- For remaining hours, use overtime from shifts with lowest overtime costs
- Use a min-heap to track available overtime costs
- If total standard hours >= H, answer is 0
- Time complexity: O(n log n) for sorting by overtime cost

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Cost Optimization, Resource Allocation

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minOvertimeCost(int n, long h, long[][] shifts) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nhLine = br.readLine();
        if (nhLine == null) return;
        String[] nh = nhLine.trim().split("\\s+");
        int n = Integer.parseInt(nh[0]);
        long h = Long.parseLong(nh[1]);

        long[][] shifts = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] sLine = br.readLine().trim().split("\\s+");
            shifts[i][0] = Long.parseLong(sLine[0]);
            shifts[i][1] = Long.parseLong(sLine[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minOvertimeCost(n, h, shifts));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_overtime_cost(self, n, h, shifts):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    h = int(input_data[1])
    idx = 2
    shifts = []
    for _ in range(n):
        shifts.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.min_overtime_cost(n, h, shifts))

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
    long long minOvertimeCost(int n, long long h, vector<vector<long long>>& shifts) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long h;
    if (!(cin >> n >> h)) return 0;

    vector<vector<long long>> shifts(n, vector<long long>(2));
    for (int i = 0; i < n; i++) {
        cin >> shifts[i][0] >> shifts[i][1];
    }

    Solution sol;
    cout << sol.minOvertimeCost(n, h, shifts) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minOvertimeCost(n, h, shifts) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const h = BigInt(input[idx++]);
  const shifts = [];
  for (let i = 0; i < n; i++) {
    shifts.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.minOvertimeCost(n, h, shifts).toString());
}

solve();
```
