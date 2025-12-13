## Problem 5: Weighted Balance Point (ARR-005)

**🏷️ Topic Tags**: `Array`, `Prefix Sum`, `Balance Point`, `Mathematical`

### 📋 Problem Summary

Find an index where the weighted sum of elements on the left equals the weighted sum on the right, where weights are distances from the balance point.

### 🌍 Real-World Scenario

**Seesaw/Lever Balance Problem**

Imagine a seesaw with children of different weights sitting at different positions:

- Each child's torque = weight × distance from pivot
- Seesaw balances when: left torque = right torque
- Need to find the pivot position

Example:

```
Children: [1, 2, 3, 4]
Index 2 as pivot:
Left: 1×2 + 2×1 = 4
Right: 4×1 = 4
Balanced! ✓
```

**Applications**:

- Physics: Finding center of mass
- Economics: Weighted equilibrium point
- Engineering: Load distribution analysis

### 📚 Detailed Explanation

**What is Weighted Balance?**
For index `i`:

- Left weighted sum: `arr[0]×(i-0) + arr[1]×(i-1) + ... + arr[i-1]×1`
- Right weighted sum: `arr[i+1]×1 + arr[i+2]×2 + ... + arr[n-1]×(n-1-i)`

**Key Insight**:
Instead of recalculating from scratch for each position, maintain running sums and update incrementally!

### ❌ Naive Approach

**Algorithm**:

```
For each index i:
  Calculate left weighted sum
  Calculate right weighted sum
  If equal, return i
Return -1
```

**⏱️ Time Complexity: O(n²)**

```
For n positions:
  Each position: O(n) to calculate weighted sums
Total: n × n = O(n²)
```

**Impact**:

- n = 100: 10,000 operations
- n = 10,000: 100,000,000 operations (slow!)
- n = 100,000: 10,000,000,000 operations (timeout!)

**📦 Space Complexity: O(1)**

- Only storing sums and counters

### ✅ Optimal Approach

**Algorithm**:

1. Precompute total weighted sum
2. Use sliding window technique:
   - Maintain leftWeightedSum as we scan
   - Calculate rightWeightedSum = total - leftWeightedSum - contributions
3. Check balance at each position

**Mathematical Trick**:

```
When moving from index i to i+1:
- All left elements' distances increase by 1
- All right elements' distances decrease by 1
- Update sums incrementally!
```

**⏱️ Time Complexity: O(n)**

```
Single pass through array: O(n)
Constant work per element: O(1)
Total: O(n)
```

**Speedup Factor**:

- From O(n²) to O(n) = **n times faster**
- n = 10,000: 100M → 10K operations (10,000× speedup!)

**📦 Space Complexity: O(1)**

- Only storing running sums

### 🎨 Visual Representation

**Example**: `arr = [1, 2, 3, 4]`

```
Index 0 (Check if balance):
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
└───┴───┴───┴───┘
  ↑
pivot

Left:  (none) = 0
Right: 2×1 + 3×2 + 4×3 = 2+6+12 = 20
0 ≠ 20 ✗

Index 1:
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
└───┴───┴───┴───┘
      ↑
   pivot

Left:  1×1 = 1
Right: 3×1 + 4×2 = 3+8 = 11
1 ≠ 11 ✗

Index 2:
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
└───┴───┴───┴───┘
          ↑
       pivot

Left:  1×2 + 2×1 = 2+2 = 4
Right: 4×1 = 4
4 = 4 ✓ FOUND!
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [1, 2, 3, 4]`

| Step | Index | Left Sum Calculation | Right Sum Calculation | Balance? |
| ---- | ----- | -------------------- | --------------------- | -------- |
| 1    | 0     | 0 (no left elements) | 2×1+3×2+4×3 = 20      | ✗        |
| 2    | 1     | 1×1 = 1              | 3×1+4×2 = 11          | ✗        |
| 3    | 2     | 1×2+2×1 = 4          | 4×1 = 4               | ✅       |

**Output**: `2`

### ⚠️ Common Mistakes

#### 1. **Wrong Distance Calculation**

```java
// ❌ WRONG
leftSum += arr[j];  // Forgot to multiply by distance!

// ✅ CORRECT
leftSum += arr[j] * (i - j);
```

#### 2. **Off-by-One in Weights**

```java
// ❌ WRONG
rightSum += arr[j] * j;  // Wrong reference point

// ✅ CORRECT
rightSum += arr[j] * (j - i);  // Distance from pivot i
```

#### 3. **Integer Overflow**

```java
// ❌ WRONG (int might overflow)
int leftSum = 0;

// ✅ CORRECT (use long for large sums)
long leftSum = 0;
```

#### 4. **Not Checking All Indices**

```java
// ❌ WRONG
for (int i = 1; i < n-1; i++)  // Misses first/last

// ✅ CORRECT
for (int i = 0; i < n; i++)  // Check all positions
```

#### 5. **Recalculating from Scratch**

```java
// ❌ WRONG (O(n²) - naive)
for (int i = 0; i < n; i++) {
    leftSum = 0;
    for (int j = 0; j < i; j++)
        leftSum += arr[j] * (i-j);
}

// ✅ CORRECT (O(n) - optimal)
// Update leftSum incrementally based on previous value
```

### 🔑 Key Algorithm Points

1. **Prefix sum approach**: Build cumulative sums
2. **Incremental updates**: Don't recalculate from scratch
3. **Mathematical optimization**: Use algebra to simplify
4. **Balance equation**: leftWeighted = rightWeighted

### 💻 Implementations

#### Java

```java
class Solution {
    public int findWeightedBalancePoint(int[] arr) {
        int n = arr.length;
        if (n == 0) return -1;
        if (n == 1) return 0;

        // Calculate initial right weighted sum (from perspective of index 0)
        long rightWeightedSum = 0;
        for (int i = 1; i < n; i++) {
            rightWeightedSum += (long) arr[i] * i;
        }

        long leftWeightedSum = 0;
        long leftSum = 0;  // Sum of all elements to the left

        for (int i = 0; i < n; i++) {
            if (leftWeightedSum == rightWeightedSum) {
                return i;
            }

            // Update for next iteration
            leftSum += arr[i];
            leftWeightedSum += leftSum;  // All left elements' distances increase by 1

            if (i + 1 < n) {
                rightWeightedSum -= (long) arr[i + 1] * (i + 1);
            }
        }

        return -1;
    }
}

// Time: O(n), Space: O(1)
```

#### Python

```python
def find_weighted_balance_point(arr):
    """
    Find index where weighted sum of left equals weighted sum of right.

    Args:
        arr: List of integers

    Returns:
        Index of balance point, or -1 if none exists
    """
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0

    # Calculate initial right weighted sum
    right_weighted_sum = sum(arr[i] * i for i in range(1, n))

    left_weighted_sum = 0
    left_sum = 0

    for i in range(n):
        if left_weighted_sum == right_weighted_sum:
            return i

        # Update for next iteration
        left_sum += arr[i]
        left_weighted_sum += left_sum

        if i + 1 < n:
            right_weighted_sum -= arr[i + 1] * (i + 1)

    return -1

# Time: O(n), Space: O(1)
```

#### C++

```cpp
class Solution {
public:
    int findWeightedBalancePoint(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return -1;
        if (n == 1) return 0;

        // Calculate initial right weighted sum
        long long rightWeightedSum = 0;
        for (int i = 1; i < n; i++) {
            rightWeightedSum += (long long) arr[i] * i;
        }

        long long leftWeightedSum = 0;
        long long leftSum = 0;

        for (int i = 0; i < n; i++) {
            if (leftWeightedSum == rightWeightedSum) {
                return i;
            }

            // Update for next iteration
            leftSum += arr[i];
            leftWeightedSum += leftSum;

            if (i + 1 < n) {
                rightWeightedSum -= (long long) arr[i + 1] * (i + 1);
            }
        }

        return -1;
    }
};

// Time: O(n), Space: O(1)
```

### 📊 Comparison Table

| **Aspect**           | **Naive (Recalculate)**        | **Optimal (Incremental)**   |
| -------------------- | ------------------------------ | --------------------------- |
| **Algorithm**        | Check each index independently | Sliding window with updates |
| **Time Complexity**  | O(n²)                          | O(n) ⭐                     |
| **Space Complexity** | O(1)                           | O(1)                        |
| **For n=1000**       | ~1,000,000 ops                 | ~1,000 ops                  |
| **For n=100,000**    | ~10,000,000,000 ops            | ~100,000 ops                |
| **Speedup**          | Baseline                       | **n times faster** ⭐       |
| **Best for**         | Learning concept               | Production use ⭐           |

### 🎯 Quiz Questions

#### Q1: Balance Point Existence

For array `[1, 1, 1, 1]`, does a balance point exist?

- A) Yes, at index 1
- B) Yes, at index 2
- C) No balance point exists
- D) Multiple balance points exist

<details>
<summary>💡 Click for Answer</summary>

**Answer: C) No balance point exists**

**Explanation**:

```
Index 0:
Left: 0
Right: 1×1 + 1×2 + 1×3 = 6
0 ≠ 6 ✗

Index 1:
Left: 1×1 = 1
Right: 1×1 + 1×2 = 3
1 ≠ 3 ✗

Index 2:
Left: 1×2 + 1×1 = 3
Right: 1×1 = 1
3 ≠ 1 ✗

Index 3:
Left: 1×3 + 1×2 + 1×1 = 6
Right: 0
6 ≠ 0 ✗
```

For uniform arrays, balance is hard to achieve!

</details>

#### Q2: Edge Case - Single Element

For array `[5]`, what is the balance point?

- A) -1 (no balance point)
- B) 0
- C) 1
- D) Error

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) 0**

**Explanation**:

```
Index 0:
Left: 0 (no elements)
Right: 0 (no elements)
0 = 0 ✓
```

By definition, a single element is always balanced - nothing on either side!

</details>

#### Q3: Why Use `long` Instead of `int`?

Why do we use `long` for weighted sums?

- A) For better precision
- B) To prevent overflow
- C) For faster computation
- D) It's required by Java

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) To prevent overflow**

**Explanation**:
With large arrays and large values:

```
arr = [10000, 10000, ..., 10000]  // 100,000 elements

Weighted sum can be:
10000 × 1 + 10000 × 2 + ... + 10000 × 100000
= 10000 × (1 + 2 + ... + 100000)
= 10000 × 5,000,050,000
= 50,000,500,000,000

This exceeds int max (2,147,483,647)!
```

**Key**: Always use `long` for cumulative sums in large arrays!

</details>

#### Q4: Incremental Update Formula

When moving from index `i` to `i+1`, how does `leftWeightedSum` change?

- A) Add `arr[i]`
- B) Add `leftSum`
- C) Add `arr[i] * i`
- D) Recalculate from scratch

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) Add `leftSum`**

**Explanation**:
When we move right one position:

- All existing left elements' distances from new pivot increase by 1
- Previous left weighted sum + sum of all left elements = new left weighted sum

```
Example: arr = [1, 2, 3, 4], moving from i=1 to i=2

At i=1: leftWeightedSum = 1×1 = 1, leftSum = 1
At i=2: leftWeightedSum should be 1×2 + 2×1 = 4

Update: leftWeightedSum = 1 + (1 + 2) = 1 + 3 = 4 ✓
```

**Formula**: `leftWeightedSum += leftSum` (where leftSum includes newly added arr[i])

</details>

#### Q5: Complexity Comparison

For n=50,000, approximately how much faster is O(n) vs O(n²)?

- A) 2× faster
- B) 100× faster
- C) 50,000× faster
- D) Same speed

<details>
<summary>💡 Click for Answer</summary>

**Answer: C) 50,000× faster**

**Explanation**:

```
O(n²): 50,000² = 2,500,000,000 operations
O(n):  50,000 operations

Speedup = 2,500,000,000 / 50,000 = 50,000×
```

**Real Impact**:

- O(n²): ~2.5 billion operations → could take minutes
- O(n): ~50,000 operations → completes in milliseconds

This is why algorithmic optimization matters! ⭐

</details>

#### Q6: Multiple Balance Points

Can an array have multiple balance points?

- A) No, at most one
- B) Yes, but only adjacent indices
- C) Yes, any indices
- D) Only if all elements are equal

<details>
<summary>💡 Click for Answer</summary>

**Answer: C) Yes, any indices**

**Example**:

```
arr = [0, 0, 0, 0]

All indices are balance points!
Every position: left weighted sum = 0, right weighted sum = 0
```

However, the problem typically asks for the **first** balance point found.

</details>

#### Q7: Boundary Check

Why check `if (i + 1 < n)` before updating `rightWeightedSum`?

- A) To avoid array index out of bounds
- B) To handle the last element
- C) To skip empty arrays
- D) For optimization

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) To handle the last element**

**Explanation**:

```java
for (int i = 0; i < n; i++) {
    // ... check balance ...

    if (i + 1 < n) {
        rightWeightedSum -= arr[i + 1] * (i + 1);
    }
}
```

When `i = n-1` (last element):

- `i + 1 = n` → out of bounds!
- No need to update rightWeightedSum (no more iterations)
- Check prevents `ArrayIndexOutOfBoundsException`

**Always**: Validate array access before use! ✓

</details>

#### Q8: Optimization Trade-off

What do we trade for the O(n) time complexity improvement?

- A) Code simplicity
- B) Space complexity
- C) Accuracy
- D) Nothing - pure win!

<details>
<summary>💡 Click for Answer</summary>

**Answer: A) Code simplicity**

**Explanation**:

- **Naive approach**: Simple nested loops, easy to understand
- **Optimal approach**: Requires understanding incremental updates, more complex logic

**But**: The trade-off is worth it!

- Naive: Simple but too slow for large inputs
- Optimal: Slightly complex but production-ready

**Lesson**: Sometimes we sacrifice simplicity for performance when needed! ⚖️

</details>

---
