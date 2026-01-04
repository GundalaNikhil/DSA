---
problem_id: QUE_CORRIDOR_WINDOW_SECOND_MINIMUM__2748
display_id: QUE-008
slug: corridor-window-second-minimum
title: "Corridor Window Second Minimum"
difficulty: Medium
difficulty_score: 48
topics:
  - Sliding Window
  - Ordered Map
  - Queue
tags:
  - sliding-window
  - multiset
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-008: Corridor Window Second Minimum

## Problem Statement

Security sensors report values along a corridor. For each sliding window of size `k`, you must output the second smallest value in that window.

If the window size is `1`, the second smallest value is defined as the only element. If the smallest value appears at least twice, the second smallest equals the smallest.

![Problem Illustration](../images/QUE-008/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (sensor values)

## Output Format

- Single line: `n - k + 1` integers, each the second smallest for a window

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5 3
6 2 5 1 7
```

**Output:**

```
5 2 5
```

**Explanation:**

Windows and second minima:

- [6, 2, 5] -> sorted [2, 5, 6], second smallest = 5
- [2, 5, 1] -> sorted [1, 2, 5], second smallest = 2
- [5, 1, 7] -> sorted [1, 5, 7], second smallest = 5

![Example Visualization](../images/QUE-008/example-1.png)

## Notes

- Maintain a balanced structure with counts to track the smallest two values
- Removing outgoing elements must update counts correctly
- Time complexity: O(n log k)
- Space complexity: O(k)

## Related Topics

Sliding Window, Multiset, Ordered Map

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findSecondMinimum(int n, int k, int[] values) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.findSecondMinimum(n, k, values);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_second_minimum(self, n, k, values):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    values = [int(x) for x in input_data[2:2+n]]
    sol = Solution()
    sol.find_second_minimum(n, k, values)

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
    void findSecondMinimum(int n, int k, const vector<int>& values) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    Solution sol;
    sol.findSecondMinimum(n, k, values);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findSecondMinimum(n, k, values) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const values = [];
  for (let i = 0; i < n; i++) values.push(parseInt(input[2 + i]));
  const sol = new Solution();
  sol.findSecondMinimum(n, k, values);
}

solve();
```
