---
problem_id: STC_MINIMAL_ROTATION_SA__6042
display_id: STC-009
slug: minimal-rotation-sa
title: "Lexicographically Minimal Rotation (SA)"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
  - Suffix Array
  - Rotation
tags:
  - strings
  - suffix-array
  - rotation
  - medium
premium: true
subscription_tier: basic
---

# STC-009: Lexicographically Minimal Rotation (SA)

## 📋 Problem Summary

Given a string `s`, you need to find the starting index of its **lexicographically minimal rotation**. A rotation is obtained by moving characters from the beginning to the end. Among all possible rotations, find the one that would appear first in a dictionary. If there are ties, return the smallest starting index.

## 🌍 Real-World Scenario

**Scenario Title:** Canonical Representation of Cyclic Data

In chemistry, molecules can be represented as cyclic graphs or strings of atoms. To check if two molecules are identical (isomorphic), we need a "canonical" representation that is the same regardless of where we start reading the cycle. The lexicographically minimal rotation of the string representing the cycle serves as this unique identifier. If two strings have the same minimal rotation, they represent the same cyclic structure.

**Why This Problem Matters:**

- **Normalization:** Used in databases to store cyclic data uniquely.
- **Geometry:** Processing polygons where the order of vertices matters but the start point doesn't.

![Real-World Application](../images/STC-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "bba"`.
Rotations:
- Index 0: `bba`
- Index 1: `ba` + `b` = `bab`
- Index 2: `a` + `bb` = `abb`

Sorted Rotations:
1. `abb` (Index 2)
2. `bab` (Index 1)
3. `bba` (Index 0)

Smallest is `abb`, starting at index 2.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s` of length `N`.
- **Output:** An integer index `0 <= i < N`.
- **Ties:** If `s = "abab"`, rotations are `abab`, `baba`, `abab`, `baba`. Minimal is `abab`. Indices 0 and 2. Return 0.

## Naive Approach

### Intuition

Generate all `N` rotations and sort them.

### Algorithm

1. Create a list of strings, where the `i`-th string is `s[i...n-1] + s[0...i-1]`.
2. Sort the list.
3. Return the index of the first string.

### Time Complexity

- **O(N^2 log N)**: Sorting `N` strings of length `N`.
- Too slow for `N=100,000`.

### Space Complexity

- **O(N^2)**: To store all rotations.

## Optimal Approach (Suffix Array)

### Key Insight

A common trick for dealing with cyclic rotations is to concatenate the string with itself: `S = s + s`.
Any substring of `S` of length `N` corresponds to a rotation of `s`.
Specifically, the substring starting at index `i` (for `0 <= i < N`) in `S` is exactly the rotation of `s` starting at `i`.
We want to find the `i` such that `S[i...i+N-1]` is lexicographically smallest.
This sounds like a Suffix Array problem! If we build the Suffix Array for `S`, the suffixes are sorted.
However, `S` has length `2N`. The suffix starting at `i` is `S[i...2N-1]`.
Since we only care about the first `N` characters, and all relevant suffixes have length `>= N`, the sorted order of suffixes in `S` will generally align with the sorted order of rotations.
The first index `i` in the Suffix Array such that `i < N` is our answer.

*Note:* Why does comparing full suffixes work?
If `suffix[i] < suffix[j]`, then `S[i...2N-1] < S[j...2N-1]`.
Since `N` is the period, this implies the rotation at `i` is smaller than or equal to the rotation at `j`.

### Algorithm

1. Construct `S = s + s`.
2. Build the Suffix Array for `S`.
3. Iterate through the Suffix Array `sa`.
4. The first `sa[i]` such that `sa[i] < |s|` is the answer.

### Time Complexity

- **O(N log N)**: Dominated by SA construction.

### Space Complexity

- **O(N)**: For SA.

### Alternative: Booth's Algorithm / Duval's Algorithm

There are O(N) algorithms specifically for this (Lyndon Factorization), but using a Suffix Array is a robust general-purpose solution that fits the "StringsClassic" theme.

![Algorithm Visualization](../images/STC-009/algorithm-visualization.png)
![Algorithm Steps](../images/STC-009/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int minimalRotationIndex(String s) {
        int n = s.length();
        if (n == 0) return 0;
        String text = s + s;
        int m = text.length();
        
        // Build Suffix Array for s + s
        Integer[] sa = new Integer[m];
        int[] rank = new int[m];
        int[] newRank = new int[m];
        
        for (int i = 0; i < m; i++) {
            sa[i] = i;
            rank[i] = text.charAt(i);
        }
        
        for (int k = 1; k < m; k *= 2) {
            int len = k;
            Arrays.sort(sa, (i, j) -> {
                if (rank[i] != rank[j]) return rank[i] - rank[j];
                int ri = (i + len < m) ? rank[i + len] : -1;
                int rj = (j + len < m) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < m; i++) {
                int prev = sa[i - 1];
                int curr = sa[i];
                int r1 = rank[prev];
                int r2 = (prev + len < m) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < m) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) newRank[curr] = newRank[prev];
                else newRank[curr] = newRank[prev] + 1;
            }
            System.arraycopy(newRank, 0, rank, 0, m);
            if (rank[sa[m - 1]] == m - 1) break;
        }
        
        // Find first index < n
        for (int i = 0; i < m; i++) {
            if (sa[i] < n) {
                return sa[i];
            }
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.minimalRotationIndex(s));
        }
        sc.close();
    }
}
```

### Python

```python
def minimal_rotation_index(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    text = s + s
    m = len(text)
    
    # Build SA
    sa = list(range(m))
    rank = [ord(c) for c in text]
    new_rank = [0] * m
    
    k = 1
    while k < m:
        key_func = lambda i: (rank[i], rank[i + k] if i + k < m else -1)
        sa.sort(key=key_func)
        
        new_rank[sa[0]] = 0
        for i in range(1, m):
            prev = sa[i-1]
            curr = sa[i]
            if key_func(prev) == key_func(curr):
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        
        rank = list(new_rank)
        if rank[sa[m-1]] == m - 1:
            break
        k *= 2
        
    for idx in sa:
        if idx < n:
            return idx
    return 0

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(minimal_rotation_index(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimalRotationIndex(const string& s) {
        int n = s.length();
        if (n == 0) return 0;
        string text = s + s;
        int m = text.length();
        
        vector<int> sa(m), rank(m), newRank(m);
        for (int i = 0; i < m; i++) {
            sa[i] = i;
            rank[i] = text[i];
        }
        
        for (int k = 1; k < m; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < m) ? rank[i + k] : -1;
                int rj = (j + k < m) ? rank[j + k] : -1;
                return ri < rj;
            };
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < m; i++) {
                if (cmp(sa[i - 1], sa[i])) newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                else newRank[sa[i]] = newRank[sa[i - 1]];
            }
            rank = newRank;
            if (rank[sa[m - 1]] == m - 1) break;
        }
        
        for (int i = 0; i < m; i++) {
            if (sa[i] < n) return sa[i];
        }
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.minimalRotationIndex(s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalRotationIndex(s) {
    const n = s.length;
    if (n === 0) return 0;
    const text = s + s;
    const m = text.length;
    
    let sa = new Array(m).fill(0).map((_, i) => i);
    let rank = new Array(m).fill(0).map((_, i) => text.charCodeAt(i));
    let newRank = new Array(m).fill(0);
    
    for (let k = 1; k < m; k *= 2) {
      sa.sort((i, j) => {
        if (rank[i] !== rank[j]) return rank[i] - rank[j];
        const ri = (i + k < m) ? rank[i + k] : -1;
        const rj = (j + k < m) ? rank[j + k] : -1;
        return ri - rj;
      });
      
      newRank[sa[0]] = 0;
      for (let i = 1; i < m; i++) {
        const prev = sa[i - 1];
        const curr = sa[i];
        const r1 = rank[prev];
        const r2 = (prev + k < m) ? rank[prev + k] : -1;
        const r3 = rank[curr];
        const r4 = (curr + k < m) ? rank[curr + k] : -1;
        
        if (r1 === r3 && r2 === r4) newRank[curr] = newRank[prev];
        else newRank[curr] = newRank[prev] + 1;
      }
      for (let i = 0; i < m; i++) rank[i] = newRank[i];
      if (rank[sa[m - 1]] === m - 1) break;
    }
    
    for (let i = 0; i < m; i++) {
      if (sa[i] < n) return sa[i];
    }
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.minimalRotationIndex(s).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`s = "bba"`
`S = "bbabba"`
Suffixes of `S`:
0. `bbabba`
1. `babba`
2. `abba`
3. `bba`
4. `ba`
5. `a`

Sorted Suffixes (SA):
1. `a` (5)
2. `abba` (2)
3. `ba` (4)
4. `babba` (1)
5. `bba` (3)
6. `bbabba` (0)

SA: `[5, 2, 4, 1, 3, 0]`

Scan SA:
- `sa[0] = 5`. `5 >= 3`. Skip.
- `sa[1] = 2`. `2 < 3`. Found!
Answer: 2.

Rotation at 2 is `s[2...] + s[0...1]` = `a` + `bb` = `abb`. Correct.

![Example Visualization](../images/STC-009/example-1.png)

## ✅ Proof of Correctness

### Invariant

The suffix of `s+s` starting at `i` (where `i < n`) begins with the rotation of `s` starting at `i`.
Since `s+s` has length `2n`, this suffix has length `2n - i > n`.
Comparing two such suffixes `i` and `j` lexicographically compares their first `n` characters (which are the rotations) first.
If the rotations are different, the suffixes will be ordered by the rotations.
If the rotations are identical, the tie is broken by characters after index `n`. But since we scan the SA from the beginning, we find the minimal one.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Booth's Algorithm**
  - Solve in O(N) without Suffix Array using a modified KMP failure function.

- **Extension 2: Duval's Algorithm**
  - Decompose string into Lyndon words. `s = w1w2...wk` where `w1 >= w2 >= ... >= wk`.

## Common Mistakes to Avoid

1. **Not doubling the string**
   - ❌ Trying to sort rotations manually or using circular indexing logic in sort.
   - ✅ Concatenation is cleaner.

2. **Returning index >= N**
   - ❌ Returning `sa[0]` blindly.
   - ✅ `sa[0]` might be an index in the second half of `s+s`. We need the first valid start index.

## Related Concepts

- **Lyndon Words**: Strings that are strictly smaller than all of their proper suffixes.
- **Burrows-Wheeler Transform**: Sorting all rotations is the first step of BWT.
