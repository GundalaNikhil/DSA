---
problem_id: ARR_POWER_WINDOW_DROP__2879
display_id: ARR-016
slug: power-window-with-drop
title: "Power Window With Drop"
difficulty: Medium
difficulty_score: 49
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-016: Power Window With Drop

## Problem Statement

Given positive integers and a window size k, find the maximum sum of any window after optionally removing one element from that window (you may also remove none).

![Problem Illustration](../images/ARR-016/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer k

## Output Format

Print the maximum adjusted window sum.

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- `1 <= arr[i] <= 1000000000`

## Example

**Input:**

```
5
2 1 5 3 2
3
```

**Output:**

```
10
```

**Explanation:**

Window [5, 3, 2] sums to 10 with no drop, which is the maximum.

![Example Visualization](../images/ARR-016/example-1.png)

## Notes

- You may drop at most one element per window.
- All elements are positive.

## Related Topics

Sliding Window, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxPowerWindow(int n, int[] arr, int k) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] arr = new int[n];
        String arrLine = br.readLine();
        if (arrLine != null) {
            String[] parts = arrLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(parts[i]);
            }
        }

        String kLine = br.readLine();
        if (kLine == null) return;
        int k = Integer.parseInt(kLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.maxPowerWindow(n, arr, k));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_power_window(self, n, arr, k):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    if len(input_data) > n+1:
        k = int(input_data[n+1])
    else:
        k = 0 # fall back

    sol = Solution()
    print(sol.max_power_window(n, arr, k))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxPowerWindow(int n, vector<int>& arr, int k) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int k;
    cin >> k;

    Solution sol;
    cout << sol.maxPowerWindow(n, arr, k) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxPowerWindow(n, arr, k) {
    // Implement here
    return BigInt(0);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(readInt());
  const k = readInt();

  const sol = new Solution();
  console.log(sol.maxPowerWindow(n, arr, k).toString());
}

solve();
```
