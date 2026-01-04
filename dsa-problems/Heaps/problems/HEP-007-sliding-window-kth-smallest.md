---
problem_id: HEP_SLIDING_WINDOW_KTH_SMALLEST__2665
display_id: HEP-007
slug: sliding-window-kth-smallest
title: "Sliding Window Kth Smallest"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Sliding Window
  - Order Statistics
tags:
  - heaps
  - sliding-window
  - order-statistics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-007: Sliding Window Kth Smallest

## Problem Statement

Given an array `arr` of length `n`, a window size `w`, and an integer `k`, output the `k`-th smallest element in every contiguous window of size `w`.

![Problem Illustration](../images/HEP-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `w`, and `k`
- Second line: `n` space-separated integers

## Output Format

- `n - w + 1` integers: the `k`-th smallest value for each window

## Constraints

- `1 <= n <= 200000`
- `1 <= w <= n`
- `1 <= k <= w`
- `-10^9 <= arr[i] <= 10^9`

## Example

**Input:**

```
5 3 2
1 3 2 6 4
```

**Output:**

```
2 3 4
```

**Explanation:**

Windows:

- [1, 3, 2] -> sorted [1, 2, 3], 2nd smallest = 2
- [3, 2, 6] -> sorted [2, 3, 6], 2nd smallest = 3
- [2, 6, 4] -> sorted [2, 4, 6], 2nd smallest = 4

![Example Visualization](../images/HEP-007/example-1.png)

## Notes

- Use two heaps to maintain lower and upper partitions
- Apply lazy deletion when elements leave the window
- Each window update runs in O(log w)
- Space complexity: O(w)

## Related Topics

Heaps, Sliding Window, Order Statistics, Median Maintenance

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> slidingWindowKthSmallest(int n, int w, int k, int[] arr) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int w = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);

        int[] arr = new int[n];
        String[] vals = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(vals[i]);
        }

        Solution sol = new Solution();
        List<Integer> result = sol.slidingWindowKthSmallest(n, w, k, arr);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < result.size(); i++) {
            out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def sliding_window_kth_smallest(self, n, w, k, arr):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    w = int(input_data[1])
    k = int(input_data[2])
    arr = list(map(int, input_data[3:3+n]))

    sol = Solution()
    result = sol.sliding_window_kth_smallest(n, w, k, arr)
    print(*(result))

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
    vector<int> slidingWindowKthSmallest(int n, int w, int k, vector<int>& arr) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, w, k;
    if (!(cin >> n >> w >> k)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution sol;
    vector<int> result = sol.slidingWindowKthSmallest(n, w, k, arr);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  slidingWindowKthSmallest(n, w, k, arr) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const w = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  const result = sol.slidingWindowKthSmallest(n, w, k, arr);
  console.log(result.join(" "));
}

solve();
```
