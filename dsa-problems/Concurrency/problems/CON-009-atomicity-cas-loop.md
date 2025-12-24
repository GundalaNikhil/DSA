---
problem_id: CON_CAS_INC_ABA__4CE0
display_id: CON-009
slug: atomicity-cas-loop
title: "Atomicity with CAS Loop"
difficulty: Medium
difficulty_score: 53
topics:
  - Concurrency
  - Atomics
  - Compare And Swap
tags:
  - concurrency
  - atomics
  - cas
  - aba
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Atomicity with CAS Loop

## Problem Statement

You are implementing a concurrent counter without a mutex.

1) Show how to implement `atomicIncrement()` using a **compare-and-swap (CAS)** loop.

2) Explain the **ABA problem**: how it can break CAS-based algorithms even when “the value looks unchanged”.

3) Propose at least one mitigation strategy (tagged pointers/version counters, hazard pointers, epoch GC, etc.), and explain when it is needed.

## Input Format

No strict input. Assume:

- A shared atomic integer `x`
- Multiple threads calling `atomicIncrement()` concurrently

## Output Format

Your answer must include:

- A correct CAS-loop sketch for increment (pseudocode is fine)
- A crisp ABA explanation with a concrete example
- At least one mitigation and its tradeoffs

## Constraints

- Many threads
- You must assume preemption can happen between any two instructions

## Example

If `x = 0` initially and 3 threads call `atomicIncrement()` concurrently, the final value must be `3` (no lost increments).

## Related Topics

Concurrency, Atomic Operations, Lock-Free Programming

