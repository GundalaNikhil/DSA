---
problem_id: ARR_PAIR_FORBID__25BE
display_id: ARR-008
slug: partner-pair-sum-forbidden
title: "Partner Pair Sum With Forbidden"
difficulty: Medium
difficulty_score: 55
topics:
  - Array
  - Two Pointers
  - Hash Set
  - Pair Finding
tags:
  - arrays
  - two-pointers
  - hashset
  - medium
premium: true
subscription_tier: basic
---

# Partner Pair Sum With Forbidden

![Problem Header](../images/ARR-008/header.png)

### 📋 Problem Summary

Find if there exists a pair of elements in a sorted array that sum to a target, but neither element can be from a "forbidden" set of indices.

### 🌍 Real-World Scenario

**Team Partner Assignment with Restrictions**

In a coding competition:

- Students ranked by skill level (sorted array)
- Need pairs that together reach target skill level
- Some students are "forbidden" (already teamed up, absent, etc.)
- Find if valid pairing exists

Example:

```
Skills: [1, 2, 3, 4, 5]
Target: 7
Forbidden indices: {1, 3}  (students at positions 1 and 3 unavailable)

Valid pairs:
- 2 (index 1) + 5 (index 4) = 7 → ✗ (index 1 forbidden)
- 3 (index 2) + 4 (index 3) = 7 → ✗ (index 3 forbidden)

No valid pair exists!
```

### 📚 Detailed Explanation

**What Makes This Tricky?**

- Normal pair sum: Use two pointers or hash set
- **With forbidden indices**: Must skip certain elements
- Maintain efficiency while checking constraints

**Key Insight**:

- Use two pointers to find pairs
- Skip elements in forbidden set
- Check sum and constraints simultaneously

### ❌ Naive Approach

**Algorithm**:

```
1. For each element, check all pairs
2. Skip forbidden indices
3. Return true if valid pair found
```

**⏱️ Time Complexity: O(n²)**

- Nested loops: O(n) for each element, O(n) for pairs

**📦 Space Complexity: O(1)**

- No extra space needed

### ✅ Optimal Approach

**Algorithm**:

```
1. Use two pointers (left, right)
2. Move pointers based on sum comparison
3. Skip forbidden indices
4. Return true if valid pair found
```

**⏱️ Time Complexity: O(n)**

- Single pass with two pointers

**📦 Space Complexity: O(1)**

- Only pointers and set for forbidden indices

### 🎨 Visual Representation

**Example**: `arr = [1, 2, 3, 4, 5], target = 7, forbidden = {1, 3}`

```
Initial:
arr: [1, 2, 3, 4, 5]
forbidden: {1, 3}
target: 7

Step-by-step:

1. Initialize pointers
left = 0, right = 4

2. Check sum
arr[left] + arr[right] = 1 + 5 = 6
6 < 7 → move left pointer

3. Move left pointer
left = 1 (forbidden, skip)
left = 2

4. Check sum
arr[left] + arr[right] = 3 + 5 = 8
8 > 7 → move right pointer

5. Move right pointer
right = 3 (forbidden, skip)
right = 2

6. Check sum
arr[left] + arr[right] = 3 + 4 = 7
7 = 7 → valid pair, but index 3 forbidden

7. Move right pointer
right = 1 (left pointer crossed, stop)

No valid pair found
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [1, 2, 3, 4, 5], target = 7, forbidden = {1, 3}`

| Step | Action     | Pointers                | Array State     | Sum Check          |
| ---- | ---------- | ----------------------- | --------------- | ------------------ |
| 1    | Initialize | left=0, right=4         | [1, 2, 3, 4, 5] | 1+5=6 (move left)  |
| 2    | Move left  | left=1 (skip), left=2   | [1, 2, 3, 4, 5] | 3+5=8 (move right) |
| 3    | Move right | right=3 (skip), right=2 | [1, 2, 3, 4, 5] | 3+4=7 (forbidden)  |
| 4    | Move right | right=1 (stop)          | [1, 2, 3, 4, 5] | -                  |

**Output**: `false`

### ⚠️ Common Mistakes

#### 1. **Not Skipping Forbidden Indices**

```java
// ❌ WRONG - doesn't skip forbidden
if (arr[left] + arr[right] == target) {
    return true;
}

// ✅ CORRECT
if (forbidden.contains(left) || forbidden.contains(right)) {
    // Skip
}
```

#### 2. **Wrong Pointer Movement**

```java
// ❌ WRONG - moves both pointers
if (sum < target) {
    left++;
    right--;
}

// ✅ CORRECT
if (sum < target) {
    left++;
} else {
    right--;
}
```

#### 3. **Not Handling Edge Cases**

```java
// ❌ WRONG - doesn't handle empty array
if (arr.length == 0) {
    return false;
}

// ✅ CORRECT
if (arr.length == 0 || arr.length == 1) {
    return false;
}
```

#### 4. **Using Nested Loops**

```java
// ❌ WRONG - O(n²) complexity
for (int i = 0; i < arr.length; i++) {
    for (int j = i + 1; j < arr.length; j++) {
        if (arr[i] + arr[j] == target) {
            return true;
        }
    }
}

// ✅ CORRECT
int left = 0, right = arr.length - 1;
while (left < right) {
    // Two-pointer approach
}
```

### 💻 Implementations

### Java

```java
class Solution {
    public boolean pairSumWithForbidden(int[] arr, int target, Set<Integer> forbidden) {
        int left = 0, right = arr.length - 1;

        while (left < right) {
            // Skip forbidden indices
            if (forbidden.contains(left)) {
                left++;
                continue;
            }
            if (forbidden.contains(right)) {
                right--;
                continue;
            }

            int sum = arr[left] + arr[right];
            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return false;
    }
}

// Time: O(n), Space: O(1)
```

### Python

```python
def pair_sum_with_forbidden(arr, target, forbidden):
    """
    Find if there exists a pair of elements that sum to target, avoiding forbidden indices.

    Args:
        arr: List of integers (sorted)
        target: Target sum
        forbidden: Set of forbidden indices

    Returns:
        True if valid pair exists, False otherwise
    """
    left, right = 0, len(arr) - 1

    while left < right:
        if left in forbidden:
            left += 1
            continue
        if right in forbidden:
            right -= 1
            continue

        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

# Time: O(n), Space: O(1)
```

### C++++

```cpp
class Solution {
public:
    bool pairSumWithForbidden(vector<int>& arr, int target, unordered_set<int>& forbidden) {
        int left = 0, right = arr.size() - 1;

        while (left < right) {
            if (forbidden.find(left) != forbidden.end()) {
                left++;
                continue;
            }
            if (forbidden.find(right) != forbidden.end()) {
                right--;
                continue;
            }

            int sum = arr[left] + arr[right];
            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return false;
    }
};

// Time: O(n), Space: O(1)
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @param {number[]} forbidden
 * @return {boolean}
 */
var pairSumWithForbidden = function(arr, target, forbidden) {
    const forbiddenSet = new Set(forbidden);
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        if (forbiddenSet.has(left)) {
            left++;
            continue;
        }
        if (forbiddenSet.has(right)) {
            right--;
            continue;
        }

        const sum = arr[left] + arr[right];
        if (sum === target) {
            return true;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return false;
};

// Time: O(n), Space: O(1)
```

### 📊 Comparison Table

| **Aspect**           | **Naive (Nested Loops)** | **Optimal (Two Pointers)** |
| -------------------- | ------------------------ | -------------------------- |
| **Algorithm**        | Check all pairs          | Two-pointer approach       |
| **Time Complexity**  | O(n²)                    | O(n) ⭐                    |
| **Space Complexity** | O(1)                     | O(1)                       |
| **Efficiency**       | Poor                     | Excellent ⭐               |
| **Best for**         | Small arrays             | Large arrays ⭐            |


