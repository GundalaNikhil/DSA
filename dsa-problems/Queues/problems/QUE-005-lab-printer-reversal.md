---
problem_id: QUE_LAB_PRINTER_REVERSAL__6429
display_id: QUE-005
slug: lab-printer-reversal
title: "Lab Printer Reversal"
difficulty: Easy
difficulty_score: 26
topics:
  - Queue
  - Stack
  - Simulation
tags:
  - queue
  - stack
  - reversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-005: Lab Printer Reversal

## Problem Statement

A lab printer processes jobs in a queue. The technician wants to reverse the first `k` jobs while preserving the order of the remaining jobs.

Given the queue and `k`, output the new queue order.

![Problem Illustration](../images/QUE-005/problem-illustration.png)

## Input Format

- First line: integer `n` (number of jobs)
- Second line: `n` space-separated integers (queue order, front to back)
- Third line: integer `k` (number of jobs to reverse from the front)

## Output Format

- Single line: updated queue values, space-separated

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5
2 4 6 8 10
4
```

**Output:**

```
8 6 4 2 10
```

**Explanation:**

Reverse the first 4 jobs:

- Original: `[2, 4, 6, 8, 10]`
- After reversal of first 4: `[8, 6, 4, 2, 10]`

![Example Visualization](../images/QUE-005/example-1.png)

## Notes

- Use a stack to reverse the first `k` elements
- Append the remaining `n - k` elements in their original order
- Time complexity: O(n)
- Space complexity: O(k)

## Related Topics

Queue, Stack, Reversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void reverseFirstK(int n, int[] jobs, int k) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] jobs = new int[n];
        for (int i = 0; i < n; i++) jobs[i] = sc.nextInt();
        int k = sc.nextInt();
        Solution sol = new Solution();
        sol.reverseFirstK(n, jobs, k);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def reverse_first_k(self, n, jobs, k):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    jobs = [int(x) for x in input_data[1:n+1]]
    k = int(input_data[n+1])
    sol = Solution()
    sol.reverse_first_k(n, jobs, k)

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
    void reverseFirstK(int n, vector<int>& jobs, int k) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> jobs(n);
    for (int i = 0; i < n; i++) cin >> jobs[i];
    int k;
    cin >> k;
    Solution sol;
    sol.reverseFirstK(n, jobs, k);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  reverseFirstK(n, jobs, k) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const jobs = [];
  for (let i = 0; i < n; i++) jobs.push(parseInt(input[1 + i]));
  const k = parseInt(input[1 + n]);
  const sol = new Solution();
  sol.reverseFirstK(n, jobs, k);
}

solve();
```
