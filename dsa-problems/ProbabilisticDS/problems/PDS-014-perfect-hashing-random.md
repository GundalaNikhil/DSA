---
problem_id: PDS_PERFECT_HASHING_RANDOM__6203
display_id: PDS-014
slug: perfect-hashing-random
title: "Perfect Hashing via Randomization"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Perfect Hashing
  - Randomization
tags:
  - probabilistic-ds
  - perfect-hashing
  - randomized
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-014: Perfect Hashing via Randomization

## Problem Statement

In two-level perfect hashing (FKS), if bucket sizes are `s_1, s_2, ..., s_t`, the total second-level table size is:

```
S = sum s_i^2
```

Compute `S` and report whether `S <= 4n`.

![Problem Illustration](../images/PDS-014/problem-illustration.png)

## Input Format

- First line: integer `n` (number of keys) and integer `t` (number of buckets)
- Second line: `t` integers (bucket sizes)

## Output Format

- Two values: `S` and `YES` if `S <= 4n`, otherwise `NO`

## Constraints

- `1 <= n <= 10^6`
- `1 <= t <= n`
- Sum of bucket sizes = n

## Example

**Input:**

```
6 3
2 1 3
```

**Output:**

```
14 YES
```

**Explanation:**

S = 4 + 1 + 9 = 14, and 4n = 24, so YES.

![Example Visualization](../images/PDS-014/example-1.png)

## Notes

- Use 64-bit integers for S
- Time complexity: O(t)

## Related Topics

Perfect Hashing, FKS, Randomization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void computeTotalTableSize(int n, int t, int[] s) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int t = sc.nextInt();
        int[] s = new int[t];
        for (int i = 0; i < t; i++) s[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.computeTotalTableSize(n, t, s);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def compute_total_table_size(self, n, t, s):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    t = int(input_data[1])
    s = [int(x) for x in input_data[2:2+t]]
    sol = Solution()
    sol.compute_total_table_size(n, t, s)

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
    void computeTotalTableSize(int n, int t, const vector<int>& s) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, t;
    if (!(cin >> n >> t)) return 0;
    vector<int> s(t);
    for (int i = 0; i < t; i++) cin >> s[i];
    Solution sol;
    sol.computeTotalTableSize(n, t, s);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computeTotalTableSize(n, t, s) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const t = parseInt(input[1]);
  const s = [];
  for (let i = 0; i < t; i++) s.push(parseInt(input[2 + i]));
  const sol = new Solution();
  sol.computeTotalTableSize(n, t, s);
}

solve();
```
