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
---

# PDS-008: Bottom-k Sampling (Min-Hash)

## 📋 Problem Summary

We are given two MinHash signatures of length `k`. Each signature consists of `k` values, where the `i`-th value is the minimum hash value observed for the `i`-th hash function. We need to estimate the Jaccard Similarity between the two original sets by comparing these signatures.

## 🌍 Real-World Scenario

**Scenario Title:** Document Deduplication

Imagine you are crawling the web (Google/Bing).
- You download billions of web pages.
- Many pages are near-duplicates (e.g., the same news article syndicated on 50 different sites, or a page with just a different timestamp).
- Storing and indexing duplicates wastes massive resources.
- **Jaccard Similarity** measures how similar two sets of words are.
- Computing exact Jaccard requires storing all words for every page (`O(N)`).
- **MinHash** compresses a page into a small signature (e.g., 100 integers).
- You can estimate similarity by just comparing these small signatures.

**Why This Problem Matters:**

- **Recommendation Systems:** Finding users with similar purchase history.
- **Genomics:** Comparing DNA sequences.
- **Malware Detection:** Identifying variants of known viruses.

![Real-World Application](../images/PDS-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: MinHash Comparison

Set A: {apple, banana}
Set B: {apple, cherry}

Hash Functions `h_1, h_2, h_3`:
`h_1(apple)=0.1, h_1(banana)=0.5, h_1(cherry)=0.9`
`h_2(apple)=0.8, h_2(banana)=0.2, h_2(cherry)=0.4`

Signatures (Min values):
Sig A: `[0.1, 0.2]`
Sig B: `[0.1, 0.4]`

Comparison:
Pos 1: `0.1 == 0.1` (Match)
Pos 2: `0.2 != 0.4` (Mismatch)

Estimate: `1/2 = 0.5`.
True Jaccard: `|A cap B| / |A cup B| = 1 / 3 ~= 0.33`.
(Estimate converges to true value with more hash functions).

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `k`: Length of signatures.
  - `A`: List of `k` floats.
  - `B`: List of `k` floats.
- **Output:** Fraction of indices `i` where `A[i] == B[i]`.
- **Note:** Floating point equality check is usually tricky, but here we assume exact matches from the same hash function on the same item. Use `==` or a very small epsilon if needed (problem says "exact position matches").

## Naive Approach

### Intuition

Iterate and count matches.

### Algorithm

1. `matches = 0`.
2. Loop `i` from 0 to `k-1`.
3. If `A[i] == B[i]`, `matches++`.
4. Return `matches / k`.

### Limitations

- None.

## Optimal Approach

### Key Insight

The probability that `min(h(A)) = min(h(B))` is exactly the Jaccard Similarity `J(A,B)`.
Thus, the fraction of matching components in the MinHash signature is an unbiased estimator of `J(A,B)`.

### Algorithm

1. Read inputs.
2. Count matches where `A[i] == B[i]`.
3. Print `matches / k`.

### Time Complexity

- **O(k)**.

### Space Complexity

- **O(1)** (ignoring input storage).

![Algorithm Visualization](../images/PDS-008/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-008/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double jaccardEstimate(double[] a, double[] b) {
        int matches = 0;
        for (int i = 0; i < a.length; i++) {
            // Use Double.compare or epsilon for robustness, 
            // but problem implies exact hash values.
            if (Double.compare(a[i], b[i]) == 0) {
                matches++;
            }
        }
        return (double) matches / a.length;
    }
}

public class Main {
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
    matches = 0
    k = len(a)
    for i in range(k):
        if a[i] == b[i]:
            matches += 1
    return matches / k

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
        int matches = 0;
        for (size_t i = 0; i < a.size(); i++) {
            if (a[i] == b[i]) {
                matches++;
            }
        }
        return (double)matches / a.size();
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
  let matches = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i] === b[i]) {
      matches++;
    }
  }
  return matches / a.length;
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

## 🧪 Test Case Walkthrough (Dry Run)

Input:
`5`
`0.1 0.2 0.3 0.4 0.5`
`0.1 0.25 0.3 0.6 0.7`

1. Compare index 0: `0.1 == 0.1` (Match)
2. Compare index 1: `0.2 != 0.25` (Mismatch)
3. Compare index 2: `0.3 == 0.3` (Match)
4. Compare index 3: `0.4 != 0.6` (Mismatch)
5. Compare index 4: `0.5 != 0.7` (Mismatch)

Matches = 2.
Estimate = 2/5 = 0.4.

Output: `0.4`. Matches example.

![Example Visualization](../images/PDS-008/example-1.png)

## ✅ Proof of Correctness

### Invariant
`P(h_min(A) = h_min(B)) = frac|A cap B||A cup B|`.

### Why the approach is correct
This is the fundamental property of MinHash. The minimum hash value comes from the union of sets. It comes from the intersection iff the element with the minimum hash is in both sets. Since hash functions are random permutations, any element is equally likely to be the minimum.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** LSH (Locality Sensitive Hashing)?
  - *Hint:* Banding technique. Group hashes into bands to find candidates with high similarity quickly.
- **Extension 2:** Weighted Jaccard?
  - *Hint:* Use Consistent Weighted Sampling (CWS).
- **Extension 3:** b-bit MinHash?
  - *Hint:* Store only the lowest `b` bits of the hash to save space, with slight accuracy loss.

### Common Mistakes to Avoid

1. **Sorting**
   - ❌ Wrong: Sorting the signatures and comparing.
   - ✅ Correct: Compare index-by-index. `h_1` must compare with `h_1`.

## Related Concepts

- **SimHash:** For cosine similarity.
- **Bloom Filter:** For containment.
