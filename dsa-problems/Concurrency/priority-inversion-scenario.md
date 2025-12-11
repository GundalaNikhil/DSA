---
unique_problem_id: concurrency_012
display_id: CONCURRENCY-012
slug: priority-inversion-scenario
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Priority Inversion
  - Priority Inheritance
  - Priority Ceiling
  - Real-Time Systems
---

# Priority Inversion Scenario

## Problem Description

Describe a scenario of priority inversion where a high-priority thread waits for a low-priority thread, which is preempted by a medium-priority thread. Propose mitigation strategies like priority inheritance or priority ceiling protocol.

## Examples

- Example 1:
  - Scenario: Threads H (high), M (medium), L (low) share a lock
    1. L acquires lock
    2. H runs, needs lock, blocks on L
    3. M runs (higher than L, no lock needed), preempts L
    4. Result: H waits for M (indirectly), inverting priorities
  - Mitigation: Priority inheritance - boost L to H's priority while holding the lock

- Example 2:
  - Priority ceiling protocol: Lock has ceiling = max priority of any thread that uses it
  - When L acquires lock, it runs at ceiling priority
  - M cannot preempt L
  - Output: H waits only for L's critical section, not for M

- Example 3:
  - No lock involved: No priority inversion possible
  - Output: Normal priority scheduling

## Constraints

- Assumes preemptive priority scheduling
- Real-time system considerations

## Function Signatures

### Java
```java
// Priority Inheritance simulation
class PriorityInheritanceLock {
    private Thread owner;
    private int originalPriority;
    
    public synchronized void lock() {
        // Implementation here
    }
    
    public synchronized void unlock() {
        // Implementation here
    }
}

// Priority Ceiling simulation
class PriorityCeilingLock {
    private final int ceiling;
    
    public PriorityCeilingLock(int ceiling) {
        this.ceiling = ceiling;
    }
    
    public synchronized void lock() {
        // Implementation here
    }
    
    public synchronized void unlock() {
        // Implementation here
    }
}
```

### Python
```python
import threading

class PriorityInheritanceLock:
    """
    Simulated priority inheritance lock.
    Note: Python doesn't have native thread priorities.
    """
    
    def __init__(self):
        pass
    
    def acquire(self, thread_priority: int) -> None:
        """Acquire lock, boosting holder's priority if needed."""
        pass
    
    def release(self) -> None:
        """Release lock and restore original priority."""
        pass
```

### C++
```cpp
#include <thread>
#include <mutex>

// Note: Real priority inheritance requires OS support (PTHREAD_PRIO_INHERIT)
class PriorityInheritanceMutex {
public:
    void lock();
    void unlock();
    
private:
    std::mutex mtx;
    // Implementation here
};
```

## Input Format

This is a design/conceptual problem with scenarios rather than specific input format.

## Hints

Priority inheritance: temporarily boost the lock holder's priority to the highest waiter's priority. Priority ceiling: set a fixed high priority for anyone holding the lock.

## Quiz

### Question 1
What is priority inversion?

A) Higher priority threads run first  
B) A high-priority thread waits for a lower-priority thread due to lock contention  
C) Priorities are assigned randomly  
D) All threads have the same priority

**Correct Answer:** B

**Explanation:** Priority inversion occurs when H waits for L (holding a lock), but M (higher than L) preempts L, making H effectively wait for M.

### Question 2
How does priority inheritance mitigate priority inversion?

A) It ignores priorities  
B) It temporarily boosts the lock holder's priority to the highest waiting thread's priority  
C) It kills low-priority threads  
D) It uses round-robin scheduling

**Correct Answer:** B

**Explanation:** By boosting L to H's priority, M cannot preempt L, and L finishes quickly, releasing the lock for H.

### Question 3
What is the priority ceiling protocol?

A) A lock has a fixed priority; any holder runs at that priority  
B) Threads at the ceiling can't acquire locks  
C) Only high-priority threads can use locks  
D) The OS sets all priorities to maximum

**Correct Answer:** A

**Explanation:** The ceiling is the highest priority of any thread that might use the lock. Holder runs at ceiling, preventing preemption by lower-ceiling threads.

### Question 4
Which famous incident highlighted priority inversion?

A) Y2K bug  
B) Mars Pathfinder mission (1997)  
C) Heartbleed  
D) Spectre/Meltdown

**Correct Answer:** B

**Explanation:** Mars Pathfinder experienced priority inversion causing system resets. The fix was enabling priority inheritance in the RTOS.
