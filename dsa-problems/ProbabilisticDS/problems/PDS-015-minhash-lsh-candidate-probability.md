---
problem_id: PDS_PROBLEM_15__4501
display_id: PDS-015
slug: minhash-lsh-candidate-probability
title: "MinHash LSH Candidate Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - MinHash
  - LSH
tags:
  - probabilistic-ds
  - lsh
  - minhash
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-015: MinHash LSH Candidate Probability

## Problem Statement

In MinHash LSH with `b` bands and `r` rows per band, the probability that two sets with Jaccard similarity `s` become a candidate pair is:

```
P = 1 - (1 - s^r)^b
```

Compute `P`.

![Problem Illustration](../images/PDS-015/problem-illustration.png)

## Input Format

- Single line: integers `b`, `r`, and real `s`

## Output Format

- Single floating-point number: candidate probability

## Constraints

- `1 <= b, r <= 1000`
- `0 <= s <= 1`

## Example

**Input:**

```
5 2 0.5
```

**Output:**

```
0.762695
```

**Explanation:**

P = 1 - (1 - 0.5^2)^5 = 0.762695.

![Example Visualization](../images/PDS-015/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

MinHash, LSH, Similarity Search

---

## Solution Template

### Java


### Python


### C++


### JavaScript

