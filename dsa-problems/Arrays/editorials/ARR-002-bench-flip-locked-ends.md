# Problem 2: Bench Flip With Locked Ends (ARR-002)

**Topic Tags**: `Array`, `Two Pointers`, `In-Place`  
**Difficulty**: Easy  
**Problem ID**: ARRAY-002

---

## Problem Summary

Reverse the middle portion of an array, keeping the first and last elements fixed.

---

## Approach 1: Naive Solution

### Idea

Copy the middle elements to a temporary array, reverse them, then copy back.

### Algorithm

1. Create a temporary array for middle elements (from index 1 to n-2)
2. Reverse the temporary array
3. Copy back to original array

### Complexity Analysis

**Time Complexity**: O(n)

- Copying middle elements: O(n)
- Reversing: O(n)
- Copying back: O(n)

**Space Complexity**: O(n)

- Temporary array for middle elements

---

## Approach 2: Optimal Solution ⭐

### Key Insight

Use two pointers to swap elements in-place from both ends of the middle section. No extra space needed!

### Algorithm

1. If `n <= 2`, return the array as-is (no middle to reverse)
2. Set `left = 1` and `right = n-2`
3. While `left < right`:
   - Swap `arr[left]` with `arr[right]`
   - Increment `left`, decrement `right`

### Complexity Analysis

**Time Complexity**: O(n)

- Single pass with two pointers
- Each element in middle is touched once

**Space Complexity**: O(1)

- In-place reversal using only pointer variables

---

## Visual Representation

### Example: `arr = [1, 2, 3, 4, 5]`

```
Initial:    [1, 2, 3, 4, 5]
             ↑  ↑     ↑  ↑
           fixed L   R fixed

Step 1: Swap arr[1] and arr[3]
[1, 4, 3, 2, 5]
    ↑     ↑
    L     R

Step 2: Move pointers
[1, 4, 3, 2, 5]
       ↑
     L,R overlap - STOP

Final:  [1, 4, 3, 2, 5]
```

### Example: `arr = [10, 20, 30, 40]`

```
Initial:    [10, 20, 30, 40]
              ↑   ↑   ↑   ↑
            fixed L   R fixed

Step 1: Swap arr[1] and arr[2]
[10, 30, 20, 40]
     ↑↑  ↑↑
     LR  RL - pointers cross, STOP

Final:  [10, 30, 20, 40]
```

---

## Edge Cases

### Case 1: Array of size 2

```
Input:  [1, 2]
Output: [1, 2]
Reason: No middle elements to reverse
```

### Case 2: Array of size 1

```
Input:  [5]
Output: [5]
Reason: No operation needed
```

### Case 3: Array of size 3

```
Input:  [1, 2, 3]
Output: [1, 2, 3]
Reason: Only one middle element, stays same
```

---

## Implementations

### Java

```java
class Solution {
    public int[] reverseMiddle(int[] arr) {
        int n = arr.length;
        if (n <= 2) return arr;

        int left = 1;
        int right = n - 2;

        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }

        return arr;
    }
}
```

### Python

```python
def reverse_middle(arr):
    n = len(arr)
    if n <= 2:
        return arr

    left = 1
    right = n - 2

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
```

### C++

```cpp
class Solution {
public:
    vector<int> reverseMiddle(vector<int>& arr) {
        int n = arr.size();
        if (n <= 2) return arr;

        int left = 1;
        int right = n - 2;

        while (left < right) {
            swap(arr[left], arr[right]);
            left++;
            right--;
        }

        return arr;
    }
};
```

---

## Common Mistakes & Pitfalls

### 1. Not Handling Edge Cases ⚠️

- ❌ Forgetting to check if array has <= 2 elements
- ✅ Always check if there's actually a middle section to reverse

### 2. Including First/Last Elements ⚠️

- ❌ Starting with `left = 0` or `right = n-1`
- ✅ Start with `left = 1` and `right = n-2` to keep ends fixed

### 3. Incorrect Loop Condition ⚠️

- ❌ Using `while (left <= right)` causes unnecessary swap when they meet
- ✅ Use `while (left < right)` to stop before they cross

### 4. Creating Unnecessary Copy ⚠️

- ❌ Creating a copy of the entire array
- ✅ Modify in-place for O(1) space

---

## Step-by-Step Dry Run

### Input: `[7, 8, 9, 10, 11]`

```
Initial State:
Array: [7, 8, 9, 10, 11]
        ↑  L      R   ↑
      fixed          fixed

Iteration 1:
  left = 1, right = 3
  Swap arr[1](8) ↔ arr[3](10)
  Array: [7, 10, 9, 8, 11]
  left++, right--
  left = 2, right = 2

Iteration 2:
  left = 2, right = 2
  Condition: left < right? NO
  Exit loop

Final: [7, 10, 9, 8, 11]
```

---

## Comparison Table

| Aspect           | Naive Approach | Optimal Approach |
| ---------------- | -------------- | ---------------- |
| Time Complexity  | O(n)           | O(n)             |
| Space Complexity | O(n)           | O(1)             |
| Extra Memory     | Yes            | No               |
| In-Place         | No             | Yes              |

---

## Quiz Questions

### Q1: What happens if we use `while (left <= right)` instead of `while (left < right)`?

- A) Program crashes
- B) Works correctly
- C) Performs an unnecessary swap when pointers meet
- D) Infinite loop

<details>
<summary>Answer</summary>

**C) Performs an unnecessary swap when pointers meet**

Explanation: When left == right, we're swapping an element with itself, which is wasteful but doesn't break correctness.

</details>

### Q2: For array `[1, 2, 3, 4, 5, 6]`, what is the output?

- A) [1, 5, 4, 3, 2, 6]
- B) [6, 5, 4, 3, 2, 1]
- C) [1, 2, 3, 4, 5, 6]
- D) [2, 3, 4, 5, 6, 1]

<details>
<summary>Answer</summary>

**A) [1, 5, 4, 3, 2, 6]**

Explanation: First and last stay fixed. Middle [2,3,4,5] reverses to [5,4,3,2].

</details>

### Q3: What is the space complexity of the optimal approach?

- A) O(n)
- B) O(log n)
- C) O(1)
- D) O(n²)

<details>
<summary>Answer</summary>

**C) O(1)**

Explanation: We only use two pointer variables (left, right) and one temp variable for swapping. Space doesn't grow with input size.

</details>

---

## Related Problems

- Reverse Entire Array
- Reverse Array in Groups
- Rotate Array

## Tags

`#arrays` `#two-pointers` `#in-place` `#easy`
