---
problem_id: CON_CONDVAR_WAIT_LOOP__3A0D
display_id: CON-011
slug: condvar-spurious-wakeup
title: "Condition Variable Spurious Wakeup Handling"
difficulty: Easy
difficulty_score: 30
topics:
  - Concurrency
  - Condition Variables
  - Synchronization
tags:
  - concurrency
  - condvar
  - spurious-wakeup
  - easy
premium: true
subscription_tier: basic
time_limit: 1500
memory_limit: 256
---

# Condition Variable Spurious Wakeup Handling

## Problem Statement

Condition variables can wake up without a matching signal (**spurious wakeup**) and signals can be “missed” if you use them incorrectly (**lost wakeup**).

Show the correct wait-loop pattern for a condition variable, and explain:

- why you must check a predicate in a loop
- how to avoid lost wakeups

## Input Format

No strict input.

## Output Format

Provide:

1. The canonical `while (!predicate) wait()` pattern (pseudocode is fine)
2. A 3–6 sentence explanation of spurious wakeups and lost wakeups
3. One common bug pattern and why it fails

## Constraints

- N/A

## Example

Shared flag starts as `false`. Waiters block. A signaller sets it to `true` and signals. Correct code wakes waiters and they proceed only after seeing the flag is `true`.

## Related Topics

Concurrency, Condition Variables, Monitors

