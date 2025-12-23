---
problem_id: PDS_COUNT_SKETCH_HEAVY_HITTERS__3405
display_id: PDS-010
slug: count-sketch-heavy-hitters
title: "Heavy Hitters with Count Sketch"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Count Sketch
  - Streaming
tags:
  - probabilistic-ds
  - count-sketch
  - heavy-hitters
  - medium
premium: true
subscription_tier: basic
---

# PDS-010: Heavy Hitters with Count Sketch

## 📋 Problem Summary

We need to estimate the frequency of an item using a Count Sketch.
- We have `d` independent estimates from `d` rows of the sketch.
- Each row `i` gives us a bucket count `C_i` and a sign `S_i in +1, -1`.
- The estimate from row `i` is `C_i x S_i`.
- The final estimate is the **median** of these `d` signed values.

## 🌍 Real-World Scenario

**Scenario Title:** Top-K Video Views

Imagine you are YouTube.
- You want to track the view counts of billions of videos.
- A **Count-Min Sketch** (PDS-004) always overestimates counts because collisions only add positive noise.
- A **Count Sketch** is unbiased. It randomly adds or subtracts noise (using the sign hash).
- The noise has mean 0. By taking the median of multiple estimates, we get a very accurate count with high probability, even for heavy hitters.
- This is crucial for accurate billing (ad revenue) where systematic overestimation is unacceptable.

**Why This Problem Matters:**

- **Signal Processing:** Compressed Sensing.
- **Machine Learning:** Feature hashing (hashing trick) often uses signed hashes to reduce collision bias.

![Real-World Application](../images/PDS-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Count Sketch Estimate

Item "X" maps to:
Row 1: Bucket 5, Sign +1. Bucket val = 100. Est = `100 x 1 = 100`.
Row 2: Bucket 2, Sign -1. Bucket val = -90. Est = `-90 x -1 = 90`.
Row 3: Bucket 8, Sign +1. Bucket val = 200. Est = `200 x 1 = 200`.

Estimates: `[100, 90, 200]`.
Sorted: `[90, 100, 200]`.
Median: 100.

Why median?
- Mean is sensitive to extreme outliers (e.g., colliding with a massive heavy hitter).
- Median is robust.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `d`: Number of rows (odd).
  - List of pairs: `(count, sign)`.
- **Output:** Median of `count * sign`.
- **Note:** `sign` is the hash value `s(x)` for the item being queried. The bucket count stores `sum c_y s(y)` for all items `y` mapping to that bucket. So we multiply by `s(x)` to "decode" the count: `s(x) sum c_y s(y) = c_x s(x)^2 + sum_y != x c_y s(y) s(x) = c_x + noise`.

## Naive Approach

### Intuition

Compute values, sort, pick middle.

### Algorithm

1. Create list `estimates`.
2. For each row: `estimates.add(count * sign)`.
3. Sort `estimates`.
4. Return `estimates[d/2]`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct implementation.

### Algorithm

1. Read `d`.
2. Loop `d` times to read `count` and `sign`.
3. Store `count * sign` in array.
4. Sort array.
5. Print element at index `d/2`.

### Time Complexity

- **O(d log d)** due to sorting. Since `d` is small (101), this is effectively `O(1)`.

### Space Complexity

- **O(d)**.

![Algorithm Visualization](../images/PDS-010/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-010/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int countSketchEstimate(int[] count, int[] sign) {
        int d = count.length;
        int[] estimates = new int[d];
        for (int i = 0; i < d; i++) {
            estimates[i] = count[i] * sign[i];
        }
        Arrays.sort(estimates);
        return estimates[d / 2];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int d = sc.nextInt();
            int[] count = new int[d];
            int[] sign = new int[d];
            for (int i = 0; i < d; i++) {
                count[i] = sc.nextInt();
                sign[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            System.out.println(solution.countSketchEstimate(count, sign));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def count_sketch_estimate(count, sign):
    estimates = []
    for c, s in zip(count, sign):
        estimates.append(c * s)
    estimates.sort()
    return estimates[len(estimates) // 2]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        d = int(next(iterator))
        count = []
        sign = []
        for _ in range(d):
            count.append(int(next(iterator)))
            sign.append(int(next(iterator)))
            
        print(count_sketch_estimate(count, sign))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countSketchEstimate(const vector<int>& count, const vector<int>& sign) {
        int d = count.size();
        vector<int> estimates(d);
        for (int i = 0; i < d; i++) {
            estimates[i] = count[i] * sign[i];
        }
        sort(estimates.begin(), estimates.end());
        return estimates[d / 2];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d;
    if (cin >> d) {
        vector<int> count(d), sign(d);
        for (int i = 0; i < d; i++) {
            cin >> count[i] >> sign[i];
        }
    
        Solution solution;
        cout << solution.countSketchEstimate(count, sign) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function countSketchEstimate(count, sign) {
  const estimates = [];
  for (let i = 0; i < count.length; i++) {
    estimates.push(count[i] * sign[i]);
  }
  estimates.sort((a, b) => a - b);
  return estimates[Math.floor(estimates.length / 2)];
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
  const d = parseInt(data[idx++], 10);
  const count = [];
  const sign = [];
  for (let i = 0; i < d; i++) {
    count.push(parseInt(data[idx++], 10));
    sign.push(parseInt(data[idx++], 10));
  }
  console.log(countSketchEstimate(count, sign));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input:
`3`
`10 1`
`9 -1`
`11 1`

1. Row 1: `10 x 1 = 10`.
2. Row 2: `9 x -1 = -9`.
3. Row 3: `11 x 1 = 11`.
4. Estimates: `[10, -9, 11]`.
5. Sorted: `[-9, 10, 11]`.
6. Median (index 1): `10`.

Output: `10`. Matches example.

![Example Visualization](../images/PDS-010/example-1.png)

## ✅ Proof of Correctness

### Invariant
The median of means estimator gives an `(epsilon, delta)`-approximation.

### Why the approach is correct
Count Sketch theory proves that the noise is symmetric around 0. The median aggregates these unbiased estimators to boost confidence.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Why not mean?
  - *Hint:* Mean variance is too high. Median bounds the tail probability exponentially.
- **Extension 2:** AMS Sketch?
  - *Hint:* Alon-Mathias-Szegedy sketch for estimating second frequency moment (`F_2`). Very similar structure (random signs).

### Common Mistakes to Avoid

1. **Sorting**
   - ❌ Wrong: Forgetting to sort before picking middle element.
   - ✅ Correct: `Arrays.sort()` / `sort()`.
2. **Sign Multiplication**
   - ❌ Wrong: Ignoring sign (treating as Count-Min).
   - ✅ Correct: `count * sign`.

## Related Concepts

- **Count-Min Sketch:** Biased, non-negative noise.
- **Feature Hashing:** Machine learning dimensionality reduction.
