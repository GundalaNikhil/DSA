---
unique_problem_id: concurrency_011
display_id: CONCURRENCY-011
slug: condvar-spurious-wakeup
version: 1.0.0
difficulty: Easy
topic_tags:
  - Concurrency
  - Condition Variables
  - Spurious Wakeup
  - Synchronization Patterns
---

# Condition Variable Spurious Wakeup Handling

## Problem Description

Demonstrate the correct wait loop pattern to handle spurious wakeups and missed signals when using condition variables.

## Examples

- Example 1:
  - Scenario: Shared flag is false, waiter blocks on condition variable
  - Another thread sets flag to true and signals
  - Output: Waiter must recheck the predicate (flag) after waking, as wakeup could be spurious

- Example 2:
  - Spurious wakeup: Thread wakes without signal
  - Output: Predicate is still false; thread re-enters wait

- Example 3:
  - Missed signal: Signal occurs before wait
  - Output: Predicate check catches this; thread doesn't wait because condition is already true

## Constraints

- Pattern must handle:
  - Spurious wakeups
  - Signals before wait
  - Multiple waiters

## Function Signatures

### Java
```java
import java.util.concurrent.locks.*;

class ConditionExample {
    private final Lock lock = new ReentrantLock();
    private final Condition condition = lock.newCondition();
    private boolean ready = false;
    
    public void waiter() throws InterruptedException {
        // Implementation here
    }
    
    public void signaler() {
        // Implementation here
    }
}
```

### Python
```python
import threading

class ConditionExample:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.ready = False
    
    def waiter(self) -> None:
        # Implementation here
        pass
    
    def signaler(self) -> None:
        # Implementation here
        pass
```

### C++
```cpp
#include <mutex>
#include <condition_variable>

class ConditionExample {
public:
    void waiter() {
        // Implementation here
    }
    
    void signaler() {
        // Implementation here
    }
    
private:
    std::mutex mutex;
    std::condition_variable cv;
    bool ready = false;
};
```

## Input Format

This is a design/pattern problem with no specific input format.

## Hints

Always use `while (!condition)` rather than `if (!condition)` when waiting. The loop handles both spurious wakeups and ensures the condition is true before proceeding.

## Quiz

### Question 1
Why must we use a while loop around wait() instead of if?

A) Performance optimization  
B) To handle spurious wakeups where wait() returns without a signal  
C) To prevent compiler optimization  
D) It's just convention

**Correct Answer:** B

**Explanation:** Condition variable can wake spuriously (no signal occurred). The while loop rechecks the predicate and re-waits if the condition isn't actually satisfied.

### Question 2
What is a "missed signal" problem?

A) Signal is lost in network  
B) Signal occurs before a thread calls wait(), so it never wakes up  
C) Signal is sent to the wrong thread  
D) Too many signals

**Correct Answer:** B

**Explanation:** If signal() is called before wait(), the signal is not "remembered." The predicate check before wait() prevents this: if condition is already true, don't wait.

### Question 3
Why check the predicate before entering wait()?

A) To avoid waiting when the condition is already satisfied  
B) To improve performance  
C) Required by the OS  
D) No reason, it's optional

**Correct Answer:** A

**Explanation:** The predicate might already be true (signal came earlier). Checking first avoids unnecessary waiting.

### Question 4
When should you use notify_all() vs notify()?

A) Always use notify()  
B) notify_all() when multiple threads may be waiting on different conditions  
C) They're identical  
D) notify_all() is slower and never needed

**Correct Answer:** B

**Explanation:** notify() wakes one waiter (may not be the right one). notify_all() wakes all, ensuring no waiter misses their condition. Use all() when waiters have different predicates.
