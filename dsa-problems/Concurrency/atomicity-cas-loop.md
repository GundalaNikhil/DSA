---
unique_problem_id: concurrency_009
display_id: CONCURRENCY-009
slug: atomicity-cas-loop
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Atomic Operations
  - Compare-And-Swap
  - Lock-Free Programming
  - ABA Problem
---

# Atomicity With CAS Loop

## Problem Description

Implement atomic increment using a compare-and-swap (CAS) loop. Discuss the ABA problem and mitigation strategies.

## Examples

- Example 1:
  - Input: Initial value = 0, 3 concurrent increments
  - Output: Final value = 3
  - Explanation: Each thread reads current value, computes new value, attempts CAS. On failure, retry.

- Example 2:
  - Input: Initial = 5, 2 decrements + 3 increments (concurrent)
  - Output: Final = 6 (5 - 2 + 3)

- Example 3:
  - ABA scenario: Thread 1 reads A, gets preempted. Thread 2 changes A→B→A. Thread 1's CAS succeeds incorrectly.
  - Mitigation: Use versioned references or double-width CAS

## Constraints

- Lock-free implementation required
- Handle high contention gracefully

## Function Signatures

### Java
```java
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicStampedReference;

class AtomicCounter {
    private AtomicInteger value = new AtomicInteger(0);
    
    public void increment() {
        // Implementation here
    }
    
    public int get() {
        // Implementation here
    }
}

// ABA-safe version using stamped reference
class ABASafeCounter {
    private AtomicStampedReference<Integer> value;
    // Implementation here
}
```

### Python
```python
import threading

class AtomicCounter:
    """
    Atomic counter using CAS-like semantics.
    Note: Python doesn't have native CAS, so we simulate with locks
    or use ctypes for true atomics.
    """
    def __init__(self, initial: int = 0):
        self._value = initial
        self._lock = threading.Lock()  # Simulated CAS
    
    def increment(self) -> None:
        """Atomically increment the counter."""
        pass
    
    def get(self) -> int:
        """Get current value."""
        pass
```

### C++
```cpp
#include <atomic>

class AtomicCounter {
public:
    AtomicCounter(int initial = 0) : value(initial) {}
    
    void increment() {
        // Implementation here
    }
    
    int get() const {
        // Implementation here
    }
    
private:
    std::atomic<int> value;
};
```

## Input Format

The input will be provided as:
- Initial value
- Number of threads and operations per thread

### Sample Input
```
0
3 1
```

## Hints

CAS atomically checks if current == expected; if yes, update to new value. If no, read again and retry. For ABA, use versioned pointers or hazard pointers.

## Quiz

### Question 1
What does CAS stand for?

A) Compute And Store  
B) Compare And Swap  
C) Copy And Set  
D) Check And Save

**Correct Answer:** B

**Explanation:** Compare-And-Swap atomically compares a memory location to an expected value and swaps it with a new value if they match.

### Question 2
What is the ABA problem?

A) Memory corruption  
B) A value changes from A to B and back to A, fooling CAS  
C) A deadlock scenario  
D) An arithmetic overflow

**Correct Answer:** B

**Explanation:** If a value changes A→B→A between read and CAS, CAS succeeds but intermediate state B was missed, potentially causing incorrect behavior.

### Question 3
How can ABA be mitigated?

A) Use locks instead  
B) Add a version/stamp counter that increments on each change  
C) Use larger integers  
D) Ignore it

**Correct Answer:** B

**Explanation:** Stamped/versioned references pair the value with an ever-increasing counter. Even if value returns to A, the stamp differs.

### Question 4
What happens in a CAS loop under high contention?

A) Threads sleep  
B) Threads spin, retrying CAS until success  
C) Threads deadlock  
D) The system crashes

**Correct Answer:** B

**Explanation:** Under contention, multiple threads may fail their CAS attempts repeatedly, spinning until eventually one succeeds.
