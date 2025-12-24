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

class Solution {
    public long maximizeCapital(int k, long C, long R, long[] cost, long[] profit, long[] risk) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        long C = sc.nextLong();
        long R = sc.nextLong();
        long[] cost = new long[n];
        long[] profit = new long[n];
        long[] risk = new long[n];
        for (int i = 0; i < n; i++) {
            cost[i] = sc.nextLong();
            profit[i] = sc.nextLong();
            risk[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.maximizeCapital(k, C, R, cost, profit, risk));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def maximize_capital(k: int, C: int, R: int, cost: List[int], profit: List[int], risk: List[int]) -> int:
    # Your implementation here
    return 0

def main():
    n, k, C, R = map(int, input().split())
    cost = []
    profit = []
    risk = []
    for _ in range(n):
        c, p, r = map(int, input().split())
        cost.append(c)
        profit.append(p)
        risk.append(r)

    result = maximize_capital(k, C, R, cost, profit, risk)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long maximizeCapital(int k, long long C, long long R, const vector<long long>& cost,
                              const vector<long long>& profit, const vector<long long>& risk) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    long long C, R;
    cin >> n >> k >> C >> R;
    vector<long long> cost(n), profit(n), risk(n);
    for (int i = 0; i < n; i++) {
        cin >> cost[i] >> profit[i] >> risk[i];
    }

    Solution solution;
    cout << solution.maximizeCapital(k, C, R, cost, profit, risk) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maximizeCapital(k, C, R, cost, profit, risk) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const C = parseInt(data[idx++], 10);
  const R = parseInt(data[idx++], 10);
  const cost = [];
  const profit = [];
  const risk = [];
  for (let i = 0; i < n; i++) {
    cost.push(parseInt(data[idx++], 10));
    profit.push(parseInt(data[idx++], 10));
    risk.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  console.log(solution.maximizeCapital(k, C, R, cost, profit, risk));
});
```
