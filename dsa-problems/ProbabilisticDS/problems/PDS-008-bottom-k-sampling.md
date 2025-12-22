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
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        double[] a = new double[k];
        double[] b = new double[k];
        for (int i = 0; i < k; i++) a[i] = sc.nextDouble();
        for (int i = 0; i < k; i++) b[i] = sc.nextDouble();

        Solution solution = new Solution();
        System.out.println(solution.jaccardEstimate(a, b));
        sc.close();
    }
}
```

### Python

```python
def jaccard_estimate(a, b):
    # Your implementation here
    return 0.0

def main():
    k = int(input())
    a = list(map(float, input().split()))
    b = list(map(float, input().split()))
    print(f"{jaccard_estimate(a, b):.6f}")

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
    double jaccardEstimate(const vector<double>& a, const vector<double>& b) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    cin >> k;
    vector<double> a(k), b(k);
    for (int i = 0; i < k; i++) cin >> a[i];
    for (int i = 0; i < k; i++) cin >> b[i];

    Solution solution;
    cout << solution.jaccardEstimate(a, b) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function jaccardEstimate(a, b) {
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
  let idx = 0;
  const k = parseInt(data[idx++], 10);
  const a = [];
  const b = [];
  for (let i = 0; i < k; i++) a.push(parseFloat(data[idx++]));
  for (let i = 0; i < k; i++) b.push(parseFloat(data[idx++]));
  console.log(jaccardEstimate(a, b).toFixed(6));
});
```
