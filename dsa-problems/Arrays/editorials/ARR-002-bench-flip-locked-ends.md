---
problem_id: ARR_BENCH_FLIP_LOCKED__1397
display_id: ARR-002
slug: bench-flip-locked-ends
title: "Bench Flip With Locked Ends"
difficulty: Easy
difficulty_score: 20
topics:
  - Arrays
  - Two Pointers
  - In-place
tags:
  - arrays
  - two-pointers
  - in-place
  - easy
premium: true
subscription_tier: basic
---

# ARR-002: Bench Flip With Locked Ends

## 📋 Problem Summary

Reverse the elements of an array *in-place*, but keep the first and last elements fixed. Only the subarray from index `1` to `n-2` is reversed.

## 🌍 Real-World Scenario

**Scenario Title:** The VIP Seating Arrangement

Imagine a long banquet table with prestigious guests.
- At the **head** (left end) sits the Host.
- At the **foot** (right end) sits the Guest of Honor.
- In the **middle** are all the other attendees.

For a special toast, the photographer asks everyone in the middle to "reverse their order" so the people near the Host are now near the Guest of Honor, and vice versa. However, the Host and Guest of Honor must **stay in their seats** to frame the picture.

If you were the event coordinator, you'd need to swap the middle guests efficiently without disturbing the VIPs at the ends!

**Why This Problem Matters:**

- **Array Manipulation**: Mastering sub-segment manipulation is crucial for more complex algorithms (like "Rotate Array" or "Next Permutation").
- **In-Place Operations**: Learning to modify data without using extra memory is a key optimization skill.
- **Pointer Management**: Handling boundary conditions (start/end) carefully is a daily task in systems programming.

![Real-World Application](../images/ARR-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Swap Process
```
Index:    0     1     2     3     4
Value:   [9]   [3]   [8]   [1]   [5]
          ^     ^           ^     ^
        Locked  |           |   Locked
                L           R
               (Swap 3 & 1)
               
Result:  [9]   [1]   [8]   [3]   [5]
          ^           ^           ^
        Locked      Done        Locked
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input Indices**: The task affects indices `1` to `n-2` inclusive.
- **Small Arrays**: If `n < 3`, there is no "middle" to reverse. The array should remain unchanged.
- **In-Place**: You should ideally modify the input array directly, not create a new one (though strictness depends on language).

Common interpretation mistake:

- ❌ Reversing the *entire* array (swapping index 0 and n-1).
- ✅ Keeping indices `0` and `n-1` UNTOUCHED and reversing the rest.

### Core Concept: Two Pointers

We use two pointers, `left` starting at 1 and `right` starting at `n-2`. We swap elements at these pointers and move them towards each other until they meet.

### Why Naive Approach is Less Efficient

A "Naive" approach might copy the middle elements to a temporary array, reverse that temporary array, and copy them back. While this works, it uses **O(N)** extra space, which is unnecessary.

## Naive Approach (Extra Space)

### Intuition

Extract the middle part, reverse it in a separate list, and put it back.

### Algorithm

1. If `n < 3`, return.
2. Create a temporary list containing elements `arr[1...n-2]`.
3. Reverse the temporary list.
4. Overwrite `arr[1...n-2]` with values from the reversed list.

### Time Complexity

- **O(N)**: We iterate through the middle elements twice (copy out, copy in).

### Space Complexity

- **O(N)**: We store the middle segment, taking memory proportional to the input size.

### Why This Works

It correctly reverses the values conceptually.

### Limitations

- **Memory Usage**: For very large arrays (e.g., restricted embedded systems), allocating O(N) memory might be disallowed.

## Optimal Approach (In-Place Two Pointers)

### Key Insight

We can reverse the segment by swapping elements pairs from the outside in.
`arr[1]` swaps with `arr[n-2]`
`arr[2]` swaps with `arr[n-3]`
...and so on.

### Algorithm

1. Handle edge case: if `n < 3`, return immediately.
2. Initialize `left = 1`.
3. Initialize `right = n - 2`.
4. While `left < right`:
   a. Swap `arr[left]` and `arr[right]`.
   b. Increment `left`.
   c. Decrement `right`.

### Time Complexity

- **O(N)**: We touch each element in the middle segment once. Specifically, we perform `(N-2)/2` swaps.

### Space Complexity

- **O(1)**: We only use two integer variables (`left`, `right`) regardless of array size.

### Why This Is Optimal

You must visit at least half the elements to swap them, so O(N) time is lower-bound. O(1) space is the theoretical minimum.

![Algorithm Visualization](../images/ARR-002/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-002/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[9, 3, 8, 1, 5]` (`n=5`)

**Setup**:
- `left` starts at 1 (value 3)
- `right` starts at 3 (value 1)

**Iteration 1**:
- Condition `left < right` (1 < 3) is true.
- **Swap** `arr[1]` and `arr[3]`.
  - Array becomes: `[9, 1, 8, 3, 5]`
- `left` becomes 2.
- `right` becomes 2.

**Iteration 2**:
- Condition `left < right` (2 < 2) is **false**.
- Loop terminates.

**Final Result**: `[9, 1, 8, 3, 5]`

![Example Visualization](../images/ARR-002/example-1.png)

## ✅ Proof of Correctness

### Invariant

At any step, the subarray `arr[1...left-1]` has been swapped with `arr[right+1...n-2]`, and the middle section `arr[left...right]` is yet to be reversed.

### Why the approach is correct

The algorithm symmetrically swaps elements from the ends of the target range inward.
- First swap exchanges the outermost elements of the inner segment.
- Subsequent swaps handle the inner layers.
- When `left >= right`, all necessary pairs have been swapped, and the center element (if any) remains in place correctly.

## 💡 Interview Extensions (High-Value Add-ons)

- **Generalization**: "Write a function to reverse a subarray from index `i` to `j`." (A: Pass `i` and `j` as initial pointer values).
- **Linked List**: "How would you do this for a Doubly Linked List?" (A: Similar logic). "Singly Linked List?" (A: Much harder, need to reverse links).

## Common Mistakes to Avoid

1. **Incorrect Bounds**
   - ❌ Starting pointers at `0` and `n-1`.
   - ✅ Read requirements carefully: FIRST and LAST are locked. Start at `1` and `n-2`.

2. **Pointer Crossing**
   - ❌ Using `while left != right`.
   - ✅ Use `while left < right`. If length is even, they will cross but never look equal.

3. **Empty/Small Array**
   - ❌ Forgetting `n=0` or `n=1` cases, leading to IndexOutOfBoundException.
   - ✅ Add check `if n < 3: return`.

## Related Concepts

- **Rotation**: Rotating an array often involves three reversals.
- **Palindrome Check**: Inspecting from ends inward.
