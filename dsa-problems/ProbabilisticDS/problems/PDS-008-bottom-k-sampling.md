---
problem_id: PDS_BOTTOM_K_SAMPLING__6358
display_id: PDS-008
slug: bottom-k-sampling
title: "Bottom-k Sampling (Min-Hash)"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - MinHash
  - Similarity Estimation
tags:
  - probabilistic-ds
  - minhash
  - similarity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-008: Bottom-k Sampling (Min-Hash)

## Problem Statement

You are given two MinHash signatures of length `k`, generated using the same hash functions. Estimate the Jaccard similarity as the fraction of positions where the signatures match.

![Problem Illustration](../images/PDS-008/problem-illustration.png)

## Input Format

- First line: integer `k`
- Second line: `k` floating-point numbers (signature A)
- Third line: `k` floating-point numbers (signature B)

## Output Format

- Single floating-point number: estimated Jaccard similarity

## Constraints

- `1 <= k <= 100000`
- Hash values are in [0, 1)

## Example

**Input:**

```
5
0.1 0.2 0.3 0.4 0.5
0.1 0.25 0.3 0.6 0.7
```

**Output:**

```
0.4
```

**Explanation:**

Matches at positions 1 and 3, so estimate = 2 / 5 = 0.4.

![Example Visualization](../images/PDS-008/example-1.png)

## Notes

- Use exact position matches
- Accept answers with absolute error <= 1e-6
- Time complexity: O(k)

## Related Topics

MinHash, Jaccard Similarity, Sketches

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateJaccard(int k, double[] sigA, double[] sigB) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        double[] sigA = new double[k];
        for (int i = 0; i < k; i++) sigA[i] = sc.nextDouble();
        double[] sigB = new double[k];
        for (int i = 0; i < k; i++) sigB[i] = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.estimateJaccard(k, sigA, sigB)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def estimate_jaccard(self, k, sig_a, sig_b):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    sig_a = [float(x) for x in input_data[1:1+k]]
    sig_b = [float(x) for x in input_data[1+k:1+2*k]]
    sol = Solution()
    print(format(sol.estimate_jaccard(k, sig_a, sig_b), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double estimateJaccard(int k, const vector<double>& sigA, const vector<double>& sigB) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    if (!(cin >> k)) return 0;
    vector<double> sigA(k), sigB(k);
    for (int i = 0; i < k; i++) cin >> sigA[i];
    for (int i = 0; i < k; i++) cin >> sigB[i];
    Solution sol;
    cout << fixed << setprecision(6) << sol.estimateJaccard(k, sigA, sigB) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateJaccard(k, sigA, sigB) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const k = parseInt(input[0]);
  const sigA = [];
  for (let i = 0; i < k; i++) sigA.push(parseFloat(input[1 + i]));
  const sigB = [];
  for (let i = 0; i < k; i++) sigB.push(parseFloat(input[1 + k + i]));
  const sol = new Solution();
  console.log(sol.estimateJaccard(k, sigA, sigB).toFixed(6));
}

solve();
```
