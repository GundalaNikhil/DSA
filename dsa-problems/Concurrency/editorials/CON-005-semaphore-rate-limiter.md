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

**Synchronization for Option A (discrete refill):**

```
Shared state:
- tokens: Semaphore(k)
- mutex: Lock
- currentTokens: k
- lastRefillTime: now()

acquire():
  tokens.acquire()                    // blocks if 0 tokens
  mutex.lock()
  currentTokens--
  mutex.unlock()

refillThread():
  loop:
    sleep(1 second)
    mutex.lock()

    elapsedSeconds = (now() - lastRefillTime) / 1000
    if elapsedSeconds >= 1:
      tokensToAdd = (elapsedSeconds * k) - (k - currentTokens)
      tokensToAdd = min(tokensToAdd, k - currentTokens)  // cap at k

      for i in 0..tokensToAdd-1:
        tokens.release(1)
      currentTokens = min(currentTokens + tokensToAdd, k)
      lastRefillTime = now()

    mutex.unlock()
```

Note: Locking the mutex during refill ensures `currentTokens` stays synchronized with actual semaphore count. Without this, an acquire and refill can interleave incorrectly.

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

### 3) Token Bucket vs Sliding Window Rate Limiting

Two different rate-limiting semantics exist:

**Token Bucket (this problem):**
- Tokens refill each second to capacity `k`
- Allows bursts: if you have all `k` tokens, you can use them instantly
- Weakness: if no requests arrive for 10 seconds, you accumulate 10k tokens and then 10k requests can proceed at once
- Use when: you want to smooth traffic over time but allow occasional bursts (e.g., API rate limiting with burst allowance)

**Sliding Window (stricter):**
- No more than `k` events can occur in any 1-second window
- If you allow `k` at time `t=0`, the next `k` events can only start at `t >= 1.0`
- Much stricter: prevents burst bursts entirely
- Use when: hard limit on peak throughput is mandatory (e.g., network bandwidth cap)

This problem statement implies **token bucket** semantics (refill per second), which is the standard rate limiter approach. If your problem requires strict sliding-window semantics, you need a different algorithm (track request timestamps in a sliding window, reject if window has k requests).

State which semantics your design implements.

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
