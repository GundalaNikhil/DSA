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
time_limit: 1500
memory_limit: 256
---

# Hazards of Signal Handlers

## Problem Statement

In POSIX, signal handlers can interrupt your program at almost any point, even while it holds locks or is inside `malloc()`.

1) Identify why many functions are **async-signal-unsafe** in a handler.

2) Design a minimal-safe handler that:

- performs only async-signal-safe operations
- sets a flag (e.g., `sig_atomic_t` or atomic boolean)
- returns quickly

3) Explain how the rest of the program should respond to that flag safely (e.g., self-pipe trick, eventfd, main loop polling).

## Input Format

No strict input.

## Output Format

Your answer must include:

- A list of common unsafe operations (malloc/printf/locking)
- A minimal handler sketch
- A safe handoff design to normal code

## Constraints

- POSIX signals

## Example

A signal arrives while the program is inside `malloc()`. A safe handler does not call `malloc()` or `printf()`; it only sets a flag and returns.

## Related Topics

Signals, Async-signal-safety, Concurrency Hazards


## Solution Template

### Python

```python
def solve():
    return 0
1. Unsafe Operations:
   - `malloc`/`free`: Maintains global locks/state. If signal interrupts malloc and handler calls malloc, deadlock or corruption.
   - `printf`/IO: Uses buffers/locks.
   - `pthread_mutex_lock`: If interrupted thread holds it -> Deadlock.

2. Minimal Handler:
   ```c
   volatile sig_atomic_t signal_flag = 0;
   
   void handler(int signum) {
       signal_flag = 1;
       // No other logic!
   }
   ```

3. Safe Handoff (Self-Pipe Trick):
   - Create a non-blocking pipe.
   - In handler: `write(pipe_fd[1], &byte, 1)`. `write` is async-signal-safe.
   - In Main Loop: `select` or `poll` on `pipe_fd[0]`.
   - When readable, wake up, read byte, and process the signal event safely in normal context (where malloc/printf are allowed).
""")

if __name__ == "__main__":
    solve()
```

