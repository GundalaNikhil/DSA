---
problem_id: PDS_PERFECT_HASHING_RANDOM__6203
display_id: PDS-014
slug: perfect-hashing-random
title: "Perfect Hashing via Randomization"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Perfect Hashing
  - Randomization
tags:
  - probabilistic-ds
  - perfect-hashing
  - randomized
  - medium
premium: true
subscription_tier: basic
---

# PDS-014: Perfect Hashing via Randomization

## 📋 Problem Summary

We are analyzing the space complexity of the FKS (Fredman, Komlós, Szemerédi) Perfect Hashing scheme.
- Level 1: Hash $n$ keys into $t$ buckets.
- Level 2: For each bucket $i$ with size $s_i$, allocate a secondary hash table of size $s_i^2$.
- The total space required for the second level is $S = \sum s_i^2$.
- We need to check if $S \le 4n$, which is the condition for linear space complexity.

## 🌍 Real-World Scenario

**Scenario Title:** Static Dictionary Lookup

Imagine you are building a spell checker for a mobile app.
- You have a fixed dictionary of 100,000 words.
- You want $O(1)$ lookup time to check if a word is valid.
- A standard hash table has collisions, which might degrade to $O(\log n)$ or $O(n)$ in worst cases.
- **Perfect Hashing** guarantees $O(1)$ worst-case lookup by ensuring *zero collisions* in the secondary tables.
- The construction is randomized: pick a hash function, check if the total space is linear ($S \le 4n$). If not, pick another hash function.
- This problem simulates the "check" step of the construction algorithm.

**Why This Problem Matters:**

- **Compiler Design:** Keyword lookup tables.
- **CD-ROM/Read-Only Databases:** Optimizing access speed for static data.

![Real-World Application](../images/PDS-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: FKS Scheme

Keys: {10, 22, 37, 40, 52, 60} ($n=6$)
Buckets ($t=3$):
- Bucket 0: {10, 40} ($s_0=2$) $\to$ Table size $2^2=4$.
- Bucket 1: {22, 52} ($s_1=2$) $\to$ Table size $2^2=4$.
- Bucket 2: {37, 60} ($s_2=2$) $\to$ Table size $2^2=4$.

Total Space $S = 4 + 4 + 4 = 12$.
Check: $12 \le 4 \times 6 = 24$. YES.

If we had a bad hash function where all 6 keys went to Bucket 0:
- Bucket 0: {all 6} ($s_0=6$) $\to$ Table size $36$.
- $S = 36$.
- Check: $36 \le 24$. NO.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - $n$: Total keys.
  - $t$: Number of buckets.
  - Sizes: Array of $t$ bucket sizes.
- **Output:**
  - $S$: Sum of squares.
  - "YES" or "NO".

## Naive Approach

### Intuition

Iterate and sum squares.

### Algorithm

1. `S = 0`.
2. For each size `s`: `S += s * s`.
3. Check condition.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct calculation.

### Algorithm

1. Read $n, t$.
2. Read sizes.
3. Compute $S = \sum s_i^2$.
4. Print $S$ and result.

### Time Complexity

- **O(t)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-014/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long totalSize(int[] sizes) {
        long S = 0;
        for (int s : sizes) {
            S += (long)s * s;
        }
        return S;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            int t = sc.nextInt();
            int[] sizes = new int[t];
            for (int i = 0; i < t; i++) sizes[i] = sc.nextInt();
    
            Solution solution = new Solution();
            long S = solution.totalSize(sizes);
            System.out.println(S + " " + (S <= 4 * n ? "YES" : "NO"));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def total_size(sizes):
    S = 0
    for s in sizes:
        S += s * s
    return S

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        t = int(next(iterator))
        sizes = []
        for _ in range(t):
            sizes.append(int(next(iterator)))
            
        S = total_size(sizes)
        print(f"{S} {'YES' if S <= 4 * n else 'NO'}")
    except StopIteration:
        pass

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
    long long totalSize(const vector<int>& sizes) {
        long long S = 0;
        for (int s : sizes) {
            S += (long long)s * s;
        }
        return S;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int t;
    if (cin >> n >> t) {
        vector<int> sizes(t);
        for (int i = 0; i < t; i++) cin >> sizes[i];
    
        Solution solution;
        long long S = solution.totalSize(sizes);
        cout << S << " " << (S <= 4 * n ? "YES" : "NO") << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function totalSize(sizes) {
  let S = 0;
  for (const s of sizes) {
    S += s * s;
  }
  return S;
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
  const n = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const sizes = [];
  for (let i = 0; i < t; i++) sizes.push(parseInt(data[idx++], 10));
  const S = totalSize(sizes);
  console.log(S + " " + (S <= 4 * n ? "YES" : "NO"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `6 3`, `2 1 3`

1. $n=6, t=3$.
2. Sizes: $[2, 1, 3]$.
3. $S = 2^2 + 1^2 + 3^2 = 4 + 1 + 9 = 14$.
4. Check: $4n = 24$.
5. $14 \le 24$ is True.

Output: `14 YES`. Matches example.

## ✅ Proof of Correctness

### Invariant
The expected value of $\sum s_i^2$ is less than $2n$ for a universal hash function.
By Markov's inequality, the probability that $\sum s_i^2 > 4n$ is less than $1/2$.

### Why the approach is correct
We are verifying the condition derived from the probabilistic analysis of FKS hashing.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if $S > 4n$?
  - *Hint:* Pick a new random hash function for the first level and rehash everything.
- **Extension 2:** Dynamic Perfect Hashing?
  - *Hint:* Cuckoo Hashing is a form of dynamic perfect hashing (amortized $O(1)$ insertion).

### Common Mistakes to Avoid

1. **Overflow**
   - ❌ Wrong: `int S` (if $n$ is large, $S$ can exceed $2^{31}-1$).
   - ✅ Correct: `long long` / `long`.

## Related Concepts

- **Cuckoo Hashing:** Another approach to $O(1)$ worst-case lookup.
- **Universal Hashing:** The theoretical foundation.
