---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: "Pairwise XOR in Band With Index Parity"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Array
tags:
  - bitwise
  - xor
  - trie
  - counting
  - medium
premium: true
subscription_tier: basic
---

# BIT-004: Pairwise XOR in Band With Index Parity

## 📋 Problem Summary

Given an array and range `[L, U]`, count the number of index pairs `(i, j)` such that `i < j`, `i + j` is even, and the XOR sum `a[i] ^ a[j]` falls within `[L, U]`.

## 🌍 Real-World Scenario

**Scenario Title:** The Parity-Synchronized Network Mesh

You are building a mesh network where nodes are assigned IDs.
- **Link Condition**: Two nodes can form a secure link if their IDs, when XORed, produce a value within a specific "Signal Strength" range `[L, U]`.
- **Timing Constraint**: Links are time-slotted. Odd-numbered nodes operate in Phase 1, Even-numbered nodes in Phase 2. A link is valid only if both nodes operate in the same phase (i.e., both Odd or both Even indices). Note: `i+j` is even if and only if `i` and `j` have the same parity.
- **Goal**: Count the total valid potential links in the network.

**Why This Problem Matters:**

- **Trie Data Structure**: Standard tool for efficient prefix-based queries (XOR, strings).
- **Decomposition**: Breaking a complex condition (`i+j` even) into simpler structural properties (Same Parity).
- **Range counting**: Reducing `[L, U]` queries to `Count(<= U) - Count(<= L-1)`.

![Real-World Application](../images/BIT-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Trie Query
```
Query: Count y < x such that (x ^ y) <= K
x = 1011 (11)
K = 0101 (5)
Trie Root
|
|-- Bit 3 (K=0): Must match x(1). Go Right (1).
    |
    |-- Bit 2 (K=1):
        |-- Match x(0) -> XOR is 0 (< 1). All sub-nodes valid. Add Count.
        |-- Diff x(1) -> XOR is 1 (= 1). Continue to check lower bits.
            |
            ...
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Array `a`, integers `L` and `U`.
- **Condition `i+j` Even**: Means `i` and `j` are both Even or both Odd.
- **Pairs**: `(i, j)` with `i < j`. Order doesn't matter for value, but counting pairs once.

Common interpretation mistake:

- ❌ Trying to handle `i + j` even inside the Trie logic directly.
- ✅ Splitting the input array into two arrays (`even_indices` and `odd_indices`) and solving the problem for each independently.

### Core Concept: XOR Range Counting with Trie

To count pairs with `XOR <= K`, we use a Trie.
Iterate through numbers. For each number `x`:
1.  **Query**: How many numbers already in Trie satisfy `num ^ x <= K`?
2.  **Insert**: Add `x` to Trie.

`Count([L, U]) = Count(<= U) - Count(<= L-1)`.

### Why Naive Approach is too slow

Checking every pair is O(N²). N=100,000 means 10^10 operations, which is TLE.
Trie approach is O(N * 30). 3 million ops. Fast.

## Naive Approach (Brute Force)

### Intuition

Double loop. Check conditions.

### Algorithm

1. `count = 0`
2. Loop `i` from 0 to `n-1`:
   - Loop `j` from `i+1` to `n-1`:
     - If `(i + j) % 2 == 0`:
       - `xor_val = a[i] ^ a[j]`
       - If `L <= xor_val <= U`: `count++`

### Time Complexity

- **O(N²)**.

### Space Complexity

- **O(1)**.

## Optimal Approach (Trie + Splitting)

### Key Insight

1. `(i + j) % 2 == 0` is equivalent to `i % 2 == j % 2`.
2. We can separate `a` into `evens` (elements at 0, 2, 4...) and `odds` (1, 3, 5...).
3. Solve the standard "Count Pairs with XOR <= K" problem for each list.
4. Total = `Solve(evens, L, U) + Solve(odds, L, U)`.
5. `Solve(arr, L, U) = Count(arr, U) - Count(arr, L - 1)`.

### Trie Logic for Count <= K

For a number `x` and limit `K`:
- Traverse bits 29 down to 0.
- `bitX`: bit of x. `bitK`: bit of K.
- We want `bitX ^ bitNode <= bitK`.
- **Case 1 (bitK == 0)**:
  - We MUST have `bitX ^ bitNode == 0` to not exceed K.
  - So `bitNode` must be `bitX`.
  - Go to child `bitX`. (If null, return current accumulated count? No, return 0 for this path).
- **Case 2 (bitK == 1)**:
  - Option A: `bitX ^ bitNode == 0`. This bit is strictly less than K (0 < 1). So ALL numbers in this subtree are valid regardless of lower bits. Add `count[child[bitX]]`.
  - Option B: `bitX ^ bitNode == 1`. This bit matches K (1 = 1). We need to check lower bits. Continue to child `!bitX` (1^bitX).

### Time Complexity

- **O(N * 30)**.

### Space Complexity

- **O(N * 30)** for Trie nodes.

![Algorithm Visualization](../images/BIT-004/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-004/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class TrieNode {
        TrieNode[] children = new TrieNode[2];
        int count = 0;
    }

    private void insert(TrieNode root, int num) {
        TrieNode curr = root;
        for (int i = 29; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
            curr.count++;
        }
    }

    private int countLessEqual(TrieNode root, int num, int K) {
        TrieNode curr = root;
        int count = 0;
        for (int i = 29; i >= 0; i--) {
            if (curr == null) break;
            int bitNum = (num >> i) & 1;
            int bitK = (K >> i) & 1;

            if (bitK == 1) {
                // If we choose path that aligns with bitNum, XOR result is 0 (0 < 1).
                // All nums in that subtree are strictly smaller.
                if (curr.children[bitNum] != null) {
                    count += curr.children[bitNum].count;
                }
                // Continue to the path that makes XOR 1 (equal to bitK)
                curr = curr.children[1 - bitNum];
            } else {
                // bitK is 0. We MUST make XOR 0. So must go to child matching bitNum.
                curr = curr.children[bitNum];
            }
        }
        if (curr != null) count += curr.count;
        return count;
    }

    private long countPairsWithLimit(List<Integer> nums, int K) {
        TrieNode root = new TrieNode();
        long total = 0;
        for (int num : nums) {
            total += countLessEqual(root, num, K);
            insert(root, num);
        }
        return total;
    }

    public long countPairwiseXorBandParity(int[] a, int L, int U) {
        List<Integer> evens = new ArrayList<>();
        List<Integer> odds = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            if (i % 2 == 0) evens.add(a[i]);
            else odds.add(a[i]);
        }

        long countEvens = countPairsWithLimit(evens, U) - countPairsWithLimit(evens, L - 1);
        long countOdds = countPairsWithLimit(odds, U) - countPairsWithLimit(odds, L - 1);

        return countEvens + countOdds;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int L = sc.nextInt();
        int U = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countPairwiseXorBandParity(a, L, U));
        sc.close();
    }
}
```

### Python

```python
import sys

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

def insert(root, num):
    curr = root
    for i in range(29, -1, -1):
        bit = (num >> i) & 1
        if curr.children[bit] is None:
            curr.children[bit] = TrieNode()
        curr = curr.children[bit]
        curr.count += 1

def count_less_equal(root, num, K):
    curr = root
    count = 0
    for i in range(29, -1, -1):
        if curr is None: break
        bit_num = (num >> i) & 1
        bit_k = (K >> i) & 1
        
        if bit_k == 1:
            # Case 0 < 1: Add all from "same bit" branch
            if curr.children[bit_num]:
                count += curr.children[bit_num].count
            # Traverse "diff bit" branch
            curr = curr.children[1 - bit_num]
        else:
            # Case 0 == 0: Must match
            curr = curr.children[bit_num]
            
    if curr:
        count += curr.count
    return count

def solve_for_list(nums, L, U):
    root_u = TrieNode()
    root_l = TrieNode()
    
    count_u = 0
    count_l = 0
    
    # We can run two passes or one pass with two Tries?
    # Actually cleanest is one helper function that builds trie
    # But rebuilding trie is costly if we do it twice per list. 
    # Just build one trie, query both? 
    # Wait, we count pairs (i, j). We query then insert.
    # We must do query(U) and query(L-1) at the same time to reuse the Trie.
    
    root = TrieNode()
    total = 0
    limit_l = L - 1
    
    for x in nums:
        c_u = count_less_equal(root, x, U)
        c_l = count_less_equal(root, x, limit_l)
        total += (c_u - c_l)
        insert(root, x)
        
    return total

def count_pairwise_xor_band_parity(a: list[int], L: int, U: int) -> int:
    evens = a[0::2]
    odds = a[1::2]
    return solve_for_list(evens, L, U) + solve_for_list(odds, L, U)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    L = int(data[ptr]); ptr += 1
    U = int(data[ptr]); ptr += 1
    
    result = count_pairwise_xor_band_parity(a, L, U)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[2];
    int count;
    
    TrieNode() {
        children[0] = children[1] = nullptr;
        count = 0;
    }
};

class Solution {
    void insert(TrieNode* root, int num) {
        TrieNode* curr = root;
        for (int i = 29; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (!curr->children[bit]) {
                curr->children[bit] = new TrieNode();
            }
            curr = curr->children[bit];
            curr->count++;
        }
    }
    
    int countLessEqual(TrieNode* root, int num, int K) {
        TrieNode* curr = root;
        int count = 0;
        for (int i = 29; i >= 0; i--) {
            if (!curr) break;
            int bitNum = (num >> i) & 1;
            int bitK = (K >> i) & 1;
            
            if (bitK == 1) {
                if (curr->children[bitNum]) {
                    count += curr->children[bitNum]->count;
                }
                curr = curr->children[1 - bitNum];
            } else {
                curr = curr->children[bitNum];
            }
        }
        if (curr) count += curr->count;
        return count;
    }
    
    long long solve(const vector<int>& nums, int L, int U) {
        TrieNode* root = new TrieNode();
        long long total = 0;
        int limitL = L - 1;
        
        for (int x : nums) {
            int cU = countLessEqual(root, x, U);
            int cL = countLessEqual(root, x, limitL);
            total += (cU - cL);
            insert(root, x);
        }
        // Memory leak check: In CP context, often ignored, but we should traverse delete
        // For strictness, assume simple struct is fine.
        return total;
    }

public:
    long long countPairwiseXorBandParity(vector<int>& a, int L, int U) {
        vector<int> evens, odds;
        for (int i = 0; i < a.size(); i++) {
            if (i % 2 == 0) evens.push_back(a[i]);
            else odds.push_back(a[i]);
        }
        return solve(evens, L, U) + solve(odds, L, U);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int L, U;
    cin >> L >> U;
    
    Solution solution;
    cout << solution.countPairwiseXorBandParity(a, L, U) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null];
    this.count = 0;
  }
}

class Solution {
  insert(root, num) {
    let curr = root;
    for (let i = 29; i >= 0; i--) {
      const bit = (num >> i) & 1;
      if (!curr.children[bit]) {
        curr.children[bit] = new TrieNode();
      }
      curr = curr.children[bit];
      curr.count++;
    }
  }

  countLessEqual(root, num, K) {
    let curr = root;
    let count = 0;
    for (let i = 29; i >= 0; i--) {
      if (!curr) break;
      const bitNum = (num >> i) & 1;
      const bitK = (K >> i) & 1;

      if (bitK === 1) {
        if (curr.children[bitNum]) {
          count += curr.children[bitNum].count;
        }
        curr = curr.children[1 - bitNum];
      } else {
        curr = curr.children[bitNum];
      }
    }
    if (curr) count += curr.count;
    return count;
  }

  solve(nums, L, U) {
    const root = new TrieNode();
    let total = 0;
    const limitL = L - 1;

    for (const x of nums) {
      const cU = this.countLessEqual(root, x, U);
      const cL = this.countLessEqual(root, x, limitL);
      total += (cU - cL);
      this.insert(root, x);
    }
    return total;
  }

  countPairwiseXorBandParity(a, L, U) {
    const evens = [];
    const odds = [];
    for (let i = 0; i < a.length; i++) {
      if (i % 2 === 0) evens.push(a[i]);
      else odds.push(a[i]);
    }
    return BigInt(this.solve(evens, L, U) + this.solve(odds, L, U));
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
    const L = Number(tokens[ptr++]);
    const U = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.countPairwiseXorBandParity(a, L, U).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `2, 3, 1, 7` (Indices 0, 1, 2, 3). `L=1, U=4`.
**Split**:
- Evens: `[2, 1]` (Idx 0, 2)
- Odds: `[3, 7]` (Idx 1, 3)

**Processing Evens**: `[2, 1]`
1. Insert 2.
   - Query 1 for valid pairs (None).
   - Trie: `{2}`.
2. Process 1.
   - Query `1 ^ y <= 4`. `y=2`. `1^2=3`. `3 <= 4`. Valid.
   - Count += 1.
   - Query `1 ^ y <= 0` (L-1). `3 <= 0` False.
   - Net pairs: 1. `(2, 1)`.

**Processing Odds**: `[3, 7]`
1. Insert 3.
2. Process 7.
   - Query `7 ^ y <= 4`. `y=3`. `7^3=4`. `4 <= 4`. Valid.
   - Count += 1.
   - Query `7 ^ y <= 0`. False.
   - Net pairs: 1. `(3, 7)`.

**Total**: 1 + 1 = 2.
Matches Example.

## ✅ Proof of Correctness

### Invariant

The condition `i+j` is even strictly partitions the search space into independent problems. The Trie logic correctly counts elements strictly less than `k` whenever a bit differs from `k` in the "smaller" direction, and follows the "equal" path otherwise. Summing these counts covers all valid leaves.

## 💡 Interview Extensions (High-Value Add-ons)

- **Max XOR**: Related classic problem.
- **Dynamic Updates**: If elements are added/removed (Trie supports deletion easily).
- **Modulo parity**: `i+j % 3 == 0`? Split into 3 buckets `0, 1, 2`. Pairs `(0,0), (1,2)`.

## Common Mistakes to Avoid

1. **Memory**:
   - ❌ Creating a new Trie for every number.
   - ✅ One Trie per sub-problem.
2. **Bit Depth**:
   - ❌ Using 32 bits when input is small? Safe but slightly slower. 30 (up to 10^9) is standard.

## Related Concepts

- **Maximum XOR of Two Numbers in an Array**: Classic Trie.
- **Count Pairs with XOR in a Range (LeetCode 1803)**: Same core problem.
