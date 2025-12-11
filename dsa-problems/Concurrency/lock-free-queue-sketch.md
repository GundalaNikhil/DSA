---
unique_problem_id: concurrency_010
display_id: CONCURRENCY-010
slug: lock-free-queue-sketch
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Lock-Free Data Structures
  - Michael-Scott Queue
  - Hazard Pointers
  - Memory Reclamation
---

# Lock-Free Queue Sketch

## Problem Description

Outline the Michael-Scott lock-free queue design with head/tail pointers. Discuss memory reclamation using hazard pointers or epoch-based reclamation to safely free dequeued nodes.

## Examples

- Example 1:
  - Operations: enqueue(A), enqueue(B), enqueue(C), dequeue(), dequeue()
  - Output: Dequeues return A, B in order

- Example 2:
  - Concurrent enqueues and dequeues
  - Output: All operations complete without locks; queue maintains FIFO order

- Example 3:
  - Memory reclamation scenario: Node X is dequeued but another thread still holds pointer
  - Output: Hazard pointer protects X until no thread references it

## Constraints

- Support many concurrent threads
- Lock-free guarantee (at least one thread makes progress)

## Function Signatures

### Java
```java
import java.util.concurrent.atomic.AtomicReference;

class Node<T> {
    T value;
    AtomicReference<Node<T>> next;
}

class LockFreeQueue<T> {
    private AtomicReference<Node<T>> head;
    private AtomicReference<Node<T>> tail;
    
    public LockFreeQueue() {
        // Implementation here
    }
    
    public void enqueue(T value) {
        // Implementation here
    }
    
    public T dequeue() {
        // Implementation here
    }
}
```

### Python
```python
from typing import TypeVar, Generic, Optional
import threading

T = TypeVar('T')

class LockFreeQueue(Generic[T]):
    """
    Note: True lock-free implementation requires atomic primitives
    not natively available in Python. This is a conceptual design.
    """
    
    def __init__(self):
        """Initialize with sentinel node."""
        pass
    
    def enqueue(self, value: T) -> None:
        """Lock-free enqueue at tail."""
        pass
    
    def dequeue(self) -> Optional[T]:
        """Lock-free dequeue from head. Returns None if empty."""
        pass
```

### C++
```cpp
#include <atomic>
#include <optional>

template<typename T>
struct Node {
    T value;
    std::atomic<Node<T>*> next;
};

template<typename T>
class LockFreeQueue {
public:
    LockFreeQueue();
    
    void enqueue(T value);
    std::optional<T> dequeue();
    
private:
    std::atomic<Node<T>*> head;
    std::atomic<Node<T>*> tail;
    // Implementation here
};
```

## Input Format

The input will be provided as:
- Commands: ENQ value | DEQ

### Sample Input
```
ENQ A
ENQ B
DEQ
DEQ
```

## Hints

Key invariant: tail.next is either null (tail is true tail) or points to a node to be linked. Multiple threads may help advance tail. Use hazard pointers to protect nodes being accessed.

## Quiz

### Question 1
What is a sentinel node in the queue?

A) A node that stores important data  
B) A dummy node that simplifies edge cases (empty queue)  
C) A node that locks the queue  
D) The last node in the queue

**Correct Answer:** B

**Explanation:** A sentinel/dummy node means head and tail are never null, simplifying the enqueue/dequeue logic for empty queue cases.

### Question 2
Why is memory reclamation challenging in lock-free structures?

A) Memory is expensive  
B) Another thread may hold a reference to a "deleted" node  
C) Lock-free means no memory management  
D) It's not challenging

**Correct Answer:** B

**Explanation:** After dequeue, another thread might still be reading the old node. Freeing it immediately causes use-after-free. Safe reclamation schemes like hazard pointers solve this.

### Question 3
What is the core idea of hazard pointers?

A) Threads publish which nodes they're accessing; nodes aren't freed while someone's accessing them  
B) Pointers that are dangerous  
C) Encrypted pointers  
D) Double pointers

**Correct Answer:** A

**Explanation:** Each thread publishes its currently-accessed node(s). Before freeing a node, check no hazard pointer points to it.

### Question 4
What progress guarantee does Michael-Scott queue provide?

A) Wait-free  
B) Lock-free (some thread always makes progress)  
C) Obstruction-free  
D) None

**Correct Answer:** B

**Explanation:** The Michael-Scott queue is lock-free: even if some threads stall, at least one thread can complete its operation.
