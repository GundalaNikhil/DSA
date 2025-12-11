---
unique_problem_id: concurrency_005
display_id: CONCURRENCY-005
slug: semaphore-rate-limiter
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Semaphores
  - Rate Limiting
  - Token Bucket
  - Throttling
---

# Semaphore-Based Rate Limiter

## Problem Description

Implement a rate limiter that allows at most `k` events per second. Use semaphores/tokens and a refill mechanism (thread or timer) to replenish permits.

## Examples

- Example 1:
  - Input: k = 2 events/second
  - Events at t = 0s, 0s, 0.5s, 1.2s
  - Output: First two events at t=0 proceed immediately. Third event at t=0.5s blocks. At t=1s, permits refill. Third event proceeds. Fourth event at t=1.2s uses newly available permit.

- Example 2:
  - Input: k = 5 events/second
  - 3 events arrive simultaneously
  - Output: All 3 proceed immediately (5 permits available)

- Example 3:
  - Input: k = 1 event/second
  - Events at t = 0, 0.1, 0.5, 1.0, 1.1
  - Output: Events at 0, 1.0 proceed immediately. Events at 0.1, 0.5 wait for refill. Event at 1.1 waits for next refill at t=2.

## Constraints

- `1 <= k <= 10^6` events per second
- Concurrent access from multiple threads

## Function Signatures

### Java
```java
import java.util.concurrent.Semaphore;

class SemaphoreRateLimiter {
    private final Semaphore permits;
    private final int maxPermits;
    
    public SemaphoreRateLimiter(int k) {
        // Implementation here
    }
    
    public void acquire() throws InterruptedException {
        // Implementation here
    }
    
    public boolean tryAcquire() {
        // Implementation here
    }
}
```

### Python
```python
import threading
import time

class SemaphoreRateLimiter:
    def __init__(self, k: int):
        """
        Rate limiter allowing k events per second.
        
        Args:
            k: Maximum events per second
        """
        pass
    
    def acquire(self) -> None:
        """Block until rate limit allows proceeding."""
        pass
    
    def try_acquire(self) -> bool:
        """Non-blocking attempt. Returns True if allowed, False if rate limited."""
        pass
```

### C++
```cpp
#include <semaphore>
#include <thread>
#include <chrono>

class SemaphoreRateLimiter {
public:
    SemaphoreRateLimiter(int k);  // k permits per second
    
    void acquire();     // Implementation here
    bool tryAcquire();  // Implementation here
    
private:
    std::counting_semaphore<> permits;
    int maxPermits;
    std::thread refillThread;
};
```

## Input Format

The input will be provided as:
- First line: Integer k (rate limit per second)
- Following lines: Event arrival times

### Sample Input
```
2
0 0 0.5 1.2
```

## Hints

Use a semaphore initialized to k. A background timer/thread refills permits to k every second (or pro-rata). Consider edge cases around burst capacity.

## Quiz

### Question 1
Why use semaphores for rate limiting?

A) They're faster than mutexes  
B) They naturally model a pool of permits that can be acquired and released  
C) They're required by POSIX  
D) They prevent deadlocks

**Correct Answer:** B

**Explanation:** Semaphores maintain a count of available resources (permits). acquire() decrements, release() increments. Perfect for modeling quotas.

### Question 2
What is the refill strategy for a token bucket?

A) Add k tokens every second, cap at k  
B) Replace all tokens with k every second  
C) Never refill, only consume  
D) Double the tokens each second

**Correct Answer:** A

**Explanation:** Token bucket adds tokens at a fixed rate (k/second) up to a maximum (bucket capacity). This allows bursts up to the bucket size.

### Question 3
What happens if tryAcquire fails?

A) The system crashes  
B) The call blocks forever  
C) It returns immediately with failure (false)  
D) It waits for a short time

**Correct Answer:** C

**Explanation:** tryAcquire is non-blocking. If no permit is available, it immediately returns false rather than waiting.

### Question 4
How do you handle rate limiting across distributed systems?

A) Use local semaphores  
B) Use a centralized rate limiting service or distributed algorithm  
C) Rate limiting is impossible in distributed systems  
D) Ignore the problem

**Correct Answer:** B

**Explanation:** Distributed rate limiting requires coordination, typically via a central service (like Redis) or distributed consensus algorithms.
