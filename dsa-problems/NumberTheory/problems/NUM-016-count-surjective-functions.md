---
problem_id: NUM_COUNT_SURJECTIVE_FUNCTIONS__7773
display_id: NUM-016
slug: count-surjective-functions
title: "Count Surjective Functions"
difficulty: Medium
difficulty_score: 55
topics:
  - Number Theory
  - Combinatorics
  - Inclusion-Exclusion
tags:
  - number-theory
  - combinatorics
  - inclusion-exclusion
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-016: Count Surjective Functions

## Problem Statement

Count the number of surjective (onto) functions from an n-element set to a k-element set. Return the result modulo `1000000007`.

![Problem Illustration](../images/NUM-016/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single integer: number of surjective functions modulo `1000000007`

## Constraints

- `1 <= k <= n <= 30`

## Example

**Input:**

```
3 2
```

**Output:**

```
6
```

**Explanation:**

There are 2^3 total functions. Remove the 2 functions that map all elements to a single value.

2^3 - 2 = 6.

![Example Visualization](../images/NUM-016/example-1.png)

## Notes

- Use inclusion-exclusion: sum\_{i=0..k} (-1)^i C(k,i) (k-i)^n
- Time complexity: O(k^2)
- Space complexity: O(k)

## Related Topics

Inclusion-Exclusion, Combinatorics, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countSurjective(int n, int k) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countSurjective(n, k));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_surjective(self, n, k):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    sol = Solution()
    print(sol.count_surjective(n, k))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    int countSurjective(int n, int k) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    Solution sol;
    cout << sol.countSurjective(n, k) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countSurjective(n, k) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const sol = new Solution();
  console.log(sol.countSurjective(n, k).toString());
}

solve();
```
