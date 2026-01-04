---
problem_id: BIT_COUNT_SETBITS_INDEXED_XOR__8407
display_id: BIT-007
slug: count-set-bits-indexed-xor
title: "Count Set Bits Of Indexed XOR"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - popcount
  - mathematics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-007: Count Set Bits Of Indexed XOR

## Problem Statement

Let b[i] = i XOR a[i] for i from 0 to n-1. Compute the total number of set bits across all values in b.

![Problem Illustration](../images/BIT-007/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the total count of set bits in b.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
2
0 2
```

**Output:**

```
2
```

**Explanation:**

b = [0 XOR 0, 1 XOR 2] = [0, 3]. The popcounts are 0 and 2, totaling 2.

![Example Visualization](../images/BIT-007/example-1.png)

## Notes

- Indices are 0-based.
- Use 64-bit arithmetic for the total.

## Related Topics

Bitwise Operations, Counting Bits

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long countTotalSetBits(int n, int[] a) {
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

        int[] a = new int[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(parts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.countTotalSetBits(n, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_total_set_bits(self, n, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.count_total_set_bits(n, a))

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
    long long countTotalSetBits(int n, const vector<int>& a) {
        // Implement here
        return 0;
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

    Solution sol;
    cout << sol.countTotalSetBits(n, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countTotalSetBits(n, a) {
    // Implement here
    return BigInt(0);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.countTotalSetBits(n, a).toString());
}

solve();
```
