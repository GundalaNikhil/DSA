---
problem_id: QUE_CIRCULAR_SHUTTLE_BUFFER_OVERWRITE__7314
display_id: QUE-002
slug: circular-shuttle-buffer-overwrite
title: "Circular Shuttle Buffer with Overwrite"
difficulty: Easy
difficulty_score: 28
topics:
  - Queue
  - Circular Buffer
  - Simulation
tags:
  - queue
  - circular-buffer
  - simulation
  - easy
premium: true
subscription_tier: basic
---

# QUE-002: Circular Shuttle Buffer with Overwrite

## 📋 Problem Summary

We need to implement a fixed-size circular buffer (capacity `k`) that supports standard queue operations plus a special overwrite mode.
- **ENQ x:** Add `x` to the rear. Fails if full.
- **ENQ_OVR x:** Add `x` to the rear. If full, overwrite the oldest element (front) and succeed.
- **DEQ:** Remove from front.
- **FRONT / REAR:** Peek at front/rear.
- **ISEMPTY / ISFULL:** Check status.

## 🌍 Real-World Scenario

**Scenario Title:** Dashcam Recording

Imagine a dashboard camera in a car.
- It records video in 1-minute chunks.
- The memory card has limited space (e.g., can hold 60 minutes).
- When the card is full, it doesn't stop recording.
- Instead, it **overwrites** the oldest footage to make room for the new minute.
- This ensures you always have the latest hour of driving footage.
- Standard file copying would be slow; a **Circular Buffer** allows this overwrite in `O(1)` time by just moving pointers.

**Why This Problem Matters:**

- **Log Rotation:** Servers keeping the last N lines of logs.
- **Audio Buffering:** Ring buffers in sound cards.
- **Network Switches:** Dropping old packets when the buffer is full (Tail Drop vs. Head Drop).

![Real-World Application](../images/QUE-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Circular Buffer Logic

Capacity `k=3`. Array `arr` of size 3.
Pointers: `head` (start), `tail` (end), `count` (size).

1. `ENQ 1`: `arr=[1, _, _]`, head=0, tail=1, count=1.
2. `ENQ 2`: `arr=[1, 2, _]`, head=0, tail=2, count=2.
3. `ENQ 3`: `arr=[1, 2, 3]`, head=0, tail=0 (wrap), count=3 (FULL).
4. `ENQ 4`: Fails (Full).
5. `ENQ_OVR 4`:
   - Full, so "remove" head (1). `head` moves to 1.
   - Insert 4 at `tail` (0). `arr=[4, 2, 3]`.
   - `tail` moves to 1.
   - `count` remains 3.
   - Queue logical order: `2 -> 3 -> 4`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Capacity `k`, then `m` commands.
- **Output:** Boolean for success/status, or values for peek/pop.
- **ENQ_OVR:** If not full, acts like normal `ENQ`. If full, reports "overwritten".

## Naive Approach

### Intuition

Use a standard list/array and shift elements.
- `ENQ`: Append.
- `DEQ`: Remove index 0 (shift all).
- `ENQ_OVR`: If full, remove index 0, then append.

### Limitations

- `DEQ` and `ENQ_OVR` (when full) are `O(k)` due to shifting.
- With `m` operations, total time `O(m x k)`, which is too slow if `k` is large.

## Optimal Approach

### Key Insight

Use a fixed-size array with `head` and `tail` indices and modulo arithmetic.
- **Index:** `(index + 1) % k`.
- **Size:** Track `count` explicitly to distinguish empty vs full (or use `(tail + 1) % k == head` rule, but explicit count is easier).

### Algorithm

1. `arr` of size `k`. `head = 0`, `tail = 0`, `count = 0`.
2. `ENQ x`:
   - If `count == k`: return `false`.
   - `arr[tail] = x`.
   - `tail = (tail + 1) % k`.
   - `count++`.
   - Return `true`.
3. `ENQ_OVR x`:
   - If `count < k`: Call `ENQ x`. Return `true` (or whatever success msg).
   - If `count == k`:
     - `head = (head + 1) % k` (Drop oldest).
     - `arr[tail] = x`.
     - `tail = (tail + 1) % k`.
     - Return "overwritten".
4. `DEQ`:
   - If `count == 0`: return "EMPTY".
   - Val = `arr[head]`.
   - `head = (head + 1) % k`.
   - `count--`.
   - Return Val.

### Time Complexity

- **O(1)** for all operations.

### Space Complexity

- **O(k)** for the array.

![Algorithm Visualization](../images/QUE-002/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-002/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `k=2`
1. `ENQ 5`: `[5, _]`, count=1. Output `true`.
2. `ENQ 6`: `[5, 6]`, count=2. Output `true`.
3. `ENQ 7`: Full. Output `false`.
4. `ENQ_OVR 8`: Full. Overwrite `5`. `head` moves to `6`. `[8, 6]`. `tail` moves to `5`'s old spot. Queue: `6 -> 8`. Output `overwritten`.
5. `FRONT`: Head is `6`. Output `6`.
6. `REAR`: Tail-1 is `8`. Output `8`.

Output matches example.

![Example Visualization](../images/QUE-002/example-1.png)

## ✅ Proof of Correctness

### Invariant
`count` always reflects the number of valid elements. `head` points to the oldest, `tail` to the next insertion slot. `ENQ_OVR` maintains capacity constraint by sacrificing `head`.

### Why the approach is correct
Modulo arithmetic correctly handles the circular wrapping of indices.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Thread Safety?
  - *Hint:* Circular buffers are popular in producer-consumer problems. Use atomic indices or locks to make it thread-safe.
- **Extension 2:** Resizable Circular Buffer?
  - *Hint:* When full, allocate array of size `2k`, copy elements (unwrapping them), and reset head/tail.

### Common Mistakes to Avoid

1. **Tail Calculation**
   - ❌ Wrong: `tail - 1` without modulo for `REAR`.
   - ✅ Correct: `(tail - 1 + k) % k` to handle wrap-around when `tail` is 0.
2. **Full/Empty Confusion**
   - ❌ Wrong: `head == tail` means empty OR full.
   - ✅ Correct: Use `count` variable or keep one slot open to distinguish.

## Related Concepts

- **Ring Buffer:** Another name for this structure.
- **Deque:** Double-ended queue (can add/remove from both ends).
