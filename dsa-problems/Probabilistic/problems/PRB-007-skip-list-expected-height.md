---
problem_id: PRB_SKIP_LIST_EXPECTED_HEIGHT__6591
display_id: PRB-007
slug: skip-list-expected-height
title: "Skip List Expected Height"
difficulty: Medium
difficulty_score: 45
topics:
  - Probability
  - Data Structures
  - Logs
tags:
  - probability
  - skip-list
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-007: Skip List Expected Height

## Problem Statement

A skip list promotes each node to the next level independently with probability `p`. Given `n` inserted elements, approximate the expected maximum height of the skip list using:

```
H = log(n) / log(1/p)
```

Output `H`.

![Problem Illustration](../images/PRB-007/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `p`

## Output Format

- Single floating-point number: expected height

## Constraints

- `1 <= n <= 10^6`
- `0 < p < 1`

## Example

**Input:**

```
1024 0.5
```

**Output:**

```
10
```

**Explanation:**

log_{1/p}(n) = log_2(1024) = 10.

![Example Visualization](../images/PRB-007/example-1.png)

## Notes

- Use natural logs in computation
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Skip Lists, Expected Value, Logarithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double expectedHeight(int n, double p) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double p = sc.nextDouble();

        Solution solution = new Solution();
        System.out.println(solution.expectedHeight(n, p));
        sc.close();
    }
}
```

### Python

```python
import math

def expected_height(n: int, p: float) -> float:
    # Your implementation here
    return 0.0

def main():
    n, p = input().split()
    print(expected_height(int(n), float(p)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    double expectedHeight(int n, double p) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    double p;
    cin >> n >> p;
    Solution solution;
    cout << solution.expectedHeight(n, p) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function expectedHeight(n, p) {
  // Your implementation here
  return 0.0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const p = parseFloat(data[1]);
  console.log(expectedHeight(n, p));
});
```
