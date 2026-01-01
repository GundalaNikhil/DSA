---
problem_id: HEP_TOP_K_FREQUENT_DECAY__5829
display_id: HEP-003
slug: top-k-frequent-decay
title: "Top K Frequent with Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Lazy Updates
  - Time Decay
tags:
  - heaps
  - decay
  - frequency
  - medium
premium: true
subscription_tier: basic
---

# HEP-003: Top K Frequent with Decay

## 📋 Problem Summary

You need to track the frequency of keys in a system where counts decay over time.
- `ADD key t`: Increment count of `key` by 1 at time `t`.
- `QUERY t`: Return the top `k` keys with the highest effective counts at time `t`.
- **Decay Rule:** Every `d` seconds, the count halves.
  - Formula: `Count_effective = Count_stored x 0.5^lfloor (t - t_last) / d rfloor`.

## 🌍 Real-World Scenario

**Scenario Title:** Trending Topics on Social Media

Imagine a "Trending Now" sidebar on Twitter.
- A hashtag like `#Olympics` gets millions of mentions (ADD events).
- However, mentions from last week shouldn't count as much as mentions today.
- The system applies a **Time Decay** factor. Old popularity fades away.
- When you load the page (QUERY), the system calculates the current "heat" of each topic and shows the top `k`.

![Real-World Application](../images/HEP-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Decay Process

Key "A", Decay Interval `d=10`.

Time 0: ADD "A". Count = 1. Last Update = 0.
Time 5: ADD "A".
- Decay from 0 to 5: `lfloor (5-0)/10 rfloor = 0` halves.
- Effective old count: `1 x 0.5^0 = 1`.
- New count: `1 + 1 = 2`. Last Update = 5.

Time 25: QUERY.
- Decay from 5 to 25: `lfloor (25-5)/10 rfloor = lfloor 20/10 rfloor = 2` halves.
- Effective count: `2 x 0.5^2 = 2 x 0.25 = 0.5`.

### Key Concept: Lazy Updates

We cannot update the count of *every* key at every second (`O(N)`).
Instead, we store `(count, last_update_time)` for each key.
- When accessing a key (ADD or QUERY), we first bring its count "up to date" using the decay formula.
- Then we perform the operation.
- This ensures we only pay the computation cost when necessary.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Operations with timestamps. Timestamps are non-decreasing.
- **Output:** List of keys.
- **Constraints:** `Q <= 10^5`, `d <= 10^9`.
- **Tie-breaking:** If counts are equal, use lexicographical order (smaller string first).
- **Floating Point:** Use `double` for counts.

## Naive Approach

### Intuition

On every `QUERY`, iterate through all keys, apply decay, sort them, pick top `k`.

### Time Complexity

- **O(Q * N log N)**: Too slow if many unique keys exist.

## Optimal Approach

### Key Insight

Let `bucket = floor(t / d)`. Store each key with:
- `count`: effective count at its last update bucket
- `bucket`: last update bucket

At query bucket `B`, the effective count is:
```
count * 0.5^(B - bucket)
```
Define a **time-invariant score**:
```
score = log(count) + bucket * ln(2)
```
Then:
```
log(effective) = score - B * ln(2)
```
The term `-B * ln(2)` is common to all keys in a query, so ordering by
effective count is **exactly** ordering by `score`, independent of `B`.

This lets us maintain a max-heap by `score` and answer each `QUERY`
without scanning all keys.

### Algorithm

1. Map `key -> {count, bucket, score, version}`.
2. Max-heap stores entries `(score, key, version)` ordered by:
   - higher `score` first
   - if tied, lexicographically smaller key first
3. **ADD(key, t):**
   - `B = floor(t / d)`
   - If key exists, decay its `count` to bucket `B`:
     `count *= 0.5^(B - bucket)`
   - `count += 1`, set `bucket = B`
   - `score = log(count) + bucket * ln(2)`
   - Increment `version` and push new heap entry
4. **QUERY(t):**
   - Pop heap until you collect `k` **valid** entries (version matches map).
   - Output their keys in heap order.
   - Push the valid entries back (query does not change state).

### Time Complexity

- **ADD:** `O(log N)`
- **QUERY:** `O(k log N)` (plus discarding stale heap entries)

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-003/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 5 1
ADD a 0
ADD a 5
ADD b 5
QUERY 10
```

1. `ADD a 0`:
   - `a`: count=1.0, last=0.
2. `ADD a 5`:
   - `a`: decay (5-0)/5 = 1 shift. `1.0 * 0.5 = 0.5`.
   - `a`: count = 0.5 + 1.0 = 1.5. last=5.
3. `ADD b 5`:
   - `b`: count=1.0, last=5.
4. `QUERY 10`:
   - `a`: decay (10-5)/5 = 1 shift. `1.5 * 0.5 = 0.75`.
   - `b`: decay (10-5)/5 = 1 shift. `1.0 * 0.5 = 0.5`.
   - Sort: `a` (0.75) > `b` (0.5).
   - Top 1: `a`.

## ✅ Proof of Correctness

### Invariant
- For each key, `(count, bucket)` is the exact effective count at that bucket.
- `score = log(count) + bucket * ln(2)` is time-invariant. For query bucket `B`,
  `log(effective) = score - B * ln(2)`, so ordering by `score` matches ordering
  by effective count.
- Heap entries with matching `version` reflect the current score; stale entries
  are ignored, so the top valid entries are the true top `k`.

## 💡 Interview Extensions

- **Extension 1:** Continuous Decay?
  - *Answer:* Use `e^-lambda t`. This allows using a global multiplier and avoiding iteration if we use a Heap with lazy updates (still hard for Top K).
- **Extension 2:** Sliding Window Count?
  - *Answer:* Use a queue of timestamps for each key.

### Common Mistakes to Avoid

1. **Updating State on Query**
   - ❌ Wrong: Updating `last_update` during a QUERY.
   - ✅ Correct: QUERY is read-only. Updating `last_update` changes the anchor for the floor function, which alters future decay steps.
2. **Integer Division**
   - ❌ Wrong: Using floating point division for shifts.
   - ✅ Correct: Use integer division `(t - last) / d`.

## Related Concepts

- **Exponential Moving Average (EMA):** Similar concept.
- **Lazy Propagation:** In segment trees.
