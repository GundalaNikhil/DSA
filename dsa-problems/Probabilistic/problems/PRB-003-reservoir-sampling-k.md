---
problem_id: PRB_RESERVOIR_SAMPLING_K__5716
display_id: PRB-003
slug: reservoir-sampling-k
title: "Reservoir Sampling K Items"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Randomized Algorithms
  - Streaming
tags:
  - probability
  - sampling
  - streaming
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-003: Reservoir Sampling K Items

## Problem Statement

You are given a stream of integers `1..n` and need to select `k` items uniformly at random using reservoir sampling. Use the following deterministic RNG for reproducibility:

```
state = seed
state = (state * 6364136223846793005 + 1) mod 2^64
rand() = state
```

For each item `i` (1-indexed):

- If `i <= k`, place `i` in the reservoir
- Else draw `j = rand() % i`. If `j < k`, replace reservoir[j]

Output the final reservoir in order.

![Problem Illustration](../images/PRB-003/problem-illustration.png)

## Input Format

- Single line: integers `n`, `k`, and `seed`

## Output Format

- Single line: `k` integers from the reservoir, space-separated
- If `k = 0`, print an empty line

## Constraints

- `0 <= k <= n <= 10^6`
- `0 <= seed < 2^64`

## Example

**Input:**

```
5 2 1
```

**Output:**

```
1 5
```

**Explanation:**

Using the specified RNG, the final reservoir contains items 1 and 5.

![Example Visualization](../images/PRB-003/example-1.png)

## Notes

- This is deterministic due to the fixed RNG
- Each item is processed once
- Time complexity: O(n)
- Space complexity: O(k)

## Related Topics

Reservoir Sampling, Randomized Streaming

---

## Solution Template

### Java


### Python


### C++


### JavaScript

