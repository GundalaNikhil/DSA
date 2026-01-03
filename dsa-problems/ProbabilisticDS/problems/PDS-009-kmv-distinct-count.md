---
problem_id: PDS_KMV_DISTINCT_COUNT__9186
display_id: PDS-009
slug: kmv-distinct-count
title: "k-Minimum Values (KMV) Distinct Count"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - KMV
  - Distinct Count
tags:
  - probabilistic-ds
  - kmv
  - distinct-count
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-009: k-Minimum Values (KMV) Distinct Count

## Problem Statement

You are given the `k` smallest hash values in (0,1) for a set. Estimate the number of distinct elements using:

```
Estimate = (k - 1) / h_k
```

where `h_k` is the k-th smallest hash value.

![Problem Illustration](../images/PDS-009/problem-illustration.png)

## Input Format

- First line: integer `k`
- Second line: `k` floating-point numbers in ascending order

## Output Format

- Single floating-point number: estimated distinct count

## Constraints

- `2 <= k <= 100000`
- `0 < h_k < 1`

## Example

**Input:**

```
3
0.1 0.2 0.4
```

**Output:**

```
5.0
```

**Explanation:**

Estimate = (3-1) / 0.4 = 5.

![Example Visualization](../images/PDS-009/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

KMV, Sketches, Distinct Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double kmvEstimate(double[] hashes) {
        //Implement here
        return 0.0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            double[] hashes = new double[k];
            for (int i = 0; i < k; i++) hashes[i] = sc.nextDouble();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.kmvEstimate(hashes)));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def kmv_estimate(hashes):
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        hashes = []
        for _ in range(k):
            hashes.append(float(next(iterator)))
            
        print(f"{kmv_estimate(hashes):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double kmvEstimate(const vector<double>& hashes) {
        //Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<double> hashes(k);
        for (int i = 0; i < k; i++) cin >> hashes[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.kmvEstimate(hashes) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function kmvEstimate(hashes) {
  //Implement here
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
  const hashes = [];
  for (let i = 0; i < k; i++) hashes.push(parseFloat(data[idx++]));
  console.log(kmvEstimate(hashes).toFixed(6));
});
```

