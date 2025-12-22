---
problem_id: STC_SUFFIX_ARRAY_DOUBLING__3726
display_id: STC-005
slug: suffix-array-doubling
title: "Suffix Array (Doubling) Construction"
difficulty: Medium
difficulty_score: 48
topics:
  - Strings
  - Suffix Array
  - Sorting
tags:
  - strings
  - suffix-array
  - doubling
  - medium
premium: true
subscription_tier: basic
---

# STC-005: Suffix Array (Doubling) Construction

## 📋 Problem Summary

Given a string `s`, you need to construct its **Suffix Array**. The suffix array is an array of integers representing the starting indices of all suffixes of `s` sorted in lexicographical (alphabetical) order. You are required to use the **Doubling Algorithm** to achieve efficient construction.

## 🌍 Real-World Scenario

**Scenario Title:** Full-Text Search Engine Indexing

Imagine you are building a search engine for a massive library of books. You want to allow users to search for any phrase (substring) within the entire corpus. A linear scan is impossible. A Suffix Array, combined with an LCP (Longest Common Prefix) array, allows you to index the text such that you can find any substring in time proportional to the length of the query and the log of the text size. This is the fundamental data structure behind many efficient string processing tools and compression algorithms like bzip2 (which uses the Burrows-Wheeler Transform, derived from the suffix array).

**Why This Problem Matters:**

- **Foundation:** Suffix Arrays are the gateway to solving complex string problems (longest repeated substring, longest common substring, etc.) efficiently.
- **Space Efficiency:** They are more space-efficient than Suffix Trees while offering similar power.
- **Algorithm Design:** The doubling technique is a powerful paradigm used in other contexts (e.g., LCA in trees).

![Real-World Application](../images/STC-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "cababa"`.
Suffixes:
0: "cababa"
1: "ababa"
2: "baba"
3: "aba"
4: "ba"
5: "a"

Sorted Suffixes:
1. "a"      (Index 5)
2. "aba"    (Index 3)
3. "ababa"  (Index 1)
4. "ba"     (Index 4)
5. "baba"   (Index 2)
6. "cababa" (Index 0)

Suffix Array: `[5, 3, 1, 4, 2, 0]`

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sentinel:** It's common to append a sentinel character `$` (smaller than 'a') to the string to simplify comparisons, but the problem asks for indices of the original string. The logic remains the same; just handle out-of-bound indices by assigning them a rank of -1.
- **Time Complexity:** O(N^2 log N) is too slow. You need O(N log^2 N) or O(N log N).
- **Output:** 0-based indices.

## Naive Approach

### Intuition

Generate all suffixes and sort them using the standard sorting algorithm.

### Algorithm

1. Create a list of indices `0` to `n-1`.
2. Sort the indices based on the substring `s[i...]`.

### Time Complexity

- **O(N^2 log N)**: Comparison of two strings takes O(N). Sorting takes O(N log N) comparisons. Total O(N^2 log N).
- With `N=100,000`, this is way too slow.

### Space Complexity

- **O(N^2)** if we actually store substrings, or **O(N)** if we just store indices and reference the original string.

## Optimal Approach (Doubling Algorithm)

### Key Insight

We can sort cyclic shifts of length `2^k` by using the results from length `2^(k-1)`.
A cyclic shift of length `2^k` starting at `i` consists of a first half (length `2^(k-1)` starting at `i`) and a second half (length `2^(k-1)` starting at `i + 2^(k-1)`).
If we have already assigned ranks to all substrings of length `2^(k-1)`, we can describe the substring of length `2^k` starting at `i` by the pair `(rank[i], rank[i + 2^(k-1)])`.
Sorting these pairs gives us the ranks for length `2^k`.

### Algorithm

1. **Initialization (k=0):** Assign initial ranks based on the character itself (e.g., 'a' -> 0, 'b' -> 1...).
2. **Iteration:** For `k = 0` to `log N`:
    - Length of current substrings is `L = 2^k`.
    - Form pairs for each index `i`: `(rank[i], rank[i + L])`. If `i + L >= n`, use -1 for the second element.
    - Sort these pairs. The sorted order determines the new ranks.
    - Re-assign ranks: `new_rank[i]` increments only if the pair for `i` is different from the pair for `i-1` in the sorted list.
    - If `L >= n`, stop.
3. **Result:** The indices sorted by their final ranks form the Suffix Array.

### Time Complexity

- **O(N log^2 N)**: If we use `std::sort` (O(N log N)) in each of the `log N` steps.
- **O(N log N)**: If we use Radix Sort (O(N)) in each step. For competitive programming, O(N log^2 N) is usually acceptable for N=100,000 (approx 1.7 * 10^7 ops), but O(N log N) is safer. We will implement the O(N log^2 N) version for simplicity as it's standard and concise, but mention the optimization.

### Space Complexity

- **O(N)**: To store ranks and the suffix array.

![Algorithm Visualization](../images/STC-005/algorithm-visualization.png)
![Algorithm Steps](../images/STC-005/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] suffixArray(String s) {
        int n = s.length();
        Integer[] sa = new Integer[n];
        int[] rank = new int[n];
        int[] newRank = new int[n];
        
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s.charAt(i);
        }
        
        for (int k = 1; k < n; k *= 2) {
            int len = k;
            Arrays.sort(sa, (i, j) -> {
                if (rank[i] != rank[j]) {
                    return rank[i] - rank[j];
                }
                int ri = (i + len < n) ? rank[i + len] : -1;
                int rj = (j + len < n) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                int prev = sa[i - 1];
                int curr = sa[i];
                
                int r1 = rank[prev];
                int r2 = (prev + len < n) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < n) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) {
                    newRank[curr] = newRank[prev];
                } else {
                    newRank[curr] = newRank[prev] + 1;
                }
            }
            System.arraycopy(newRank, 0, rank, 0, n);
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        return Arrays.stream(sa).mapToInt(Integer::intValue).toArray();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] sa = solution.suffixArray(s);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < sa.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(sa[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def suffix_array(s: str) -> list[int]:
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    new_rank = [0] * n
    
    k = 1
    while k < n:
        # Sort based on pair (rank[i], rank[i+k])
        # Python's sort is stable and handles tuples efficiently
        key_func = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
        sa.sort(key=key_func)
        
        new_rank[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i-1]
            curr = sa[i]
            if key_func(prev) == key_func(curr):
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        
        rank = list(new_rank)
        if rank[sa[n-1]] == n - 1:
            break
        k *= 2
        
    return sa

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    sa = suffix_array(s)
    print(*(sa))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> suffixArray(const string& s) {
        int n = s.length();
        vector<int> sa(n), rank(n), newRank(n);
        
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s[i];
        }
        
        for (int k = 1; k < n; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < n) ? rank[i + k] : -1;
                int rj = (j + k < n) ? rank[j + k] : -1;
                return ri < rj;
            };
            
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                if (cmp(sa[i - 1], sa[i])) {
                    newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                } else {
                    newRank[sa[i]] = newRank[sa[i - 1]];
                }
            }
            rank = newRank;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        return sa;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        vector<int> sa = solution.suffixArray(s);
        for (int i = 0; i < (int)sa.size(); i++) {
            if (i > 0) cout << " ";
            cout << sa[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  suffixArray(s) {
    const n = s.length;
    let sa = new Array(n).fill(0).map((_, i) => i);
    let rank = new Array(n).fill(0).map((_, i) => s.charCodeAt(i));
    let newRank = new Array(n).fill(0);
    
    for (let k = 1; k < n; k *= 2) {
      sa.sort((i, j) => {
        if (rank[i] !== rank[j]) return rank[i] - rank[j];
        const ri = (i + k < n) ? rank[i + k] : -1;
        const rj = (j + k < n) ? rank[j + k] : -1;
        return ri - rj;
      });
      
      newRank[sa[0]] = 0;
      for (let i = 1; i < n; i++) {
        const prev = sa[i - 1];
        const curr = sa[i];
        
        const r1 = rank[prev];
        const r2 = (prev + k < n) ? rank[prev + k] : -1;
        const r3 = rank[curr];
        const r4 = (curr + k < n) ? rank[curr + k] : -1;
        
        if (r1 === r3 && r2 === r4) {
          newRank[curr] = newRank[prev];
        } else {
          newRank[curr] = newRank[prev] + 1;
        }
      }
      
      for (let i = 0; i < n; i++) rank[i] = newRank[i];
      if (rank[sa[n - 1]] === n - 1) break;
    }
    return sa;
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
  const sa = solution.suffixArray(s);
  console.log(sa.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`s = "aba"`

**Init:**
`rank = [97, 98, 97]` (ASCII for a, b, a)
`sa = [0, 1, 2]`

**k = 1:**
Pairs:
`i=0`: `(97, 98)`
`i=1`: `(98, 97)`
`i=2`: `(97, -1)`

Sorted Pairs:
1. `(97, -1)` -> `i=2` ("a")
2. `(97, 98)` -> `i=0` ("ab")
3. `(98, 97)` -> `i=1` ("ba")

`sa = [2, 0, 1]`
`newRank`:
`sa[0]=2`: rank 0
`sa[1]=0`: pair `(97, 98)` != `(97, -1)`, rank 1
`sa[2]=1`: pair `(98, 97)` != `(97, 98)`, rank 2
`rank = [1, 2, 0]`

**k = 2:**
Pairs:
`i=0`: `(1, 0)` (rank[0], rank[2])
`i=1`: `(2, -1)` (rank[1], rank[3] -> -1)
`i=2`: `(0, -1)` (rank[2], rank[4] -> -1)

Sorted Pairs:
1. `(0, -1)` -> `i=2` ("a")
2. `(1, 0)` -> `i=0` ("aba")
3. `(2, -1)` -> `i=1` ("ba")

`sa = [2, 0, 1]`
Ranks will be `0, 1, 2`. Unique ranks found. Stop.

Final SA: `2 0 1`.
Suffixes: "a", "aba", "ba". Correct.

![Example Visualization](../images/STC-005/example-1.png)

## ✅ Proof of Correctness

### Invariant

After step `k`, `rank[i]` represents the lexicographical rank of the substring `s[i...i + 2^k - 1]` among all such substrings of length `2^k`.

### Why the approach is correct

By sorting pairs `(rank[i], rank[i + 2^k])`, we are effectively comparing substrings of length `2^(k+1)`.
`s[i...i + 2^(k+1) - 1]` is composed of `s[i...i + 2^k - 1]` (represented by `rank[i]`) and `s[i + 2^k...i + 2^(k+1) - 1]` (represented by `rank[i + 2^k]`).
Lexicographical comparison of two strings `A` and `B` is equivalent to comparing their first halves, and if equal, comparing their second halves.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: LCP Array**
  - How to compute the Longest Common Prefix array efficiently given the Suffix Array? (Kasai's Algorithm).

- **Extension 2: Number of Distinct Substrings**
  - Sum of `(n - sa[i] - lcp[i])`.

- **Extension 3: Longest Repeated Substring**
  - Max value in LCP array.

### Common Mistakes to Avoid

1. **Incorrect Pair Comparison**
   - ❌ Comparing characters instead of ranks in the loop.
   - ✅ Must use the ranks computed in the previous step.

2. **Out of Bounds Access**
   - ❌ Accessing `rank[i + k]` when `i + k >= n`.
   - ✅ Treat out-of-bound ranks as -1 (or a value smaller than any valid rank).

3. **Not Updating Ranks Correctly**
   - ❌ Just using the sorted index as rank.
   - ✅ Must handle duplicates. If two substrings are identical, they must have the same rank.

## Related Concepts

- **Kasai's Algorithm**: For LCP array construction.
- **Suffix Automaton**: Another structure for similar problems.
- **Burrows-Wheeler Transform**: Uses cyclic shifts sorting (conceptually similar).
