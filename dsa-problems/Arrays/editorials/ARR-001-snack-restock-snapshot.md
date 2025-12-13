# Problem 1: Snack Restock Snapshot (ARR-001)

**Topic Tags**: `Array`, `Prefix Sum`, `Mathematics`  
**Difficulty**: Easy  
**Problem ID**: ARRAY-001

---

## Problem Summary

Given an array of daily inventory values, compute the prefix average rounded down for each position.

## Real-World Scenario

Imagine you're managing a campus snack shop. Each day you record the inventory count. To understand trends, you want to know "What has been the average inventory from Day 1 up to today?" for every day. This helps identify if inventory is increasing, decreasing, or stable over time.

---

## Detailed Explanation

### Why Prefix Average?

- Prefix average at position `i` = average of all elements from index `0` to `i`
- Formula: `(arr[0] + arr[1] + ... + arr[i]) / (i + 1)`
- We use **integer division** (floor), so 7/2 = 3, not 3.5

---

## Approach 1: Naive Solution

### Idea

For each position `i`, sum all elements from `0` to `i` and divide by `(i+1)`.

### Why is this inefficient?

```
For position 0: sum 1 element
For position 1: sum 2 elements
For position 2: sum 3 elements
...
For position n-1: sum n elements
```

Total operations = 1 + 2 + 3 + ... + n = **n(n+1)/2 ≈ O(n²)**

### Complexity Analysis

**Time Complexity**: O(n²)

- **Why?** We have n positions, and for each position, we recalculate the entire sum from scratch. This means position `i` requires `i+1` additions.
- **Detailed breakdown**: Σ(i+1) for i=0 to n-1 = n + n(n-1)/2 = O(n²)

**Space Complexity**: O(1) - excluding output array

---

## Approach 2: Optimal Solution ⭐

### Key Insight

Instead of recalculating sum from scratch, **reuse the previous sum**!

- Sum up to index 0 = arr[0]
- Sum up to index 1 = previous sum + arr[1]
- Sum up to index 2 = previous sum + arr[2]

This eliminates redundant calculations!

### Algorithm

1. Initialize `runningSum = 0`
2. For each position `i`:
   - Add `arr[i]` to `runningSum`
   - Compute `result[i] = runningSum / (i+1)` (integer division)

### Complexity Analysis

**Time Complexity**: O(n)

- **Why?** We traverse the array exactly once, performing constant-time operations (one addition, one division) at each step.
- **Detailed breakdown**: n iterations × O(1) work per iteration = O(n)
- **Improvement**: From O(n²) to O(n) - this is **n times faster** for large inputs!

**Space Complexity**: O(1) - excluding output array

- **Why?** We only use a single variable (`sum`) regardless of input size. The result array doesn't count as extra space since it's required output.

---

## Visual Representation

### Example: `arr = [4, 6, 6, 0]`

```
Step-by-step calculation:

Index:     0    1    2    3
Value:     4    6    6    0
---------------------------------
Sum:       4   10   16   16
Count:     1    2    3    4
Average:  4/1  10/2 16/3 16/4
Result:    4    5    5    4

Visual Flow:
Day 0: [4] → sum=4, count=1 → avg = 4
       ↓
Day 1: [4, 6] → sum=10, count=2 → avg = 5
       ↓
Day 2: [4, 6, 6] → sum=16, count=3 → avg = 5 (16÷3 = 5.33, floor = 5)
       ↓
Day 3: [4, 6, 6, 0] → sum=16, count=4 → avg = 4
```

---

## Test Case Walkthrough

### Input: `arr = [1, 2, 3, 4, 5, 6]`

```
Running Visualization:

i=0: sum=0+1=1    → avg=1/1=1    result=[1]
     Running sum: 1

i=1: sum=1+2=3    → avg=3/2=1    result=[1,1]
     Running sum: 1→3

i=2: sum=3+3=6    → avg=6/3=2    result=[1,1,2]
     Running sum: 1→3→6

i=3: sum=6+4=10   → avg=10/4=2   result=[1,1,2,2]
     Running sum: 1→3→6→10

i=4: sum=10+5=15  → avg=15/5=3   result=[1,1,2,2,3]
     Running sum: 1→3→6→10→15

i=5: sum=15+6=21  → avg=21/6=3   result=[1,1,2,2,3,3]
     Running sum: 1→3→6→10→15→21
```

**Output**: `[1, 1, 2, 2, 3, 3]`

---

## Common Mistakes & Pitfalls

### 1. Integer Overflow ⚠️

- ❌ Using `int` for sum when array has large values
- ✅ Use `long` to prevent overflow
- Example: If array has 1000 elements each with value 1,000,000, sum = 1,000,000,000 (fits in int), but barely!

### 2. Floating Point Division ⚠️

- ❌ Using `sum / (i+1)` might give float in some languages
- ✅ Use integer division explicitly: `sum // (i+1)` in Python, `(int)(sum/(i+1))` in Java

### 3. Off-by-One Error ⚠️

- ❌ Dividing by `i` instead of `i+1`
- ✅ Remember: for index `i`, we have `i+1` elements (indices 0 to i)

### 4. Recomputing Sum Each Time (Naive Approach) ⚠️

- ❌ Starting inner loop from 0 each time
- ✅ Maintain running sum

---

## Implementations

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
```

### Python

```python
def prefix_averages(arr):
    n = len(arr)
    result = [0] * n
    running_sum = 0

    for i in range(n):
        running_sum += arr[i]
        result[i] = running_sum // (i + 1)  # Floor division

    return result
```

### C++

```cpp
class Solution {
public:
    vector<int> prefixAverages(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n);
        long long sum = 0;  // Use long long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = sum / (i + 1);  // Integer division
        }

        return result;
    }
};
```

---

## Quick Comparison Table

| Aspect          | Naive O(n²)             | Optimal O(n)             |
| --------------- | ----------------------- | ------------------------ |
| For n=1000      | ~500,000 ops            | ~1,000 ops               |
| For n=10,000    | ~50,000,000 ops         | ~10,000 ops              |
| Space           | O(1)                    | O(1)                     |
| Redundant work? | Yes (recalculates sums) | No (reuses previous sum) |

---

## Quiz Questions

### Q1: What is the time complexity of computing prefix averages using the naive approach for an array of size n?

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(2^n)

<details>
<summary>Answer</summary>

**C) O(n²)**

Explanation: For each position i (n positions total), we sum elements from 0 to i (up to n elements). Total operations = 1+2+3+...+n = n(n+1)/2 = O(n²).

</details>

### Q2: If the array is `[10, 20, 30]`, what is the prefix average at index 1?

- A) 10
- B) 15
- C) 20
- D) 30

<details>
<summary>Answer</summary>

**B) 15**

Explanation: At index 1, we average elements [10, 20]. Sum = 30, count = 2, average = 30/2 = 15.

</details>

### Q3: Why do we use `long` instead of `int` for the running sum?

- A) To make the program faster
- B) To prevent integer overflow
- C) To store decimal values
- D) It's not necessary, int is fine

<details>
<summary>Answer</summary>

**B) To prevent integer overflow**

Explanation: If we have many large values, the cumulative sum might exceed int range (2³¹-1 ≈ 2 billion). Using long (2⁶³-1) prevents overflow errors.

</details>

### Q4: What is the space complexity of the optimal solution (excluding output array)?

- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary>Answer</summary>

**A) O(1)**

Explanation: We only use a single variable `sum` regardless of input size. The result array doesn't count as it's required output.

</details>

### Q5: For array `[5, 5, 5, 5]`, what is the output?

- A) [5, 5, 5, 5]
- B) [5, 10, 15, 20]
- C) [1, 2, 3, 4]
- D) [0, 5, 10, 15]

<details>
<summary>Answer</summary>

**A) [5, 5, 5, 5]**

Explanation:

- Index 0: 5/1 = 5
- Index 1: (5+5)/2 = 10/2 = 5
- Index 2: (5+5+5)/3 = 15/3 = 5
- Index 3: (5+5+5+5)/4 = 20/4 = 5

</details>

---

## Related Problems

- Prefix Sum Array
- Running Average in Streams
- Cumulative Statistics

## Tags

`#arrays` `#prefix-sum` `#mathematics` `#easy`
