---
problem_id: ARR_ZERO_COMPRESS__1105
display_id: ARR-005
slug: zero-compression
title: "Zero Compression"
difficulty: Easy
difficulty_score: 25
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - compression
  - data-structures
  - searching
  - state-machine
  - technical-interview-prep
  - two-pointers
  - zero-handling
premium: false
subscription_tier: basic
---

# ARR-005: Zero Compression

## 📋 Problem Summary

This problem asks you to perform a specific type of data compression on an array.

**The Algorithm:**

1. Identify all **Zero Blocks**. A zero block is a continuous sequence of one or more zeros.
2. Remove all existing zeros from the array while preserving the order of the non-zero numbers.
3. For every original zero block, append exactly **one zero** to the end of the array.

**Key Distinction:** This is _not_ just "Move Zeros to the End." In standard zero-moving, an array like `[1, 0, 0, 2]` becomes `[1, 2, 0, 0]`. In **Zero Compression**, it becomes `[1, 2, 0]` because the `0, 0` block is compressed into a single `0`.

## 🌍 Real-World Scenarios

**Scenario 1: 📡 Sparse Signal Transmission (Run-Length Encoding)**
In digital communication, a series of zeros often represents "silence" or "no change." Transmitting every single zero is a waste of bandwidth. Instead, the transmitter compresses blocks of silence into a single "Silence Marker" (Zero) and moves them to the end of the data packet for synchronization. This is a simplified version of **Run-Length Encoding (RLE)**.

**Scenario 2: 🛒 Inventory "Stock-Out" Batching**
A warehouse log tracks items on a shelf. A `0` represents an empty slot. When generating a report for a picker, the manager doesn't need to know _how many_ adjacent slots are empty; they just need to know _where_ there is a gap. Compressing these empty gaps into a single marker at the bottom of the list makes the picking path clearer and highlights the "Stock-Out" zones.

**Scenario 3: 🧹 Garbage Collection and Memory Defragmentation**
In computer memory, "zeros" can represent unallocated or freed blocks. A defragmenter moves all the useful data to the front (preserving order). Instead of tracking every individual empty byte, the OS might consolidate contiguous free blocks into a single "Free Space Descriptor" to simplify the memory map.

**Scenario 4: 📝 Text Processing (Whitespace Normalization)**
In some data formats, sequences of spaces or null characters (zeros) carry the same meaning regardless of length. "Hello [0][0][0] World" is the same as "Hello [0] World." Compressing these sequences helps in standardizing inputs for database storage.

**Scenario 5: 🎭 Video Frame Difference Compression**
In video compression, a `0` represents "No Change" from the previous frame. If a stationary object occupies 100 pixels, it generates 100 zeros. A simple compression algorithm consolidates these "No Change" regions into markers to reduce file size.

### Real-World Relevance

Zero Compression is about **Information Density**. When a repetitive value doesn't provide additional meaning beyond "this state exists," we compress it to save space and focus on the high-value (non-zero) data points.

## 🚀 Detailed Explanation

### 1. The "State" Transition Logic

To solve this in one pass, you need to track whether you are currently "inside" a zero block or "outside" one.

Imagine you are a traveler walking through the array:

- If you see a non-zero number, you keep it immediately. You are now "Outside" a zero block.
- If you see a zero:
  - If you were already in a zero block, you ignore it.
  - If you were _not_ in a zero block, you note that a new block has started. You increment your "Block Count." You are now "Inside" a zero block.

### 2. The Step-by-Step Procedure

1. Create a container (like a new array or a dynamic list) to store the results.
2. Maintain a counter for `zero_blocks`.
3. Iterate through input `A`:
   - If `A[i] != 0`:
     - Add `A[i]` to the result list.
   - If `A[i] == 0`:
     - If `(i == 0 || A[i-1] != 0)`:
       - This is the start of a new block. `zero_blocks++`.
4. Finally, append `zero_blocks` number of zeros to the result list.

### 3. Complexity Optimization

Because we need to preserve order, we can't easily do this in-place without a lot of swapping. Using a temporary result array is $O(N)$ and much cleaner to implement correctly.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Init[ResultList = []<br>blockCount = 0<br>isInsideBlock = False]
    Init --> Loop{For each x in Array}

    Loop -- x != 0 --> AddNonZero[Add x to ResultList<br>isInsideBlock = False]
    Loop -- x == 0 --> CheckBlock{isInsideBlock == True?}

    CheckBlock -- No --> NewBlock[blockCount++<br>isInsideBlock = True]
    CheckBlock -- Yes --> Skip[Ignore this zero]

    AddNonZero --> Loop
    NewBlock --> Loop
    Skip --> Loop

    Loop -- Done --> AppendZeros[Add 'blockCount' zeros to ResultList]
    AppendZeros --> End([Return ResultList])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N)$

- We iterate through the array once to extract non-zeros and count blocks.
- We perform a simple append operation for the compressed zeros at the end.
- Total Complexity: $O(N)$. For $N=200,000$, this is extremely fast.

### Space Complexity: $O(N)$

- In the worst case (no zeros), the result array is size $N$.
- In the best case (all zeros), the result is size 1.
- Average: $O(N)$ for the output storage.

## 🧪 Edge Cases & Testing

### 1. No Zeros at All

- **Input:** `[1, 2, 3]`
- **Logic:** `blockCount = 0`. No zeros appended.
- **Output:** Length 3, `[1, 2, 3]`.

### 2. All Elements are Zeros

- **Input:** `[0, 0, 0, 0]`
- **Logic:** One massive block. `blockCount = 1`.
- **Output:** Length 1, `[0]`.

### 3. Interleaved Zeros (Standard Case)

- **Input:** `[1, 0, 2, 0, 3]`
- **Output:** `[1, 2, 3, 0, 0]`.

### 4. Zeros at Boundaries

- **Input:** `[0, 0, 1, 2, 0]`
- **Logic:** Block at start, block at end.
- **Output:** `[1, 2, 0, 0]`.

### 5. Large Values

- **Input:** `-10^9, 10^9`.
- **Logic:** Handled normally; non-zero check is robust.

### 6. Single Element

- **Input:** `[0]` $\rightarrow$ `[0]`.
- **Input:** `[5]` $\rightarrow$ `[5]`.

## ⚠️ Common Pitfalls & Debugging

**1. The "Every Zero" Bug**

- **Pitfall:** Appending a zero whenever you see one.
- **Correction:** You must only count the _start_ of a zero sequence. Check if the previous element was non-zero (or if this is the first element).

**2. Preservation of Order**

- **Pitfall:** Sorting the array to group zeros.
- **Correction:** Sorting is $O(N \log N)$ and **destroys** the relative order of non-zero elements (e.g., `[2, 1]` might become `[1, 2]`). The problem strictly requires preserving order.

**3. Output Length**

- **Pitfall:** Returning an array of size $N$ with the end padded with extra junk or missing zeros.
- **Correction:** The problem asks for the _compressed_ length $m$. Ensure your output matches exactly the number of non-zeros + the number of blocks.

**4. 1-Based vs 0-Based**

- If implementing the "Previous Element check," ensure you don't check `a[-1]` when `i=0`.

## 🎯 Variations & Extensions

### Variation 1: Compress Any Value $X$

Instead of zeros, compress blocks of any arbitrary value $X$.

### Variation 2: Max Compression Limit

A block of zeros is compressed to at most $M$ zeros.
_Example: If $M=2$, `[0, 0, 0, 0]` becomes `[0, 0]`._

### Variation 3: Non-Contiguous Compression

If _any_ zeros exist, replace all of them with a single zero at the end.

### Variation 4: Two-Way Compression

Compress zeros and also compress consecutive identical non-zero numbers.
_Example: `[1, 1, 0, 0, 2, 2]` becomes `[1, 0, 2]`._

### Variation 5: Circular Consistency

If the array starts and ends with zeros, do they count as one single block? (Usually no, unless specified).

## 🎓 Key Takeaways

1. **Block vs Element:** This problem shifts the focus from individual elements to groups of identical, adjacent elements.
2. **State Tracking:** Using a flag like `isInsideBlock` simplifies the logic for sequential scanning.
3. **Difference from Standard:** Be careful not to assume a problem is a "classic" like LeetCode Move Zeros; always read the specific compression rule.
4. **Ordering:** When order must be preserved, use a linear $O(N)$ scan—avoid sorting.

## 📚 Related Problems

- **Move Zeros (LeetCode 283):** The naive version of this problem.
- **Remove Duplicates from Sorted Array:** A variation where $X$ is any duplicate.
- **String Compression:** Compressing characters into `char + count`.
- **Group Anagrams:** Using buckets for non-sequential grouping.
- **ARR-008:** Distinct Until Repeat (Eliminating adjacent non-zero duplicates).
