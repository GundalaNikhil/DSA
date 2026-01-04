---
problem_id: ARR_PREFIX_AVG__4252
display_id: ARR-001
slug: snack-restock-snapshot
title: "Snack Restock Snapshot"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-001: Snack Restock Snapshot

## Problem Statement

You are given an array of daily deliveries. For each day i, compute the average of all deliveries from day 0 to day i (inclusive), rounded down to an integer.
Return the list of prefix averages in order.

![Problem Illustration](../images/ARR-001/problem-illustration.png)

## Input Format

- First line: integer n, the number of days
- Second line: n space-separated integers arr[i]

## Output Format

Print n integers: the prefix averages, in order, space-separated.

## Constraints

- `1 <= n <= 100000`
- `0 <= arr[i] <= 1000000`

## Example

**Input:**

```
4
4 6 6 0
```

**Output:**

```
4 5 5 4
```

**Explanation:**

Running sums are 4, 10, 16, 16. Dividing by 1, 2, 3, 4 and rounding down gives
4, 5, 5, 4.

![Example Visualization](../images/ARR-001/example-1.png)

## Notes

- Use 64-bit arithmetic for the running sum.
- Output values are integers using floor division.

## Related Topics

Arrays, Prefix Sum, Math

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] prefixAverages(int n, int[] arr) {
        // Implement here
        return new long[0];
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

        Solution sol = new Solution();
        long[] result = sol.prefixAverages(n, arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def prefix_averages(self, n, arr):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))

    sol = Solution()
    result = sol.prefix_averages(n, arr)

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
    vector<long long> prefixAverages(int n, vector<int>& arr) {
        // Implement here
        return {};
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

    Solution sol;
    vector<long long> result = sol.prefixAverages(n, arr);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
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
  prefixAverages(n, arr) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  const result = sol.prefixAverages(n, arr);

  console.log(result.join(" "));
}

solve();
```
