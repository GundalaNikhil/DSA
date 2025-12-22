---
problem_id: NUM_MINIMAL_BASE_REPRESENTATION__6628
display_id: NUM-004
slug: minimal-base-representation
title: "Minimal Base Representation"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Bases
  - Optimization
tags:
  - number-theory
  - bases
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-004: Minimal Base Representation

## Problem Statement

Given an integer `x` (>= 2), find the smallest base `b` (2 <= b <= 36) such that the sum of digits of `x` in base `b` is minimized. If multiple bases yield the same minimal digit sum, choose the smallest base. Output `b` and the minimal digit sum.

![Problem Illustration](../images/NUM-004/problem-illustration.png)

## Input Format

- Single line: integer `x`

## Output Format

- Two integers: `b` and `digitSum`

## Constraints

- `2 <= x <= 10^12`
- `2 <= b <= 36`

## Example

**Input:**

```
31
```

**Output:**

```
5 3
```

**Explanation:**

31 in base 5 is 111, digit sum = 3. No smaller base gives a smaller digit sum.

![Example Visualization](../images/NUM-004/example-1.png)

## Notes

- Try all bases from 2 to 36
- Convert by repeated division and sum digits
- Time complexity: O(36 * log_b(x))
- Space complexity: O(1)

## Related Topics

Number Bases, Digit Sum, Search

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] minimalBase(long x) {
        // Your implementation here
        return new long[]{2, x};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        Solution solution = new Solution();
        long[] res = solution.minimalBase(x);
        System.out.println(res[0] + " " + res[1]);
        sc.close();
    }
}
```

### Python

```python
def minimal_base(x: int):
    # Your implementation here
    return 2, x

def main():
    x = int(input())
    b, s = minimal_base(x)
    print(b, s)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    pair<long long, long long> minimalBase(long long x) {
        // Your implementation here
        return {2, x};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x;
    cin >> x;
    Solution solution;
    auto res = solution.minimalBase(x);
    cout << res.first << " " << res.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function minimalBase(x) {
  // Your implementation here
  return [2, x];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const x = parseInt(data[0], 10);
  const res = minimalBase(x);
  console.log(res[0] + " " + res[1]);
});
```
