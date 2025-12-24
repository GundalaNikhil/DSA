---
problem_id: CON_SEM_RATE_LIMIT__9B3A
display_id: CON-005
slug: semaphore-rate-limiter
title: "Semaphore-Based Rate Limiter"
difficulty: Medium
difficulty_score: 54
topics:
  - Concurrency
  - Semaphores
  - Rate Limiting
tags:
  - concurrency
  - semaphore
  - rate-limiter
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Semaphore-Based Rate Limiter

## Problem Statement

Design a rate limiter that allows at most **`k` events per second** across multiple threads.

Requirements:

- Threads call `acquire()` before doing an event.
- If the rate limit is exceeded, callers must **block** (or wait) until they are allowed.
- Use a **semaphore/token** approach with a refill mechanism (timer thread or time-based refill).
- Ensure correctness under concurrency (no “double spending” tokens).

## Input Format

Given:

- `k` (tokens per second)
- Many threads calling `acquire()` concurrently

## Output Format

Provide a design including:

1. Which semaphore you use and what it represents
2. How tokens are refilled each second (or continuously)
3. How you handle bursts and clock drift
4. Complexity and scaling notes for `k` up to `10^6`

## Constraints

- `1 <= k <= 10^6`
- Many threads can call `acquire()` simultaneously
- Assume wall-clock time can jump; monotonic clock is preferred

## Example

If `k=2` and events arrive at times `t=0s, 0s, 0.5s, 1.2s`:

- First two events at `t=0s` proceed immediately (consume 2 tokens).
- Event at `t=0.5s` blocks because no tokens remain.
- After refill at `t=1s`, one token is available; the blocked event proceeds.
- Event at `t=1.2s` uses the second token for that second.

## Related Topics

Concurrency, Semaphores, Timing, Rate Limiting

