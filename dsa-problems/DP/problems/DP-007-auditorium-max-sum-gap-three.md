---
problem_id: DP_MAXSUM_GAP3__7706
display_id: DP-007
slug: auditorium-max-sum-gap-three
title: "Auditorium Max Sum With Gap Three"
difficulty: Medium
difficulty_score: 45
topics:
  - Dynamic Programming
  - Array
  - Optimization
tags:
  - dp
  - arrays
  - maximum-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-007: Auditorium Max Sum With Gap Three

## Problem Statement

You are given an integer array `a` of length `n`. You want to select a subset of indices to maximize the sum of selected values, with the constraint:

For any two selected indices `i` and `j` (`i != j`), `|i - j| >= 3`.

In other words, if you pick index `i`, you cannot pick `i-1`, `i-2`, `i+1`, or `i+2`.

Return the maximum possible sum.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513329/dsa/dp/h8i7w3bhazyte9aqd0pc.jpg)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `a[i]`

## Output Format

Print one integer: the maximum sum achievable under the gap constraint.

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
5
4 1 2 9 3
```

**Output:**

```
13
```

**Explanation:**

One optimal selection is indices `0` and `3`:

- `a[0] + a[3] = 4 + 9 = 13`
- Distance between indices: `3` (allowed)

So the answer is `13`.

![Example Visualization](../images/DP-007/example-1.png)

## Notes

- You are allowed to pick **no elements**; in that case the sum is `0`. This matters when all numbers are negative.
- This is a “House Robber”-style DP with a skip of 2 indices between picks.
- Use 64-bit integer arithmetic for sums.

## Related Topics

Dynamic Programming, Array DP, Maximum Sum

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maximizeSum(int n, long[] a) {
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

        long[] a = new long[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] aParts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(aParts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.maximizeSum(n, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def maximize_sum(self, n, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:1+n]))

    sol = Solution()
    print(sol.maximize_sum(n, a))

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
    long long maximizeSum(int n, const vector<long long>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution sol;
    cout << sol.maximizeSum(n, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maximizeSum(n, a) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(BigInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.maximizeSum(n, a).toString());
}

solve();
```
