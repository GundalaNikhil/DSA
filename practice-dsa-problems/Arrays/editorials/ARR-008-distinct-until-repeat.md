---
problem_id: ARR_DISTINCT_REP__8291
display_id: ARR-008
slug: distinct-until-repeat
title: "Distinct Until Repeat"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - prefix
  - searching
  - set
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-008: Distinct Until Repeat

## 📋 Problem Summary

Given an array of integers, determine the length of the longest prefix where all elements are unique (no duplicates). Process the array from left to right and stop **before** encountering the first repeated element.

**Key Points:**

- Start from index 0
- Continue while all elements seen so far are distinct
- Return the count of unique elements before the first duplicate
- If no duplicates exist, return the entire array length

**Examples:**

```
[1, 2, 3, 4, 2] → 4 (stop before second occurrence of 2)
[5, 5, 5] → 1 (stop before second occurrence of 5)
[1, 2, 3] → 3 (all unique)
```

## 🌍 Real-World Scenarios

**Scenario 1:** 🛡️ **Session ID Uniqueness Verification**

A server generates session IDs sequentially. To guarantee uniqueness, you monitor the stream: `ID_001`, `ID_002`, `ID_003`, ..., `ID_002`. The moment you see a collision (duplicate), the system must halt and report how many valid unique IDs were generated before the collision.

**Scenario 2:** 📦 **Package Tracking Validation**

A shipping facility scans package barcodes as they move down a conveyor belt. Each package should have a unique barcode. Count how many packages pass through successfully before a duplicate barcode is detected, indicating an error in the system.

**Scenario 3:** 🎮 **Unique Card Draw in Games**

In a card game, players draw cards from a deck. Cards should be unique until the deck reshuffles. Track how many unique cards are drawn before getting a repeat, which would indicate a shuffling error or deck corruption.

**Scenario 4:** 📡 **Network Packet Sequence Number Monitoring**

Network packets have sequence numbers. Normally they're unique in a sliding window. Monitor incoming packets and detect when a sequence number repeats (indicating retransmission or error), tracking how many unique packets arrived first.

**Scenario 5:** 🔐 **Token Generation Collision Detection**

Security tokens (authentication codes) must be unique. A token generator produces tokens one by one. Continuously verify uniqueness and immediately flag the system when the first collision occurs, reporting the count of valid tokens generated.

### Real-World Relevance

- **Data Validation:** Ensuring uniqueness constraints in streams
- **Quality Control:** Detecting production errors in serialization systems
- **Security:** Validating random number generator quality
- **Database Systems:** Checking unique indexes during bulk inserts
- **Stream Processing:** Real-time duplicate detection

## 🚀 Detailed Explanation

### 1. Problem Breakdown

We need to track **seen elements** as we iterate through the array. The moment we encounter an element we've already seen, we stop and return the current count.

**Algorithm Intuition:**

- Maintain a **hash set** of elements seen so far
- For each element:
  - If element exists in set → **STOP**, return current count
  - If element doesn't exist → add to set, continue
- If loop completes → return array length (all unique)

### 2. Hash Set Approach (Optimal)

**Why Hash Set?**

- O(1) average-case lookup: "Have we seen this element?"
- O(1) average-case insertion: "Add this element to seen set"
- Dynamically grows as needed

**Detailed Walkthrough:**

```
Input: arr = [3, 7, 1, 3, 9]

Step 0: Initialize
  seen = {}
  count = 0

Step 1: Process arr[0] = 3
  Is 3 in seen? NO
  Add 3 to seen: {3}
  count = 1

Step 2: Process arr[1] = 7
  Is 7 in seen? NO
  Add 7 to seen: {3, 7}
  count = 2

Step 3: Process arr[2] = 1
  Is 1 in seen? NO
  Add 1 to seen: {3, 7, 1}
  count = 3

Step 4: Process arr[3] = 3
  Is 3 in seen? YES! ← DUPLICATE FOUND
  Stop immediately
  Return count = 3

Result: 3 unique elements before first duplicate
```

**Visual Representation:**

```
Array:   [3,  7,  1,  3,  9]
          ↓   ↓   ↓   ↓
Seen:    {3} {3,7} {3,7,1} STOP!
Count:    1    2     3      3

Element 3 appears again at index 3
We processed 3 unique elements (indices 0, 1, 2)
```

### 3. Alternative: Nested Loop Approach (Naive)

For comparison, here's the O(n²) approach:

```
For i from 0 to n-1:
    For j from 0 to i-1:
        If arr[j] == arr[i]:
            Return i  // Found duplicate at position i
    // No duplicate found yet
Return n  // All unique
```

**Why it's slow:**

- For each element i, scan all previous elements [0...i-1]
- Time: O(1) + O(2) + O(3) + ... + O(n-1) = O(n²)

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Initialize empty HashSet 'seen']
    B --> C[Initialize count = 0]
    C --> D[Loop i from 0 to N-1]
    D --> E{arr[i] in seen?}
    E -- Yes → Duplicate! --> F[Return count]
    E -- No → Unique --> G[Add arr[i] to seen]
    G --> H[count++]
    H --> D
    D -- End Loop --> I[Return count = N]
```


**JavaScript Note:**

- `Set` object for unique value storage
- `has()` method checks membership
- `add()` inserts element

## 🔍 Complexity Analysis

### Time Complexity

**Hash Set Approach: O(N)**

- Single pass through array: N iterations
- Each iteration:
  - Set lookup: O(1) average-case
  - Set insertion: O(1) average-case
- **Total: O(N)** average-case
- **Worst-case: O(N)** for hash collisions (rare with good hash function)

**Naive Approach: O(N²)**

- For each element i, check all previous i-1 elements
- Total comparisons: 0 + 1 + 2 + ... + (N-1) = N(N-1)/2
- **Total: O(N²)**

### Space Complexity

**Hash Set Approach: O(N)**

- Worst case: all N elements are unique
- Set stores all N elements
- **Total: O(N)** auxiliary space

**Naive Approach: O(1)**

- Only uses loop variables
- No additional data structures
- **Total: O(1)** auxiliary space

### Trade-off Analysis

| Approach        | Time  | Space | Notes                                 |
| --------------- | ----- | ----- | ------------------------------------- |
| Hash Set        | O(N)  | O(N)  | Optimal for large arrays              |
| Nested Loop     | O(N²) | O(1)  | Only viable for tiny arrays (N < 100) |
| Boolean Array\* | O(N)  | O(R)  | If value range R is small and known   |

\*Boolean Array: If values are in range [0, R], use `boolean[] seen = new boolean[R+1]`

## 🧪 Edge Cases & Testing

### Edge Case 1: Empty Array

```
Input: arr = []
Output: 0
Explanation: No elements, length is 0
```

### Edge Case 2: Single Element

```
Input: arr = [42]
Output: 1
Explanation: One element is always unique
```

### Edge Case 3: Immediate Duplicate

```
Input: arr = [5, 5, 1, 2]
Output: 1
Explanation: Second element is duplicate, only 1 unique element before it
```

### Edge Case 4: All Duplicates of Same Number

```
Input: arr = [7, 7, 7, 7]
Output: 1
Explanation: Only first occurrence is unique
```

### Edge Case 5: All Unique Elements

```
Input: arr = [1, 2, 3, 4, 5]
Output: 5
Explanation: No duplicates, return full length
```

### Edge Case 6: Duplicate at Last Position

```
Input: arr = [10, 20, 30, 10]
Output: 3
Explanation: Duplicate at index 3, processed 3 unique elements [10, 20, 30]
```

### Edge Case 7: Large Value Range

```
Input: arr = [1000000, -1000000, 0, 1000000]
Output: 3
Explanation: Hash set handles large values efficiently
```

### Edge Case 8: Negative Numbers

```
Input: arr = [-1, -2, -3, -1]
Output: 3
Explanation: Hash set works with negative integers
```

> [!TIP]
> Always test with: empty array, single element, immediate duplicate, all unique, negative numbers, and duplicate at the end.

## ⚠️ Common Pitfalls & Debugging

### Pitfall 1: Off-by-One Error in Return Value

```java
// ❌ Wrong: Returning i+1 instead of i
if (seen.contains(arr[i])) {
    return i + 1;  // Wrong! i already represents the count
}

// ✓ Correct: i is the count of elements BEFORE the duplicate
if (seen.contains(arr[i])) {
    return i;  // Correct!
}
```

**Explanation:**

```
arr = [1, 2, 1]
When i=2, arr[2]=1 is the duplicate
We processed elements at indices 0, 1 (count = 2)
Return 2, not 3!
```

### Pitfall 2: Forgetting to Add Element to Set

```python
# ❌ Wrong: Checking but not adding
if value not in seen:
    # Forgot to add!
    pass

# ✓ Correct: Always add after checking
if value in seen:
    return i
seen.add(value)  # Must add!
```

### Pitfall 3: Using List Instead of Set

```javascript
// ❌ Wrong:Slow O(N) lookup
const seen = [];
if (seen.includes(arr[i])) {
  // O(N) lookup!
  return i;
}
seen.push(arr[i]);

// ✓ Correct: Fast O(1) lookup
const seen = new Set();
if (seen.has(arr[i])) {
  // O(1) lookup!
  return i;
}
seen.add(arr[i]);
```

### Pitfall 4: Not Handling Empty Array

```cpp
// ❌ Wrong: Potential undefined behavior
int distinctUntilRepeat(vector<int>& arr) {
    // No check for empty array
    int first = arr[0];  // Crashes if arr is empty!
    // ...
}

// ✓ Correct: Handle edge case
int distinctUntilRepeat(vector<int>& arr) {
    if (arr.empty()) return 0;
    // ... rest of logic
}
```

## 🎯 Variations & Extensions

### Variation 1: Return the Duplicate Value

Instead of count, return the first duplicate value:

```python
def firstDuplicate(arr):
    seen = set()
    for value in arr:
        if value in seen:
            return value  # Return the duplicate itself
        seen.add(value)
    return -1  # No duplicate found
```

### Variation 2: Return All Unique Elements Before Duplicate

```java
public List<Integer> uniquePrefix(int[] arr) {
    Set<Integer> seen = new HashSet<>();
    List<Integer> result = new ArrayList<>();

    for (int value : arr) {
        if (seen.contains(value)) break;
        seen.add(value);
        result.add(value);
    }
    return result;
}
```

### Variation 3: Count Total Duplicates

Count how many duplicates exist in entire array:

```python
def countDuplicates(arr):
    seen = set()
    duplicates = 0
    for value in arr:
        if value in seen:
            duplicates += 1
        else:
            seen.add(value)
    return duplicates
```

### Variation 4: Find Index of First Duplicate

Return the index where the first duplicate appears:

```java
public int findFirstDuplicate(int[] arr) {
    Set<Integer> seen = new HashSet<>();
    for (int i = 0; i < arr.length; i++) {
        if (seen.contains(arr[i])) {
            return i;  // Index of duplicate
        }
        seen.add(arr[i]);
    }
    return -1;  // No duplicate
}
```

### Variation 5: Case-Insensitive String Uniqueness

For strings, ignore case:

```python
def distinctStringsIgnoreCase(arr):
    seen = set()
    for i, s in enumerate(arr):
        lower = s.lower()
        if lower in seen:
            return i
        seen.add(lower)
    return len(arr)
```

### Variation 6: K-Distance Duplicates

Element is duplicate only if it appears within K indices:

```python
def distinctWithinK(arr, K):
    window = set()
    for i, value in enumerate(arr):
        if value in window:
            return i
        window.add(value)
        if i >= K:
            window.remove(arr[i - K])  # Slide window
    return len(arr)
```

## 🎓 Key Takeaways

1. **Hash sets** provide O(1) average-case membership testing
2. **Space-time tradeoff**: O(N) space for O(N) time vs O(1) space for O(N²) time
3. **Early termination** is key - stop as soon as duplicate is found
4. **Index vs count**: When returning at index i, that's also the count of previous elements
5. **Hash-based structures** (HashSet, unordered_set, Set) are ideal for uniqueness checking

## 📚 Related Problems

- **Contains Duplicate:** Check if array has any duplicates (boolean return)
- **First Unique Character:** Find first non-repeating element
- **Longest Substring Without Repeating Characters:** 2D version with sliding window
- **Remove Duplicates from Sorted Array:** In-place duplicate removal
- **Find All Duplicates in Array:** Identify all duplicate values

## 🔗 Additional Resources

- **Hash Table Fundamentals:** Understanding hash-based data structures
- **Set Theory:** Mathematical foundation of uniqueness
- **Stream Processing:** Handling infinite streams with limited memory
- **Bloom Filters:** Probabilistic uniqueness checking for massive datasets
