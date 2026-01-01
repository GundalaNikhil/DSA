---
problem_id: PDS_BOTTOM_K_SAMPLING__6358
display_id: PDS-008
slug: bottom-k-sampling
title: "Bottom-k Sampling (Min-Hash)"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - MinHash
  - Similarity Estimation
tags:
  - probabilistic-ds
  - minhash
  - similarity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-008: Bottom-k Sampling (Min-Hash)

## Problem Statement

You are given two MinHash signatures of length `k`, generated using the same hash functions. Estimate the Jaccard similarity as the fraction of positions where the signatures match.

![Problem Illustration](../images/PDS-008/problem-illustration.png)

## Input Format

- First line: integer `k`
- Second line: `k` floating-point numbers (signature A)
- Third line: `k` floating-point numbers (signature B)

## Output Format

- Single floating-point number: estimated Jaccard similarity

## Constraints

- `1 <= k <= 100000`
- Hash values are in [0, 1)

## Example

**Input:**

```
5
0.1 0.2 0.3 0.4 0.5
0.1 0.25 0.3 0.6 0.7
```

**Output:**

```
0.4
```

**Explanation:**

Matches at positions 1 and 3, so estimate = 2 / 5 = 0.4.

![Example Visualization](../images/PDS-008/example-1.png)

## Notes

- Use exact position matches
- Accept answers with absolute error <= 1e-6
- Time complexity: O(k)

## Related Topics

MinHash, Jaccard Similarity, Sketches

---

## Solution Template

### Java


### Python


### C++


### JavaScript

