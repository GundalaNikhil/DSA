---
problem_id: ARR_MERGE_PRIOR__3B97
display_id: ARR-007
slug: hostel-roster-merge
title: "Hostel Roster Merge With Priority"
difficulty: Medium
difficulty_score: 50
topics:
  - Array
  - Merge
  - Sorted Arrays
  - Priority Merge
tags:
  - arrays
  - merge
  - sorting
  - medium
premium: true
subscription_tier: basic
---

# Hostel Roster Merge With Priority

![Problem Header](../images/ARR-007/header.png)

### 📋 Problem Summary

Merge two sorted arrays `A` and `B` into a single sorted array. When two elements are equal (one from A, one from B), place the element from A first.

### 🌍 Real-World Scenario

**Hostel Roster Merging**

Two sorted lists of student roll numbers need to be merged:

- List A: Current residents (they maintain their relative order)
- List B: New students (also maintain their relative order)
- **Rule**: When merging, if a student number appears in both lists, current residents get priority (appear first)

Example:

```
A = [1, 3, 3]
B = [3, 4]

Merge with A-priority:
[1, 3 (from A), 3 (from A), 3 (from B), 4]

Result: [1, 3, 3, 3, 4]
```

**Applications**:

- Merging two sorted lists while preserving source priority
- Stable merge operation in databases
- Priority-based data consolidation in distributed systems

### 📚 Detailed Explanation

**What Makes This Straightforward?**

- Standard two-pointer merge technique
- **With tie-breaker**: When values are equal, pick from A first
- No additional constraints or spacing requirements
- Straightforward two-pointer approach

**Key Insight**:

- Process both arrays with two pointers
- Compare current elements from A and B
- When equal, take from A first, then B
- Move the pointer of whichever array was picked from

### ✅ Optimal Approach: Two-Pointer Merge

**Algorithm**:

```
1. Create result array of size n + m
2. Initialize pointers: iA = 0, iB = 0, result_idx = 0
3. While both pointers are valid:
   - If A[iA] < B[iB]: add A[iA], move iA
   - Else if A[iA] > B[iB]: add B[iB], move iB
   - Else (A[iA] == B[iB]): add A[iA] first, then B[iB], move both
4. Copy remaining elements from A or B
5. Return result
```

**⏱️ Time Complexity: O(n + m)**

```
Single pass through both arrays: O(n + m)
```

**📦 Space Complexity: O(n + m)**

- Result array of size n + m

**Key Points**:
- Compare current elements
- When equal, take from A first (preserves A-priority)
- Standard merge with tie-breaker logic

### 🎨 Visual Representation

**Example**: `A = [1, 3, 3]`, `B = [3, 4]`

```
Step-by-step merge with A-priority:

Initial:
A: [1, 3, 3]    (iA=0)
B: [3, 4]       (iB=0)
Result: []

Step 1: Compare A[0]=1 vs B[0]=3
1 < 3 → Add A[0]=1
Result: [1]
iA=1, iB=0

Step 2: Compare A[1]=3 vs B[0]=3
3 == 3 → Add A first, then B
Result: [1, 3, 3]
iA=2, iB=1

Step 3: Compare A[2]=3 vs B[1]=4
3 < 4 → Add A[2]=3
Result: [1, 3, 3, 3]
iA=3, iB=1
(iA reached end, copy remaining from B)

Step 4: Copy remaining from B
Add B[1]=4
Result: [1, 3, 3, 3, 4]
Final: [1, 3, 3, 3, 4]
```
- Current position would be 4
- 4 - 3 = 1 < 2 (not enough!)
- Need position 3+2=5

Result: [1, _, 2, 4, _, 5]
                      ↑
                   B[1] at pos=5
```

### 🧪 Test Case Walkthrough

**Input**: `A = [1, 3], B = [2, 4], gap = 1`

| Step | Action     | Current Pos | Array State    | Gap Check         |
| ---- | ---------- | ----------- | -------------- | ----------------- |
| 1    | Add A[0]=1 | 0           | `[1]`          | lastA=0           |
| 2    | Add B[0]=2 | 1           | `[1, 2]`       | 1-0=1 ✓ (gap met) |
| 3    | Add A[1]=3 | 2           | `[1, 2, 3]`    | lastA=2           |
| 4    | Add B[1]=4 | 3           | `[1, 2, 3, 4]` | 3-2=1 ✓           |

**Output**: `[1, 2, 3, 4]`

### ⚠️ Common Mistakes

#### 1. **Not Tracking Last A Position**

```java
// ❌ WRONG - forgets to track
for (int b : B) {
    result.add(b);  // Where's the gap check?
}

// ✅ CORRECT
int lastAPos = -gap;  // Initialize far enough back
for each A element at position p:
    lastAPos = p;
for each B element:
    ensure currentPos - lastAPos >= gap
```

#### 2. **Wrong Gap Calculation**

```java
// ❌ WRONG - off by one
if (currentPos - lastAPos > gap)  // Should be >=

// ✅ CORRECT
if (currentPos - lastAPos >= gap)
```

#### 3. **Not Handling Remaining Elements**

```java
// ❌ WRONG - forgets remaining B elements
while (iA < A.length) {
    add A[iA++];
}
// Forgot B!

// ✅ CORRECT
while (iA < A.length) add A[iA++];
while (iB < B.length) add B[iB++];  // Don't forget!
```

#### 4. **Insufficient Result Array Size**

```java
// ❌ WRONG - not enough space
int[] result = new int[A.length + B.length];

// ✅ CORRECT - account for gaps
int[] result = new int[A.length + B.length + B.length * gap];
```

#### 5. **Not Maintaining Sort Order**

```java
// ❌ WRONG - adds B without checking if A[iA] should come first
add B[iB++];

// ✅ CORRECT - compare values
if (A[iA] < B[iB] || !gapSatisfied) {
    add A[iA++];
} else {
    add B[iB++];
}
```

### 💻 Implementations

### Java

```java
class Solution {
    public List<Integer> mergeWithGap(int[] A, int[] B, int gap) {
        List<Integer> result = new ArrayList<>();
        int iA = 0, iB = 0;
        int lastAPos = -gap - 1;  // Initialize so first B can be added immediately if needed

        while (iA < A.length && iB < B.length) {
            int currentPos = result.size();

            // Check if we can add from B (gap constraint)
            boolean canAddB = (currentPos - lastAPos >= gap);

            if (A[iA] <= B[iB]) {
                // Add from A
                result.add(A[iA++]);
                lastAPos = currentPos;
            } else if (canAddB) {
                // Add from B (gap satisfied and B[iB] < A[iA])
                result.add(B[iB++]);
            } else {
                // Need gap, but can't add B yet - add spacer or wait
                // For now, add from A to maintain progress
                result.add(A[iA++]);
                lastAPos = currentPos;
            }
        }

        // Add remaining A elements
        while (iA < A.length) {
            result.add(A[iA++]);
            lastAPos = result.size() - 1;
        }

        // Add remaining B elements (with gap constraint)
        while (iB < B.length) {
            int currentPos = result.size();
            if (currentPos - lastAPos >= gap) {
                result.add(B[iB++]);
            } else {
                // Add filler (or skip based on problem variation)
                result.add(Integer.MAX_VALUE);  // Placeholder
            }
        }

        return result;
    }
}

// Time: O(n+m), Space: O(n+m)
```

### Python

```python
def merge_with_gap(A, B, gap):
    """
    Merge two sorted arrays with minimum gap constraint between A and B elements.

    Args:
        A: First sorted array (priority)
        B: Second sorted array (must maintain gap)
        gap: Minimum positions between corresponding elements

    Returns:
        Merged list with gap constraint satisfied
    """
    result = []
    iA, iB = 0, 0
    last_a_pos = -gap - 1

    while iA < len(A) and iB < len(B):
        current_pos = len(result)
        can_add_b = (current_pos - last_a_pos >= gap)

        if A[iA] <= B[iB]:
            result.append(A[iA])
            last_a_pos = current_pos
            iA += 1
        elif can_add_b:
            result.append(B[iB])
            iB += 1
        else:
            result.append(A[iA])
            last_a_pos = current_pos
            iA += 1

    # Add remaining A
    while iA < len(A):
        result.append(A[iA])
        last_a_pos = len(result) - 1
        iA += 1

    # Add remaining B
    while iB < len(B):
        current_pos = len(result)
        if current_pos - last_a_pos >= gap:
            result.append(B[iB])
            iB += 1
        else:
            result.append(float('inf'))  # Placeholder

    return result

# Time: O(n+m), Space: O(n+m)
```

### C++++

```cpp
class Solution {
public:
    vector<int> mergeWithGap(vector<int>& A, vector<int>& B, int gap) {
        vector<int> result;
        int iA = 0, iB = 0;
        int lastAPos = -gap - 1;

        while (iA < A.size() && iB < B.size()) {
            int currentPos = result.size();
            bool canAddB = (currentPos - lastAPos >= gap);

            if (A[iA] <= B[iB]) {
                result.push_back(A[iA++]);
                lastAPos = currentPos;
            } else if (canAddB) {
                result.push_back(B[iB++]);
            } else {
                result.push_back(A[iA++]);
                lastAPos = currentPos;
            }
        }

        // Add remaining A
        while (iA < A.size()) {
            result.push_back(A[iA++]);
            lastAPos = result.size() - 1;
        }

        // Add remaining B
        while (iB < B.size()) {
            int currentPos = result.size();
            if (currentPos - lastAPos >= gap) {
                result.push_back(B[iB++]);
            } else {
                result.push_back(INT_MAX);  // Placeholder
            }
        }

        return result;
    }
};

// Time: O(n+m), Space: O(n+m)
```

### JavaScript

```javascript
/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number} gap
 * @return {number[]}
 */
var mergeWithGap = function(A, B, gap) {
    const result = [];
    let iA = 0, iB = 0;
    let lastAPos = -gap - 1;

    while (iA < A.length && iB < B.length) {
        const currentPos = result.length;
        const canAddB = (currentPos - lastAPos >= gap);

        if (A[iA] <= B[iB]) {
            result.push(A[iA++]);
            lastAPos = currentPos;
        } else if (canAddB) {
            result.push(B[iB++]);
        } else {
            result.push(A[iA++]);
            lastAPos = currentPos;
        }
    }

    while (iA < A.length) {
        result.push(A[iA++]);
        lastAPos = result.length - 1;
    }

    while (iB < B.length) {
        const currentPos = result.length;
        if (currentPos - lastAPos >= gap) {
            result.push(B[iB++]);
        } else {
            result.push(Infinity); // Placeholder
        }
    }

    return result;
};

// Time: O(n+m), Space: O(n+m)
```

### 📊 Comparison Table

| **Aspect**           | **Naive (Merge then Shift)** | **Optimal (Gap-Aware Merge)** |
| -------------------- | ---------------------------- | ----------------------------- |
| **Algorithm**        | Merge normally, insert gaps  | Merge with gap tracking       |
| **Time Complexity**  | O((n+m)²)                    | O(n+m) ⭐                     |
| **Space Complexity** | O(n+m)                       | O(n+m)                        |
| **Passes**           | 2 (merge + insert)           | 1 (single merge)              |
| **Gap handling**     | Post-processing              | During merge                  |
| **Best for**         | Small arrays                 | Large arrays ⭐               |
