---
problem_id: HSH_MAX_REPEATED_BLOCK_LENGTH__5827
display_id: HSH-008
slug: max-repeated-block-length
title: "Maximum Repeated Block Length"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Binary Search
  - String Algorithms
tags:
  - hashing
  - binary-search
  - substring
  - medium
premium: true
subscription_tier: basic
---

# HSH-008: Maximum Repeated Block Length

## 📋 Problem Summary

You are given a string `s`. Find the maximum length `L` such that there are two **non-overlapping** substrings of length `L` that are identical.
Non-overlapping means if the first substring is at indices `[i, i+L-1]` and the second at `[j, j+L-1]`, then the intervals must not intersect (i.e., `i+L <= j` assuming `i < j`).

## 🌍 Real-World Scenario

**Scenario Title:** Audio Sample Looping

Imagine you are editing a music track. You want to find the longest "loop" or repeated beat that occurs in the song to use it as a sample.
- However, the loop must be distinct; you can't just pick a sound that overlaps with itself (like a continuous "aaaaa" sound).
- You need two separate occurrences of the same sound pattern to create a clean transition or echo effect.

![Real-World Application](../images/HSH-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Overlapping vs Non-Overlapping

String: "aaaaa"

**Length 2:**
- "aa" at index 0 (0-1)
- "aa" at index 2 (2-3)
- Indices: [0,1] and [2,3]. No overlap. Valid.

**Length 3:**
- "aaa" at index 0 (0-2)
- "aaa" at index 1 (1-3) -> Overlap!
- "aaa" at index 2 (2-4) -> Overlap with index 0?
  - [0,2] and [2,4]. Overlap at index 2?
  - Indices are inclusive. 0,1,2 vs 2,3,4. Overlap at 2.
  - Usually means `end1 < start2`.
  - `0+3 = 3`. Next start must be `>= 3`.
  - Can we find "aaa" starting at `>= 3`? No. String length 5.
  - So Length 3 is invalid.

Max Length: 2.

### Key Concept: Binary Search on Answer

If a non-overlapping repeated substring of length `L` exists, does one of length `L-1` exist?
Yes. Just trim the last character of both occurrences. They remain equal and non-overlapping.
This monotonicity allows **Binary Search**.
- Range: `[0, N/2]`. (Max possible length is N/2).
- Check `possible(len)`:
  - Use Rolling Hash.
  - Store the **first occurrence index** of each hash in a Map.
  - For current substring at `i`, if hash exists in Map at `first_pos`:
    - Check if `first_pos + len <= i`.
    - If yes, return true.
    - If no, keep the `first_pos` (don't update it, we want the earliest start to maximize gap).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`.
- **Output:** Integer `L`.
- **Constraints:** `|s| <= 10^5`.
- **Non-overlapping:** `end1 < start2`.

## Naive Approach

### Intuition

Check all pairs of substrings.

### Algorithm

1. Loop length `len` from `N/2` down to 1.
2. Loop `i` from 0 to `N - 2*len`.
3. Loop `j` from `i + len` to `N - len`.
4. Compare `s[i..i+len]` with `s[j..j+len]`.
5. If match, return `len`.

### Time Complexity

- **O(N^3)**: Three nested loops. Too slow.

## Optimal Approach

### Key Insight

Combine **Binary Search** and **Rolling Hash**.
- Binary search for length `L`.
- For a fixed `L`, compute rolling hashes.
- Store `Map<Long, Integer>` mapping `hash -> first_start_index`.
- When seeing a hash again at `curr_start_index`:
  - If `curr_start_index >= map.get(hash) + L`, valid! Return true.
  - Else, ignore (don't update map, keeping the earliest occurrence gives best chance for non-overlap).

### Algorithm

1. `low = 0`, `high = n / 2`.
2. While `low <= high`:
   - `mid = (low + high) / 2`.
   - If `check(mid)`: `ans = mid`, `low = mid + 1`.
   - Else: `high = mid - 1`.
3. Return `ans`.

**Check(len):**
1. Map `first_occurrence`.
2. Compute rolling hash for window size `len`.
3. For each window starting at `i`:
   - If hash not in map, `put(hash, i)`.
   - Else if `i >= map.get(hash) + len`, return true.
4. Return false.

### Time Complexity

- **O(N \log N)**.

### Space Complexity

- **O(N)**: Map storage.

![Algorithm Visualization](../images/HSH-008/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abcabc
```
`N=6`. Range `[0, 3]`.

**Check 1 (Mid=1):**
- "a" at 0. "a" at 3. Gap `>= 1`. Valid.
- Ans = 1. Range `[2, 3]`.

**Check 2 (Mid=2):**
- "ab" at 0. "ab" at 3. Gap `>= 2`. Valid.
- Ans = 2. Range `[3, 3]`.

**Check 3 (Mid=3):**
- "abc" at 0. "abc" at 3. Gap `>= 3`. Valid.
- Ans = 3. Range `[4, 3]`. Loop ends.

**Result:** 3.

## ✅ Proof of Correctness

### Invariant
If we find a valid pair of length `L`, we record it.
Since we search for the *maximum* `L`, and the property is monotonic, binary search works.
The non-overlapping condition `start2 >= start1 + L` is strictly enforced.

## 💡 Interview Extensions

- **Extension 1:** Allow overlapping?
  - *Answer:* Just check `firstOccurrence.containsKey(hash)`. Don't check indices.
- **Extension 2:** Find the actual substring?
  - *Answer:* Return the substring corresponding to the hash when found.

### Common Mistakes to Avoid

1. **Overlapping Check**
   - ❌ Wrong: `start2 > start1`.
   - ✅ Correct: `start2 >= start1 + len`.
2. **Updating Map**
   - ❌ Wrong: Always updating `firstOccurrence` to the latest index.
   - ✅ Correct: Only set it if it's the *first* time seeing the hash. We want the maximum gap.

## Related Concepts

- **Longest Repeated Substring:** Usually allows overlap.
- **Suffix Tree:** Can solve this in `O(N)`.
