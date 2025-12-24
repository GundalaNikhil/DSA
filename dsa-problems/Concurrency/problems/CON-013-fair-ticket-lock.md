---
problem_id: CON_TICKET_LOCK__55D9
display_id: CON-013
slug: fair-ticket-lock
title: "Fair Ticket Lock"
difficulty: Medium
difficulty_score: 57
topics:
  - Concurrency
  - Locks
  - Atomics
  - Fairness
tags:
  - concurrency
  - ticket-lock
  - fairness
  - cache-coherence
  - medium
premium: true
subscription_tier: basic
time_limit: 2500
memory_limit: 256
---

# Fair Ticket Lock

## Problem Statement

Implement a fair lock using the **ticket lock** idea:

- `nextTicket` is an atomic counter that hands out ticket numbers.
- `nowServing` is an atomic counter indicating which ticket may enter.

A thread:

1. Fetches a ticket number.
2. Spins (or waits) until `nowServing` matches its ticket.
3. On unlock, increments `nowServing`.

Additionally, discuss cache contention and how ticket locks behave under high core counts.

## Input Format

No strict input.

## Output Format

Provide:

1. Pseudocode for `lock()` and `unlock()`
2. Why this is FIFO fair
3. Cache-coherence contention discussion (everyone reading `nowServing`)
4. One improvement idea (e.g., MCS lock) and when it’s better

## Constraints

- Many threads / many cores

## Related Topics

Concurrency, Locks, Fairness, Atomics

