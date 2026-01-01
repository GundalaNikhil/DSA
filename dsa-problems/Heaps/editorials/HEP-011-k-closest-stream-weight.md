---
problem_id: HEP_K_CLOSEST_STREAM_WEIGHT__4950
display_id: HEP-011
slug: k-closest-stream-weight
title: "K Closest Points to Origin (Stream) with Weight"
difficulty: Medium
difficulty_score: 53
topics:
  - Heaps
  - Streaming
  - Geometry
tags:
  - heaps
  - streaming
  - geometry
  - medium
premium: true
subscription_tier: basic
---

# HEP-011: K Closest Points to Origin (Stream) with Weight

## 📋 Problem Summary

You receive a stream of points `(x, y)` with weight `w`.
Weighted distance `D = (x^2 + y^2) / w`.
Maintain the `k` points with the smallest `D`.
On `QUERY`, return IDs of these `k` points sorted by distance (asc).
IDs are 1-based, assigned sequentially.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Response Prioritization

Imagine an emergency dispatch system.
- Incidents occur at locations `(x, y)`.
- `w` represents urgency or priority (higher `w` means more urgent).
- The "cost" to respond is proportional to distance but inversely proportional to urgency.
- A high-priority incident far away can still be "closer" in terms of response rank than a low-priority incident nearby.
- You want to keep track of the top `k` incidents to dispatch units to.

![Real-World Application](../images/HEP-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Heap Maintenance

`k=2`.
Stream:
1. ID 1: `(1,1), w=1`. `D = 2/1 = 2`. Heap: `[(2, 1)]`.
2. ID 2: `(2,2), w=1`. `D = 8/1 = 8`. Heap: `[(8, 2), (2, 1)]` (Max-Heap).
3. ID 3: `(1,1), w=10`. `D = 2/10 = 0.2`.
   - Heap full. Max is 8 (ID 2).
   - `0.2 < 8`. Pop 8. Push 0.2.
   - Heap: `[(2, 1), (0.2, 3)]`.

Query: Sort heap. `(0.2, 3), (2, 1)`. Output: `3 1`.

### Key Concept: Max-Heap for Top K Smallest

To keep the `k` *smallest* values, we use a **Max-Heap** of size `k`.
- The root of the Max-Heap is the largest of the `k` smallest.
- When a new value comes:
  - If heap size < k: Push.
  - If heap size == k: Compare new value with root.
    - If new < root: Pop root, Push new.
    - Else: Ignore new (it's larger than the k-th smallest).

### Floating Point Precision

The distance is `(x^2 + y^2) / w`.
Comparing `A/B` vs `C/D`:
- Avoid division.
- Check `A * D < C * B`.
- Use `long` (64-bit integer) for cross-multiplication to avoid precision issues.
- `x, y <= 10^6 implies x^2+y^2 ~= 2 * 10^12`.
- `w <= 10^6`.
- Cross product: `(2 * 10^12) * 10^6 = 2 * 10^18`.
- Fits in signed 64-bit integer (max `~= 9 * 10^18`).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `ADD` and `QUERY`.
- **Output:** IDs.
- **Tie-Breaking:**
  - For `QUERY` output: Ascending distance. If tie, smaller ID first.
  - For Heap maintenance: If new distance == max distance in heap, do we replace?
    - We want the `k` smallest.
    - If tie, we prefer smaller ID?
    - The problem says "break ties by smaller id" for output.
    - Usually, "k closest" implies we want the set of k best.
    - If we have `(Dist=10, ID=5)` in heap (root) and new is `(Dist=10, ID=6)`.
      - 6 is worse than 5 (larger ID). Don't replace.
    - If new is `(Dist=10, ID=4)`.
      - 4 is better than 5. Replace.
    - So, strict ordering: `(D1, ID1) < (D2, ID2)` if `D1 < D2` or `D1 == D2 && ID1 < ID2`.
    - Max-Heap keeps the "worst" of the best.
    - "Worst" means largest Distance, or same Distance and largest ID.

## Naive Approach

### Intuition

Store all points. Sort on query.

### Time Complexity

- **O(Q * N log N)**: Too slow.

## Optimal Approach

### Key Insight

Use Max-Heap of size `k`.
Store objects `Point { long num; long den; int id; }`.
Comparator:
- `compare(a, b)`:
  - `valA = a.num * b.den`
  - `valB = b.num * a.den`
  - If `valA != valB`, return `compare(valA, valB)`.
  - Else return `compare(a.id, b.id)`.

### Algorithm

1. `id_counter = 1`.
2. Max-Heap `pq`.
3. **ADD:**
   - Calculate `num = x*x + y*y`, `den = w`.
   - Create `p = new Point(num, den, id)`.
   - If `pq.size() < k`: `pq.push(p)`.
   - Else:
     - Compare `p` with `pq.peek()`.
     - If `p` is "smaller" (better) than `pq.peek()`:
       - `pq.pop()`.
       - `pq.push(p)`.
   - `id_counter++`.
4. **QUERY:**
   - Create copy of heap elements.
   - Sort copy by "smaller" logic.
   - Output IDs.

### Time Complexity

- **O(Q log K)**.
- Query takes **O(K log K)**.

### Space Complexity

- **O(K)**.

![Algorithm Visualization](../images/HEP-011/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 1`.
1. `ADD 1 1 1`: `D=2`. ID=1. Heap: `[(2, 1)]`.
2. `ADD 2 2 1`: `D=8`. ID=2.
   - Heap full (k=1). Top is `(2, 1)`.
   - New `(8, 2)`. Is 8 < 2? No. Ignore.
   - Heap: `[(2, 1)]`.
3. `QUERY`: Output `1`.

My manual trace:
- `ADD 1 1 1` -> Dist 2.
- `ADD 2 2 1` -> Dist 8.
- k=1. We want smallest.
- Heap has `(2, 1)`.
- New is `(8, 2)`.
- `8 > 2`. New is worse. Keep `(2, 1)`.
- Query: `1`. Correct.

**Another Case:** k=2.
1. `ADD 1 1 1` (2, 1). Heap: `[(2, 1)]`.
2. `ADD 2 2 1` (8, 2). Heap: `[(8, 2), (2, 1)]`. (Max at top: 8).
3. `ADD 1 1 10` (0.2, 3).
   - Top is 8.
   - 0.2 < 8. Replace.
   - Heap: `[(2, 1), (0.2, 3)]`. (Max at top: 2).
4. `QUERY`: Sort `(0.2, 3), (2, 1)`. Output `3 1`.

## ✅ Proof of Correctness

### Invariant
- The Max-Heap maintains the `k` smallest elements seen so far.
- The root is the largest of these `k`.
- Any new element smaller than the root belongs in the set of `k` smallest, replacing the root.

## 💡 Interview Extensions

- **Extension 1:** Weighted median?
  - *Answer:* Two heaps (min/max) balancing weights.
- **Extension 2:** Moving window?
  - *Answer:* Sliding window logic with lazy deletion.

### Common Mistakes to Avoid

1. **Floating Point Errors**
   - ❌ Wrong: `double dist = (x*x+y*y)/w`.
   - ✅ Correct: Cross-multiplication `a.num * b.den < b.num * a.den`.
2. **Heap Direction**
   - ❌ Wrong: Min-Heap for top k smallest (keeps k largest).
   - ✅ Correct: Max-Heap to evict large elements.

## Related Concepts

- **Top K Elements:** Standard heap pattern.
- **Streaming Algorithms:** Reservoir sampling (related).
