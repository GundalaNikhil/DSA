---
problem_id: NUM_MINIMAL_SPLIT_EQUAL_PRODUCT__3562
display_id: NUM-012
slug: minimal-split-equal-product
title: "Minimal Split for Equal Product"
difficulty: Medium
difficulty_score: 46
topics:
  - Number Theory
  - Parsing
  - Optimization
tags:
  - number-theory
  - digits
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-012: Minimal Split for Equal Product

## Problem Statement

Given an integer `x`, split its decimal digits into two non-empty parts (preserving order in each part). Interpret each part as a decimal integer (leading zeros allowed). Among all splits with non-zero product, return the minimal product.

![Problem Illustration](../images/NUM-012/problem-illustration.png)

## Input Format

- Single line: integer `x`

## Output Format

- Single integer: minimal non-zero product

## Constraints

- `10 <= x <= 10^12`
- At least one split yields a non-zero product

## Example

**Input:**

```
1234
```

**Output:**

```
234
```

**Explanation:**

Splits:

- 1 | 234 -> 1 \* 234 = 234
- 12 | 34 -> 12 \* 34 = 408
- 123 | 4 -> 123 \* 4 = 492

Minimum non-zero product is 234.

![Example Visualization](../images/NUM-012/example-1.png)

## Notes

- Try all split positions in the digit string
- Convert substrings to integers and track minimal product
- Time complexity: O(len(x)^2) if conversion is repeated; O(len(x)) with incremental parsing
- Space complexity: O(1)

## Related Topics

Digit Parsing, Brute Force Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minimalSplitProduct(String x) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String x = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.minimalSplitProduct(x));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def minimal_split_product(self, x_str):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x_str = input_data[0]
    sol = Solution()
    print(sol.minimal_split_product(x_str))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minimalSplitProduct(string x) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string x;
    if (!(cin >> x)) return 0;
    Solution sol;
    cout << sol.minimalSplitProduct(x) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minimalSplitProduct(x) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const sol = new Solution();
  console.log(sol.minimalSplitProduct(input).toString());
}

solve();
```
