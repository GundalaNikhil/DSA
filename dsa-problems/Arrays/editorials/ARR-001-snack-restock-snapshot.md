---
problem_id: ARR_PREFIX_AVG__4252
display_id: ARR-001
slug: snack-restock-snapshot
title: "Snack Restock Snapshot"
difficulty: Easy
difficulty_score: 25
topics:
  - Array
  - Prefix Sum
  - Mathematics
  - Running Sum
tags:
  - arrays
  - prefix-sum
  - mathematics
  - easy
premium: true
subscription_tier: basic
---

# Snack Restock Snapshot

![Problem Header](../images/ARR-001/header.png)

### 📋 Problem Summary

Given an array representing daily inventory values, compute the prefix average (rounded down) for each position.

![Problem Concept](../images/ARR-001/problem-illustration.png)

### 🌍 Real-World Scenario

**Campus Snack Shop Manager**

Imagine you manage a college snack shop. Every evening, you count the inventory:

- Day 1: 4 items
- Day 2: 6 items
- Day 3: 6 items
- Day 4: 0 items (forgot to restock!)

Your boss asks: "What's been the **average inventory** from opening day until each day?"

This is exactly what prefix averages solve! It helps identify trends:

- Is inventory improving or declining?
- Do we need to order more frequently?
- Are we maintaining sufficient stock?

### 📚 Detailed Explanation

**What is a Prefix Average?**

- At position `i`, it's the average of ALL elements from start (index 0) to current position (index i)
- Formula: `(arr[0] + arr[1] + ... + arr[i]) / (i + 1)`
- We use **floor division** (integer division): 7÷2 = 3, not 3.5

**Why "Prefix"?**
Because we're looking at the **prefix** (beginning portion) of the array up to each point.

### ❌ Naive Approach

**Idea**: For each day, recalculate the average from scratch.

```
For Day 0: Sum elements [0 to 0] → divide by 1
For Day 1: Sum elements [0 to 1] → divide by 2
For Day 2: Sum elements [0 to 2] → divide by 3
...
```

**Code Pattern**:

```python
for i in range(n):
    sum = 0
    for j in range(i+1):  # Recalculate sum every time!
        sum += arr[j]
    result[i] = sum // (i+1)
```

**⏱️ Time Complexity: O(n²)**

**Why O(n²)?** Let's count operations:

- Position 0: 1 addition (sum 1 element)
- Position 1: 2 additions (sum 2 elements)
- Position 2: 3 additions (sum 3 elements)
- ...
- Position n-1: n additions

Total = 1 + 2 + 3 + ... + n = **n(n+1)/2**

Using Big-O notation: Drop constants and lower terms → **O(n²)**

**Real Impact**:

- n = 100 → ~5,000 operations
- n = 1,000 → ~500,000 operations
- n = 10,000 → ~50,000,000 operations (SLOW!)

**📦 Space Complexity: O(1)** (excluding output)

- Only using a few variables regardless of input size

### ✅ Optimal Approach

**💡 Key Insight**: Don't recalculate from scratch! **Reuse previous work**.

Think of it like counting money:

- You counted $10 yesterday
- Today you earned $5 more
- Total = `10 +`5 = `15 (you don't recount the original`10!)

**Approach**: Maintain a **running sum**

```
Sum after Day 0 = arr[0]
Sum after Day 1 = (previous sum) + arr[1]
Sum after Day 2 = (previous sum) + arr[2]
...
```

**⏱️ Time Complexity: O(n)**

**Detailed Breakdown**:

- We visit each element exactly **once**
- At each element:
  - 1 addition operation (O(1))
  - 1 division operation (O(1))
- Total: n × O(1) = **O(n)**

**Improvement Factor**: O(n²) → O(n) means **n times faster**!

- For n=1,000: 500,000 ops → 1,000 ops (500× faster!)
- For n=10,000: 50,000,000 ops → 10,000 ops (5,000× faster!)

**📦 Space Complexity: O(1)** (excluding output)

**Why O(1)?**

- We only use ONE extra variable: `runningSum`
- Memory usage doesn't grow with input size
- Output array doesn't count (it's required output, not "extra" space)

### 🎨 Visual Representation

**Example**: `arr = [4, 6, 6, 0]`

```
┌─────────────────────────────────────────────────────────┐
│  Day-by-Day Calculation (Optimal Approach)             │
└─────────────────────────────────────────────────────────┘

Day 0:
┌───┐
│ 4 │  → Running Sum = 4, Count = 1
└───┘     Average = 4 ÷ 1 = 4 ✓

Day 1:
┌───┬───┐
│ 4 │ 6 │  → Running Sum = 4+6 = 10, Count = 2
└───┴───┘     Average = 10 ÷ 2 = 5 ✓

Day 2:
┌───┬───┬───┐
│ 4 │ 6 │ 6 │  → Running Sum = 10+6 = 16, Count = 3
└───┴───┴───┘     Average = 16 ÷ 3 = 5.33... → ⌊5⌋ = 5 ✓

Day 3:
┌───┬───┬───┬───┐
│ 4 │ 6 │ 6 │ 0 │  → Running Sum = 16+0 = 16, Count = 4
└───┴───┴───┴───┘     Average = 16 ÷ 4 = 4 ✓

Result: [4, 5, 5, 4]
```

**Flow Diagram**:

```
arr[0]=4  →  sum=4   →  avg=4/1=4   →  result[0]=4
              ↓
arr[1]=6  →  sum=10  →  avg=10/2=5  →  result[1]=5
              ↓
arr[2]=6  →  sum=16  →  avg=16/3=5  →  result[2]=5
              ↓
arr[3]=0  →  sum=16  →  avg=16/4=4  →  result[3]=4
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [1, 2, 3, 4, 5, 6]`

**Detailed Step-by-Step**:

```
┌──────┬───────┬────────────┬──────────┬─────────┐
│ Step │ Value │ Running    │ Count    │ Average │
│      │       │ Sum        │          │ (Floor) │
├──────┼───────┼────────────┼──────────┼─────────┤
│  0   │   1   │  0+1=1     │    1     │  1÷1=1  │
│  1   │   2   │  1+2=3     │    2     │  3÷2=1  │
│  2   │   3   │  3+3=6     │    3     │  6÷3=2  │
│  3   │   4   │  6+4=10    │    4     │ 10÷4=2  │
│  4   │   5   │ 10+5=15    │    5     │ 15÷5=3  │
│  5   │   6   │ 15+6=21    │    6     │ 21÷6=3  │
└──────┴───────┴────────────┴──────────┴─────────┘

Output: [1, 1, 2, 2, 3, 3]
```

**Trace Visualization**:

```
i=0: [1]             sum=1   avg=1  ✓
i=1: [1, 2]          sum=3   avg=1  ✓  (3÷2=1.5→1)
i=2: [1, 2, 3]       sum=6   avg=2  ✓
i=3: [1, 2, 3, 4]    sum=10  avg=2  ✓  (10÷4=2.5→2)
i=4: [1, 2, 3, 4, 5] sum=15  avg=3  ✓
i=5: [1,2,3,4,5,6]   sum=21  avg=3  ✓  (21÷6=3.5→3)
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Integer Overflow** 🔴

**Problem**:

```java
int sum = 0;  // ❌ DANGER!
for (int i = 0; i < n; i++) {
    sum += arr[i];  // Can overflow!
}
```

**Scenario**: Array with 1000 elements, each = 1,000,000

- Sum = 1,000,000,000 (still fits in int)
- But if array is slightly larger, OVERFLOW!

**Solution**:

```java
long sum = 0;  // ✅ SAFE!
```

**Why?**

- `int` range: -2³¹ to 2³¹-1 (≈ -2.1B to 2.1B)
- `long` range: -2⁶³ to 2⁶³-1 (≈ -9.2×10¹⁸ to 9.2×10¹⁸)

#### 2. **Floating Point Division** 🔴

**Problem**:

```python
result[i] = sum / (i+1)  # ❌ Gives float in Python 3!
```

**Output**: `[4.0, 5.0, 5.0, 4.0]` (wrong type!)

**Solution**:

```python
result[i] = sum // (i+1)  # ✅ Floor division
```

**In Java**:

```java
result[i] = (int)(sum / (i+1));  // Cast to int
```

#### 3. **Off-by-One Error** 🔴

**Problem**:

```java
result[i] = sum / i;  // ❌ Division by zero at i=0!
```

**Why Wrong?**

- At index i, we have elements from 0 to i
- That's **i+1** elements, not i elements!
- Example: indices [0,1,2] = 3 elements

**Solution**:

```java
result[i] = sum / (i + 1);  // ✅ Correct count
```

#### 4. **Recalculating Sum (Naive Approach)** 🔴

**Problem**:

```java
for (int i = 0; i < n; i++) {
    int sum = 0;
    for (int j = 0; j <= i; j++) {  // ❌ O(n²)
        sum += arr[j];
    }
    result[i] = sum / (i+1);
}
```

**Why Wrong?**: Wastes time recalculating what we already know!

**Solution**: Use running sum (shown in optimal approach)

#### 5. **Not Handling Empty Array** 🔴

**Problem**: What if `arr = []`?

**Solution**:

```java
if (arr.length == 0) return new int[0];
```

### 🔑 Algorithm Steps

**Optimal O(n) Algorithm**:

1. **Initialize**:

   ```
   runningSum = 0
   result = empty array of size n
   ```

2. **Iterate** through each index i from 0 to n-1:

   ```
   a. Add current element to runningSum
   b. Calculate average = runningSum ÷ (i+1) [integer division]
   c. Store average in result[i]
   ```

3. **Return** result array

**Pseudocode**:

```
function prefixAverages(arr):
    n = length of arr
    result = array of size n
    sum = 0

    for i from 0 to n-1:
        sum = sum + arr[i]
        result[i] = floor(sum / (i+1))

    return result
```

### 💻 Implementations

### Java

```java
class Solution {
    public int[] prefixAverages(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        long sum = 0;  // Use long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = (int)(sum / (i + 1));  // Integer division
        }

        return result;
    }
}

// Time: O(n), Space: O(1) excluding output
```

### Python

```python
def prefix_averages(arr):
    """
    Calculate prefix averages for each position.

    Args:
        arr: List of integers representing daily inventory

    Returns:
        List of integers with prefix averages (floor division)
    """
    n = len(arr)
    result = [0] * n
    running_sum = 0

    for i in range(n):
        running_sum += arr[i]
        result[i] = running_sum // (i + 1)  # Floor division operator

    return result

# Time: O(n), Space: O(1) excluding output
```

### C++++

```cpp
class Solution {
public:
    vector<int> prefixAverages(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n);
        long long sum = 0;  // Use long long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = sum / (i + 1);  // Integer division by default
        }

        return result;
    }
};

// Time: O(n), Space: O(1) excluding output
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var prefixAverages = function(arr) {
    const n = arr.length;
    const result = new Array(n);
    let sum = 0;

    for (let i = 0; i < n; i++) {
        sum += arr[i];
        result[i] = Math.floor(sum / (i + 1));
    }

    return result;
};

// Time: O(n), Space: O(1) excluding output
```

### 📊 Comparison Table

| **Aspect**            | **Naive O(n²)**           | **Optimal O(n)**     |
| --------------------- | ------------------------- | -------------------- |
| **Algorithm**         | Recalculate sum each time | Maintain running sum |
| **Time for n=100**    | ~5,000 ops                | ~100 ops             |
| **Time for n=1,000**  | ~500,000 ops              | ~1,000 ops           |
| **Time for n=10,000** | ~50,000,000 ops           | ~10,000 ops          |
| **Space (extra)**     | O(1)                      | O(1)                 |
| **Redundant work?**   | ✅ Yes                    | ❌ No                |
| **Efficiency**        | Poor                      | Excellent            |

