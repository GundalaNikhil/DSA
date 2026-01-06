---
problem_id: NUM_PRIME_DETECTION_SIEVE_MILLER_RABIN__7179
display_id: NTB-NUM-7179
slug: prime-detection-sieve-miller-rabin
title: "Prime Detection with Sieve and Deterministic Miller-Rabin"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - modular-arithmetic
  - numbertheory
  - prime-detection-sieve-miller-rabin
  - primes
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Prime Detection with Sieve and Deterministic Miller-Rabin

## Problem Statement

You are given an integer limit `N` and `Q` queries. Use a sieve to precompute primes up to `N`. For each query value `x`:

- If `x <= N`, answer using the sieve.
- If `x > N`, first check divisibility by all primes `<= N`. If any divides `x`, it is composite.
- Otherwise, run deterministic Miller-Rabin with the fixed witnesses below and report prime or composite.

Witness set (in this exact order):

```
2 3 5 7 11 13 17 19 23 29 31 37
```

Your output must follow this deterministic procedure.

## Input Format

- First line: integers `N` and `Q`
- Next `Q` lines: one integer `x` per line

## Output Format

- For each query, output `PRIME` or `COMPOSITE` on its own line

## Constraints

- `1 <= N <= 10^7`
- `1 <= Q <= 200000`
- `1 <= x <= 10^18`

## Clarifying Notes

- The sieve is required; do not run Miller-Rabin for `x <= N`.
- If `x` is divisible by any prime `<= N`, it is composite without Miller-Rabin.
- The specified witness set is deterministic for 64-bit inputs.

## Example Input

```
30 5
2
15
31
37
49
```

## Example Output

```
PRIME
COMPOSITE
PRIME
PRIME
COMPOSITE
```
