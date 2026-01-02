---
problem_id: PDS_BLOOMIER_FILTER__6841
display_id: PDS-012
slug: bloomier-filter
title: "Bloomier Filter Key-Value"
difficulty: Hard
difficulty_score: 65
topics:
  - Probabilistic Data Structures
  - Bloomier Filter
  - False Positives
tags:
  - probabilistic-ds
  - bloomier
  - key-value
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-012: Bloomier Filter Key-Value

## Problem Statement

A Bloomier filter stores key-value mappings with an `r`-bit value cell. The false positive probability for a random non-key is approximately:

```
FPR = 2^{-r}
```

Given the table size `m` and bits per cell `r`, compute:

- Total memory in bits: `m * r`
- False positive probability `FPR`

![Problem Illustration](../images/PDS-012/problem-illustration.png)

## Input Format

- Single line: integers `m` and `r`

## Output Format

- Two values: `memory_bits` and `FPR`

## Constraints

- `1 <= m <= 10^6`
- `1 <= r <= 32`

## Example

**Input:**

```
6 4
```

**Output:**

```
24 0.062500
```

**Explanation:**

Memory = 6 * 4 = 24 bits, FPR = 1/16 = 0.0625.

![Example Visualization](../images/PDS-012/example-1.png)

## Notes

- Use double precision for FPR
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Bloomier Filter, Key-Value Sketches

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public Object[] bloomierStats(long m, int r) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long m = sc.nextLong();
            int r = sc.nextInt();
    
            Solution solution = new Solution();
            Object[] res = solution.bloomierStats(m, r);
            System.out.println(res[0] + " " + String.format("%.6f", (double)res[1]));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def bloomier_stats(m: int, r: int):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    r = int(data[1])
    mem, fpr = bloomier_stats(m, r)
    print(f"{mem} {fpr:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    pair<long long, double> bloomierStats(long long m, int r) {
        long long mem = m * r;
        double fpr = pow(2.0, -r);
        return {mem, fpr};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    int r;
    if (cin >> m >> r) {
        Solution solution;
        auto res = solution.bloomierStats(m, r);
        cout << res.first << " " << fixed << setprecision(6) << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function bloomierStats(m, r) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const m = parseInt(data[0], 10);
  const r = parseInt(data[1], 10);
  const res = bloomierStats(m, r);
  console.log(res[0] + " " + res[1].toFixed(6));
});
```

