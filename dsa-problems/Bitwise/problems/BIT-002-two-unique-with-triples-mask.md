---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-002: Two Unique With Triple Others Under Mask

## Problem Statement

Every number appears exactly three times except two distinct numbers that appear once each. You are also given a mask M; the two uniques are guaranteed to differ in at least one bit that is set in M. Find the two unique values.

![Problem Illustration](../images/BIT-002/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer M

## Output Format

Print the two unique values in ascending order.

## Constraints

- `2 <= n <= 200000`
- `0 <= M <= 1000000000`

## Example

**Input:**

```
8
5 5 5 9 9 9 3 6
1
```

**Output:**

```
3 6
```

**Explanation:**

The only values appearing once are 3 and 6, so they are returned in ascending
order.

![Example Visualization](../images/BIT-002/example-1.png)

## Notes

- The output must be in ascending order for deterministic checking.
- The mask M guarantees a separating bit for partitioning.

## Related Topics

Bitwise Operations, Counting Bits

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] findTwoUniques(int n, long[] a, long m) {
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

        long[] a = new long[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(parts[i]);
            }
        }

        String mLine = br.readLine();
        if (mLine == null) return;
        long m = Long.parseLong(mLine.trim());

        Solution sol = new Solution();
        long[] res = sol.findTwoUniques(n, a, m);
        System.out.println(res[0] + " " + res[1]);
    }
}
```

### Python

```python
import sys

class Solution:
    def find_two_uniques(self, n, a, m):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    m = int(input_data[n+1])

    sol = Solution()
    res = sol.find_two_uniques(n, a, m)
    print(f"{res[0]} {res[1]}")

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
    pair<long long, long long> findTwoUniques(int n, vector<long long>& a, long long m) {
        // Implement here
        return {0, 0};
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

    long long m_mask;
    cin >> m_mask;

    Solution sol;
    pair<long long, long long> res = sol.findTwoUniques(n, a, m_mask);
    cout << res.first << " " << res.second << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findTwoUniques(n, a, m) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(BigInt(input[idx++]));
  }
  const m = BigInt(input[idx++]);

  const sol = new Solution();
  const res = sol.findTwoUniques(n, a, m);
  console.log(res[0].toString() + " " + res[1].toString());
}

solve();
```
