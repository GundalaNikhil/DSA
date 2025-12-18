# Editorial: Count Set Bits Of Indexed XOR

## Problem ID

- **Display ID**: BIT-007
- **Internal ID**: BIT_COUNT_SET_BITS_INDEXED_XOR\_\_8407
- **Slug**: count-set-bits-indexed-xor
- **Difficulty**: Medium
- **Category**: Bitwise Operations, Mathematics, Bit Counting

---

## Real-World Scenario: Error Detection in Distributed Storage

Imagine you're designing a distributed storage system where data blocks are indexed and stored across multiple servers. To detect corruption or inconsistencies:

1. **Block Indexing**: Each block has an index `i`
2. **Data Value**: Block contains value `arr[i]`
3. **Checksum Calculation**: For validation, compute `i ⊕ arr[i]`
4. **Error Metric**: Count the number of set bits in all checksums

**Application**: This helps identify potential corruption patterns - a high total count might indicate systematic issues. The XOR of index with value creates a fingerprint sensitive to both position and content errors.

**ASCII Visualization: Storage Block Checksums**

```
Array: [3, 6, 2, 8]
Index:  0  1  2  3

Block 0: index=0 (00), value=3 (011)
         0⊕3 = 011 → 2 set bits

Block 1: index=1 (01), value=6 (110)
         1⊕6 = 111 → 3 set bits

Block 2: index=2 (10), value=2 (010)
         2⊕2 = 000 → 0 set bits

Block 3: index=3 (11), value=8 (1000)
         3⊕8 = 1011 → 3 set bits

Total set bits: 2 + 3 + 0 + 3 = 8
```

---

## Understanding the Problem

### Key Concepts

1. **Index XOR Value**: For each position `i`, compute `i ⊕ arr[i]`
2. **Set Bits (Popcount)**: Count the number of 1s in binary representation
3. **Total Sum**: Sum the set bit counts across all indices

### Straightforward Approach

```
total = 0
for i from 0 to n-1:
    xor_value = i ^ arr[i]
    total += count_set_bits(xor_value)
return total
```

**ASCII: Step-by-Step Calculation**

```
Array: [5, 3, 8, 1]

i=0: 0⊕5 = 0⊕101 = 101 → popcount = 2
i=1: 1⊕3 = 001⊕011 = 010 → popcount = 1
i=2: 2⊕8 = 010⊕1000 = 1010 → popcount = 2
i=3: 3⊕1 = 011⊕001 = 010 → popcount = 1

Total: 2+1+2+1 = 6
```

---

## Approach 1: Naive Iteration with Bit Counting

### Algorithm

For each index, compute XOR and count bits naively.

```python
def count_set_bits_naive(xor_val):
    count = 0
    while xor_val:
        count += xor_val & 1
        xor_val >>= 1
    return count

total = 0
for i in range(n):
    xor_val = i ^ arr[i]
    total += count_set_bits_naive(xor_val)
```

### Complexity

- **Time**: O(n × log(max_value))
  - n iterations, each counting bits in O(log V) time
- **Space**: O(1)

---

## Approach 2: Using Built-in Popcount (Optimal)

### Key Insight

Modern CPUs have hardware instructions for counting set bits. Most languages provide built-in functions:

- **Java**: `Integer.bitCount()`
- **Python**: `bin().count('1')`
- **C++**: `__builtin_popcount()`
- **JavaScript**: Manual implementation

### Algorithm

```python
total = 0
for i in range(n):
    xor_val = i ^ arr[i]
    total += popcount(xor_val)
return total
```

### Complexity

- **Time**: O(n) - popcount is O(1) per call
- **Space**: O(1)

---

## Approach 3: Brian Kernighan's Algorithm

### Key Insight

Instead of checking all bits, only iterate through set bits using `x & (x-1)`.

```python
def count_set_bits_kernighan(xor_val):
    count = 0
    while xor_val:
        xor_val &= (xor_val - 1)  # Clear rightmost set bit
        count += 1
    return count

total = 0
for i in range(n):
    xor_val = i ^ arr[i]
    total += count_set_bits_kernighan(xor_val)
```

**ASCII: Brian Kernighan's Magic**

```
xor_val = 13 (1101)

Step 1: 1101 & (1101-1) = 1101 & 1100 = 1100
        (cleared rightmost 1)
        count = 1

Step 2: 1100 & (1100-1) = 1100 & 1011 = 1000
        count = 2

Step 3: 1000 & (1000-1) = 1000 & 0111 = 0000
        count = 3

Total: 3 set bits (loops = set bits count)
```

### Complexity

- **Time**: O(n × k) where k = average set bits per XOR
- **Space**: O(1)
- **Advantage**: Faster when XOR values have few set bits

---

## Complete Implementation

### Java Solution

```java
public class Solution {
    /**
     * Count total set bits in all (index XOR value) pairs
     *
     * @param arr Array of integers
     * @return Total count of set bits
     */
    public static int countSetBitsIndexedXor(int[] arr) {
        int n = arr.length;
        int total = 0;

        for (int i = 0; i < n; i++) {
            int xorValue = i ^ arr[i];
            total += Integer.bitCount(xorValue);
        }

        return total;
    }

    // Alternative: Brian Kernighan's algorithm
    public static int countSetBitsKernighan(int[] arr) {
        int n = arr.length;
        int total = 0;

        for (int i = 0; i < n; i++) {
            int xorValue = i ^ arr[i];

            // Count set bits using Kernighan's algorithm
            while (xorValue > 0) {
                xorValue &= (xorValue - 1);
                total++;
            }
        }

        return total;
    }

    public static void main(String[] args) {
        int[] arr1 = {3, 6, 2, 8};
        System.out.println(countSetBitsIndexedXor(arr1)); // Expected: 8

        int[] arr2 = {5, 3, 8, 1};
        System.out.println(countSetBitsIndexedXor(arr2)); // Expected: 6

        int[] arr3 = {0, 0, 0, 0};
        System.out.println(countSetBitsIndexedXor(arr3)); // Expected: 4
    }
}
```

### Python Solution

```python
def count_set_bits_indexed_xor(arr: list[int]) -> int:
    """
    Count total set bits in all (index XOR value) pairs.

    For each index i, compute i ⊕ arr[i] and count set bits.
    Sum all counts.

    Args:
        arr: List of integers

    Returns:
        Total count of set bits across all XOR operations
    """
    total = 0

    for i, value in enumerate(arr):
        xor_value = i ^ value
        total += bin(xor_value).count('1')

    return total


def count_set_bits_kernighan(arr: list[int]) -> int:
    """Alternative using Brian Kernighan's algorithm."""
    total = 0

    for i, value in enumerate(arr):
        xor_value = i ^ value

        # Count set bits using Kernighan's algorithm
        while xor_value:
            xor_value &= (xor_value - 1)
            total += 1

    return total


# Test cases
if __name__ == "__main__":
    print(count_set_bits_indexed_xor([3, 6, 2, 8]))  # Expected: 8
    print(count_set_bits_indexed_xor([5, 3, 8, 1]))  # Expected: 6
    print(count_set_bits_indexed_xor([0, 0, 0, 0]))  # Expected: 4
```

### C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    /**
     * Count total set bits in all (index XOR value) pairs
     */
    static int countSetBitsIndexedXor(const vector<int>& arr) {
        int n = arr.size();
        int total = 0;

        for (int i = 0; i < n; i++) {
            int xorValue = i ^ arr[i];
            total += __builtin_popcount(xorValue);
        }

        return total;
    }

    // Alternative: Brian Kernighan's algorithm
    static int countSetBitsKernighan(const vector<int>& arr) {
        int n = arr.size();
        int total = 0;

        for (int i = 0; i < n; i++) {
            int xorValue = i ^ arr[i];

            while (xorValue) {
                xorValue &= (xorValue - 1);
                total++;
            }
        }

        return total;
    }
};

int main() {
    vector<int> arr1 = {3, 6, 2, 8};
    cout << Solution::countSetBitsIndexedXor(arr1) << endl; // Expected: 8

    vector<int> arr2 = {5, 3, 8, 1};
    cout << Solution::countSetBitsIndexedXor(arr2) << endl; // Expected: 6

    vector<int> arr3 = {0, 0, 0, 0};
    cout << Solution::countSetBitsIndexedXor(arr3) << endl; // Expected: 4

    return 0;
}
```

### JavaScript Solution

```javascript
/**
 * Count set bits in a number
 */
function popcount(n) {
  let count = 0;
  while (n) {
    n &= n - 1; // Clear rightmost set bit
    count++;
  }
  return count;
}

/**
 * Count total set bits in all (index XOR value) pairs
 *
 * @param {number[]} arr - Array of integers
 * @return {number} Total count of set bits
 */
function countSetBitsIndexedXor(arr) {
  let total = 0;

  for (let i = 0; i < arr.length; i++) {
    const xorValue = i ^ arr[i];
    total += popcount(xorValue);
  }

  return total;
}

// Alternative: String conversion method
function countSetBitsAlt(arr) {
  let total = 0;

  for (let i = 0; i < arr.length; i++) {
    const xorValue = i ^ arr[i];
    total += (xorValue.toString(2).match(/1/g) || []).length;
  }

  return total;
}

// Test cases
console.log(countSetBitsIndexedXor([3, 6, 2, 8])); // Expected: 8
console.log(countSetBitsIndexedXor([5, 3, 8, 1])); // Expected: 6
console.log(countSetBitsIndexedXor([0, 0, 0, 0])); // Expected: 4
```

---

## Edge Cases and Special Scenarios

### Edge Case 1: Single Element

```
Input: arr = [5]
Output: 2

Explanation: 0⊕5 = 5 (101) → 2 set bits
```

### Edge Case 2: All Zeros

```
Input: arr = [0, 0, 0, 0]
Output: 4

Explanation:
0⊕0 = 0 (00) → 0 bits
1⊕0 = 1 (01) → 1 bit
2⊕0 = 2 (10) → 1 bit
3⊕0 = 3 (11) → 2 bits
Total: 0+1+1+2 = 4
```

### Edge Case 3: Identity (arr[i] = i)

```
Input: arr = [0, 1, 2, 3]
Output: 0

Explanation: i⊕i = 0 for all i → 0 set bits
```

### Edge Case 4: Powers of 2

```
Input: arr = [1, 2, 4, 8]
Output: 7

Explanation:
0⊕1 = 1 (001) → 1
1⊕2 = 3 (011) → 2
2⊕4 = 6 (110) → 2
3⊕8 = 11 (1011) → 3
Total: 1+2+2+3 = 8
Wait, let me recalculate: 1+2+2+3 = 8, not 7
Actually: 8
```

### Edge Case 5: Large Values

```
Input: arr = [1000000, 999999, 1000000, 999999]
Output: varies

Each XOR might have many set bits
```

---

## Common Mistakes and How to Avoid Them

### Mistake 1: Forgetting Index Starts at 0

```python
# WRONG: Starting index from 1
for i in range(1, n+1):
    xor_val = i ^ arr[i-1]  # Confusing!

# CORRECT: Use 0-based indexing naturally
for i in range(n):
    xor_val = i ^ arr[i]
```

### Mistake 2: Incorrect Bit Counting

```java
// WRONG: Counting digits instead of bits
String binary = Integer.toBinaryString(xorValue);
total += binary.length();  // This is wrong!

// CORRECT: Count '1' characters
total += binary.replace("0", "").length();
// OR use built-in
total += Integer.bitCount(xorValue);
```

### Mistake 3: Integer Overflow

```cpp
// WRONG: Using int for large arrays
int total = 0;  // Might overflow for n=100000

// CORRECT: Use long long
long long total = 0;
```

### Mistake 4: Off-by-One in Loop

```python
# WRONG: Missing last element
for i in range(n-1):
    xor_val = i ^ arr[i]

# CORRECT: Include all elements
for i in range(n):
    xor_val = i ^ arr[i]
```

### Mistake 5: Not Handling Empty Array

```javascript
// WRONG: No check for empty array
function countSetBits(arr) {
  let total = 0;
  for (let i = 0; i < arr.length; i++) {
    // ...
  }
  return total;
}

// CORRECT: Handle edge case
function countSetBits(arr) {
  if (!arr || arr.length === 0) return 0;
  // ... rest of code
}
```

---

## Interview Extensions

### Extension 1: Find Maximum Individual Count

**Question**: Which index has the maximum set bits in its XOR?

**Answer**:

```python
max_count = 0
max_index = -1

for i in range(n):
    xor_val = i ^ arr[i]
    count = bin(xor_val).count('1')
    if count > max_count:
        max_count = count
        max_index = i

return max_index, max_count
```

### Extension 2: Count Positions with Even Set Bits

**Question**: How many indices have an even number of set bits in their XOR?

**Answer**:

```python
even_count = 0
for i in range(n):
    xor_val = i ^ arr[i]
    if bin(xor_val).count('1') % 2 == 0:
        even_count += 1
return even_count
```

### Extension 3: Cumulative Count Array

**Question**: Return array where result[i] = total set bits for indices 0 to i.

**Answer**:

```python
cumulative = []
total = 0
for i in range(n):
    xor_val = i ^ arr[i]
    total += bin(xor_val).count('1')
    cumulative.append(total)
return cumulative
```

### Extension 4: Bit Position Frequency

**Question**: Count how many times each bit position appears as 1 across all XORs.

**Answer**:

```python
bit_freq = [0] * 32  # Assuming 32-bit integers
for i in range(n):
    xor_val = i ^ arr[i]
    for bit_pos in range(32):
        if (xor_val >> bit_pos) & 1:
            bit_freq[bit_pos] += 1
return bit_freq
```

### Extension 5: Modify to Use Different Operation

**Question**: What if we use AND instead of XOR?

**Answer**: Same structure, replace `^` with `&`:

```python
total = 0
for i in range(n):
    and_val = i & arr[i]
    total += bin(and_val).count('1')
return total
```

---

## Optimization: Bit-Level Analysis

### Advanced Insight

For very large arrays, we can analyze bit positions independently:

**For bit position b**:

- Count how many indices have bit b set
- Count how many values have bit b set
- XOR property: bit b is set in result when exactly one of (index, value) has it set

```python
def count_set_bits_optimized(arr):
    n = len(arr)
    total = 0
    max_bits = 20  # log2(max_value)

    for bit in range(max_bits):
        indices_with_bit = 0
        values_with_bit = 0

        for i in range(n):
            if (i >> bit) & 1:
                indices_with_bit += 1
            if (arr[i] >> bit) & 1:
                values_with_bit += 1

        # XOR: set when exactly one has the bit
        # Count pairs where index has bit XOR value has bit
        set_in_xor = (indices_with_bit * (n - values_with_bit) +
                      (n - indices_with_bit) * values_with_bit)
        total += set_in_xor

    return total
```

**Complexity**: Still O(n × B) but more cache-friendly for large n.

---

## Practice Problems

1. **LeetCode 461**: Hamming Distance (related concept)
2. **LeetCode 477**: Total Hamming Distance
3. **LeetCode 1863**: Sum of All Subset XOR Totals
4. **LeetCode 338**: Counting Bits
5. **Codeforces 165E**: Compatible Numbers

---

## Summary Table

| Approach           | Time       | Space | Best For           |
| ------------------ | ---------- | ----- | ------------------ |
| Naive Bit Loop     | O(n log V) | O(1)  | Learning           |
| Built-in Popcount  | O(n)       | O(1)  | Production         |
| Brian Kernighan    | O(n × k)   | O(1)  | Sparse bits        |
| Bit-Level Analysis | O(n × B)   | O(1)  | Cache optimization |

**Recommended Solution**: Use built-in popcount function for simplicity and performance.

---

## Key Takeaways

1. **Index XOR Value**: Natural checksum combining position and content
2. **Popcount**: Efficient bit counting is crucial (use built-ins)
3. **XOR Properties**: Commutative, associative, self-inverse
4. **Brian Kernighan**: Efficient for sparse set bits
5. **Hardware Support**: Modern CPUs have popcount instructions
6. **Linear Time**: O(n) with built-in functions
7. **Simple Problem**: No complex algorithms needed, just iterate and count!
