---
problem_id: PDS_PROBLEM_15__4501
display_id: PDS-015
slug: minhash-lsh-candidate-probability
title: "MinHash LSH Candidate Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - MinHash
  - LSH
tags:
  - probabilistic-ds
  - lsh
  - minhash
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-015: MinHash LSH Candidate Probability

## Problem Statement

In MinHash LSH with `b` bands and `r` rows per band, the probability that two sets with Jaccard similarity `s` become a candidate pair is:

```
P = 1 - (1 - s^r)^b
```

Compute `P`.

![Problem Illustration](../images/PDS-015/problem-illustration.png)

## Input Format

- Single line: integers `b`, `r`, and real `s`

## Output Format

- Single floating-point number: candidate probability

## Constraints

- `1 <= b, r <= 1000`
- `0 <= s <= 1`

## Example

**Input:**

```
5 2 0.5
```

**Output:**

```
0.762695
```

**Explanation:**

P = 1 - (1 - 0.5^2)^5 = 0.762695.

![Example Visualization](../images/PDS-015/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

MinHash, LSH, Similarity Search

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double computeCandidateProbability(int b, int r, double s) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int b = sc.nextInt();
        int r = sc.nextInt();
        double s = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.computeCandidateProbability(b, r, s)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def compute_candidate_probability(self, b, r, s):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    b = int(input_data[0])
    r = int(input_data[1])
    s = float(input_data[2])
    sol = Solution()
    print(format(sol.compute_candidate_probability(b, r, s), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    double computeCandidateProbability(int b, int r, double s) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int b, r;
    double s;
    if (!(cin >> b >> r >> s)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.computeCandidateProbability(b, r, s) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computeCandidateProbability(b, r, s) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const b = parseInt(input[0]);
  const r = parseInt(input[1]);
  const s = parseFloat(input[2]);
  const sol = new Solution();
  console.log(sol.computeCandidateProbability(b, r, s).toFixed(6));
}

solve();
```
