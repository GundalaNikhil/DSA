---
problem_id: QUE_HALLWAY_INTERLEAVE__1582
display_id: QUE-004
slug: hallway-interleave
title: "Hallway Interleave"
difficulty: Easy
difficulty_score: 24
topics:
  - Queue
  - Interleaving
  - Simulation
tags:
  - queue
  - interleaving
  - easy
  - simulation
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-004: Hallway Interleave

## Problem Statement

A hallway line of students has even length. You must interleave the first half of the line with the second half while preserving the relative order inside each half.

For example, `[11, 12, 13, 14]` becomes `[11, 13, 12, 14]`.

![Problem Illustration](../images/QUE-004/problem-illustration.png)

## Input Format

- First line: even integer `n` (queue length)
- Second line: `n` space-separated integers (queue order, front to back)

## Output Format

- Single line: interleaved queue values, space-separated

## Constraints

- `2 <= n <= 100000`
- `n` is even
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4
11 12 13 14
```

**Output:**

```
11 13 12 14
```

**Explanation:**

First half: `[11, 12]`
Second half: `[13, 14]`

Interleaving yields `[11, 13, 12, 14]`.

![Example Visualization](../images/QUE-004/example-1.png)

## Notes

- Use an auxiliary queue or stack to split halves
- The relative order within each half must not change
- Time complexity: O(n)
- Space complexity: O(n) for auxiliary storage

## Related Topics

Queue, Interleaving, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void interleaveQueue(int n, int[] queue) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] queue = new int[n];
        for (int i = 0; i < n; i++) queue[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.interleaveQueue(n, queue);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def interleave_queue(self, n, queue):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    queue = [int(x) for x in input_data[1:n+1]]
    sol = Solution()
    sol.interleave_queue(n, queue)

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
    void interleaveQueue(int n, vector<int>& queue) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> queue(n);
    for (int i = 0; i < n; i++) cin >> queue[i];
    Solution sol;
    sol.interleaveQueue(n, queue);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  interleaveQueue(n, queue) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const queue = [];
  for (let i = 0; i < n; i++) queue.push(parseInt(input[1 + i]));
  const sol = new Solution();
  sol.interleaveQueue(n, queue);
}

solve();
```
