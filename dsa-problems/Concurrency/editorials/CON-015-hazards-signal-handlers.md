---
problem_id: CON_SIGNAL_HANDLER_SAFETY__6B90
display_id: CON-015
slug: hazards-signal-handlers
title: "Hazards of Signal Handlers"
difficulty: Medium
difficulty_score: 59
topics:
  - Concurrency
  - POSIX Signals
  - Low-level Systems
tags:
  - concurrency
  - signals
  - posix
  - async-signal-safe
  - medium
premium: true
subscription_tier: basic
---

# Hazards of Signal Handlers

## Problem summary

Signals are asynchronous interrupts:

- they can arrive at almost any instruction
- they run on the interrupted thread’s stack
- they may interrupt code that holds locks or is inside libc internals

So signal handlers must be extremely restricted.

## What “async-signal-safe” means

A function is async-signal-safe if it can be safely called from a signal handler.

Many functions are unsafe because they:

- take locks internally (risk deadlock if signal interrupts code holding the same lock)
- allocate memory (malloc/free use shared internal state and locks)
- use buffered I/O (printf uses locks and global buffers)

Common unsafe operations in handlers:

- `malloc`, `free`
- `printf`, `fprintf`, most stdio
- `pthread_mutex_lock`
- any code that is not re-entrant and not explicitly documented safe

## The minimal safe handler pattern

Best practice:

- do the minimum
- set a flag of type `volatile sig_atomic_t` (C) or an atomic boolean
- optionally write a byte to a pipe/eventfd (async-signal-safe) to wake a main loop
- return

Pseudocode:

```
global volatile sig_atomic_t gotSignal = 0

handler(signum):
  gotSignal = 1
  // optional: write(selfPipeFd, "x", 1)
  return
```

The rest of the program periodically checks `gotSignal` in a safe context and performs real work.

## Why “just log it” is wrong

Students often say: “In handler, call printf to log the signal.”

That is unsafe:

- if the signal interrupts `malloc()` or `printf()` itself, calling `printf()` can deadlock or corrupt state.

If you want to log, write to `STDERR_FILENO` using `write()` (async-signal-safe) and keep it minimal.

## Handoff designs

Two standard ways to notify main code:

1) Polling a flag
   - simplest, but latency depends on polling frequency

2) Self-pipe trick / eventfd
   - handler writes a byte
   - main loop is blocked in `select/poll/epoll` and wakes immediately

## Takeaway

Signal handlers are concurrency hazards. Safe handler = set a flag, optionally wake a loop, return. Do everything else in normal code.

