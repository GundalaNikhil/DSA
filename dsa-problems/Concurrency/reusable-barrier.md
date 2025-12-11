---
unique_problem_id: concurrency_004
display_id: CONCURRENCY-004
slug: reusable-barrier
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Barrier Synchronization
  - Condition Variables
  - Semaphores
  - Thread Coordination
---

# Reusable Barrier

## Problem Description

Implement a reusable barrier for N threads using condition variables or semaphores. All N threads must arrive before any can proceed. The barrier should be reusable across multiple phases without re-initialization.

## Examples

- Example 1:
  - Input: N = 3 threads, 2 phases
  - Phase 1: Threads 1, 2, 3 arrive → all released
  - Phase 2: Same threads arrive again → all released again
  - Output: All threads synchronized at each phase boundary

- Example 2:
  - Input: N = 2 threads
  - Thread 1 arrives → blocks
  - Thread 2 arrives → both released
  - Output: Both threads proceed together

- Example 3:
  - Input: N = 1 thread
  - Output: Thread proceeds immediately (trivial barrier)

## Constraints

- `1 <= N <= 10,000`
- Barrier must be reusable for multiple synchronization points

## Function Signatures

### Java
```java
import java.util.concurrent.locks.*;

class ReusableBarrier {
    private final int parties;
    private int count;
    private int phase;
    
    public ReusableBarrier(int n) {
        // Implementation here
    }
    
    public void await() throws InterruptedException {
        // Implementation here
    }
}
```

### Python
```python
import threading

class ReusableBarrier:
    def __init__(self, n: int):
        """
        Create a reusable barrier for n threads.
        
        Args:
            n: Number of threads to synchronize
        """
        pass
    
    def await(self) -> None:
        """
        Wait for all threads to arrive, then proceed together.
        Automatically resets for the next phase.
        """
        pass
```

### C++
```cpp
#include <mutex>
#include <condition_variable>

class ReusableBarrier {
public:
    ReusableBarrier(int n);
    
    void await();  // Implementation here
    
private:
    int parties;
    int count;
    int phase;
    std::mutex mutex;
    std::condition_variable cv;
};
```

## Input Format

The input will be provided as:
- First line: Integer N (number of threads)
- Commands simulating thread arrivals at barrier

### Sample Input
```
3
ARRIVE thread1
ARRIVE thread2
ARRIVE thread3
```

## Hints

Track arrival count and a phase number. When the last thread arrives, increment phase and broadcast. Other threads wait while their observed phase matches current phase and count < N.

## Quiz

### Question 1
Why is a phase counter needed for reusability?

A) To track execution time  
B) To distinguish between old waiters (from last phase) and new arrivals  
C) To count the number of uses  
D) To implement timeout

**Correct Answer:** B

**Explanation:** Without a phase counter, threads released from the barrier might re-enter and interfere with freshly waiting threads. The phase distinguishes iterations.

### Question 2
What is the "barrier broken" scenario?

A) When too many threads arrive  
B) When a thread is interrupted while waiting  
C) When the barrier is never used  
D) When threads arrive too quickly

**Correct Answer:** B

**Explanation:** If a thread waiting at the barrier is interrupted, the barrier might not reach N arrivals, breaking synchronization.

### Question 3
How does broadcasting work in the barrier?

A) The first arriving thread notifies all  
B) The last arriving thread (Nth) notifies all waiting threads  
C) Each thread notifies the next  
D) No notification needed

**Correct Answer:** B

**Explanation:** When the Nth thread arrives, it broadcasts/notifies all, waking them to proceed past the barrier.

### Question 4
Can barriers be used for iterative algorithms like parallel matrix computation?

A) No, barriers are one-time use  
B) Yes, reusable barriers synchronize phases of iterative algorithms  
C) Only with special modifications  
D) Barriers are not for algorithms

**Correct Answer:** B

**Explanation:** Iterative parallel algorithms often synchronize at each iteration. Reusable barriers perfectly fit this pattern.
