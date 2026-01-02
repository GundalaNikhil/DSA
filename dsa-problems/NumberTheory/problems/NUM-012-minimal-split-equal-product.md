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

- 1 | 234 -> 1 * 234 = 234
- 12 | 34 -> 12 * 34 = 408
- 123 | 4 -> 123 * 4 = 492

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
    public long minimalProductSplit(long x) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x = sc.nextLong();
            Solution solution = new Solution();
            System.out.println(solution.minimalProductSplit(x));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def minimal_product_split(x: int) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x = int(data[0])
    print(minimal_product_split(x))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long minimalProductSplit(long long x) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x;
    if (cin >> x) {
        Solution solution;
        cout << solution.minimalProductSplit(x) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function minimalProductSplit(x) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  // Use BigInt for input parsing to handle 10^12 safely in JS (though Number is fine up to 9*10^15)
  // But consistent BigInt usage is better.
  const x = BigInt(data[0]);
  console.log(minimalProductSplit(x));
});
```

