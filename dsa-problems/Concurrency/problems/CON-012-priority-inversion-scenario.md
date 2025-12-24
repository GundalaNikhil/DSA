---
problem_id: CON_PRIORITY_INVERSION__8F42
display_id: CON-012
slug: priority-inversion-scenario
title: "Priority Inversion Scenario"
difficulty: Medium
difficulty_score: 50
topics:
  - Concurrency
  - Scheduling
  - Real-Time Systems
tags:
  - concurrency
  - scheduling
  - priority-inversion
  - medium
premium: true
subscription_tier: basic
time_limit: 1500
memory_limit: 256
---

# Priority Inversion Scenario

## Problem Statement

Describe a concrete scenario of **priority inversion**:

- A high-priority thread is blocked waiting for a lock held by a low-priority thread.
- A medium-priority thread runs and prevents the low-priority thread from making progress.
- Result: high-priority thread is indirectly delayed by the medium-priority thread.

Then propose and explain mitigation:

- **priority inheritance**, and/or
- **priority ceiling protocol**

## Input Format

No strict input.

## Output Format

Your answer must include:

1. Timeline with 3 threads: `H` (high), `M` (medium), `L` (low)
2. Where the lock is acquired and where blocking happens
3. Mitigation explanation and what changes in scheduling
4. One limitation or caveat

## Constraints

- N/A (conceptual)

## Related Topics

Concurrency, Scheduling, Locks, Real-Time Systems

