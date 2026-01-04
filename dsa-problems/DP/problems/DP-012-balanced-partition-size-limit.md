---
problem_id: DP_BAL_PART_SIZE__5120
display_id: DP-012
slug: balanced-partition-size-limit
title: "Balanced Partition With Size Limit"
difficulty: Medium
difficulty_score: 56
topics:
  - Dynamic Programming
  - Subset Sum
  - Optimization
tags:
  - dp
  - subset-sum
  - partition
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-012: Balanced Partition With Size Limit

## Problem Statement

You are given an array `a` of length `n` and an integer `D`. Partition the array into two groups (each element goes to exactly one group) such that:

- The absolute difference of the two group sums is at most `D`.
- Among all such valid partitions, minimize the size of the **larger** group.

Return the minimum possible larger-group size. If no valid partition exists, return `-1`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513332/dsa/dp/slhopnkq5djpuzkeit9k.jpg)

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers `a[i]`

## Output Format

Print one integer: the minimum larger-group size, or `-1` if impossible.

## Constraints

- `1 <= n <= 50`
- `-500 <= a[i] <= 500`
- `0 <= D <= 5000`

## Example

**Input:**

```
4 1
3 1 4 2
```

**Output:**

```
2
```

**Explanation:**

Partition into `{3,2}` and `{1,4}`:

- sums: 5 and 5, difference = 0 ≤ 1
- group sizes: 2 and 2, larger size = 2 (minimum possible)

![Example Visualization](../images/DP-012/example-1.png)

## Notes

- Groups can be empty, but that may be suboptimal. Check constraints carefully.
- Negative values are allowed; sums can be negative.
- We minimize the larger group size, **not** the difference (difference is constrained).

## Related Topics

Dynamic Programming, Subset Sum, Partitioning

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minLargerGroupSize(int n, int D, int[] a) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nDLine = br.readLine();
        if (nDLine == null) return;
        String[] nDParts = nDLine.trim().split("\\s+");
        int n = Integer.parseInt(nDParts[0]);
        int D = Integer.parseInt(nDParts[1]);

        int[] a = new int[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] aParts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(aParts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.minLargerGroupSize(n, D, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_larger_group_size(self, n, D, a):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    D = int(input_data[1])
    a = list(map(int, input_data[2:2+n]))

    sol = Solution()
    print(sol.min_larger_group_size(n, D, a))

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
    int minLargerGroupSize(int n, int D, const vector<int>& a) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, D;
    if (!(cin >> n >> D)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution sol;
    cout << sol.minLargerGroupSize(n, D, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minLargerGroupSize(n, D, a) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const D = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.minLargerGroupSize(n, D, a));
}

solve();
```
