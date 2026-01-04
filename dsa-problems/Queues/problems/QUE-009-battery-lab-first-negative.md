---
problem_id: QUE_BATTERY_LAB_FIRST_NEGATIVE__8630
display_id: QUE-009
slug: battery-lab-first-negative
title: "Battery Lab First Negative"
difficulty: Easy
difficulty_score: 32
topics:
  - Sliding Window
  - Queue
  - Array
tags:
  - sliding-window
  - queue
  - negatives
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-009: Battery Lab First Negative

## Problem Statement

A battery lab records voltage deltas over time. For each window of size `k`, report the first negative value in that window. If a window contains no negative values, output `0`.

![Problem Illustration](../images/QUE-009/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (voltage deltas)

## Output Format

- Single line: `n - k + 1` integers, each the first negative in the window or `0`

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5 2
5 -2 -7 3 4
```

**Output:**

```
-2 -2 -7 0
```

**Explanation:**

Windows:

- [5, -2] -> first negative is -2
- [-2, -7] -> first negative is -2
- [-7, 3] -> first negative is -7
- [3, 4] -> no negatives -> 0

![Example Visualization](../images/QUE-009/example-1.png)

## Notes

- Store indices of negative values in a queue
- Remove indices that fall out of the window
- The front of the queue is always the first negative
- Time complexity: O(n)

## Related Topics

Sliding Window, Queue, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findFirstNegative(int n, int k, int[] deltas) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] deltas = new int[n];
        for (int i = 0; i < n; i++) deltas[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.findFirstNegative(n, k, deltas);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_first_negative(self, n, k, deltas):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    deltas = [int(x) for x in input_data[2:2+n]]
    sol = Solution()
    sol.find_first_negative(n, k, deltas)

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
    void findFirstNegative(int n, int k, const vector<int>& deltas) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> deltas(n);
    for (int i = 0; i < n; i++) cin >> deltas[i];
    Solution sol;
    sol.findFirstNegative(n, k, deltas);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findFirstNegative(n, k, deltas) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const deltas = [];
  for (let i = 0; i < n; i++) deltas.push(parseInt(input[2 + i]));
  const sol = new Solution();
  sol.findFirstNegative(n, k, deltas);
}

solve();
```
