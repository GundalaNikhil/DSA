---
problem_id: QUE_ASSEMBLY_LINE_BUFFER_SWAP__9053
display_id: QUE-016
slug: assembly-line-buffer-swap
title: "Assembly Line Buffer Swap"
difficulty: Easy
difficulty_score: 29
topics:
  - Queue
  - Simulation
  - In-Place
tags:
  - queue
  - swap
  - simulation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-016: Assembly Line Buffer Swap

## Problem Statement

An assembly line has two buffers, each represented by a queue of equal length. Swap their contents using only queue operations.

Given the two queues, output their contents after the swap.

![Problem Illustration](../images/QUE-016/problem-illustration.png)

## Input Format

- First line: integer `n` (length of each queue)
- Second line: `n` space-separated integers (Queue 1, front to back)
- Third line: `n` space-separated integers (Queue 2, front to back)

## Output Format

- First line: Queue 1 after the swap
- Second line: Queue 2 after the swap

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
2
4 5
7 8
```

**Output:**

```
7 8
4 5
```

**Explanation:**

After swapping, the entire contents of the queues are exchanged.

![Example Visualization](../images/QUE-016/example-1.png)

## Notes

- The queues have equal length
- Use only enqueue and dequeue operations conceptually
- Time complexity: O(n)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Simulation, In-Place Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void swapQueues(int n, int[] q1, int[] q2) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] q1 = new int[n];
        for (int i = 0; i < n; i++) q1[i] = sc.nextInt();
        int[] q2 = new int[n];
        for (int i = 0; i < n; i++) q2[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.swapQueues(n, q1, q2);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def swap_queues(self, n, q1, q2):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q1 = [int(x) for x in input_data[1:1+n]]
    q2 = [int(x) for x in input_data[1+n:1+2*n]]
    sol = Solution()
    sol.swap_queues(n, q1, q2)

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
    void swapQueues(int n, vector<int>& q1, vector<int>& q2) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> q1(n), q2(n);
    for (int i = 0; i < n; i++) cin >> q1[i];
    for (int i = 0; i < n; i++) cin >> q2[i];
    Solution sol;
    sol.swapQueues(n, q1, q2);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  swapQueues(n, q1, q2) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const q1 = [];
  for (let i = 0; i < n; i++) q1.push(parseInt(input[1 + i]));
  const q2 = [];
  for (let i = 0; i < n; i++) q2.push(parseInt(input[1 + n + i]));
  const sol = new Solution();
  sol.swapQueues(n, q1, q2);
}

solve();
```
