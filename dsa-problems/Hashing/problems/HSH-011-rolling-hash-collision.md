---
problem_id: HSH_ROLLING_HASH_COLLISION__8932
display_id: HSH-011
slug: rolling-hash-collision
title: "Rolling Hash Collision Finder"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Collision
  - Brute Force
tags:
  - hashing
  - collision
  - cryptography
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-011: Rolling Hash Collision Finder

## Problem Statement

Given a base `B`, modulus `M`, and length `L`, find two different strings of length `L` that produce the same polynomial hash value (a hash collision).

Return any pair of distinct strings that collide under the given hash parameters.

![Problem Illustration](../images/HSH-011/problem-illustration.png)

## Input Format

- Single line: three integers `B M L`

## Output Format

- Two lines, each containing a string of length `L` that produces the same hash

## Constraints

- `1 <= L <= 8`
- `1 <= B <= 10^9`
- `1 <= M <= 10^9 + 7`
- Strings contain only lowercase English letters

## Example

**Input:**

```
3 7 3
```

**Output:**

```
aaa
dac
```

**Explanation:**

Base B=3, Modulus M=7, Length L=3

hash("aaa") = (0*3^2 + 0*3 + 0) mod 7 = 0
hash("dac") = (3*9 + 0*3 + 2) mod 7 = 29 mod 7 = 1

(Note: Example may vary, any valid collision pair is acceptable)

![Example Visualization](../images/HSH-011/example-1.png)

## Notes

- Use birthday paradox approach or brute force search
- Generate random strings and store their hashes
- When a collision is found, return the pair
- Small L makes brute force feasible
- Time complexity: O(26^L) worst case
- Space complexity: O(26^L)

## Related Topics

Hash Collision, Birthday Paradox, Brute Force Search, Cryptography

---

## Solution Template

### Java


### Python


### C++


### JavaScript

