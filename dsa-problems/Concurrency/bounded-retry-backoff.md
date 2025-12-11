---
unique_problem_id: concurrency_014
display_id: CONCURRENCY-014
slug: bounded-retry-backoff
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Retry Patterns
  - Exponential Backoff
  - Fault Tolerance
  - Distributed Systems
---

# Bounded Retry with Exponential Backoff

## Problem Description

Implement retry logic with exponential backoff capped at a maximum delay for handling transient failures. Include jitter to prevent thundering herd.

## Examples

- Example 1:
  - Operation fails 2 times, then succeeds
  - Backoff sequence: 1ms delay, 2ms delay, then success on 3rd attempt

- Example 2:
  - Max delay = 1000ms, base = 100ms
  - Sequence: 100ms, 200ms, 400ms, 800ms, 1000ms (capped), 1000ms, ...
  - With jitter: 100±50ms, 200±100ms, etc.

- Example 3:
  - Max retries = 5, all fail
  - Output: Throw final exception after 5 attempts

## Constraints

- Configurable base delay, max delay, max retries
- Jitter recommended for distributed systems

## Function Signatures

### Java
```java
import java.util.concurrent.*;
import java.util.function.Supplier;
import java.util.Random;

class RetryWithBackoff {
    private final int maxRetries;
    private final long baseDelayMs;
    private final long maxDelayMs;
    private final Random random = new Random();
    
    public RetryWithBackoff(int maxRetries, long baseDelayMs, long maxDelayMs) {
        this.maxRetries = maxRetries;
        this.baseDelayMs = baseDelayMs;
        this.maxDelayMs = maxDelayMs;
    }
    
    public <T> T execute(Supplier<T> operation) throws Exception {
        // Implementation here
    }
}
```

### Python
```python
import time
import random
from typing import TypeVar, Callable

T = TypeVar('T')

class RetryWithBackoff:
    def __init__(self, max_retries: int, base_delay_ms: int, max_delay_ms: int):
        """
        Retry with exponential backoff.
        """
        self.max_retries = max_retries
        self.base_delay_ms = base_delay_ms
        self.max_delay_ms = max_delay_ms
    
    def execute(self, operation: Callable[[], T]) -> T:
        """Execute operation with retries on failure."""
        # Implementation here
        pass
```

### C++
```cpp
#include <functional>
#include <chrono>
#include <thread>
#include <random>

template<typename T>
class RetryWithBackoff {
public:
    RetryWithBackoff(int maxRetries, int baseDelayMs, int maxDelayMs)
        : maxRetries(maxRetries), baseDelayMs(baseDelayMs), maxDelayMs(maxDelayMs) {}
    
    T execute(std::function<T()> operation) {
        // Implementation here
    }
    
private:
    int maxRetries, baseDelayMs, maxDelayMs;
};
```

## Input Format

Configuration parameters and a simulated operation that fails N times before succeeding.

### Sample Input
```
max_retries=5 base_delay=100 max_delay=1000
failures_before_success=2
```

## Hints

Double the delay each retry (exponential). Cap at max_delay. Add random jitter (e.g., ±50% of current delay) to prevent synchronized retries across clients.

## Quiz

### Question 1
Why use exponential backoff instead of constant delay?

A) Simpler implementation  
B) Reduces load on failing service, allowing it to recover  
C) Guarantees success  
D) Uses less memory

**Correct Answer:** B

**Explanation:** Exponential backoff spreads out retries over time, reducing pressure on an overloaded or failing service, giving it time to recover.

### Question 2
Why add jitter to the delay?

A) For randomness  
B) To prevent multiple clients from retrying at exactly the same time  
C) To confuse attackers  
D) For debugging

**Correct Answer:** B

**Explanation:** Without jitter, synchronized failures cause synchronized retries (thundering herd), overwhelming the service again. Jitter staggers retries.

### Question 3
What happens when max delay is reached?

A) Retries stop  
B) Delay stays at max for subsequent retries instead of continuing to grow  
C) Exception is thrown  
D) Delay resets to base

**Correct Answer:** B

**Explanation:** The delay is capped at max_delay to prevent unreasonably long waits while still providing backoff benefit.

### Question 4
When should you NOT retry?

A) On transient network errors  
B) On permanent errors like authentication failure  
C) On timeout  
D) On rate limiting

**Correct Answer:** B

**Explanation:** Permanent errors (4xx auth errors, invalid input) won't be fixed by retrying. Only retry transient failures (5xx, timeouts, network issues).
