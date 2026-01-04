---
problem_id: QUE_BUS_LOOP_ONE_SKIP__2986
display_id: QUE-012
slug: bus-loop-one-skip
title: "Bus Loop With One Free Skip"
difficulty: Medium
difficulty_score: 58
topics:
  - Greedy
  - Queue
  - Circular Route
tags:
  - greedy
  - circular
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-012: Bus Loop With One Free Skip

## Problem Statement

A circular bus route has `n` stops. At stop `i`, the bus can gain `gain[i]` fuel and must spend `cost[i]` fuel to reach the next stop.

You must skip refueling at exactly one stop (the fuel there is lost). Find a starting index that allows the bus to complete one full loop with that single skip. If no such start exists, output `-1`.

![Problem Illustration](../images/QUE-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `gain[i]`
- Third line: `n` space-separated integers `cost[i]`

## Output Format

- Single integer: a valid starting index (0-based), or `-1` if impossible

## Constraints

- `1 <= n <= 100000`
- `0 <= gain[i], cost[i] <= 10^9`

## Example

**Input:**

```
3
4 5 1
3 3 2
```

**Output:**

```
0
```

**Explanation:**

Start at index 0 and skip refuel at stop 2:

- Stop 0: gain 4, cost 3 -> fuel 1
- Stop 1: gain 5, cost 3 -> fuel 3
- Stop 2: skip gain 1, cost 2 -> fuel 1

The bus completes the loop with fuel remaining, so index 0 is valid.

![Example Visualization](../images/QUE-012/example-1.png)

## Notes

- Track two running balances: without skip and with skip used
- If both balances drop below 0, reset the start
- The total gain minus the skipped refuel must still cover total cost
- Time complexity: O(n)

## Related Topics

Greedy, Circular Array, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int canCompleteLoop(int n, int[] gain, int[] cost) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] gain = new int[n];
        for (int i = 0; i < n; i++) gain[i] = sc.nextInt();
        int[] cost = new int[n];
        for (int i = 0; i < n; i++) cost[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.canCompleteLoop(n, gain, cost));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def can_complete_loop(self, n, gain, cost):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    gain = [int(x) for x in input_data[1:1+n]]
    cost = [int(x) for x in input_data[1+n:1+2*n]]
    sol = Solution()
    print(sol.can_complete_loop(n, gain, cost))

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
    int canCompleteLoop(int n, const vector<int>& gain, const vector<int>& cost) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> gain(n), cost(n);
    for (int i = 0; i < n; i++) cin >> gain[i];
    for (int i = 0; i < n; i++) cin >> cost[i];
    Solution sol;
    cout << sol.canCompleteLoop(n, gain, cost) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  canCompleteLoop(n, gain, cost) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const gain = [];
  for (let i = 0; i < n; i++) gain.push(parseInt(input[1 + i]));
  const cost = [];
  for (let i = 0; i < n; i++) cost.push(parseInt(input[1 + n + i]));
  const sol = new Solution();
  console.log(sol.canCompleteLoop(n, gain, cost));
}

solve();
```
