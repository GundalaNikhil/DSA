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


## Solution Template

### Python

```python
def solve():
    return 0
1. Semaphore Usage:
   - Use a Semaphore initialized to `k`. Each `acquire()` call decrements it.
   - The semaphore represents "available tokens" for the current time window.

2. Refill Mechanism:
   - Token Bucket Approach:
     - Background thread or lazy refill.
     - **Lazy Refill (preferred)**: On `acquire`, check `now`.
     - Calculate `tokens_to_add = (now - last_refill_time) * rate`.
     - Update `current_tokens = min(capacity, current_tokens + tokens_to_add)`.
     - `last_refill_time = now`.
   - Alternatively, for strict 1-second windows: A timer thread adds `k` tokens every second (up to max `k`).

3. Handling Bursts & Drift:
   - **Bursts**: Cap the semaphore value at `k` (capacity). This allows a burst of up to `k` immediately, but no more until time passes.
   - **Drift**: Use a monotonic clock. If using lazy refill, calculation absorbs drift naturally. If using a timer thread, drift is negligible over short periods.

4. Scalability:
   - Standard semaphore operations are O(1).
   - For High Concurrency (`k=10^6`): Contention on the single semaphore lock can be a bottleneck.
   - Mitigation: Striping (multiple semaphores) or using Atomic CAS for token count can improve throughput.
""")

if __name__ == "__main__":
    solve()
```

