---
unique_problem_id: concurrency_015
display_id: CONCURRENCY-015
slug: hazards-signal-handlers
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Signal Handling
  - Async-Signal-Safety
  - POSIX Signals
  - Reentrancy
---

# Hazards of Signal Handlers

## Problem Description

Identify async-signal-unsafe functions and design a minimal safe signal handler that sets an atomic flag and returns. Explain why calling unsafe functions in signal handlers is dangerous.

## Examples

- Example 1:
  - Scenario: Signal arrives during malloc()
  - Unsafe: Calling malloc() or printf() in signal handler can cause deadlock or corruption
  - Safe: Handler just sets `volatile sig_atomic_t flag = 1` and returns

- Example 2:
  - Main thread checks flag in main loop
  - When flag is set, performs cleanup safely outside handler

- Example 3:
  - Unsafe functions in handlers: malloc, free, printf, any function that uses global state or locks

## Constraints

- POSIX signal semantics
- Async-signal-safe functions are very limited (see signal-safety(7))

## Function Signatures

### Java
```java
// Java doesn't have native Unix signal handling
// Use sun.misc.Signal (non-standard) or Runtime.addShutdownHook

class SignalExample {
    private static volatile boolean shutdownRequested = false;
    
    static {
        // Implementation here
    }
    
    public static void mainLoop() {
        // Implementation here
    }
}
```

### Python
```python
import signal
import sys

# Volatile flag (Python doesn't need volatile, GIL provides visibility)
shutdown_requested = False

def signal_handler(signum, frame):
    """
    Minimal signal handler.
    """
    # Implementation here
    pass

def main():
    # Implementation here
    pass
```

### C++
```cpp
#include <csignal>
#include <atomic>

// Async-signal-safe flag
volatile sig_atomic_t shutdown_flag = 0;

void signal_handler(int signum) {
    // Implementation here
}

int main() {
    // Implementation here
    return 0;
}
```

## Input Format

This is a design/pattern problem about safe signal handling practices.

## Hints

Only sig_atomic_t and a handful of functions (write, _exit, signal) are async-signal-safe. Set a flag and return; do everything else in the main loop.

## Quiz

### Question 1
Why is calling malloc() in a signal handler dangerous?

A) malloc() is slow  
B) Signal may arrive while malloc() holds an internal lock, causing deadlock  
C) malloc() uses too much memory  
D) malloc() is deprecated

**Correct Answer:** B

**Explanation:** If malloc() is interrupted by a signal that also calls malloc(), the internal lock is already held, causing deadlock or data structure corruption.

### Question 2
What is an async-signal-safe function?

A) A fast function  
B) A function safe to call from a signal handler, guaranteed not to interfere with interrupted code  
C) A function that handles signals  
D) A function that can't be interrupted

**Correct Answer:** B

**Explanation:** Async-signal-safe functions use no global state or locks that could be held when interrupted. Examples: write(), _exit(), signal().

### Question 3
Why use volatile sig_atomic_t for the flag?

A) Performance  
B) Guarantees atomic read/write and prevents compiler from caching the value  
C) Larger range of values  
D) Required by the OS

**Correct Answer:** B

**Explanation:** volatile prevents the compiler from optimizing out reads (main loop must re-read). sig_atomic_t guarantees atomic access, safe between handler and main.

### Question 4
Is printf() safe in a signal handler?

A) Yes, always  
B) No, it uses internal buffers and locks  
C) Only for short strings  
D) Only on Linux

**Correct Answer:** B

**Explanation:** printf() is not async-signal-safe. It uses internal state (buffers, locks) that may be corrupt if interrupted. Use write() instead if output is essential.
