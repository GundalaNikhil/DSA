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
    public long solve(int[] arr) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            long result = solution.solve(arr);
            System.out.println(result);
        }
        sc.close();
    }
}
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long solve(const vector<int>& arr) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        Solution solution;
        long long result = solution.solve(arr);
        cout << result << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(arr) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.solve(arr);
  console.log(result);
});
```

