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

Merge two sorted arrays into one sorted array, with a priority rule: when elements are equal, elements from the first array should appear before elements from the second array.

### 🌍 Real-World Scenario

**University Hostel Room Assignment**

Two sorted lists of students by roll number:

- List A: Current residents (priority)
- List B: New applicants (must maintain distance)
- **Gap rule**: Each new student must be assigned at least `gap` rooms after the corresponding current resident

Example:

```
A = [1, 3, 5]
B = [2, 4, 6]
gap = 2

Merge with gap constraint:
[1, _, _, 2, 3, _, 4, 5, _, 6]
 ↑        ↑           ↑
 A[0]     B[0]       B[2]
         (gap=2)
```

**Applications**:

- Social distancing in seating arrangements
- Network packet spacing (minimum inter-packet gap)
- Manufacturing: minimum spacing between products on conveyor

### 📚 Detailed Explanation

**What Makes This Complex?**

- Normal merge: simply interleave based on values
- **With gap constraint**: Must respect minimum distance
- Balance between maintaining sort order AND gap requirement

**Key Insight**:

- Process both arrays using two pointers
- When adding from array B, ensure gap positions have passed since corresponding A element
- May need to add "spacers" or skip positions

### ❌ Naive Approach

**Algorithm**:

```
1. Merge normally without gap
2. Post-process to insert gaps
3. Shift elements as needed
```

**⏱️ Time Complexity: O(n²)**

- Initial merge: O(n)
- Inserting gaps requires shifting: O(n²) worst case

**📦 Space Complexity: O(n)**

- Result array

### ✅ Optimal Approach

**Algorithm**:

```
1. Use result array large enough to accommodate gaps
2. Two pointers for A and B
3. Track "last position from A" to enforce gap
4. Add from A or B based on:
   - Sort order
   - Gap constraint satisfaction
```

**⏱️ Time Complexity: O(n + m)**

```
Single pass through both arrays: O(n + m)
```

**📦 Space Complexity: O(n + m + gaps)**

- Result array with space for gaps

### 🎨 Visual Representation

**Example**: `A = [1, 4], B = [2, 5], gap = 2`

```
Step-by-step merge:

Initial:
A: [1, 4]    (pointers: iA=0)
B: [2, 5]    (pointers: iB=0)
Result: []

Step 1: Add A[0]=1
Result: [1]
         ↑
    lastA position = 0

Step 2: Try to add B[0]=2
- Need gap=2 from lastA=0
- Current position would be 1
- 1 - 0 = 1 < 2 (gap not satisfied!)
- Add filler or skip

Result: [1, _, 2]
         ↑     ↑
        lastA  B[0]
       pos=0  pos=2 (gap=2 satisfied!)

Step 3: Add A[1]=4
Result: [1, _, 2, 4]
                  ↑
             lastA pos=3

Step 4: Add B[1]=5
- Need gap=2 from lastA=3
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
