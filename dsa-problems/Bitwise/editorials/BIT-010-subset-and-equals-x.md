---
problem_id: BIT_SUBSET_AND_EQUALS_X__8410
display_id: BIT-010
slug: subset-and-equals-x
title: "Subset AND Equals X"
difficulty: Medium
difficulty_score: 52
topics:
  - Bitwise Operations
  - AND
  - Subset
  - Dynamic Programming
tags:
  - bitwise
  - and-operation
  - subset
  - dp
  - medium
premium: true
subscription_tier: basic
---

# BIT-010: Subset AND Equals X

## 📋 Problem Summary

Given an array of integers and a target `X`, count the number of non-empty subsets such that the bitwise AND of the subset elements is exactly `X`.

## 🌍 Real-World Scenario

**Scenario Title:** The Strict Permission Group

You are analyzing access control lists (ACLs).
- **Users**: Each user has a set of permissions (bits set to 1).
- **Requirement**: You want to form a committee (subset of users).
- **Consensus**: The committee can only perform an action if *everyone* in the committee has the permission for it (Committee Permission = AND of User Permissions).
- **Goal**: You need to find how many ways you can form a committee such that the resulting set of actionable permissions is *exactly* `X`.
  - It must have *all* permissions in `X`.
  - It must *not* have any extra permissions common to everyone (consensus on `X` only).

**Why This Problem Matters:**

- **Parameter Constraints**: Recognizing that `N <= 20` allows exponential solutions ($O(2^N)$).
- **Filtering**: Pruning the search space by pre-checking validity.
- **Inclusion-Exclusion**: A key concept if `N` were larger.

![Real-World Application](../images/BIT-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Subset AND
```
Array: [6 (110), 4 (100), 2 (010)]
Target X = 2 (010)

Subsets:
- {6}: AND=6. No.
- {4}: AND=4. No.
- {2}: AND=2. Yes.
- {6, 4}: AND=4. No.
- {6, 2}: AND=2. Yes.
- {4, 2}: AND=0. No.
- {6, 4, 2}: AND=0. No.

Matches: {2}, {6, 2}. Total 2.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: `n` (up to 20), Array `a`, Target `X`.
- **Output**: Count of subsets.
- **Empty Subset**: Not counted.

Common interpretation mistake:

- ❌ Assuming `N` is large and trying complicated DP.
- ✅ Checking constraints first. `N=20` implies $2^{20} \approx 10^6$ ops, which fits in 2 seconds.

### Core Concept: Small N Iteration

When `N` is small (<= 20), iterating through all $2^N$ subsets is standard practice.
We can use a bitmask from `1` to `(1<<N) - 1` to represent each non-empty subset.

## Naive Approach (Bitmask Iteration)

### Intuition

Generate every subset, compute AND, check partial equality? No, check exact equality.

### Algorithm

1. `count = 0`.
2. Loop `mask` from 1 to `(1 << n) - 1`:
   - `current_and = -1` (All 1s)
   - Loop `i` from 0 to `n-1`:
     - If `(mask >> i) & 1`:
       - `current_and &= a[i]`
   - If `current_and == X`: `count++`
3. Return `count`.

### Time Complexity

- **O(N * 2^N)**.
- $20 \times 10^6 = 2 \times 10^7$ ops. Very safe.

### Space Complexity

- **O(1)**.

## Optimal Approach (Pre-filtering + Iteration)

### Key Insight

We can optimize slightly.
For a subset to have `AND == X`:
1. Every element MUST be a supermask of `X` (i.e. `(elem & X) == X`). If an element has a 0 where X has a 1, the total AND will have 0 there, failing the match.
2. The AND of the chosen elements must not have any *extra* bits set that are not in X.

### Algorithm

1. Filter `a`: keep only elements where `(v & X) == X`. Let this new list be `b`.
2. Iterate all subsets of `b`.
3. Compute AND. Check if `AND == X`.

This reduces the base of the exponent if many elements are incompatible.

**Alternative High-N Approach (Context)**:
If `N` was 100,000 but values were small ($< 2^{20}$), we would use **Sum Over Subsets (SOS) DP**.
`Count(AND=X) = Sum( (-1)^|S^X| * (2^{Freq[S]} - 1) )` for all `S` supermask of `X`.
But here, standard iteration is optimal.

### Time Complexity

- **O(N * 2^K)** where K is number of valid supermasks. Worst case **O(N * 2^N)**.

### Space Complexity

- **O(N)** for filtered list.

![Algorithm Visualization](../images/BIT-010/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-010/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long subsetAndEqualsX(int[] a, int X) {
        // Pruning: Keep only elements that are supermasks of X
        ArrayList<Integer> candidates = new ArrayList<>();
        for (int v : a) {
            if ((v & X) == X) {
                candidates.add(v);
            }
        }
        
        int n = candidates.size();
        long count = 0;
        
        // Iterate subsets of filtered array
        // Loop limit is 1<<n. Since n <= 20, loop fits in int.
        int limit = 1 << n;
        for (int mask = 1; mask < limit; mask++) {
            // Compute AND of this subset
            // Initialize with all 1s (identity for AND) 
            // OR simpler: initialize with first element found
            int currentAnd = -1; 
            boolean empty = true;
            
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    if (empty) {
                        currentAnd = candidates.get(i);
                        empty = false;
                    } else {
                        currentAnd &= candidates.get(i);
                    }
                    
                    // Optimization: If currentAnd drops below X (missing bits), simplify break?
                    // We know (v & X) == X, so currentAnd will always have bits of X set.
                    // It will never be "less" than X in set-bit terms. 
                    // It will only converge towards X.
                }
            }
            
            if (!empty && currentAnd == X) {
                count++;
            }
        }
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int X = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.subsetAndEqualsX(a, X));
        sc.close();
    }
}
```

### Python

```python
import sys

def subset_and_equals_x(a: list[int], X: int) -> int:
    # Filter candidates
    candidates = [v for v in a if (v & X) == X]
    n = len(candidates)
    
    count = 0
    limit = 1 << n
    
    for mask in range(1, limit):
        current_and = -1
        first = True
        
        for i in range(n):
            if (mask >> i) & 1:
                if first:
                    current_and = candidates[i]
                    first = False
                else:
                    current_and &= candidates[i]
        
        if not first and current_and == X:
            count += 1
            
    return count

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1

    X = int(data[ptr]); ptr += 1

    result = subset_and_equals_x(a, X)
    print(result)

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
    long long subsetAndEqualsX(vector<int>& a, int X) {
        vector<int> candidates;
        for (int v : a) {
            if ((v & X) == X) {
                candidates.push_back(v);
            }
        }
        
        int n = candidates.size();
        long long count = 0;
        int limit = 1 << n;
        
        for (int mask = 1; mask < limit; mask++) {
            int currentAnd = -1;
            bool first = true;
            
            for (int i = 0; i < n; i++) {
                if ((mask >> i) & 1) {
                    if (first) {
                        currentAnd = candidates[i];
                        first = false;
                    } else {
                        currentAnd &= candidates[i];
                    }
                }
            }
            if (!first && currentAnd == X) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int X;
    cin >> X;
    
    Solution solution;
    cout << solution.subsetAndEqualsX(a, X) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  subsetAndEqualsX(a, X) {
    const candidates = [];
    for (const v of a) {
      if ((v & X) === X) {
        candidates.push(v);
      }
    }
    
    const n = candidates.length;
    let count = 0;
    const limit = 1 << n;
    
    for (let mask = 1; mask < limit; mask++) {
      let currentAnd = -1;
      let first = true;
      
      for (let i = 0; i < n; i++) {
        if ((mask >>> i) & 1) {
          if (first) {
            currentAnd = candidates[i];
            first = false;
          } else {
            currentAnd &= candidates[i];
          }
        }
      }
      
      if (!first && currentAnd === X) {
        count++;
      }
    }
    
    return count;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    
    const X = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.subsetAndEqualsX(a, X)));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `6, 4, 2`. `X=2`.
1. **Filter**:
   - 6 (110) & 2 (010) = 2 == 2. OK.
   - 4 (100) & 2 (010) = 0 != 2. Reject.
   - 2 (010) & 2 (010) = 2 == 2. OK.
   Candidates: `[6, 2]`.
2. **Subsets**:
   - `[6]` -> AND 6. (6 != 2).
   - `[2]` -> AND 2. (2 == 2). Count 1.
   - `[6, 2]` -> 6 & 2 = 2. (2 == 2). Count 2.
3. **Result**: 2.

## ✅ Proof of Correctness

### Invariant

We iterate all possible subsets of potentially valid candidates. Since we essentially brute force the check, correctness is guaranteed. The filter step is valid because any `v` such that `(v & X) != X` would force the result to have a 0 bit where X has a 1 bit, making equality impossible.

## 💡 Interview Extensions (High-Value Add-ons)

- **Large N (10^5)**: Use SOS DP (Sum Over Subsets).
- **Count Supermasks**: Simpler problem.

## Common Mistakes to Avoid

1. **All Subsets**:
   - ❌ Including empty subset (usually AND is undefined or -1).
   - ✅ Loop `mask` from 1.
2. **Filter Logic**:
   - ❌ Filtering `v & X != 0`.
   - ✅ Filtering `v & X == X`.

## Related Concepts

- **Sum Over Subsets (SOS) DP**: For scaling to large N.
- **Inclusion-Exclusion Principle**: For solving equations.
