---
problem_id: CON_BACKOFF_RETRY__1CC6
display_id: CON-014
slug: bounded-retry-backoff
title: "Bounded Retry with Exponential Backoff"
difficulty: Medium
difficulty_score: 45
topics:
  - Concurrency
  - Backoff
  - Reliability
tags:
  - concurrency
  - backoff
  - retry
  - medium
premium: true
subscription_tier: basic
time_limit: 1500
memory_limit: 256
---

# Bounded Retry with Exponential Backoff

## Problem Statement

When many threads retry at the same time (e.g., lock-free CAS failures, transient network errors), immediate retries can cause a **thundering herd** and reduce throughput.

Design bounded retry logic with **exponential backoff**:

- Start with a small delay (e.g., 1ms)
- Double delay after each failure
- Cap delay at `maxDelay`
- Stop after `maxRetries` (or return failure)
- (Optional but recommended) add **jitter** to avoid synchronized retries

## Input Format

Given:

- `maxRetries`
- `initialDelayMs`
- `maxDelayMs`

## Output Format

Provide:

1. Pseudocode for retry loop with backoff (and jitter if used)
2. Why backoff improves behavior under contention
3. How you choose caps and retry budget

## Constraints

- N/A

## Example

Operation fails 2 times then succeeds:

- Retry delays: 1ms, 2ms, then success on the 3rd attempt.

## Related Topics

Concurrency, Lock-Free Algorithms, Reliability Patterns


## Solution Template

### Python

```python
def solve():
    return 0
1. Retry Loop with Exponential Backoff + Jitter:
   ```python
   def retry_op(max_retries, initial_delay, max_cap):
       return 0
   ```

2. Why it improves behavior:
   - **Exponential**: Quickly reduces load if the system is overloaded. If 1000 threads fail, they spread out their retries (1ms, 2ms, 4ms...) rather than hammering repeatedly at fixed intervals.
   - **Jitter**: Prevents "synchronized" retries where batches of threads wake up, fail together, and wait together. Randomness de-synchronizes the herd.

3. Choosing Caps:
   - `initialDelay`: Round-trip time or expected recovery time (e.g., 5-50ms).
   - `maxDelay`: Depends on user latency tolerance (e.g., 1s for interactive, 30s for background).
   - `maxRetries`: Budget for total waiting time.
""")

if __name__ == "__main__":
    solve()
```

