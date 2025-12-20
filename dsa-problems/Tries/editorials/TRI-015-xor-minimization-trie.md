---
problem_id: TRI_XOR_MINIMIZATION__9417
display_id: TRI-015
slug: xor-minimization-trie
title: "XOR Minimization With Trie"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - Binary Trie
  - XOR
  - Bit Manipulation
tags:
  - trie
  - xor
  - binary
  - prefix-xor
premium: true
subscription_tier: basic
---

# TRI-015: XOR Minimization With Trie

## 📋 Problem Summary

Given an array `a` and an integer `X`, find the subarray whose XOR, when XOR'd with `X`, produces the minimum value. Return that minimal XOR result.

## 🌍 Real-World Scenario

**Network Error Detection & Correction**

In telecommunications and computer networks, XOR operations are fundamental to error detection codes like parity bits and cyclic redundancy checks (CRC).

Consider a data transmission system:

- Packets are transmitted with computed checksums (XOR-based)
- Receiver wants to find the transmission window with minimum error (minimum XOR difference from expected)
- This helps identify which data segment needs retransmission

**Industry Applications:**

1. **RAID Storage Systems**: XOR-based redundancy to reconstruct lost data with minimal computation
2. **Cryptography**: XOR cipher analysis and key recovery
3. **Signal Processing**: Finding signal segments with minimum noise (represented as XOR difference)
4. **Data Deduplication**: Identifying similar data blocks using XOR distance metrics
5. **Error-Correcting Codes**: Hamming distance minimization in coding theory

The problem models finding the data window that, when combined (XOR'd) with a reference pattern `X`, produces the smallest deviation—critical for error correction and data integrity.

![Real-World Application](../images/TRI-015/real-world-scenario.png)

## Detailed Explanation

**Problem Breakdown:**

Given:

- Array `a` of n integers
- Target value `X`

Find:

- Subarray `[i, j]` such that `(a[i] ⊕ a[i+1] ⊕ ... ⊕ a[j]) ⊕ X` is minimized
- Return the minimum value

**Key Insights:**

1. **Prefix XOR Technique**:

   - Let `prefix[i] = a[0] ⊕ a[1] ⊕ ... ⊕ a[i-1]`
   - Subarray XOR `[i, j] = prefix[j+1] ⊕ prefix[i]`

2. **Transform Problem**:

   - We want to minimize `(prefix[j+1] ⊕ prefix[i]) ⊕ X`
   - This equals `prefix[j+1] ⊕ prefix[i] ⊕ X`
   - For each prefix[j+1], find prefix[i] that minimizes `prefix[i] ⊕ (prefix[j+1] ⊕ X)`

3. **Binary Trie for XOR Minimization**:
   - Store prefix XORs in a binary trie (bit by bit, MSB first)
   - For a query value, traverse trie greedily: prefer bit that matches (keeps XOR small)
   - Time: O(log(max_value)) per query

**Example Walkthrough:**

Array: `a = [4, 1, 2]`, X = 3

**XOR Prefix Trie:**

```
Step 1: Compute prefix XORs
  prefix[0] = 0 (empty)
  prefix[1] = 4        = 100₂
  prefix[2] = 4 ⊕ 1   = 101₂ = 5
  prefix[3] = 5 ⊕ 2   = 111₂ = 7

Binary Trie (3 bits for clarity):
             Root
            /    \
          0       1
         /       / \
        0       0   1
       /       /     \
      0       0       1
    (000)   (100)   (111)
     =0      =4      =7

  Also insert 5=101:
             Root
            /    \
          0       1
         /       / \
        0       0   1
       /       /   / \
      0       0   0   1
    (000)   (100)(101)(111)
     =0      =4   =5   =7

Query Process (minimize prefix[i] ⊕ target):
────────────────────────────────────────────
prefix[1] = 4, target = 4⊕3 = 7 (111₂)
  Trie has: {0=000}
  Query 111: Try to match each bit
    Bit 2: want 1, only 0 available → go 0
    Bit 1: want 1, only 0 available → go 0
    Bit 0: want 1, only 0 available → go 0
  Result: 0 ⊕ 7 = 7
  Subarray XOR = 4, 4⊕3 = 7

prefix[2] = 5, target = 5⊕3 = 6 (110₂)
  Trie has: {0=000, 4=100}
  Query 110:
    Bit 2: want 1, have both → prefer 1 → go 1
    Bit 1: want 1, only 0 available → go 0
    Bit 0: want 0, only 0 available → go 0
  Result: 4=100, 4⊕6 = 2
  Subarray XOR = 1, 1⊕3 = 2

prefix[3] = 7, target = 7⊕3 = 4 (100₂)
  Trie has: {0=000, 4=100, 5=101}
  Query 100:
    Bit 2: want 1, have both → prefer 1 → go 1
    Bit 1: want 0, have both → prefer 0 → go 0
    Bit 0: want 0, have both → prefer 0 → go 0
  Result: 4=100, 4⊕4 = 0 ✓
  Subarray XOR = 3, 3⊕3 = 0

Minimum: 0
```

Step 1: Compute prefix XORs

- prefix[0] = 0 (empty)
- prefix[1] = 4
- prefix[2] = 4 ⊕ 1 = 5
- prefix[3] = 4 ⊕ 1 ⊕ 2 = 7

Step 2: For each prefix[j], query for best prefix[i] where i < j

- Goal: minimize `prefix[i] ⊕ (prefix[j] ⊕ X)`

Query for prefix[1]=4 with target=4⊕3=7:

- Trie contains: {0}
- Best match: 0
- XOR: 0 ⊕ 7 = 7
- Subarray: [0,0], XOR=4, result=4⊕3=7

Query for prefix[2]=5 with target=5⊕3=6:

- Trie contains: {0, 4}
- Best match: 6? Let's check:
  - 0 ⊕ 6 = 6
  - 4 ⊕ 6 = 2 ← better!
- Result: 2
- Subarray: [1,1], XOR=1, result=1⊕3=2

Query for prefix[3]=7 with target=7⊕3=4:

- Trie contains: {0, 4, 5}
- Best match:
  - 0 ⊕ 4 = 4
  - 4 ⊕ 4 = 0 ← best!
  - 5 ⊕ 4 = 1
- Result: 0
- Subarray: [1,2], XOR=1⊕2=3, result=3⊕3=0

**Answer: 0** (subarray [1,2] has XOR=3, and 3⊕3=0)

![Problem Illustration](../images/TRI-015/problem-illustration.png)

## Naive Approach

**Intuition:**

Check all possible subarrays, compute their XOR, then XOR with X, and find the minimum.

**Algorithm:**

1. For each starting index i:
   - For each ending index j >= i:
     - Compute XOR of subarray [i, j]
     - Compute result = subarray_XOR ⊕ X
     - Track minimum result

**Time Complexity:** O(n²)

- Two nested loops: O(n²)
- Computing XOR on the fly: O(1) per iteration

**Space Complexity:** O(1)

**Limitations:**

- Quadratic time is slow for large arrays
- Doesn't leverage XOR properties for optimization
- No reuse of previously computed XORs

## Optimal Approach

**Key Insight:**

Use **prefix XOR array** + **binary trie** to efficiently find the minimum XOR.

**Algorithm:**

1. **Compute Prefix XORs**:

   ```
   prefix[0] = 0
   prefix[i] = a[0] ⊕ a[1] ⊕ ... ⊕ a[i-1]
   ```

2. **Build Binary Trie with Queries**:

   - For each position j from 0 to n:
     - Query trie for value closest to `prefix[j] ⊕ X`
       - This finds the best prefix[i] to minimize `prefix[i] ⊕ (prefix[j] ⊕ X)`
     - Update minimum result
     - Insert prefix[j] into trie

3. **Binary Trie Query**:
   - Represent numbers as 32-bit binary (or based on max value)
   - Traverse trie from MSB to LSB
   - At each bit position:
     - If query bit is B, prefer child B (to make XOR=0 at this bit)
     - If child B doesn't exist, take the other child (XOR=1 at this bit)
   - Accumulated path gives the closest match

**Time Complexity:** O(n × log(MAX_VAL))

- n iterations, each doing O(log(MAX_VAL)) trie operations

**Space Complexity:** O(n × log(MAX_VAL)) for the trie

**Why This Is Optimal:**

- **Linear in Array Size**: Each element processed once
- **Logarithmic in Value Range**: Trie depth is log(max_value), typically 30-32 bits
- **Optimal XOR Query**: Binary trie provides best possible match in O(log V) time
- **No Redundant Computation**: Reuses prefix XORs efficiently

![Algorithm Visualization](../images/TRI-015/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class TrieNode {
    TrieNode[] children = new TrieNode[2];  // 0 and 1
}

class Solution {
    private TrieNode root = new TrieNode();
    private static final int MAX_BITS = 30;

    public int minimizeXOR(int[] a, int X) {
        int n = a.length;
        int[] prefix = new int[n + 1];

        // Compute prefix XORs
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] ^ a[i];
        }

        int minXor = Integer.MAX_VALUE;

        // Process each prefix
        for (int j = 0; j <= n; j++) {
            if (root.children[0] != null || root.children[1] != null) {
                // Query for best match
                int target = prefix[j] ^ X;
                int closest = query(target);
                minXor = Math.min(minXor, closest ^ target);
            }
            // Insert current prefix
            insert(prefix[j]);
        }

        return minXor;
    }

    private void insert(int num) {
        TrieNode node = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node.children[bit] == null) {
                node.children[bit] = new TrieNode();
            }
            node = node.children[bit];
        }
    }

    private int query(int num) {
        TrieNode node = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            // Prefer same bit (to minimize XOR)
            if (node.children[bit] != null) {
                node = node.children[bit];
            } else {
                // Take opposite bit
                result |= (1 << i);
                node = node.children[1 - bit];
            }
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int X = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.minimizeXOR(a, X);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    MAX_BITS = 30

    def __init__(self):
        self.root = TrieNode()

    def minimize_xor(self, a: List[int], X: int) -> int:
        n = len(a)
        prefix = [0] * (n + 1)

        # Compute prefix XORs
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ a[i]

        min_xor = float('inf')

        # Process each prefix
        for j in range(n + 1):
            if self.root.children[0] is not None or self.root.children[1] is not None:
                # Query for best match
                target = prefix[j] ^ X
                closest = self._query(target)
                min_xor = min(min_xor, closest ^ target)
            # Insert current prefix
            self._insert(prefix[j])

        return min_xor

    def _insert(self, num: int):
        node = self.root
        for i in range(self.MAX_BITS, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def _query(self, num: int) -> int:
        node = self.root
        result = 0

        for i in range(self.MAX_BITS, -1, -1):
            bit = (num >> i) & 1

            # Prefer same bit (to minimize XOR)
            if node.children[bit] is not None:
                node = node.children[bit]
            else:
                # Take opposite bit
                result |= (1 << i)
                node = node.children[1 - bit]

        return result

def main():
    import sys
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])
    X = int(input_data[1])
    a = [int(input_data[i + 2]) for i in range(n)]

    solution = Solution()
    result = solution.minimize_xor(a, X)

    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
};

class Solution {
private:
    TrieNode* root;
    static const int MAX_BITS = 30;

    void insert(int num) {
        TrieNode* node = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node->children[bit] == nullptr) {
                node->children[bit] = new TrieNode();
            }
            node = node->children[bit];
        }
    }

    int query(int num) {
        TrieNode* node = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            if (node->children[bit] != nullptr) {
                node = node->children[bit];
            } else {
                result |= (1 << i);
                node = node->children[1 - bit];
            }
        }

        return result;
    }

public:
    Solution() { root = new TrieNode(); }

    int minimizeXOR(vector<int>& a, int X) {
        int n = a.size();
        vector<int> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] ^ a[i];
        }

        int minXor = INT_MAX;

        for (int j = 0; j <= n; j++) {
            if (root->children[0] != nullptr || root->children[1] != nullptr) {
                int target = prefix[j] ^ X;
                int closest = query(target);
                minXor = min(minXor, closest ^ target);
            }
            insert(prefix[j]);
        }

        return minXor;
    }
};

int main() {
    int n, X;
    cin >> n >> X;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    int result = solution.minimizeXOR(a, X);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null];
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.MAX_BITS = 30;
  }

  insert(num) {
    let node = this.root;
    for (let i = this.MAX_BITS; i >= 0; i--) {
      const bit = (num >> i) & 1;
      if (node.children[bit] === null) {
        node.children[bit] = new TrieNode();
      }
      node = node.children[bit];
    }
  }

  query(num) {
    let node = this.root;
    let result = 0;

    for (let i = this.MAX_BITS; i >= 0; i--) {
      const bit = (num >> i) & 1;

      if (node.children[bit] !== null) {
        node = node.children[bit];
      } else {
        result |= 1 << i;
        node = node.children[1 - bit];
      }
    }

    return result;
  }

  minimizeXOR(a, X) {
    const n = a.length;
    const prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] ^ a[i];
    }

    let minXor = Infinity;

    for (let j = 0; j <= n; j++) {
      if (this.root.children[0] !== null || this.root.children[1] !== null) {
        const target = prefix[j] ^ X;
        const closest = this.query(target);
        minXor = Math.min(minXor, closest ^ target);
      }
      this.insert(prefix[j]);
    }

    return minXor;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, X] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);

  const solution = new Solution();
  const result = solution.minimizeXOR(a, X);

  console.log(result);
});
```

## Common Mistakes

1. **Not Using Prefix XOR**: Computing subarray XOR directly for each pair is O(n³) or O(n²)
2. **Incorrect Bit Order**: Must traverse MSB to LSB in binary trie
3. **Off-by-One in Prefix**: Forgetting prefix[0]=0 for empty subarray
4. **Overflow Issues**: Not handling integer limits properly

## Related Concepts

- Binary Trie
- XOR Properties
- Prefix XOR
- Bit Manipulation
- Greedy Algorithms
- Error Detection Codes
