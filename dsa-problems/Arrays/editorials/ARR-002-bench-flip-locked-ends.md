---
problem_id: ARR_REVERSE_MID__66B6
display_id: ARR-002
slug: bench-flip-locked-ends
title: "Bench Flip With Locked Ends"
difficulty: Easy
difficulty_score: 30
topics:
  - Array
  - Two Pointers
  - In-Place Algorithm
  - Reversal
tags:
  - arrays
  - two-pointers
  - reversal
  - easy
premium: true
subscription_tier: basic
---

# Bench Flip With Locked Ends

![Problem Header](../images/ARR-002/header.png)

### 📋 Problem Summary

Reverse the middle portion of an array while keeping the first and last elements fixed in their positions.

### 🌍 Real-World Scenario

**Park Bench Rearrangement**

Imagine a row of park benches at your college campus. Each bench has a number painted on it. Due to weathering, you want to flip the middle benches around for maintenance, but:

- The **first bench** must stay (it's cemented near the entrance)
- The **last bench** must stay (it's cemented at the exit)
- Only the **middle benches** can be rearranged

Example:

```
Original: [A, B, C, D, E]
           ↑           ↑
         Fixed      Fixed

After:    [A, D, C, B, E]
           ↑  reversed  ↑
```

This is useful when you want to:

- Reverse a substring without affecting boundaries
- Maintain anchor points while transforming data
- Implement palindrome checkers with fixed endpoints

### 📚 Detailed Explanation

**What does "reverse middle" mean?**

- Keep `arr[0]` and `arr[n-1]` unchanged
- Reverse everything between them
- For array `[5, 3, 8, 1, 9]`:
  - Fixed: 5 (start) and 9 (end)
  - Reverse: [3, 8, 1] → [1, 8, 3]
  - Result: [5, 1, 8, 3, 9]

**Edge Cases**:

- If n ≤ 2: No middle to reverse (just first/last or single element)
- Example: [1, 2] → [1, 2] (no change)

### ❌ Naive Approach

**Idea**: Create a temporary array, copy middle elements in reverse order, then copy back.

```
1. Extract middle elements → temp = [3, 8, 1]
2. Reverse temp → [1, 8, 3]
3. Copy back to original array
```

**Code Pattern**:

```python
middle = arr[1:n-1]  # Extract middle
middle.reverse()     # Reverse it
arr[1:n-1] = middle  # Copy back
```

**⏱️ Time Complexity: O(n)**

- Extract middle: O(n)
- Reverse: O(n)
- Copy back: O(n)
- Total: O(n) + O(n) + O(n) = O(n)

**📦 Space Complexity: O(n)**

- Temporary array to store middle elements
- Size proportional to input

**Why is this "naive"?**
We can do the same thing **without extra space**!

### ✅ Optimal Approach

**💡 Key Insight**: Use two pointers to swap elements in-place!

Think of it like two people walking towards each other:

- Person A starts from left end of middle (index 1)
- Person B starts from right end of middle (index n-2)
- They swap what they're holding
- Both take one step towards center
- Repeat until they meet

**No extra array needed!**

**⏱️ Time Complexity: O(n)**

**Detailed Breakdown**:

- We have n-2 middle elements (excluding first and last)
- Need (n-2)/2 swaps (each swap fixes 2 positions)
- Each swap is O(1)
- Total: (n-2)/2 × O(1) = O(n)

**Why O(n) and not O((n-2)/2)?**

- In Big-O, we drop constants: (n-2)/2 → n/2 → n
- We express it as O(n) for simplicity

**📦 Space Complexity: O(1)**

**Why O(1)?**

- Only use 3 variables: `left`, `right`, `temp` (for swapping)
- Memory doesn't grow with input size
- Swapping in-place = no extra arrays!

**Improvement over Naive**: Same time but O(n) → O(1) space!

### 🎨 Visual Representation

**Example**: `arr = [5, 3, 8, 1, 9]`

```
Initial State:
┌───┬───┬───┬───┬───┐
│ 5 │ 3 │ 8 │ 1 │ 9 │
└───┴───┴───┴───┴───┘
  ↑   ↑       ↑   ↑
  │   └───────┘   │
Fixed   Middle   Fixed
        (to reverse)

Step-by-Step Process:

Step 1: Initialize pointers
┌───┬───┬───┬───┬───┐
│ 5 │ 3 │ 8 │ 1 │ 9 │
└───┴───┴───┴───┴───┘
      ↑       ↑
    left    right
    (1)     (3)

Step 2: Swap arr[left] ↔ arr[right]
┌───┬───┬───┬───┬───┐
│ 5 │ 1 │ 8 │ 3 │ 9 │
└───┴───┴───┴───┴───┘
      ↓       ↓
    swapped!

Step 3: Move pointers inward
┌───┬───┬───┬───┬───┐
│ 5 │ 1 │ 8 │ 3 │ 9 │
└───┴───┴───┴───┴───┘
          ↑
      left=right
      (stop!)

Final Result:
┌───┬───┬───┬───┬───┐
│ 5 │ 1 │ 8 │ 3 │ 9 │
└───┴───┴───┴───┴───┘
  ↑   ←──────←   ↑
Fixed  Reversed  Fixed
```

**Another Example**: `arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`

```
Initial:
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
 ↑   ↑                   ↑   ↑
keep left             right keep

Iteration 1: Swap 9 ↔ 2
[10, 2, 8, 7, 6, 5, 4, 3, 9, 1]
     ↑               ↑
   left++         right--

Iteration 2: Swap 8 ↔ 3
[10, 2, 3, 7, 6, 5, 4, 8, 9, 1]
        ↑           ↑
      left++     right--

Iteration 3: Swap 7 ↔ 4
[10, 2, 3, 4, 6, 5, 7, 8, 9, 1]
           ↑       ↑
         left++ right--

Iteration 4: Swap 6 ↔ 5
[10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
              ↑ ↑
        left > right (STOP)

Result: [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [100, 1, 2, 3, 4, 5, 100]`

```
┌──────┬─────────────┬──────────┬────────────────────────────────┐
│ Step │ Action      │ Pointers │ Array State                    │
├──────┼─────────────┼──────────┼────────────────────────────────┤
│  0   │ Initialize  │ L=1, R=5 │ [100, 1, 2, 3, 4, 5, 100]      │
│  1   │ Swap 1↔5    │ L=2, R=4 │ [100, 5, 2, 3, 4, 1, 100]      │
│  2   │ Swap 2↔4    │ L=3, R=3 │ [100, 5, 4, 3, 2, 1, 100]      │
│  3   │ L==R (stop) │    -     │ [100, 5, 4, 3, 2, 1, 100]      │
└──────┴─────────────┴──────────┴────────────────────────────────┘

Output: [100, 5, 4, 3, 2, 1, 100]

Middle [1,2,3,4,5] became [5,4,3,2,1] ✓
```

**Edge Case**: `arr = [1, 2]`

```
n = 2
left = 1, right = 0
Condition: left < right? NO (1 < 0 is false)
Loop doesn't execute
Result: [1, 2] (unchanged) ✓
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Not Handling Small Arrays** 🔴

**Problem**:

```java
// ❌ Crashes on small arrays!
int left = 1;
int right = arr.length - 2;
// What if arr.length = 1? right = -1!
```

**Solution**:

```java
// ✅ Handle edge cases
if (arr.length <= 2) return arr;
```

#### 2. **Wrong Pointer Initialization** 🔴

**Problem**:

```java
int left = 0;      // ❌ Should be 1!
int right = n - 1; // ❌ Should be n-2!
```

**Why Wrong?**

- `left = 0` means we're including the first element (should be fixed!)
- `right = n-1` means we're including the last element (should be fixed!)

**Solution**:

```java
int left = 1;      // ✅ First middle element
int right = n - 2; // ✅ Last middle element
```

#### 3. **Forgetting to Move Pointers** 🔴

**Problem**:

```java
while (left < right) {
    swap(arr[left], arr[right]);
    // ❌ Forgot left++ and right--!
    // Infinite loop!
}
```

**Solution**:

```java
while (left < right) {
    swap(arr[left], arr[right]);
    left++;   // ✅ Move inward
    right--;  // ✅ Move inward
}
```

#### 4. **Wrong Loop Condition** 🔴

**Problem**:

```java
while (left <= right) {  // ❌ Will swap middle element with itself!
```

**Why Wrong?**

- When `left == right`, we're at the same position
- Swapping it with itself is wasteful (though harmless)

**Solution**:

```java
while (left < right) {  // ✅ Stop when they meet
```

#### 5. **Creating Extra Array** 🔴

**Problem**: Using O(n) space when not needed

```python
# ❌ Unnecessary space usage
middle = arr[1:-1]
middle.reverse()
arr[1:-1] = middle
```

**Solution**: Swap in-place!

### 🔑 Algorithm Steps

**Optimal O(n) Time, O(1) Space Algorithm**:

1. **Edge Case Check**:

   ```
   if n <= 2: return arr (no middle to reverse)
   ```

2. **Initialize Two Pointers**:

   ```
   left = 1 (first middle element)
   right = n-2 (last middle element)
   ```

3. **Swap and Move**:

   ```
   while left < right:
       swap arr[left] with arr[right]
       left++
       right--
   ```

4. **Return** modified array

**Pseudocode**:

```
function reverseMiddle(arr):
    n = length of arr
    if n <= 2:
        return arr

    left = 1
    right = n - 2

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left = left + 1
        right = right - 1

    return arr
```

### 💻 Implementations

#### Java

```java
class Solution {
    public int[] reverseMiddle(int[] arr) {
        int n = arr.length;

        // Edge case: no middle to reverse
        if (n <= 2) return arr;

        int left = 1;        // First middle element
        int right = n - 2;   // Last middle element

        // Two-pointer swap
        while (left < right) {
            // Swap arr[left] and arr[right]
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            // Move pointers inward
            left++;
            right--;
        }

        return arr;
    }
}

// Time: O(n) - traverse half of middle section
// Space: O(1) - only use 3 variables
```

#### Python

```python
def reverse_middle(arr):
    """
    Reverse the middle portion of array, keeping first and last fixed.

    Args:
        arr: List of integers

    Returns:
        Modified list with middle reversed
    """
    n = len(arr)

    # Edge case: arrays of length 0, 1, or 2 have no middle
    if n <= 2:
        return arr

    left = 1        # Start of middle section
    right = n - 2   # End of middle section

    # Swap elements from outside-in
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Pythonic swap!
        left += 1
        right -= 1

    return arr

# Time: O(n), Space: O(1)
```

#### C++

```cpp
class Solution {
public:
    vector<int> reverseMiddle(vector<int>& arr) {
        int n = arr.size();

        // Edge case: no middle to reverse
        if (n <= 2) return arr;

        int left = 1;       // First middle element
        int right = n - 2;  // Last middle element

        // Two-pointer swap approach
        while (left < right) {
            swap(arr[left], arr[right]);  // C++ STL swap
            left++;
            right--;
        }

        return arr;
    }
};

// Time: O(n), Space: O(1)
```

### 📊 Comparison Table

| **Aspect**            | **Naive (Extra Array)**          | **Optimal (In-Place)** |
| --------------------- | -------------------------------- | ---------------------- |
| **Algorithm**         | Copy to temp, reverse, copy back | Two-pointer swap       |
| **Time Complexity**   | O(n)                             | O(n)                   |
| **Space Complexity**  | O(n)                             | O(1) ⭐                |
| **Memory for n=1000** | ~4KB extra                       | ~12 bytes              |
| **Memory for n=1M**   | ~4MB extra                       | ~12 bytes              |
| **Modifications**     | Creates new array                | Modifies in-place      |
| **Best for**          | When you need original           | Production code ⭐     |


