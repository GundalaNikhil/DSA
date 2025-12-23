---
problem_id: TRI_BIN_MIN_XOR__4256
display_id: TRI-005
slug: binary-trie-min-xor-pair-limit
title: "Binary Trie Min XOR Pair Under Limit"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - Binary Trie
  - Bit Manipulation
  - XOR
tags:
  - trie
  - binary-trie
  - bit-manipulation
  - xor
  - medium
premium: true
subscription_tier: basic
---

# Binary Trie Min XOR Pair Under Limit

![Problem Header](../images/TRI-005/header.png)

### 📋 Problem Summary

Find the minimum XOR value among all pairs in an array where the XOR is at most a given limit L.

![Problem Concept](../images/TRI-005/problem-illustration.png)

### 🌍 Real-World Scenario

**Network Packet Routing Optimization**

Imagine you're designing a network router that needs to find similar IP addresses for efficient packet routing. IP addresses can be represented as 32-bit integers, and XOR measures "difference" between addresses.

- **Goal**: Find pairs of IPs with minimal difference (XOR) below a threshold
- **Why**: Route similar traffic through same channels for cache efficiency
- **Example**: IPs 3 (0011) and 5 (0101) have XOR = 6 (0110) - only 2 bits different

Applications:

- Network traffic optimization
- Data deduplication systems
- Error-correcting codes
- Cryptographic key generation
- Database index optimization

### 📚 Detailed Explanation

**XOR Properties**:

- a XOR a = 0
- a XOR 0 = a
- XOR is commutative and associative
- Lower XOR = more similar numbers in binary

**Problem**: Given [3, 10, 5, 25] and L=8, find min XOR ≤ 8

Binary representations:

```
 3 = 00011
10 = 01010
 5 = 00101
25 = 11001
```

Check all pairs:

- 3^10 = 9 (> 8) ❌
- 3^5 = 6 (≤ 8) ✓
- 3^25 = 26 (> 8) ❌
- 10^5 = 15 (> 8) ❌
- 10^25 = 19 (> 8) ❌
- 5^25 = 28 (> 8) ❌

Answer: 6

### ❌ Naive Approach

**Idea**: Check all pairs, compute XOR, track minimum that's ≤ L.

```python
def min_xor_naive(arr, L):
    min_xor = float('inf')
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            xor_val = arr[i] ^ arr[j]
            if xor_val <= L:
                min_xor = min(min_xor, xor_val)

    return min_xor if min_xor != float('inf') else -1
```

**⏱️ Time Complexity: O(n²)**

- Two nested loops: n choose 2 = n(n-1)/2 pairs
- For n=100,000: ~5 billion operations

**📦 Space Complexity: O(1)**

### ✅ Optimal Approach

**💡 Key Insight**: Use binary trie to efficiently find numbers with minimal XOR.

**Binary Trie Structure**:

- Each level represents one bit position (MSB to LSB)
- Each node has 2 children: left (0) and right (1)
- Greedy traversal finds min XOR

** Binary Trie for [3, 5, 10]:**

```
Numbers in binary (4 bits for clarity):
3  = 0011
5  = 0101
10 = 1010

Binary Trie:
            Root
           /    \
         0        1
        /          \
      0             0
     / \             \
    1   1             1
   /     \             \
  1(3)   0(5)          0(10)

Path for 3:  0 → 0 → 1 → 1
Path for 5:  0 → 1 → 0 → 1
Path for 10: 1 → 0 → 1 → 0

Query 5 (0101) for min XOR:
Bit 3: Want 0 (have 0) → go left  ✓
Bit 2: Want 1 (have 0,1) → go 1  ✓
Bit 1: Want 0 (only 0) → go 0   ✓
Bit 0: Want 1 (only 1) → go 1   ✓
Result: 0101 = 5, XOR(5,5) = 0

Query 5 for next best:
Try 0→0 path:
Result: 0011 = 3, XOR(5,3) = 6
```

**Approach**:

1. Insert all numbers into binary trie
2. For each number, query trie to find closest match
3. Track minimum XOR ≤ L

**Greedy Query Strategy**:
For each bit position, prefer same bit (XOR = 0) to minimize XOR:

- If current bit is 0, try left child first
- If current bit is 1, try right child first

**Example**: Find closest to 5 (0101)

```
Trie contains: 3 (0011), 10 (1010)

Query 5 (0101):
Bit 3 (MSB): Want 0, path: left (has 3)
Bit 2: Want 1, but only 0 available under 3
Bit 1: Want 0, available
Bit 0: Want 1, but only 1 available

Result: 3, XOR = 5^3 = 6
```

**⏱️ Time Complexity: O(n × 30)**

- Insert n numbers: O(n × 30) where 30 = bit depth
- Query n times: O(n × 30)
- Total: O(n) for practical purposes

**📦 Space Complexity: O(n × 30)**

- Trie nodes for all numbers

### 🎨 Visual Representation

**Binary Trie for [3, 10, 5]**:

```
        root
       /    \
      0      1
     /        \
    0          0
   / \          \
  0   1          1
 / \ / \        / \
1  0 1  0      1   0
```

Numbers stored:

- 3 = 0011: root→0→0→0→1→1
- 10 = 1010: root→1→0→1→0
- 5 = 0101: root→0→1→0→1

### 🧪 Test Case Walkthrough

**Input**: arr = [3, 10, 5, 25], L = 8

**Step 1: Build Trie**
Insert 3, 10, 5, 25 into binary trie (30-bit representation)

**Step 2: Query Each Number**

Query 3:

- Find closest to 3 in trie
- Best: 5, XOR = 6 ≤ 8 ✓

Query 10:

- Find closest to 10
- Best: 3, XOR = 9 > 8 ❌

Query 5:

- Find closest to 5
- Best: 3, XOR = 6 ≤ 8 ✓

Query 25:

- Find closest to 25
- All XORs > 8 ❌

**Step 3: Result**
Minimum XOR ≤ 8: 6

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Wrong Bit Order** 🔴

**Problem**: Processing LSB to MSB instead of MSB to LSB
**Solution**: Start from bit 29 (or 31) down to 0

#### 2. **Not Handling L Constraint** 🔴

**Problem**: Finding absolute min XOR without checking L
**Solution**: Only update result if XOR ≤ L

#### 3. **Counting Same Element Twice** 🔴

**Problem**: Computing a[i] XOR a[i] = 0
**Solution**: Query before inserting, or skip i==j

#### 4. **Integer Overflow** 🔴

**Problem**: XOR results exceeding int range
**Solution**: Use appropriate data types (int is sufficient for XOR)

### 🔑 Algorithm Steps

**Binary Trie Algorithm**:

1. **Create empty binary trie**

2. **For each number in array**:

   - Query trie for closest number
   - Compute XOR with closest
   - If XOR ≤ L, update minimum
   - Insert current number into trie

3. **Return** minimum XOR found, or -1

**Pseudocode**:

```
function minXOR(arr, L):
    trie = new BinaryTrie()
    min_xor = infinity

    for num in arr:
        if trie not empty:
            closest = trie.findClosest(num)
            xor_val = num XOR closest
            if xor_val <= L:
                min_xor = min(min_xor, xor_val)

        trie.insert(num)

    return min_xor if min_xor != infinity else -1
```

### 💻 Implementations

### Java

```java
class TrieNode {
    TrieNode[] children = new TrieNode[2];
}

class Solution {
    private static final int MAX_BITS = 30;
    private TrieNode root;

    public int minXORPairUnderLimit(int[] arr, int L) {
        if (arr == null || arr.length < 2) return -1;

        root = new TrieNode();
        int minXOR = Integer.MAX_VALUE;

        for (int num : arr) {
            if (root.children[0] != null || root.children[1] != null) {
                int closest = findClosest(num);
                int xorVal = num ^ closest;
                if (xorVal <= L) {
                    minXOR = Math.min(minXOR, xorVal);
                }
            }
            insert(num);
        }

        return minXOR == Integer.MAX_VALUE ? -1 : minXOR;
    }

    private void insert(int num) {
        TrieNode curr = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
        }
    }

    private int findClosest(int num) {
        TrieNode curr = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            // Prefer same bit for minimum XOR
            if (curr.children[bit] != null) {
                curr = curr.children[bit];
            } else {
                bit = 1 - bit;
                curr = curr.children[bit];
            }

            result |= (bit << i);
        }

        return result;
    }
}

// Time: O(n × 30), Space: O(n × 30)
```

### Python

```python
class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    MAX_BITS = 30

    def min_xor_pair_under_limit(self, arr: list, L: int) -> int:
        """
        Find minimum XOR pair value under limit L using binary trie.

        Args:
            arr: Array of integers
            L: Maximum allowed XOR value

        Returns:
            Minimum XOR value <= L, or -1 if none exists
        """
        if not arr or len(arr) < 2:
            return -1

        self.root = TrieNode()
        min_xor = float('inf')

        for num in arr:
            # Query before insert to avoid XOR with self
            if self.root.children[0] or self.root.children[1]:
                closest = self._find_closest(num)
                xor_val = num ^ closest
                if xor_val <= L:
                    min_xor = min(min_xor, xor_val)

            self._insert(num)

        return min_xor if min_xor != float('inf') else -1

    def _insert(self, num):
        curr = self.root
        for i in range(self.MAX_BITS, -1, -1):
            bit = (num >> i) & 1
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def _find_closest(self, num):
        curr = self.root
        result = 0

        for i in range(self.MAX_BITS, -1, -1):
            bit = (num >> i) & 1

            # Prefer same bit for minimum XOR
            if curr.children[bit]:
                curr = curr.children[bit]
            else:
                bit = 1 - bit
                curr = curr.children[bit]

            result |= (bit << i)

        return result

# Time: O(n × 30), Space: O(n × 30)

if __name__ == "__main__":
    first_line = input().strip().split()
    n = int(first_line[0])
    L = int(first_line[1])
    arr = list(map(int, input().strip().split()))

    solution = Solution()
    result = solution.min_xor_pair_under_limit(arr, L)
    print(result)
```

### C++++

```cpp
struct TrieNode {
    TrieNode* children[2];

    TrieNode() {
        children[0] = children[1] = nullptr;
    }
};

class Solution {
private:
    static const int MAX_BITS = 30;
    TrieNode* root;

    void insert(int num) {
        TrieNode* curr = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (!curr->children[bit]) {
                curr->children[bit] = new TrieNode();
            }
            curr = curr->children[bit];
        }
    }

    int findClosest(int num) {
        TrieNode* curr = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            if (curr->children[bit]) {
                curr = curr->children[bit];
            } else {
                bit = 1 - bit;
                curr = curr->children[bit];
            }

            result |= (bit << i);
        }

        return result;
    }

public:
    int minXORPairUnderLimit(vector<int>& arr, int L) {
        if (arr.size() < 2) return -1;

        root = new TrieNode();
        int minXOR = INT_MAX;

        for (int num : arr) {
            if (root->children[0] || root->children[1]) {
                int closest = findClosest(num);
                int xorVal = num ^ closest;
                if (xorVal <= L) {
                    minXOR = min(minXOR, xorVal);
                }
            }
            insert(num);
        }

        return minXOR == INT_MAX ? -1 : minXOR;
    }
};

// Time: O(n × 30), Space: O(n × 30)
```

### JavaScript

```javascript
class TrieNode {
  constructor() {
    this.children = [null, null];
  }
}

class Solution {
  static MAX_BITS = 30;

  minXORPairUnderLimit(arr, L) {
    if (!arr || arr.length < 2) return -1;

    this.root = new TrieNode();
    let minXOR = Infinity;

    for (const num of arr) {
      if (this.root.children[0] || this.root.children[1]) {
        const closest = this.findClosest(num);
        const xorVal = num ^ closest;
        if (xorVal <= L) {
          minXOR = Math.min(minXOR, xorVal);
        }
      }
      this.insert(num);
    }

    return minXOR === Infinity ? -1 : minXOR;
  }

  insert(num) {
    let curr = this.root;
    for (let i = Solution.MAX_BITS; i >= 0; i--) {
      const bit = (num >> i) & 1;
      if (!curr.children[bit]) {
        curr.children[bit] = new TrieNode();
      }
      curr = curr.children[bit];
    }
  }

  findClosest(num) {
    let curr = this.root;
    let result = 0;

    for (let i = Solution.MAX_BITS; i >= 0; i--) {
      let bit = (num >> i) & 1;

      if (curr.children[bit]) {
        curr = curr.children[bit];
      } else {
        bit = 1 - bit;
        curr = curr.children[bit];
      }

      result |= bit << i;
    }

    return result;
  }
}

// Time: O(n × 30), Space: O(n × 30)
```

### 📊 Comparison Table

| **Aspect**        | **Naive O(n²)** | **Binary Trie** |
| ----------------- | --------------- | --------------- |
| **Time**          | O(n²)           | O(n × 30)       |
| **Space**         | O(1)            | O(n × 30)       |
| **For n=100,000** | ~5B operations  | ~3M operations  |
| **Scalability**   | Poor            | Excellent       |

### 🎯 Key Takeaways

1. **Binary tries optimize XOR operations**
2. **Greedy bit-by-bit matching** finds minimum XOR efficiently
3. **Process from MSB to LSB** for correct results
4. **Query before insert** to avoid self-XOR
5. **Time-space tradeoff**: Use O(n) space for O(n) time

### 🔗 Related Problems

- Maximum XOR of Two Numbers
- Maximum XOR Subarray
- Count Pairs With XOR in Range
- Minimum XOR Sum of Two Arrays

---

**Difficulty**: Medium  
**Topics**: Trie, Binary Trie, Bit Manipulation, XOR  
**Companies**: Google, Microsoft, Amazon


## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 0 ≤ a[i] ≤ 10^9
- 0 ≤ L ≤ 10^9