---
unique_problem_id: concurrency_008
display_id: CONCURRENCY-008
slug: threadpool-work-stealing
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Thread Pool
  - Work Stealing
  - Load Balancing
  - Deque
---

# Thread Pool with Work Stealing

## Problem Description

Design a work-stealing thread pool where each worker has its own deque of tasks. Workers process their own tasks from the "hot" end (LIFO for locality). Idle workers steal tasks from the "cold" end of other workers' deques (FIFO to avoid contention with the owner).

## Examples

- Example 1:
  - Input: 4 workers, tasks distributed unevenly (worker 1 has 100 tasks, others have 0)
  - Output: Idle workers steal from worker 1's queue; balanced completion time

- Example 2:
  - Input: 2 workers, tasks arrive dynamically
  - Output: Each worker processes own tasks; when idle, steals from the other

- Example 3:
  - Input: 1 worker, no stealing possible
  - Output: Pure LIFO task execution

## Constraints

- Number of workers: configurable
- Total tasks up to 10^6

## Function Signatures

### Java
```java
import java.util.concurrent.*;
import java.util.function.Supplier;

class WorkStealingPool {
    private final int numWorkers;
    private final Deque<Runnable>[] queues;  // One per worker
    
    public WorkStealingPool(int numWorkers) {
        // Implementation here
    }
    
    public void submit(int preferredWorker, Runnable task) {
        // Implementation here
    }
    
    public <T> Future<T> submit(int preferredWorker, Callable<T> task) {
        // Implementation here
    }
    
    public void shutdown() {
        // Implementation here
    }
}
```

### Python
```python
import threading
from collections import deque
from typing import Callable, Any, List

class WorkStealingPool:
    def __init__(self, num_workers: int):
        """
        Work-stealing thread pool.
        
        Args:
            num_workers: Number of worker threads
        """
        pass
    
    def submit(self, preferred_worker: int, task: Callable[[], Any]) -> None:
        """Submit a task to a preferred worker's queue."""
        pass
    
    def shutdown(self) -> None:
        """Gracefully shutdown the pool."""
        pass
```

### C++
```cpp
#include <deque>
#include <vector>
#include <thread>
#include <functional>
#include <mutex>

class WorkStealingPool {
public:
    WorkStealingPool(int numWorkers);
    
    void submit(int preferredWorker, std::function<void()> task);
    void shutdown();
    
private:
    std::vector<std::deque<std::function<void()>>> queues;
    std::vector<std::thread> workers;
    std::vector<std::mutex> queueLocks;
};
```

## Input Format

The input will be provided as:
- First line: Number of workers
- Following lines: Task submissions with preferred worker

### Sample Input
```
4
SUBMIT 0 task1
SUBMIT 0 task2
SUBMIT 0 task3
```

## Hints

Use double-ended queues (deques). Owner takes from one end (LIFO - good cache locality), thieves steal from the opposite end (reduces contention). Use lock-free or fine-grained locking for the deque.

## Quiz

### Question 1
Why do owners pop from one end and thieves from the other?

A) To confuse the implementation  
B) Reduces contention between owner and thieves  
C) It's required by the OS  
D) No particular reason

**Correct Answer:** B

**Explanation:** Owner works LIFO (good locality), thieves work FIFO (opposite end). Less contention since they access different ends of the deque.

### Question 2
What is the advantage of work stealing over a global task queue?

A) Simpler implementation  
B) Better cache locality and reduced contention  
C) Fewer threads  
D) Guaranteed ordering

**Correct Answer:** B

**Explanation:** Each worker primarily works on its own queue (cache-local), and only occasionally steals, reducing contention on a central queue.

### Question 3
In Java, which built-in pool uses work stealing?

A) ThreadPoolExecutor  
B) ForkJoinPool  
C) ScheduledThreadPoolExecutor  
D) None of them

**Correct Answer:** B

**Explanation:** ForkJoinPool uses work stealing for parallel stream operations and fork-join tasks.

### Question 4
What data structure is ideal for work stealing?

A) Array  
B) Singly-linked list  
C) Double-ended queue (deque)  
D) Priority queue

**Correct Answer:** C

**Explanation:** Deque allows efficient operations at both ends: push/pop at owner's end, steal from the opposite end.
