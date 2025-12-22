---
problem_id: PDS_XOR_FILTERS__7789
display_id: PDS-013
slug: xor-filters
title: "XOR Filters"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - XOR Filters
  - False Positives
tags:
  - probabilistic-ds
  - xor-filter
  - false-positives
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-013: XOR Filters

## Problem Statement

An XOR filter stores fingerprints of `b` bits. The false positive rate is approximately:

```
FPR = 2^{-b}
```

Assume the filter uses `ceil(1.23 * n)` cells. Given `n` and `b`, compute:

- Total memory bits: `ceil(1.23 * n) * b`
- False positive rate `FPR`

![Problem Illustration](../images/PDS-013/problem-illustration.png)

## Input Format

- Single line: integers `n` and `b`

## Output Format

- Two values: `memory_bits` and `FPR`

## Constraints

- `1 <= n <= 10^6`
- `1 <= b <= 16`

## Example

**Input:**

```
1000 8
```

**Output:**

```
9840 0.003906
```

**Explanation:**

Cells = ceil(1.23 * 1000) = 1230. Memory = 1230 * 8 = 9840 bits. FPR = 1/256.

![Example Visualization](../images/PDS-013/example-1.png)

## Notes

- Use double precision for FPR
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

XOR Filters, Fingerprints, Approximate Membership

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public Object[] xorFilterStats(long n, int b) {
        // Your implementation here
        return new Object[]{0L, 0.0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int b = sc.nextInt();

        Solution solution = new Solution();
        Object[] res = solution.xorFilterStats(n, b);
        System.out.println(res[0] + " " + String.format("%.6f", (double)res[1]));
        sc.close();
    }
}
```

### Python

```python
def xor_filter_stats(n: int, b: int):
    # Your implementation here
    return 0, 0.0

def main():
    n, b = map(int, input().split())
    mem, fpr = xor_filter_stats(n, b)
    print(f"{mem} {fpr:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Solution {
public:
    pair<long long, double> xorFilterStats(long long n, int b) {
        // Your implementation here
        return {0, 0.0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int b;
    cin >> n >> b;
    Solution solution;
    auto res = solution.xorFilterStats(n, b);
    cout << res.first << " " << fixed << setprecision(6) << res.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function xorFilterStats(n, b) {
  // Your implementation here
  return [0, 0.0];
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
  const b = parseInt(data[1], 10);
  const res = xorFilterStats(n, b);
  console.log(res[0] + " " + res[1].toFixed(6));
});
```
