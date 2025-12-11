---
unique_problem_id: concurrency_002
display_id: CONCURRENCY-002
slug: producer-consumer-priority-aging
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Producer-Consumer
  - Priority Queue
  - Thread Safety
  - Starvation Prevention
  - Condition Variables
---

# Producer-Consumer with Priority and Aging

## Problem Description

Design a bounded, thread-safe priority queue with multiple producers and consumers. Higher priority numbers indicate higher priority. Producers block when the queue is full. To prevent starvation, implement aging: after `T` milliseconds in the queue, an item's priority increases by 1. Avoid lost wakeups.

## Examples

- Example 1:
  - Input: Buffer size = 2, T = 100ms
    - Producer adds item with priority 1
    - Producer adds item with priority 5
    - Producer with priority 2 blocks (buffer full)
    - After 100ms, first item ages to priority 2
    - Consumer dequeues
  - Output: Consumers receive items in priority order: [5, 2 (aged from 1), ...]

- Example 2:
  - Input: Buffer size = 3, T = 50ms
    - Items with priorities [3, 1, 2] enter
    - After 50ms: priorities become [4, 2, 3]
    - Consumer dequeues highest
  - Output: Consumer gets priority 4 (originally 3)

- Example 3:
  - Input: Buffer size = 1, no aging (T = ∞)
  - Output: Simple bounded buffer behavior with priority ordering

## Constraints

- Buffer size up to 10^6
- Multiple concurrent producers and consumers
- T (aging interval) is given

## Function Signatures

### Java
```java
import java.util.concurrent.*;

class PriorityBlockingBuffer<T> {
    private final int capacity;
    private final long agingIntervalMs;
    
    public PriorityBlockingBuffer(int capacity, long agingIntervalMs) {
        // Implementation here
    }
    
    public void produce(T item, int priority) throws InterruptedException {
        // Implementation here
    }
    
    public T consume() throws InterruptedException {
        // Implementation here
    }
}
```

### Python
```python
import threading
import heapq
from typing import TypeVar, Generic
from dataclasses import dataclass
import time

T = TypeVar('T')

class PriorityBlockingBuffer(Generic[T]):
    def __init__(self, capacity: int, aging_interval_ms: int):
        """
        Thread-safe priority queue with aging.
        
        Args:
            capacity: Maximum number of items
            aging_interval_ms: Milliseconds after which priority increases
        """
        pass
    
    def produce(self, item: T, priority: int) -> None:
        """Add item with given priority, block if full."""
        pass
    
    def consume(self) -> T:
        """Remove and return highest priority item, block if empty."""
        pass
```

### C++
```cpp
#include <queue>
#include <mutex>
#include <condition_variable>

class PriorityBlockingBuffer {
public:
    PriorityBlockingBuffer(int capacity, int agingIntervalMs);
    
    void produce(T item, int priority);  // Implementation here
    T consume();  // Implementation here
    
private:
    // Implementation here
};
```

## Input Format

The input will be provided as:
- Configuration line: Buffer size and aging interval T
- Commands: PRODUCE item priority | CONSUME

### Sample Input
```
2 100
PRODUCE A 1
PRODUCE B 5
CONSUME
```

## Hints

Use a condition variable for full/empty signaling. For aging, either use lazy evaluation (calculate effective priority at dequeue time) or a background timer.

## Quiz

### Question 1
Why is aging important in a priority queue?

A) To improve performance  
B) To prevent low-priority items from being starved indefinitely  
C) To reduce memory usage  
D) To simplify the implementation

**Correct Answer:** B

**Explanation:** Without aging, low-priority items might never be processed if high-priority items keep arriving. Aging ensures all items eventually get served.

### Question 2
What is a "lost wakeup" in producer-consumer?

A) A thread that never terminates  
B) A signal/notify that occurs when no thread is waiting, causing it to be missed  
C) A thread that loses its priority  
D) A deadlock situation

**Correct Answer:** B

**Explanation:** Lost wakeup happens when notify() is called before wait(). Proper synchronization with while-loops (not if) around wait prevents this.

### Question 3
How can aging be implemented efficiently?

A) Modify all items' priorities every T milliseconds  
B) Store insertion time and compute effective priority lazily at dequeue  
C) Use a separate thread for each item  
D) Ignore aging for performance

**Correct Answer:** B

**Explanation:** Lazy evaluation: store (insertionTime, basePriority) and compute effectivePriority = basePriority + (now - insertionTime) / T at comparison time.

### Question 4
What synchronization primitives are needed?

A) Only mutex  
B) Mutex and one condition variable  
C) Mutex and two condition variables (not-full, not-empty)  
D) Only semaphores

**Correct Answer:** C

**Explanation:** We need: mutex for exclusive access, condvar for "not full" (producers wait), condvar for "not empty" (consumers wait).
