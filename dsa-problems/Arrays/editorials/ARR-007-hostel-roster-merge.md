## Problem 7: Hostel Roster Merge With Gap (ARR-007)

**🏷️ Topic Tags**: `Array`, `Merge`, `Sorted Arrays`, `Gap Requirement`

### 📋 Problem Summary

Merge two sorted arrays into one sorted array, but ensure each element in the second array is placed at least `gap` positions after the corresponding element from the first array.

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

#### Java

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

#### Python

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

#### C++

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

### 📊 Comparison Table

| **Aspect**           | **Naive (Merge then Shift)** | **Optimal (Gap-Aware Merge)** |
| -------------------- | ---------------------------- | ----------------------------- |
| **Algorithm**        | Merge normally, insert gaps  | Merge with gap tracking       |
| **Time Complexity**  | O((n+m)²)                    | O(n+m) ⭐                     |
| **Space Complexity** | O(n+m)                       | O(n+m)                        |
| **Passes**           | 2 (merge + insert)           | 1 (single merge)              |
| **Gap handling**     | Post-processing              | During merge                  |
| **Best for**         | Small arrays                 | Large arrays ⭐               |

### 🎯 Quiz Questions

#### Q1: Gap Definition

For `gap=2`, element B[i] must be at least how many positions after A[i]?

- A) 1 position
- B) 2 positions
- C) 3 positions
- D) Depends on values

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) 2 positions**

**Explanation**:

```
gap = 2 means:
A[i] at position p
B[i] must be at position p+2 or later

Example:
A[0] at position 0
B[0] must be at position 2 or later

[A[0], _, B[0], ...]
  0    1   2
       └─┘
      gap=2
```

</details>

#### Q2: All A Before B

If `gap=0`, what does the result look like?

- A) Normal merged sorted array
- B) All A elements before all B elements
- C) Alternating A and B
- D) Undefined

<details>
<summary>💡 Click for Answer</summary>

**Answer: A) Normal merged sorted array**

**Explanation**:

```
gap = 0 means no minimum distance required
Result is standard merge of two sorted arrays

Example:
A = [1, 3]
B = [2, 4]
gap = 0

Result: [1, 2, 3, 4] (standard merge)
```

gap=0 removes the constraint entirely!

</details>

#### Q3: Maximum Result Length

For `A.length=n`, `B.length=m`, `gap=g`, what's the maximum result length?

- A) n + m
- B) n + m + g
- C) n + m + m×g
- D) n + m + n×g

<details>
<summary>💡 Click for Answer</summary>

**Answer: C) n + m + m×g (worst case)**

**Explanation**:
Worst case: Each B element needs maximum gap from last A

```
Example: A = [1], B = [2, 3], gap = 2

Result could be:
[1, _, 2, _, _, 3, ...]
     └─┘     └──┘
     gap=2   gap from last A position

Length = 1 (A) + 2 (B) + 2×2 (gaps) = 7
```

In practice, often much smaller!

</details>

#### Q4: Empty Array A

If A is empty, what happens?

- A) Error
- B) Return B as-is
- C) Gap constraint doesn't apply
- D) B and C

<details>
<summary>💡 Click for Answer</summary>

**Answer: D) B and C**

**Explanation**:

```
A = []
B = [1, 2, 3]
gap = 5

Since no A elements exist:
- No "last A position" to track
- Gap constraint is meaningless
- Simply return B

Result: [1, 2, 3]
```

Gap constraint requires A elements to measure from!

</details>

#### Q5: Maintaining Sort Order

Which takes priority: sort order or gap constraint?

- A) Sort order always
- B) Gap constraint always
- C) Depends on problem statement
- D) Both must be satisfied

<details>
<summary>💡 Click for Answer</summary>

**Answer: C) Depends on problem statement**

**Explanation**:
Two common variations:

**Variation 1: Gap is hard constraint**

```
Maintain gap even if it breaks sort order
Result might not be fully sorted
```

**Variation 2: Sort order is hard constraint**

```
Maintain sort order, add "spacers" to satisfy gap
Result is sorted but may have gaps/placeholders
```

**Key**: Always read problem carefully! 📖

</details>

#### Q6: Optimal Data Structure

What's the best way to store the result during construction?

- A) Array (fixed size)
- B) ArrayList/List (dynamic)
- C) LinkedList
- D) Queue

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) ArrayList/List (dynamic)**

**Explanation**:

- Don't know final size in advance (depends on gaps needed)
- Need random access for reading
- Need efficient append operation

```java
List<Integer> result = new ArrayList<>();  // ✓
// Can grow dynamically
// O(1) amortized append
// O(1) random access
```

LinkedList would be O(n) for position tracking! ✗

</details>

#### Q7: Time Complexity Proof

Why is the optimal approach O(n+m)?

- A) We use sorting
- B) Single pass through both arrays
- C) Binary search optimization
- D) Divide and conquer

<details>
<summary>💡 Click for Answer</summary>

**Answer: B) Single pass through both arrays**

**Explanation**:

```
while (iA < n && iB < m) {  // At most n+m iterations
    // O(1) work per iteration
    // Either iA++ or iB++ each time
}

Total iterations ≤ n + m
Each iteration: O(1)
Total: O(n + m)
```

**Key insight**: Each element processed exactly once! ✓

</details>

#### Q8: Real-World Gap

In network packet transmission, why enforce minimum gap?

- A) To slow down transmission
- B) To prevent buffer overflow
- C) To ensure receiver can process
- D) B and C

<details>
<summary>💡 Click for Answer</summary>

**Answer: D) B and C**

**Explanation**:
**Minimum Inter-Packet Gap (IPG)**:

```
Packet stream:
[PKT1] -- gap -- [PKT2] -- gap -- [PKT3]

Gap ensures:
1. Receiver has time to process PKT1 before PKT2 arrives
2. Network buffers don't overflow
3. Fair bandwidth sharing

Without gap:
[PKT1][PKT2][PKT3]... → Buffer overflow! ✗
```

Similar to our problem:

- A elements = high-priority packets
- B elements = regular packets
- Gap = minimum processing time

This is a real systems programming constraint! 🌐

</details>

---
