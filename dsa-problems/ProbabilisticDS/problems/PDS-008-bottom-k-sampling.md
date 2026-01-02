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
    public double jaccardEstimate(double[] a, double[] b) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            double[] a = new double[k];
            double[] b = new double[k];
            for (int i = 0; i < k; i++) a[i] = sc.nextDouble();
            for (int i = 0; i < k; i++) b[i] = sc.nextDouble();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.jaccardEstimate(a, b)));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def jaccard_estimate(a, b):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        a = []
        for _ in range(k):
            a.append(float(next(iterator)))
        b = []
        for _ in range(k):
            b.append(float(next(iterator)))
            
        print(f"{jaccard_estimate(a, b):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double jaccardEstimate(const vector<double>& a, const vector<double>& b) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<double> a(k), b(k);
        for (int i = 0; i < k; i++) cin >> a[i];
        for (int i = 0; i < k; i++) cin >> b[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.jaccardEstimate(a, b) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function jaccardEstimate(a, b) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const k = parseInt(data[idx++], 10);
  const a = [];
  const b = [];
  for (let i = 0; i < k; i++) a.push(parseFloat(data[idx++]));
  for (let i = 0; i < k; i++) b.push(parseFloat(data[idx++]));
  console.log(jaccardEstimate(a, b).toFixed(6));
});
```

