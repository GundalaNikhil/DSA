---
title: Deque Balance Rearrange
slug: deque-balance-rearrange
difficulty: Medium
difficulty_score: 41
tags:
- Deque
- Two Pointers
- Simulation
problem_id: QUE_DEQUE_BALANCE_REARRANGE__5142
display_id: QUE-014
topics:
- Deque
- Two Pointers
- Simulation
---
# Deque Balance Rearrange - Editorial

## Problem Summary

You are given an array of integers. You need to construct a new sequence by alternately picking elements from the beginning and the end of the original array. The process starts by picking the first element, then the last, then the second, then the second-to-last, and so on, until all elements have been picked.

## Real-World Scenario

Imagine a **Card Dealer** shuffling a deck of cards. One common technique is to take the top card, place it down, then take the bottom card, place it down, and repeat. This "interleaving" from both ends rearranges the deck in a specific deterministic pattern.

Another example is **Load Balancing** in a server cluster where tasks are queued. To ensure fairness or to mix high-priority (front) and low-priority (back) tasks, a scheduler might pick one task from the head of the queue and one from the tail alternately.

## Problem Exploration

### 1. Understanding the Pattern
Given an array `A` of size `n`:
-   Step 1: Pick `A[0]` (Front)
-   Step 2: Pick `A[n-1]` (Back)
-   Step 3: Pick `A[1]` (Front)
-   Step 4: Pick `A[n-2]` (Back)
-   ...

### 2. Stopping Condition
We continue this process until we have picked all `n` elements. If `n` is odd, the last element picked will be the middle element. We must be careful not to pick the middle element twice.

### 3. Data Structures
While the problem mentions "Deque" in the title, the input is given as an array. We can simulate the deque behavior using **Two Pointers** on the array, which is more efficient than actually creating a Deque and popping elements.

## Approaches

### Approach 1: Simulation with Deque

We can literally load all elements into a Double-Ended Queue (Deque). Then, we loop while the deque is not empty:
1.  Pop from front and add to result.
2.  If deque is not empty, pop from back and add to result.

-   **Complexity**:
    -   Time: $O(N)$
    -   Space: $O(N)$ to store the deque.

### Approach 2: Two Pointers (Optimal)

We can avoid the overhead of a Deque data structure by using two pointers, `left` starting at `0` and `right` starting at `n-1`.

-   **Algorithm**:
    1.  Initialize `left = 0`, `right = n - 1`.
    2.  Initialize an empty result list/array.
    3.  Loop while `left <= right`:
        a.  Add `A[left]` to result.
        b.  If `left != right` (to avoid duplicates when `n` is odd), add `A[right]` to result.
        c.  Increment `left`, decrement `right`.
    4.  Return result.

-   **Visual Execution**:
    Input: `[2, 4, 6, 8, 10]`
    `left = 0`, `right = 4`

    1.  Add `A[0]` (2). `left` becomes 1.
    2.  `0 != 4`, so add `A[4]` (10). `right` becomes 3.
    3.  Add `A[1]` (4). `left` becomes 2.
    4.  `1 != 3`, so add `A[3]` (8). `right` becomes 2.
    5.  Add `A[2]` (6). `left` becomes 3.
    6.  `2 == 2`, skip adding `A[right]`. `right` becomes 1.
    7.  Loop ends (`3 > 1`).

    Result: `[2, 10, 4, 8, 6]`

-   **Complexity**:
    -   **Time**: $O(N)$. We visit each element exactly once.
    -   **Space**: $O(N)$ for the output array. (Auxiliary space is $O(1)$).

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] buildDeque(int[] values) {
        int n = values.length;
        int[] result = new int[n];
        int left = 0;
        int right = n - 1;
        int index = 0;
        
        while (left <= right) {
            // Take from front
            result[index++] = values[left];
            
            // Take from back if it's not the same element
            if (left != right) {
                result[index++] = values[right];
            }
            
            left++;
            right--;
        }
        
        return result;
    }
}
```

### Python

```python
from typing import List

def build_deque(values: List[int]) -> List[int]:
    n = len(values)
    result = []
    left, right = 0, n - 1
    
    while left <= right:
        result.append(values[left])
        if left != right:
            result.append(values[right])
        left += 1
        right -= 1
        
    return result
```

### C++

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> buildDeque(const vector<int>& values) {
        vector<int> result;
        int n = values.size();
        result.reserve(n);
        
        int left = 0;
        int right = n - 1;
        
        while (left <= right) {
            result.push_back(values[left]);
            if (left != right) {
                result.push_back(values[right]);
            }
            left++;
            right--;
        }
        
        return result;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number[]} values
   * @return {number[]}
   */
  buildDeque(values) {
    const result = [];
    let left = 0;
    let right = values.length - 1;
    
    while (left <= right) {
      result.push(values[left]);
      if (left !== right) {
        result.push(values[right]);
      }
      left++;
      right--;
    }
    
    return result;
  }
}
```

## Test Case Walkthrough

**Input:** `[10, 20, 30, 40, 50]`

1.  `left=0`, `right=4`. Add `10`. `left!=right`, add `50`. Result: `[10, 50]`. `left=1`, `right=3`.
2.  `left=1`, `right=3`. Add `20`. `left!=right`, add `40`. Result: `[10, 50, 20, 40]`. `left=2`, `right=2`.
3.  `left=2`, `right=2`. Add `30`. `left==right`, skip. Result: `[10, 50, 20, 40, 30]`. `left=3`, `right=1`.
4.  Stop.

**Output:** `10 50 20 40 30`

## Proof of Correctness

The algorithm iterates `ceil(n/2)` times. In each iteration, it adds the `left`-th element. If `left != right`, it also adds the `right`-th element.
-   Since `left` starts at 0 and increments, it covers 0, 1, 2...
-   Since `right` starts at `n-1` and decrements, it covers `n-1`, `n-2`...
-   The condition `left <= right` ensures we process all elements.
-   The check `if (left != right)` handles the middle element case for odd `n` correctly, preventing duplication.
Thus, every element is added exactly once in the specified alternating order.

## Interview Extensions

1.  **What if we need to reconstruct the original array from the rearranged one?**
    -   This is the inverse problem. We would place elements from the rearranged array into `left` and `right` positions of a new array alternately.
    -   `result[left] = rearranged[0]`, `result[right] = rearranged[1]`, etc.

2.  **Can we do this in-place?**
    -   Doing this in-place with $O(1)$ extra space is difficult because we are overwriting elements we might need later. It would likely require a complex cycle-following algorithm or $O(N)$ swaps, which is much harder to implement than using an output array.

3.  **What if the input is a Linked List?**
    -   We would need to find the middle, reverse the second half, and then merge the two halves (similar to "Reorder List" problem).

### Common Mistakes

-   **Double counting middle element**: Forgetting the `if (left != right)` check inside the loop when `n` is odd will result in the middle element being added twice.
-   **Off-by-one errors**: Incorrect loop condition (e.g., `left < right`) might miss the middle element.
-   **Modifying input**: If the problem requires the input array to remain unchanged, ensure you are reading from it and writing to a new array (or clarify requirements).

## Related Concepts

-   **Two Pointers**: The primary technique used.
-   **Deque**: The conceptual data structure being simulated.
-   **In-place Array Manipulation**: Related advanced topic.
