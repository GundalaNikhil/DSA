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
---

# Bounded Retry with Exponential Backoff

## Problem summary

When many threads repeatedly retry the same operation immediately, you get contention amplification:

- lock-free algorithms: CAS fails repeatedly
- distributed systems: retry storms
- database contention: hot row retries

Exponential backoff is the standard fix: wait a bit, then wait longer if it keeps failing, but cap the wait and cap retries.

## A correct retry loop

Pseudocode:

```
delay = initialDelayMs
for attempt in 1..maxRetries:
  ok = tryOperation()
  if ok: return SUCCESS

  sleep(delayWithJitter(delay))
  delay = min(maxDelayMs, delay * 2)
return FAILURE
```

Jitter:

- Instead of sleeping exactly `delay`, sleep a random value in `[0, delay]` or `[delay/2, delay]`.

Reason: if 100 threads fail at the same time and all sleep exactly 1ms, they will wake up and collide again. Jitter de-synchronizes retries.

## Why it improves throughput under contention

Immediate retries create a tight loop:

- you consume CPU
- you increase contention
- you reduce the chance any thread can make progress

Backoff reduces the number of concurrent contenders, giving the system a chance to “drain” the critical section or the bottleneck.

## How to choose parameters (interview-accurate)

- `initialDelay`: small enough to keep latency low when contention is mild (1–5ms in many systems, but can be microseconds for CAS backoff).
- `maxDelay`: prevents unbounded delays (cap at something reasonable, e.g., 1s).
- `maxRetries`: depends on SLA; after this, return error or fall back to a mutex/slow path.

In lock-free algorithms, typical backoff delays are in CPU cycles or nanoseconds, not milliseconds. State your unit based on context.

### Common mistakes

- No cap: delay grows too large and kills latency.
- No jitter: synchronized retries keep colliding.
- Infinite retries: can create live-lock under persistent failure.

## Takeaway

Exponential backoff is a contention control mechanism, not just “sleep to be nice”. Bound it and add jitter for real systems.

