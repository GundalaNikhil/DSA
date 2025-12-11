---
unique_problem_id: concurrency_001
display_id: CONCURRENCY-001
slug: mutex-vs-spinlock-selection
version: 1.0.0
difficulty: Easy
topic_tags:
  - Concurrency
  - Synchronization Primitives
  - Mutex
  - Spinlock
  - Performance Analysis
---

# Mutex vs Spinlock Selection

## Problem Description

Given contention time estimates (critical section duration and expected wait time), decide whether to use a mutex or spinlock and justify your reasoning.

## Examples

- Example 1:
  - Input: Critical section duration = 1µs, Expected wait time = 50µs
  - Output: **Prefer Mutex**
  - Explanation: Wait time (50µs) >> critical section (1µs). Spinning wastes CPU cycles. Mutex allows the thread to sleep and be woken up, saving resources.

- Example 2:
  - Input: Critical section duration = 100ns, Expected wait time = 200ns
  - Output: **Prefer Spinlock**
  - Explanation: Wait time is very short (200ns). Context switch overhead (~1-10µs) exceeds the wait. Spinning is more efficient.

- Example 3:
  - Input: Critical section duration = 5ms, Expected wait time = 10ms
  - Output: **Prefer Mutex**
  - Explanation: Both times are in milliseconds. Definitely don't spin-wait for 10ms. Use mutex to yield CPU.

## Constraints

- Provide reasoning, not code
- Consider context switch overhead (~1-10 microseconds typically)
- Consider CPU utilization and power consumption

## Function Signatures

### Java
```java
class Solution {
    /**
     * Recommend lock type based on timing characteristics.
     * 
     * @param criticalSectionNs Critical section duration in nanoseconds
     * @param expectedWaitNs Expected wait time in nanoseconds
     * @return "mutex" or "spinlock" with justification
     */
    public String recommendLockType(long criticalSectionNs, long expectedWaitNs) {
        // Implementation here
    }
}
```

### Python
```python
def recommend_lock_type(critical_section_ns: int, expected_wait_ns: int) -> str:
    """
    Recommend mutex or spinlock based on timing characteristics.
    
    Args:
        critical_section_ns: Duration of critical section in nanoseconds
        expected_wait_ns: Expected wait time in nanoseconds
    
    Returns:
        "mutex" or "spinlock" with justification
    """
    pass
```

### C++
```cpp
#include <string>
using namespace std;

class Solution {
public:
    string recommendLockType(long criticalSectionNs, long expectedWaitNs) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Critical section duration (with unit: ns, µs, or ms)
- Second line: Expected wait time (with same unit convention)

### Sample Input
```
1us
50us
```

## Hints

The key threshold is context switch overhead. If expected wait time < context switch cost, prefer spinlock. Otherwise, prefer mutex.

## Quiz

### Question 1
What is the main disadvantage of spinlocks?

A) They require kernel calls  
B) They waste CPU cycles while waiting  
C) They can cause deadlocks  
D) They are not portable

**Correct Answer:** B

**Explanation:** Spinlocks continuously check the lock in a loop, consuming CPU cycles even while waiting, which wastes power and CPU resources.

### Question 2
When is a mutex preferable over a spinlock?

A) When the critical section is very short  
B) When contention is expected to last longer than context switch overhead  
C) When running on a single-core CPU  
D) Both B and C

**Correct Answer:** D

**Explanation:** Mutex is better for longer waits (B) and on single-core (C) where spinning wastes the only CPU that could release the lock.

### Question 3
What is the typical context switch overhead?

A) 1-10 nanoseconds  
B) 1-10 microseconds  
C) 1-10 milliseconds  
D) 1-10 seconds

**Correct Answer:** B

**Explanation:** Context switches typically take 1-10 microseconds, depending on the OS and hardware.

### Question 4
Why might spinlocks be preferred in kernel code?

A) They are simpler to implement  
B) Context switches may not be possible in certain interrupt contexts  
C) Kernels don't have mutexes  
D) Spinlocks are always faster

**Correct Answer:** B

**Explanation:** In interrupt handlers or when interrupts are disabled, the scheduler can't run, making sleeping locks impossible. Spinlocks are used instead.
