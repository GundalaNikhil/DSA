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
---

# Semaphore-Based Rate Limiter

## Problem summary

Implement a limiter that enforces: across all threads, at most `k` events can pass per second.

The simplest mental model is a bucket of tokens:

- each event consumes one token
- tokens are replenished over time (refill)
- if no token is available, the caller waits

The concurrency part is: “no double spending tokens, no races, no missed wakeups”.

## Real-world scenario

BTech-friendly framing: “You are calling a third-party API that bans you if you send more than `k` requests/sec. Your backend is multi-threaded; all threads must obey the same limit.”

Interview framing: “Global rate limit shared across worker threads.”

### Core design: counting semaphore as the token bucket

Use a counting semaphore `tokens`:

- semaphore count = number of available tokens
- `acquire()` consumes one token (blocks if 0)

Refill strategy options:

### Option A: Discrete refill each second

Every second, refill back to `k`.

Implementation detail: semaphore usually supports `release(n)`; but you must avoid letting the count exceed `k`.

So you need an auxiliary atomic integer `currentTokens` (or query if the semaphore supports it, many do not).

Refill algorithm (conceptual):

- once per second:
  - compute `missing = k - currentTokens`
  - `tokens.release(missing)`
  - set `currentTokens = k`

But `currentTokens` must be updated atomically with actual acquires/releases, so you end up building a small monitor around it.

### Option B: Continuous refill (smoother, better burst control)

Instead of adding `k` tokens at once each second, add tokens at a steady rate:

- every `1/k` seconds, release 1 token

This reduces burstiness, but `k` can be up to `10^6`, which makes “wake up 1e6 times per second” impossible.

So for large `k`, you refill in batches:

- every 10ms, add `k/100` tokens (rounded), capped at `k`

That’s the production compromise.

### Correctness concerns (what students must say)

### 1) Use a monotonic clock

Wall clock can jump backward/forward (NTP). If you schedule refills based on wall clock, you can over-refill or starve.

### 2) Cap the bucket size

If you only call `release()` without capping, tokens can accumulate and you lose the “per second” guarantee (you turn it into “average rate” over a long time).

This is a classic bug.

### 3) Burst vs strict per-second

Clarify the contract:

- Strict “no more than k in any 1-second window” is harder (sliding window).
- Token bucket typically allows bursts up to bucket capacity.

This problem statement implies a simple per-second refill, so bursts within a second are limited by remaining tokens, which matches token-bucket behavior with capacity `k`.

If asked in an interview: state which semantics you implement.

## Scaling notes for `k` up to 10^6

- Do not refill one token at a time.
- Use a timer thread with a reasonable tick (10–100ms) and add tokens in batches.
- Avoid a global mutex on every acquire if semaphore acquisition is fast in your runtime; otherwise consider a lock-free counter + sleep (but that is more complex).

## Minimal pseudocode sketch

- `tokens = Semaphore(k)` initially full
- `refillThread`:
  - loop:
    - sleep(1 second)
    - add enough tokens to bring semaphore back to `k` (capped)
- `acquire()`:
  - `tokens.acquire()`

Then discuss how you track the current count safely (because many semaphore APIs don’t expose it).

## Takeaway

Strong answers clearly separate:

- policy: token bucket with cap `k`
- mechanism: semaphore for blocking + refill scheduler
- time correctness: monotonic time

