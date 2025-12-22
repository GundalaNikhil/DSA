---
problem_id: BIT_XOR_ODD_OCCURRENCE__8401
display_id: BIT-001
slug: odd-after-bit-salt
title: "Odd After Bit Salt"
difficulty: Easy
difficulty_score: 30
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Mathematics
tags:
  - bitwise
  - xor
  - array
  - mathematics
  - easy
premium: true
subscription_tier: basic
---

# Odd After Bit Salt

![Problem Header](../images/BIT-001/header.png)

### 📋 Problem Summary

Given an array where each element is XORed with a `salt` value, find the transformed value that appears an odd number of times **without explicitly creating the transformed array**.

![Problem Concept](../images/BIT-001/problem-illustration.png)

### 🌍 Real-World Scenario

**Campus Network Security System**

Imagine you're a cybersecurity engineer at a university. Students' ID numbers are encrypted using XOR with a secret `salt` before being stored in the access log:

- Original IDs: `[4, 1, 2, 1, 2, 4, 7]`
- Salt: `3`
- Encrypted: `[4⊕3=7, 1⊕3=2, 2⊕3=1, 1⊕3=2, 2⊕3=1, 4⊕3=7, 7⊕3=4]`
- Encrypted log: `[7, 2, 1, 2, 1, 7, 4]`

Your security system detects that exactly ONE encrypted ID appears an **odd number of times** (possible breach - someone swiped in but never out!). You need to identify this encrypted ID to investigate.

The catch? The encrypted log is HUGE (200,000 entries). You can't decrypt each entry—it would take too long. Can you find the odd occurrence directly?

**This is what this problem solves!** It helps identify anomalies in encrypted data efficiently.

### 📚 Detailed Explanation

**What is XOR (⊕)?**

XOR (exclusive OR) is a bitwise operation:

```
0 ⊕ 0 = 0    (same bits → 0)
0 ⊕ 1 = 1    (different bits → 1)
1 ⊕ 0 = 1    (different bits → 1)
1 ⊕ 1 = 0    (same bits → 0)
```

**Example**: `5 ⊕ 3`

```
5 = 101
3 = 011
------
    110 = 6
```

**Key XOR Properties** (CRUCIAL for this problem!):

1. **Self-Inverse**: `a ⊕ a = 0`

   - Any number XORed with itself = 0
   - Example: `5 ⊕ 5 = 0`

2. **Identity**: `a ⊕ 0 = a`

   - XORing with 0 doesn't change the number
   - Example: `7 ⊕ 0 = 7`

3. **Commutative**: `a ⊕ b = b ⊕ a`

   - Order doesn't matter
   - Example: `3 ⊕ 5 = 5 ⊕ 3`

4. **Associative**: `(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)`
   - Grouping doesn't matter
   - Example: `(2 ⊕ 3) ⊕ 4 = 2 ⊕ (3 ⊕ 4)`

**Why "Odd Occurrence"?**

When you XOR all elements:

- Elements appearing **even** times cancel out (due to `a ⊕ a = 0`)
- Only the element appearing **odd** times survives!

**Example**:

```
arr = [5, 3, 5, 3, 7]
5 ⊕ 3 ⊕ 5 ⊕ 3 ⊕ 7
= (5 ⊕ 5) ⊕ (3 ⊕ 3) ⊕ 7
= 0 ⊕ 0 ⊕ 7
= 7  ✓ (7 appears odd times!)
```

### ❌ Naive Approach

**Idea**: Transform array explicitly, then find odd occurrence using a hash map.

```
Step 1: Create transformed array
  For each element x:
    transformed[i] = x ⊕ salt

Step 2: Count frequencies
  Use hash map to count occurrences

Step 3: Find odd occurrence
  Check which value has odd count
```

**Code Pattern**:

```python
def naive_approach(arr, salt):
    # Step 1: Transform array
    transformed = []
    for x in arr:
        transformed.append(x ^ salt)

    # Step 2: Count frequencies
    freq = {}
    for val in transformed:
        freq[val] = freq.get(val, 0) + 1

    # Step 3: Find odd occurrence
    for val, count in freq.items():
        if count % 2 == 1:
            return val
```

**⏱️ Time Complexity: O(n)**

**Detailed Breakdown**:

- Step 1: Transform array → O(n) [one pass]
- Step 2: Build frequency map → O(n) [another pass]
- Step 3: Find odd count → O(k) where k = unique values
- Total: O(n) + O(n) + O(k) = **O(n)**

**📦 Space Complexity: O(n)**

**Why O(n)?**

- `transformed` array: O(n) space
- `freq` hash map: O(k) space where k ≤ n
- Total: **O(n)** extra space

**❌ Problems**:

1. **Memory waste**: Creates entire transformed array
2. **Cache inefficiency**: Two separate passes through data
3. **Hash map overhead**: Additional memory and lookup time
4. **Not elegant**: Doesn't leverage XOR properties!

### ✅ Optimal Approach

**💡 Key Insight**: Use the **mathematical property** of XOR!

**The Magic Formula**:

```
(a ⊕ salt) ⊕ (b ⊕ salt) = a ⊕ b ⊕ (salt ⊕ salt)
                         = a ⊕ b ⊕ 0
                         = a ⊕ b
```

**What does this mean?**

When you XOR all transformed values:

```
(arr[0]⊕salt) ⊕ (arr[1]⊕salt) ⊕ ... ⊕ (arr[n-1]⊕salt)
= arr[0] ⊕ arr[1] ⊕ ... ⊕ arr[n-1] ⊕ (salt⊕salt⊕...⊕salt)
                                           └─ n times ─┘
```

**If n is even**: `salt ⊕ salt ⊕ ... ⊕ salt` = 0 (pairs cancel)
**If n is odd**: `salt ⊕ salt ⊕ ... ⊕ salt` = salt (one left over)

**Final Formula**:

```
result = (arr[0] ⊕ arr[1] ⊕ ... ⊕ arr[n-1]) ⊕ (n is odd ? salt : 0)
```

**But wait—there's an even SIMPLER approach!**

Since elements appearing **even times** in transformed array cancel out:

```
(x⊕salt) ⊕ (x⊕salt) = 0
```

We can just:

1. XOR all original elements
2. XOR with salt (if n is odd)

**⏱️ Time Complexity: O(n)**

**Detailed Breakdown**:

- Single pass through array
- At each element: 1 XOR operation (O(1))
- Total: n × O(1) = **O(n)**

**Compared to Naive**: Same time complexity, but:

- Only ONE pass (better cache locality)
- No hash map operations (faster constant factors)
- In practice: **2-3× faster** than naive!

**📦 Space Complexity: O(1)**

**Why O(1)?**

- Only use ONE variable: `xor_result`
- No extra arrays or hash maps
- Memory usage independent of input size!

**Improvement**: O(n) space → O(1) space = **HUGE SAVINGS** for large arrays!

### 🎨 Visual Representation

**Example**: `arr = [4, 1, 2, 1, 2, 4, 7], salt = 3`

**Step 1: Understanding Transformation**

```
┌─────────────────────────────────────────────────────────┐
│  Original vs Transformed Array                          │
└─────────────────────────────────────────────────────────┘

Original:     [4,  1,  2,  1,  2,  4,  7]
               ↓   ↓   ↓   ↓   ↓   ↓   ↓  (each ⊕ 3)
Transformed:  [7,  2,  1,  2,  1,  7,  4]

Frequency Count in Transformed:
  7 appears 2 times (EVEN - will cancel)
  2 appears 2 times (EVEN - will cancel)
  1 appears 2 times (EVEN - will cancel)
  4 appears 1 time  (ODD - survives!) ✓
```

**Step 2: XOR All Original Elements**

```
XOR all originals:
4 ⊕ 1 ⊕ 2 ⊕ 1 ⊕ 2 ⊕ 4 ⊕ 7

Binary representation:
  100  (4)
⊕ 001  (1)
⊕ 010  (2)
⊕ 001  (1)
⊕ 010  (2)
⊕ 100  (4)
⊕ 111  (7)
-------
  111  (7)

Notice: 4⊕4=0, 1⊕1=0, 2⊕2=0 (pairs cancel!)
Result: 7
```

**Step 3: Handle Salt**

```
n = 7 (ODD), so XOR with salt:
result = 7 ⊕ 3

Binary:
  111  (7)
⊕ 011  (3)
-------
  100  (4)  ✓ ANSWER!
```

**Flow Diagram**:

```
Original Array: [4, 1, 2, 1, 2, 4, 7]
                 │
                 ↓ XOR all elements
                 │
              4⊕1⊕2⊕1⊕2⊕4⊕7 = 7
                 │
                 ↓ n=7 is ODD, so XOR with salt
                 │
                7 ⊕ 3 = 4
                 │
                 ↓
            ANSWER: 4 ✓
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [4, 1, 2, 1, 2, 4, 7], salt = 3`

**Detailed Step-by-Step**:

```
┌──────┬───────┬────────────┬──────────────────────┐
│ Step │ Value │ XOR Result │ Binary Explanation   │
├──────┼───────┼────────────┼──────────────────────┤
│  0   │   4   │     4      │ 100                  │
│  1   │   1   │   4⊕1=5    │ 100⊕001 = 101        │
│  2   │   2   │   5⊕2=7    │ 101⊕010 = 111        │
│  3   │   1   │   7⊕1=6    │ 111⊕001 = 110        │
│  4   │   2   │   6⊕2=4    │ 110⊕010 = 100        │
│  5   │   4   │   4⊕4=0    │ 100⊕100 = 000        │
│  6   │   7   │   0⊕7=7    │ 000⊕111 = 111        │
└──────┴───────┴────────────┴──────────────────────┘

After XORing all: result = 7
n = 7 (ODD), so: result = 7 ⊕ 3 = 4

Verification:
Transformed array: [7, 2, 1, 2, 1, 7, 4]
  - 7 appears 2 times (even)
  - 2 appears 2 times (even)
  - 1 appears 2 times (even)
  - 4 appears 1 time (ODD) ✓ CORRECT!
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Forgetting to Handle Salt** 🔴

**Problem**:

```java
int result = 0;
for (int x : arr) {
    result ^= x;
}
return result;  // ❌ Missing salt adjustment!
```

**Why Wrong?**

- We XORed original values, but need transformed values
- Must account for salt based on array length parity

**Solution**:

```java
int result = 0;
for (int x : arr) {
    result ^= x;
}
if (arr.length % 2 == 1) {  // ✅ Odd length
    result ^= salt;
}
return result;
```

#### 2. **Always XORing with Salt** 🔴

**Problem**:

```python
result = 0
for x in arr:
    result ^= x
result ^= salt  # ❌ Always XOR with salt
return result
```

**Why Wrong?**

- Only XOR with salt if array length is ODD
- If length is even, salts cancel out in pairs!

**Example**:

```
arr = [1, 2], salt = 3
Transformed = [1⊕3=2, 2⊕3=1]
XOR of transformed = 2 ⊕ 1 = 3

Using always-XOR approach:
(1 ⊕ 2) ⊕ 3 = 3 ⊕ 3 = 0  ❌ WRONG!

Correct approach (even length, skip salt):
1 ⊕ 2 = 3  ✓ CORRECT!
```

**Solution**:

```python
if len(arr) % 2 == 1:  # ✅ Only if odd length
    result ^= salt
```

#### 3. **Creating Transformed Array** 🔴

**Problem**:

```cpp
vector<int> transformed;
for (int x : arr) {
    transformed.push_back(x ^ salt);  // ❌ Wastes O(n) space!
}
// Then find odd occurrence in transformed...
```

**Why Wrong?**: Defeats the purpose of the optimal solution!

**Solution**: XOR directly without creating intermediate array

#### 4. **Incorrect Parity Check** 🔴

**Problem**:

```java
if (n % 2 == 0) {  // ❌ Backwards!
    result ^= salt;
}
```

**Why Wrong?**: XOR with salt only when length is **ODD**, not even!

**Mnemonic**: "**O**dd length needs **O**peration with salt"

#### 5. **Integer Overflow (Less Common Here)** 🔴

**Problem**: In languages with small int types (not Java/Python)

```c
int result = 0;  // If array values exceed int range
```

**Solution**: Use appropriate data type matching array element type

```c
long long result = 0;  // Match array type
```

### 🔑 Algorithm Steps

**Optimal O(n) Time, O(1) Space Algorithm**:

1. **Initialize**:

   ```
   xor_result = 0
   ```

2. **XOR all array elements**:

   ```
   For each element x in arr:
       xor_result = xor_result ⊕ x
   ```

3. **Adjust for salt** (if array length is odd):

   ```
   If len(arr) is odd:
       xor_result = xor_result ⊕ salt
   ```

4. **Return** xor_result

**Pseudocode**:

```
function oddAfterSalt(arr, salt):
    n = length of arr
    result = 0

    // XOR all elements
    for i from 0 to n-1:
        result = result XOR arr[i]

    // If odd length, XOR with salt
    if n % 2 == 1:
        result = result XOR salt

    return result
```

**Why It Works - Mathematical Proof**:

```
Let transformed array be T where T[i] = arr[i] ⊕ salt

XOR of all transformed elements:
T[0] ⊕ T[1] ⊕ ... ⊕ T[n-1]
= (arr[0]⊕salt) ⊕ (arr[1]⊕salt) ⊕ ... ⊕ (arr[n-1]⊕salt)

Rearrange (XOR is commutative & associative):
= (arr[0] ⊕ arr[1] ⊕ ... ⊕ arr[n-1]) ⊕ (salt ⊕ salt ⊕ ... ⊕ salt)
                                              └─── n times ────┘

If n is even: (salt ⊕ salt ⊕ ... ⊕ salt) = 0
If n is odd:  (salt ⊕ salt ⊕ ... ⊕ salt) = salt

Therefore:
result = (XOR of all arr) ⊕ (salt if n is odd, else 0)
```

### 💻 Implementations

### Java

```java
class Solution {
    /**
     * Find the transformed value appearing odd number of times.
     *
     * Time: O(n) - single pass through array
     * Space: O(1) - only one variable
     *
     * @param arr Array of integers
     * @param salt XOR salt value
     * @return Transformed value with odd occurrence
     */
    public int oddAfterSalt(int[] arr, int salt) {
        int result = 0;

        // XOR all array elements
        for (int x : arr) {
            result ^= x;
        }

        // If array length is odd, XOR with salt
        if (arr.length % 2 == 1) {
            result ^= salt;
        }

        return result;
    }
}

// Time: O(n), Space: O(1)
```

**Compact Version**:

```java
class Solution {
    public int oddAfterSalt(int[] arr, int salt) {
        int result = 0;
        for (int x : arr) result ^= x;
        return arr.length % 2 == 1 ? result ^ salt : result;
    }
}
```

### Python

```python
def odd_after_salt(arr, salt):
    """
    Find the transformed value appearing odd number of times.

    Each element x is transformed to x XOR salt. In the transformed
    array, exactly one value appears odd times. Find that value
    WITHOUT creating the transformed array.

    Args:
        arr: List of integers (original array)
        salt: Integer salt value for XOR transformation

    Returns:
        Integer - the transformed value with odd occurrence

    Time: O(n) - single pass
    Space: O(1) - constant extra space
    """
    result = 0

    # XOR all array elements
    for x in arr:
        result ^= x

    # If array length is odd, XOR with salt
    if len(arr) % 2 == 1:
        result ^= salt

    return result


# Alternative: Using functools.reduce
from functools import reduce
import operator

def odd_after_salt_functional(arr, salt):
    """Functional programming style using reduce."""
    xor_all = reduce(operator.xor, arr, 0)
    return xor_all ^ salt if len(arr) % 2 == 1 else xor_all


# Time: O(n), Space: O(1)
```

### C++++

```cpp
class Solution {
public:
    /**
     * Find the transformed value appearing odd number of times.
     *
     * @param arr Vector of integers
     * @param salt XOR salt value
     * @return Transformed value with odd occurrence
     */
    int oddAfterSalt(vector<int>& arr, int salt) {
        int result = 0;

        // XOR all array elements
        for (int x : arr) {
            result ^= x;
        }

        // If array length is odd, XOR with salt
        if (arr.size() % 2 == 1) {
            result ^= salt;
        }

        return result;
    }
};

// Time: O(n), Space: O(1)
```

**Using STL Accumulate**:

```cpp
#include <numeric>
#include <functional>

class Solution {
public:
    int oddAfterSalt(vector<int>& arr, int salt) {
        int result = accumulate(arr.begin(), arr.end(), 0, bit_xor<int>());
        return arr.size() % 2 == 1 ? result ^ salt : result;
    }
};
```

### JavaScript

```javascript
/**
 * Find the transformed value appearing odd number of times.
 *
 * @param {number[]} arr - Array of integers
 * @param {number} salt - XOR salt value
 * @return {number} - Transformed value with odd occurrence
 */
function oddAfterSalt(arr, salt) {
  let result = 0;

  // XOR all array elements
  for (let x of arr) {
    result ^= x;
  }

  // If array length is odd, XOR with salt
  if (arr.length % 2 === 1) {
    result ^= salt;
  }

  return result;
}

// Using reduce
function oddAfterSaltReduce(arr, salt) {
  const xorAll = arr.reduce((acc, x) => acc ^ x, 0);
  return arr.length % 2 === 1 ? xorAll ^ salt : xorAll;
}

// Time: O(n), Space: O(1)
```

### 📊 Complexity Comparison

| **Approach**    | **Time** | **Space** | **Passes** | **Cache Friendly** |
| --------------- | -------- | --------- | ---------- | ------------------ |
| **Naive**       | O(n)     | O(n)      | 2-3        | ❌ No              |
| **Hash Map**    | O(n)     | O(k)      | 2          | ❌ No              |
| **Optimal XOR** | O(n)     | O(1)      | 1          | ✅ Yes             |

### 💡 Key Insights Summary

```
┌─────────────────────────────────────────────────────────┐
│  Core Concepts                                          │
├─────────────────────────────────────────────────────────┤
│  1. XOR of duplicates = 0 (a ⊕ a = 0)                  │
│  2. XOR is commutative & associative                    │
│  3. Transform analysis: (x⊕s)⊕(y⊕s) = x⊕y⊕(s⊕s) = x⊕y  │
│  4. Parity matters: odd length → adjust with salt      │
│  5. No intermediate storage needed!                     │
└─────────────────────────────────────────────────────────┘
```

**The Beautiful One-Liner** (Python):

```python
def solve(arr, salt):
    return reduce(operator.xor, arr, 0) ^ (salt if len(arr) % 2 else 0)
```

---

**Remember**: In computer science, the most elegant solutions often come from deeply understanding mathematical properties rather than brute-forcing through the problem! 🚀
