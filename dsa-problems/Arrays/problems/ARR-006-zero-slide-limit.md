---
problem_id: ARR_ZERO_SLIDE_LIMIT__4908
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Medium
difficulty_score: 34
topics:
  - Arrays
  - Two Pointers
  - Simulation
tags:
  - arrays
  - two-pointers
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-006: Zero Slide With Limit

## Problem Statement

Move all zeros to the end of the array, but you may perform at most m swaps in total. Once the swap budget is exhausted, stop and return the current array.

![Problem Illustration](../images/ARR-006/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer m, the maximum number of swaps

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 1000000000`

## Example

**Input:**

```
5
0 4 0 5 7
1
```

**Output:**

```
4 0 0 5 7
```

**Explanation:**

One swap moves 4 left of a zero, and the swap budget is exhausted.

![Example Visualization](../images/ARR-006/example-1.png)

## Notes

- A swap is counted when a non-zero moves left across a zero.
- Stop immediately when the swap count reaches m.

## Related Topics

Arrays, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] slideZerosWithLimit(int n, int[] arr, int m) {
        // Implement here
        return new int[0];
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

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        Solution sol = new Solution();
        int[] result = sol.slideZerosWithLimit(n, arr, m);

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
    def slide_zeros_with_limit(self, n, arr, m):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    m = int(input_data[n+1])

    sol = Solution()
    result = sol.slide_zeros_with_limit(n, arr, m)

    print(*(result))

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
    vector<int> slideZerosWithLimit(int n, vector<int>& arr, int m) {
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

    int m;
    cin >> m;

    Solution sol;
    vector<int> result = sol.slideZerosWithLimit(n, arr, m);

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
  slideZerosWithLimit(n, arr, m) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[idx++]));
  }
  const m = parseInt(input[idx++]);

  const sol = new Solution();
  const result = sol.slideZerosWithLimit(n, arr, m);

  console.log(result.join(" "));
}

solve();
```
