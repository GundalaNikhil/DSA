---
problem_id: QUE_EVENT_REGISTRATION_MERGE__6205
display_id: QUE-011
slug: event-registration-merge
title: "Event Registration Merge"
difficulty: Easy
difficulty_score: 22
topics:
  - Queue
  - Merge
  - Two Pointers
tags:
  - queue
  - merge
  - two-pointers
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-011: Event Registration Merge

## Problem Statement

Two event registration lines are already sorted by registration ID. Merge the two queues into one sorted queue while preserving the order of equal IDs.

![Problem Illustration](../images/QUE-011/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first queue)
- Second line: `n` space-separated integers (first queue)
- Third line: integer `m` (length of second queue)
- Fourth line: `m` space-separated integers (second queue)

## Output Format

- Single line: merged queue values in nondecreasing order
- If both queues are empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
3 5 9
3
1 4 10
```

**Output:**

```
1 3 4 5 9 10
```

**Explanation:**

Merge by repeatedly taking the smaller front value:

- 1 (from second)
- 3 (from first)
- 4 (from second)
- 5 (from first)
- 9 (from first)
- 10 (from second)

![Example Visualization](../images/QUE-011/example-1.png)

## Notes

- This is the queue version of merge in merge sort
- Always compare fronts of both queues
- Time complexity: O(n + m)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Merge, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void mergeQueues(int n, int[] q1, int m, int[] q2) {
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
        int m = sc.nextInt();
        int[] q2 = new int[m];
        for (int i = 0; i < m; i++) q2[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.mergeQueues(n, q1, m, q2);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def merge_queues(self, n, q1, m, q2):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    n = int(input_data[idx])
    idx += 1
    q1 = [int(x) for x in input_data[idx:idx+n]]
    idx += n
    m = int(input_data[idx])
    idx += 1
    q2 = [int(x) for x in input_data[idx:idx+m]]
    sol = Solution()
    sol.merge_queues(n, q1, m, q2)

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
    void mergeQueues(int n, vector<int>& q1, int m, vector<int>& q2) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n)) return 0;
    vector<int> q1(n);
    for (int i = 0; i < n; i++) cin >> q1[i];
    cin >> m;
    vector<int> q2(m);
    for (int i = 0; i < m; i++) cin >> q2[i];
    Solution sol;
    sol.mergeQueues(n, q1, m, q2);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  mergeQueues(n, q1, m, q2) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  let idx = 0;
  const n = parseInt(input[idx++]);
  const q1 = [];
  for (let i = 0; i < n; i++) q1.push(parseInt(input[idx++]));
  const m = parseInt(input[idx++]);
  const q2 = [];
  for (let i = 0; i < m; i++) q2.push(parseInt(input[idx++]));
  const sol = new Solution();
  sol.mergeQueues(n, q1, m, q2);
}

solve();
```
