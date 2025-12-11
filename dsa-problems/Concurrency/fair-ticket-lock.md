---
unique_problem_id: concurrency_013
display_id: CONCURRENCY-013
slug: fair-ticket-lock
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Lock Fairness
  - Ticket Lock
  - FIFO Ordering
  - Cache Contention
---

# Fair Ticket Lock

## Problem Description

Implement a fair lock using a ticket dispenser and serving number mechanism. Threads acquire tickets in order and wait until their ticket number is being served. Discuss cache contention implications.

## Examples

- Example 1:
  - Threads A, B, C arrive in order
  - A gets ticket 0, B gets ticket 1, C gets ticket 2
  - Serving counter starts at 0
  - Output: A acquires lock, releases, serving becomes 1, B acquires, etc. FIFO order guaranteed.

- Example 2:
  - B finishes before A (but arrived later)
  - Output: Still FIFO - B waits for A to release first

- Example 3:
  - High contention: 100 threads spinning on serving counter
  - Output: Cache line bounces between cores, causing contention

## Constraints

- Must guarantee FIFO fairness
- Many concurrent threads

## Function Signatures

### Java
```java
import java.util.concurrent.atomic.AtomicInteger;

class FairTicketLock {
    private final AtomicInteger ticketDispenser = new AtomicInteger(0);
    private final AtomicInteger servingNow = new AtomicInteger(0);
    
    public void lock() {
        // Implementation here
    }
    
    public void unlock() {
        // Implementation here
    }
}
```

### Python
```python
import threading
import itertools

class FairTicketLock:
    def __init__(self):
        self._ticket_counter = itertools.count()
        self._serving = 0
        self._lock = threading.Lock()
    
    def acquire(self) -> None:
        """Acquire lock in FIFO order."""
        # Implementation here
        pass
    
    def release(self) -> None:
        """Release lock, advance serving counter."""
        # Implementation here
        pass
```

### C++
```cpp
#include <atomic>

class FairTicketLock {
public:
    void lock() {
        // Implementation here
    }
    
    void unlock() {
        // Implementation here
    }
    
private:
    std::atomic<int> ticketDispenser{0};
    std::atomic<int> servingNow{0};
};
```

## Input Format

This is a design/implementation problem demonstrating the ticket lock pattern.

## Hints

Ticket lock: atomically get next ticket, spin until serving == myTicket. Unlock by incrementing serving. Problem: all waiters spin on same cache line (servingNow), causing invalidation traffic.

## Quiz

### Question 1
Why is ticket lock considered "fair"?

A) All threads have equal CPU time  
B) Threads acquire the lock in the order they arrived (FIFO)  
C) It uses random selection  
D) Priority determines order

**Correct Answer:** B

**Explanation:** Ticket numbers are assigned in arrival order, and threads acquire the lock strictly in ticket order, ensuring FIFO.

### Question 2
What is the main performance issue with basic ticket locks?

A) Deadlock  
B) All waiting threads spin on the same memory location, causing cache contention  
C) Too many ticket numbers  
D) Complex implementation

**Correct Answer:** B

**Explanation:** All spinners read `servingNow`. When it updates, all cores must invalidate their cache line, causing a "thundering herd" of cache misses.

### Question 3
How can cache contention be reduced in ticket locks?

A) Use more tickets  
B) Use proportional backoff based on (myTicket - servingNow) distance  
C) Remove fairness  
D) Use bigger integers

**Correct Answer:** B

**Explanation:** If myTicket is far from servingNow, back off longer before checking again. MCS and CLH locks further improve by giving each waiter its own spin location.

### Question 4
What is the space complexity of a ticket lock?

A) O(n) where n is number of threads  
B) O(1) - just two counters  
C) O(log n)  
D) Depends on ticket size

**Correct Answer:** B

**Explanation:** Only two atomic integers (ticket dispenser and serving counter) are needed, regardless of the number of threads.
