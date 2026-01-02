---
problem_id: PDS_COUNT_MIN_SKETCH__4815
display_id: PDS-004
slug: count-min-sketch
title: "Count-Min Sketch Error Bound"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Sketches
  - Error Bounds
tags:
  - probabilistic-ds
  - sketch
  - error-bound
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-004: Count-Min Sketch Error Bound

## Problem Statement

Given desired error `epsilon` and failure probability `delta`, compute parameters for a Count-Min Sketch:

```
w = ceil(e / epsilon)
d = ceil(ln(1 / delta))
```

Output `w` and `d`.

![Problem Illustration](../images/PDS-004/problem-illustration.png)

## Input Format

- Single line: real `epsilon` and real `delta`

## Output Format

- Two integers: `w` and `d`

## Constraints

- `0 < epsilon < 1`
- `0 < delta < 1`

## Example

**Input:**

```
0.01 0.01
```

**Output:**

```
272 5
```

**Explanation:**

w = ceil(e / 0.01) = 272, d = ceil(ln(100)) = 5.

![Example Visualization](../images/PDS-004/example-1.png)

## Notes

- Use natural log
- Time complexity: O(1)

## Related Topics

Count-Min Sketch, Approximate Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] cmsParams(double epsilon, double delta) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextDouble()) {
            double epsilon = sc.nextDouble();
            double delta = sc.nextDouble();

            Solution solution = new Solution();
            long[] res = solution.cmsParams(epsilon, delta);
            System.out.println(res[0] + " " + res[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def cms_params(epsilon: float, delta: float):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    epsilon = float(data[0])
    delta = float(data[1])
    w, d = cms_params(epsilon, delta)
    print(f"{w} {d}")

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
    pair<long long, long long> cmsParams(double epsilon, double delta) {
        long long w = (long long) ceil(exp(1.0) / epsilon);
        long long d = (long long) ceil(log(1.0 / delta));
        return {w, d};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double epsilon, delta;
    if (cin >> epsilon >> delta) {
        Solution solution;
        auto res = solution.cmsParams(epsilon, delta);
        cout << res.first << " " << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function cmsParams(epsilon, delta) {
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
  const epsilon = parseFloat(data[0]);
  const delta = parseFloat(data[1]);
  const res = cmsParams(epsilon, delta);
  console.log(res[0] + " " + res[1]);
});
```

