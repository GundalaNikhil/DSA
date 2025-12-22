---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
---

# Two Unique With Triple Others Under Mask

![Problem Header](../images/BIT-002/header.png)

### 📋 Problem Summary

Given an array where every number appears exactly **three times** except two distinct numbers that appear **once** each, find these two unique numbers. You're also given a mask `M` that guarantees the two uniques differ in at least one bit position set in `M`.

![Problem Concept](../images/BIT-002/problem-illustration.png)

### 🌍 Real-World Scenario

**Manufacturing Quality Control System**

A semiconductor factory tracks component IDs through three inspection stages. Each good component gets scanned 3 times (initial, mid-process, final). However, two defective components failed early and were scanned only once before being flagged.

The system log: `[5,5,5, 9,9,9, 3, 6]`

- Components 5 and 9: Passed all 3 inspections ✓
- Components 3 and 6: Defective (single scan) ⚠️

The mask `M=2` indicates which sensor bit is reliable for distinguishing between different defect types. Find both defective component IDs efficiently!

### 📚 Detailed Explanation

**Why This is Harder Than "Single Unique"**:

In the classic problem (all appear twice except one), we simply XOR everything:

```
a ⊕ a = 0  (pairs cancel)
Result: the unique number
```

But with **two uniques** and **triples**, we have two challenges:

1. XOR alone gives us `a ⊕ b`, not separate values
2. Triples don't naturally cancel with XOR (1⊕1⊕1 = 1, not 0!)

**Key Insight: Bit Counting Modulo 3**

For each bit position across all numbers:

- If a number appears 3 times, its bits contribute 0 (mod 3)
- Only the two uniques contribute to the remainder

**Example**:

```
Number 5 = 101 appears 3 times
Bit 0: 1+1+1 = 3 → 3 % 3 = 0 ✓ (cancels)
Bit 2: 1+1+1 = 3 → 3 % 3 = 0 ✓ (cancels)
```

**The Three-Phase Algorithm**:

**Phase 1**: Count bits mod 3 to get `xor_both = a ⊕ b`
**Phase 2**: Find a differentiating bit using mask M  
**Phase 3**: Partition array and find each unique separately

### ❌ Naive Approach

**Idea**: Use hash map to count frequencies.

```python
def naive_approach(arr, M):
    from collections import Counter
    freq = Counter(arr)

    result = [num for num, count in freq.items() if count == 1]
    return sorted(result)
```

**⏱️ Time Complexity: O(n)**
**📦 Space Complexity: O(n)** - Hash map stores unique values

**Problem**: Uses O(n) space, not suitable for memory-constrained systems!

### ✅ Optimal Approach - Phase by Phase

#### Phase 1: Extract XOR of Two Uniques

**Concept**: Count each bit position mod 3.

```python
def get_xor_of_uniques(arr):
    bit_count = [0] * 32  # For 32-bit integers

    # Count each bit across all numbers
    for num in arr:
        for i in range(32):
            if num & (1 << i):
                bit_count[i] += 1

    # Build XOR from remainders
    xor_both = 0
    for i in range(32):
        if bit_count[i] % 3 != 0:
            xor_both |= (1 << i)

    return xor_both
```

**Why This Works**:

- Numbers appearing 3× contribute 0 or 3 to each bit count
- Remainders after % 3 come only from the two uniques
- If bit i has remainder 1 or 2, one or both uniques have that bit set

**Important**: The remainder tells us about `a ⊕ b`:

- Remainder 1: One unique has bit i set (contributes to XOR)
- Remainder 2: Both uniques have bit i set (XOR = 0) OR neither (also XOR = 0)


- If both have bit set: count = 2 (mod 3) → contributes to result
- If one has bit set: count = 1 (mod 3) → contributes to result
- If neither has bit set: count = 0 (mod 3) → doesn't contribute


XOR truth table:

- 0 ⊕ 0 = 0
- 0 ⊕ 1 = 1
- 1 ⊕ 0 = 1
- 1 ⊕ 1 = 0

If bit i appears count times total from the two uniques:

- count = 0: Neither has bit → a⊕b bit i = 0⊕0 = 0
- count = 1: One has bit → a⊕b bit i = 1⊕0 = 1
- count = 2: Both have bit → a⊕b bit i = 1⊕1 = 0

So only count % 3 = 1 contributes to XOR!

#### Phase 2: Find Differentiating Bit in Mask

```python
def find_diff_bit(xor_both, M):
    # xor_both has 1s where a and b differ
    # M indicates which bits are reliable
    # Find any bit that's 1 in both

    masked_diff = xor_both & M

    # Get rightmost set bit
    diff_bit = masked_diff & -masked_diff

    return diff_bit
```

**Explanation**:

- `xor_both` has 1s where a and b differ
- `M` tells us which bits are guaranteed to show difference
- `masked_diff` isolates differing bits within the mask
- We pick any such bit to partition the array

#### Phase 3: Partition and Find Both

```python
def find_both_uniques(arr, M):
    # Phase 1: Get XOR
    xor_both = get_xor_of_uniques(arr)

    # Phase 2: Find differentiating bit
    diff_bit = find_diff_bit(xor_both, M)

    # Phase 3: Partition by diff_bit
    unique1, unique2 = 0, 0

    bit_count_0 = [0] * 32
    bit_count_1 = [0] * 32

    for num in arr:
        if num & diff_bit:
            # Group 1: diff_bit is set
            for i in range(32):
                if num & (1 << i):
                    bit_count_1[i] += 1
        else:
            # Group 0: diff_bit is not set
            for i in range(32):
                if num & (1 << i):
                    bit_count_0[i] += 1

    # Reconstruct uniques from remainders
    for i in range(32):
        if bit_count_0[i] % 3 == 1:
            unique1 |= (1 << i)
        if bit_count_1[i] % 3 == 1:
            unique2 |= (1 << i)

    return sorted([unique1, unique2])
```

**⏱️ Time Complexity: O(n)**

- Phase 1: O(n × 32) = O(n)
- Phase 2: O(1)
- Phase 3: O(n × 32) = O(n)
- Total: **O(n)**

**📦 Space Complexity: O(1)**

- Only fixed-size arrays (2 × 32 integers)
- No hash maps!

### 🎨 Visual Representation

**Example**: `arr = [5,5,5,9,9,9,3,6], M=2`

**Binary Representations**:

```
5 = 0101 (appears 3×)
9 = 1001 (appears 3×)
3 = 0011 (appears 1×)
6 = 0110 (appears 1×)
M = 0010 (bit 1 is the mask)
```

**Phase 1: Bit Counting Mod 3**

```
Count each bit position:
Bit 0: 1(×3) + 1(×3) + 1 + 0 = 7 → 7%3 = 1 ✓
Bit 1: 0(×3) + 0(×3) + 1 + 1 = 2 → 2%3 = 2
Bit 2: 1(×3) + 0(×3) + 0 + 1 = 4 → 4%3 = 1 ✓
Bit 3: 0(×3) + 1(×3) + 0 + 0 = 3 → 3%3 = 0

Remainders: [1, 2, 1, 0]
```

**Interpretation**:

- Bit 0: remainder 1 → one unique has it set → XOR bit 0 = 1
- Bit 1: remainder 2 → both have it set → XOR bit 1 = 0
- Bit 2: remainder 1 → one unique has it set → XOR bit 2 = 1
- Bit 3: remainder 0 → neither has it set → XOR bit 3 = 0

**xor_both = 0101 = 5**

Verify: 3 ⊕ 6 = 0011 ⊕ 0110 = 0101 = 5 ✓

**Phase 2: Find Diff Bit**

```
xor_both = 0101
M        = 0010
xor_both & M = 0000

No overlap means M does not match a set bit in xor_both.
In xor_both = 5 = 0101, bit 1 is 0, so this mask cannot separate the uniques.

So there's NO differentiating bit in the mask!
```

This suggests the example in the problem statement may have an issue. Use a corrected example:

**Corrected Example**: `arr = [5,5,5,9,9,9,3,6], M=4`

```
M = 4 = 0100 (bit 2 is the mask)
xor_both = 0101
xor_both & M = 0100 ✓ (bit 2 can differentiate!)

diff_bit = 0100 (use bit 2)
```

**Phase 3: Partition**

```
Partition by bit 2:
- Bit 2 = 0: [5,5,5,3] → count mod 3 → 3
- Bit 2 = 1: [9,9,9,6] → count mod 3 → 6

Result: [3, 6] ✓
```

### 🧪 Test Case Walkthrough

Clearer example:

**Input**: `arr = [2,2,2, 8,8,8, 3, 5], M=2`

**Step-by-Step**:

```
2 = 0010 (×3)
8 = 1000 (×3)
3 = 0011 (×1)
5 = 0101 (×1)

Phase 1: Bit counting
Bit 0: 0+0+0 + 0+0+0 + 1 + 1 = 2 → 2%3 = 2
Bit 1: 1+1+1 + 0+0+0 + 1 + 0 = 4 → 4%3 = 1 ✓
Bit 2: 0+0+0 + 0+0+0 + 0 + 1 = 1 → 1%3 = 1 ✓
Bit 3: 0+0+0 + 1+1+1 + 0 + 0 = 3 → 3%3 = 0

xor_both = 0110 = 6

Verify: 3⊕5 = 0011⊕0101 = 0110 = 6 ✓

Phase 2: Find diff bit
M = 0010 (bit 1)
xor_both & M = 0110 & 0010 = 0010 ✓
diff_bit = 0010 (bit 1)

Phase 3: Partition by bit 1
Group 0 (bit 1 = 0): [8,8,8,5]
  Bit 0: 0+0+0+1 = 1 → 1%3 = 1 ✓
  Bit 2: 0+0+0+1 = 1 → 1%3 = 1 ✓
  → unique = 0101 = 5 ✓

Group 1 (bit 1 = 1): [2,2,2,3]
  Bit 0: 0+0+0+1 = 1 → 1%3 = 1 ✓
  Bit 1: 1+1+1+1 = 4 → 4%3 = 1 ✓
  → unique = 0011 = 3 ✓

Result: [3, 5] ✓
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Misunderstanding Bit Count Remainders** 🔴

**Problem**:

```python
# Wrong: Using remainder directly as bit value
if bit_count[i] % 3 > 0:
    result |= bit_count[i] % 3  # ❌ WRONG!
```

**Why Wrong**: Remainder 2 doesn't mean "set bit to 2"!

**Correct**:

```python
# Only remainder 1 contributes to XOR
if bit_count[i] % 3 == 1:
    result |= (1 << i)  # ✅ Set bit i
```

#### 2. **Forgetting to Use the Mask** 🔴

**Problem**:

```python
# Using any differentiating bit
diff_bit = xor_both & -xor_both  # ❌ Might not be in M!
```

**Why Wrong**: Problem guarantees difference in M, not anywhere!

**Correct**:

```python
diff_bit = (xor_both & M) & -(xor_both & M)  # ✅ Use M
```

#### 3. **Not Handling Negative Numbers** 🔴

For negative numbers in two's complement, bit operations work the same, but be careful with sign extension.

#### 4. **Off-by-One in Bit Indexing** 🔴

Remember: bit positions are 0-indexed. Bit 0 is the LSB (rightmost).

### 🔑 Algorithm Steps

**Complete Algorithm**:

```
function findTwoUniques(arr, M):
    // Phase 1: Get XOR of both uniques
    bit_count = array of 32 zeros

    for each num in arr:
        for i from 0 to 31:
            if bit i of num is set:
                bit_count[i]++

    xor_both = 0
    for i from 0 to 31:
        if bit_count[i] % 3 == 1:
            set bit i of xor_both

    // Phase 2: Find differentiating bit in mask
    masked_diff = xor_both & M
    diff_bit = masked_diff & -masked_diff  // rightmost set bit

    // Phase 3: Partition and find each unique
    bit_count_0 = array of 32 zeros
    bit_count_1 = array of 32 zeros

    for each num in arr:
        if (num & diff_bit) is set:
            count num's bits in bit_count_1
        else:
            count num's bits in bit_count_0

    unique1 = reconstruct from bit_count_0 (remainder 1 positions)
    unique2 = reconstruct from bit_count_1 (remainder 1 positions)

    return sorted [unique1, unique2]
```

### 💻 Implementations

### Python

```python
def find_two_uniques(arr, M):
    """
    Find two numbers appearing once when all others appear thrice.

    Args:
        arr: List of integers
        M: Mask indicating reliable differentiating bits

    Returns:
        List of two unique numbers in sorted order

    Time: O(n), Space: O(1)
    """
    # Phase 1: Get XOR of both uniques
    bit_count = [0] * 32

    for num in arr:
        for i in range(32):
            if num & (1 << i):
                bit_count[i] += 1

    xor_both = 0
    for i in range(32):
        if bit_count[i] % 3 == 1:
            xor_both |= (1 << i)

    # Phase 2: Find differentiating bit
    masked_diff = xor_both & M
    diff_bit = masked_diff & -masked_diff

    # Phase 3: Partition and find both
    bit_count_0 = [0] * 32
    bit_count_1 = [0] * 32

    for num in arr:
        for i in range(32):
            if num & (1 << i):
                if num & diff_bit:
                    bit_count_1[i] += 1
                else:
                    bit_count_0[i] += 1

    unique1, unique2 = 0, 0
    for i in range(32):
        if bit_count_0[i] % 3 == 1:
            unique1 |= (1 << i)
        if bit_count_1[i] % 3 == 1:
            unique2 |= (1 << i)

    return sorted([unique1, unique2])


# Time: O(n), Space: O(1)
```

### Java

```java
class Solution {
    public int[] findTwoUniques(int[] arr, int M) {
        // Phase 1: Get XOR of both uniques
        int[] bitCount = new int[32];

        for (int num : arr) {
            for (int i = 0; i < 32; i++) {
                if ((num & (1 << i)) != 0) {
                    bitCount[i]++;
                }
            }
        }

        int xorBoth = 0;
        for (int i = 0; i < 32; i++) {
            if (bitCount[i] % 3 == 1) {
                xorBoth |= (1 << i);
            }
        }

        // Phase 2: Find differentiating bit
        int maskedDiff = xorBoth & M;
        int diffBit = maskedDiff & -maskedDiff;

        // Phase 3: Partition and find both
        int[] bitCount0 = new int[32];
        int[] bitCount1 = new int[32];

        for (int num : arr) {
            for (int i = 0; i < 32; i++) {
                if ((num & (1 << i)) != 0) {
                    if ((num & diffBit) != 0) {
                        bitCount1[i]++;
                    } else {
                        bitCount0[i]++;
                    }
                }
            }
        }

        int unique1 = 0, unique2 = 0;
        for (int i = 0; i < 32; i++) {
            if (bitCount0[i] % 3 == 1) {
                unique1 |= (1 << i);
            }
            if (bitCount1[i] % 3 == 1) {
                unique2 |= (1 << i);
            }
        }

        int[] result = {Math.min(unique1, unique2), Math.max(unique1, unique2)};
        return result;
    }
}

// Time: O(n), Space: O(1)
```

### C++++

```cpp
class Solution {
public:
    vector<int> findTwoUniques(vector<int>& arr, int M) {
        // Phase 1: Get XOR of both uniques
        vector<int> bitCount(32, 0);

        for (int num : arr) {
            for (int i = 0; i < 32; i++) {
                if (num & (1 << i)) {
                    bitCount[i]++;
                }
            }
        }

        int xorBoth = 0;
        for (int i = 0; i < 32; i++) {
            if (bitCount[i] % 3 == 1) {
                xorBoth |= (1 << i);
            }
        }

        // Phase 2: Find differentiating bit
        int maskedDiff = xorBoth & M;
        int diffBit = maskedDiff & -maskedDiff;

        // Phase 3: Partition and find both
        vector<int> bitCount0(32, 0);
        vector<int> bitCount1(32, 0);

        for (int num : arr) {
            for (int i = 0; i < 32; i++) {
                if (num & (1 << i)) {
                    if (num & diffBit) {
                        bitCount1[i]++;
                    } else {
                        bitCount0[i]++;
                    }
                }
            }
        }

        int unique1 = 0, unique2 = 0;
        for (int i = 0; i < 32; i++) {
            if (bitCount0[i] % 3 == 1) {
                unique1 |= (1 << i);
            }
            if (bitCount1[i] % 3 == 1) {
                unique2 |= (1 << i);
            }
        }

        return {min(unique1, unique2), max(unique1, unique2)};
    }
};

// Time: O(n), Space: O(1)
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} M
 * @return {number[]}
 */
var findTwoUniques = function(arr, M) {
    // Phase 1: Get XOR of both uniques
    const bitCount = new Array(32).fill(0);

    for (const num of arr) {
        for (let i = 0; i < 32; i++) {
            if (num & (1 << i)) {
                bitCount[i]++;
            }
        }
    }

    let xorBoth = 0;
    for (let i = 0; i < 32; i++) {
        if (bitCount[i] % 3 === 1) {
            xorBoth |= (1 << i);
        }
    }

    // Phase 2: Find differentiating bit
    const maskedDiff = xorBoth & M;
    const diffBit = maskedDiff & -maskedDiff;

    // Phase 3: Partition and find both
    const bitCount0 = new Array(32).fill(0);
    const bitCount1 = new Array(32).fill(0);

    for (const num of arr) {
        for (let i = 0; i < 32; i++) {
            if (num & (1 << i)) {
                if (num & diffBit) {
                    bitCount1[i]++;
                } else {
                    bitCount0[i]++;
                }
            }
        }
    }

    let unique1 = 0, unique2 = 0;
    for (let i = 0; i < 32; i++) {
        if (bitCount0[i] % 3 === 1) {
            unique1 |= (1 << i);
        }
        if (bitCount1[i] % 3 === 1) {
            unique2 |= (1 << i);
        }
    }

    return [Math.min(unique1, unique2), Math.max(unique1, unique2)];
};

// Time: O(n), Space: O(1)
```

### 📊 Complexity Comparison

| **Approach** | **Time** | **Space** | **Passes** |
| ------------ | -------- | --------- | ---------- |
| **Naive**    | O(n)     | O(n)      | 2          |
| **Optimal**  | O(n)     | O(1)      | 2          |

### 💡 Key Insights Summary

```
┌─────────────────────────────────────────────────────────┐
│  Core Concepts                                          │
├─────────────────────────────────────────────────────────┤
│  1. Triples cancel with MOD 3, not XOR                 │
│  2. Remainder 1 means bit contributes to XOR           │
│  3. Mask M guarantees differentiating bit exists       │
│  4. Partition by diff_bit isolates each unique        │
│  5. O(1) space using fixed-size bit arrays            │
└─────────────────────────────────────────────────────────┘
```

---

**Remember**: When XOR fails (non-powers-of-2 repetition), think modular arithmetic! 🚀
