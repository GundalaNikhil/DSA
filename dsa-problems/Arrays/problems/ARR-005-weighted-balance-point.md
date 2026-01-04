---
problem_id: ARR_WEIGHTED_BALANCE_POINT__7742
display_id: ARR-005
slug: weighted-balance-point
title: "Weighted Balance Point"
difficulty: Medium
difficulty_score: 44
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-005: Weighted Balance Point

## Problem Statement

Find the smallest index i such that the weighted sum of elements to the left of i equals the weighted sum of elements to the right of i. The left side excludes i and is multiplied by L, the right side excludes i and is multiplied by R.

![Problem Illustration](../images/ARR-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: two integers L and R

## Output Format

Print the smallest index i (0-based) that satisfies the condition, or -1.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`
- `1 <= L, R <= 1000000`

## Example

**Input:**

```
5
2 3 -1 3 2
2 1
```

**Output:**

```
2
```

**Explanation:**

At i = 2, left sum is 5 and right sum is 8. 5 _ 2 == 8 _ 1, so the answer is 2.

![Example Visualization](../images/ARR-005/example-1.png)

## Notes

- Use 64-bit integers to avoid overflow.
- Left and right sums exclude index i.

## Related Topics

Arrays, Prefix Sum, Math

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int findWeightedBalancePoint(int n, int[] a, int l, int r) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] a = new int[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(parts[i]);
            }
        }

        String lrLine = br.readLine();
        if (lrLine == null) return;
        String[] lrParts = lrLine.trim().split("\\s+");
        int l = Integer.parseInt(lrParts[0]);
        int r = Integer.parseInt(lrParts[1]);

        Solution sol = new Solution();
        System.out.println(sol.findWeightedBalancePoint(n, a, l, r));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_weighted_balance_point(self, n, a, l, r):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    l = int(input_data[n+1])
    r = int(input_data[n+2])

    sol = Solution()
    print(sol.find_weighted_balance_point(n, a, l, r))

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
    int findWeightedBalancePoint(int n, vector<int>& a, int l, int r) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int l, r;
    cin >> l >> r;

    Solution sol;
    cout << sol.findWeightedBalancePoint(n, a, l, r) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findWeightedBalancePoint(n, a, l, r) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(input[idx++]));
  }
  const l = parseInt(input[idx++]);
  const r = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.findWeightedBalancePoint(n, a, l, r));
}

solve();
```
