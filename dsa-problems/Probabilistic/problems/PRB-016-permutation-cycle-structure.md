---
problem_id: PRB_PERMUTATION_CYCLE_STRUCTURE__9150
display_id: PRB-016
slug: permutation-cycle-structure
title: "Random Permutation Cycle Structure"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Combinatorics
  - Expectations
tags:
  - probability
  - permutations
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-016: Random Permutation Cycle Structure

## Problem Statement

For a uniformly random permutation of `n` elements:

- The expected number of cycles of length exactly `k` is `1/k`
- The expected length of the longest cycle is approximately `0.624330 * n`

Given `n` and `k`, output both values.

![Problem Illustration](../images/PRB-016/problem-illustration.png)

## Input Format

- Single line: integers `n` and `k`

## Output Format

- Two floating-point numbers: expected cycles of length `k`, and expected longest cycle length

## Constraints

- `1 <= k <= n <= 100000`

## Example

**Input:**

```
5 2
```

**Output:**

```
0.500000 3.121650
```

**Explanation:**

Expected cycles of length 2 is 1/2. Expected longest cycle length ≈ 0.624330 * 5.

![Example Visualization](../images/PRB-016/example-1.png)

## Notes

- Use the constant 0.624330 for the longest cycle approximation
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Random Permutations, Cycle Decomposition, Expectations

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void cycleStructure(int n, int k) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        Solution sol = new Solution();
        sol.cycleStructure(n, k);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def cycle_structure(self, n, k):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    sol = Solution()
    sol.cycle_structure(n, k)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>

using namespace std;

class Solution {
public:
    void cycleStructure(int n, int k) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    Solution sol;
    sol.cycleStructure(n, k);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  cycleStructure(n, k) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const sol = new Solution();
  sol.cycleStructure(n, k);
}

solve();
```
