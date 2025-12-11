---
unique_problem_id: concurrency_003
display_id: CONCURRENCY-003
slug: readers-writers-lease
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Readers-Writers Problem
  - Lease-based Locking
  - Lock Fairness
  - Read-Write Locks
---

# Readers-Writers with Lease Expiry

## Problem Description

Implement a readers-writers lock where each reader holds a lease for time `L`. After the lease expires, the reader must renew or release the lock. Writers must wait for all active leases to expire or readers to release. Design the algorithm to ensure writers don't starve.

## Examples

- Example 1:
  - Input: Readers acquire with L = 50ms, writer arrives at 20ms, readers consider renewal
  - Output: Writer proceeds after reader leases end (50ms); no starvation
  - Explanation: Even if readers want to renew, once a writer is waiting, renewals are blocked to ensure the writer eventually gets access.

- Example 2:
  - Input: Multiple readers with L = 100ms, no writers
  - Output: Readers can freely renew indefinitely
  - Explanation: Without writers waiting, readers simply renew their leases.

- Example 3:
  - Input: Reader lease = 10ms, writer arrives, reader releases at 8ms
  - Output: Writer proceeds immediately after reader releases

## Constraints

- Many concurrent threads (readers and writers)
- Lease times up to seconds
- Writers should not starve

## Function Signatures

### Java
```java
import java.util.concurrent.locks.*;

class LeaseReadWriteLock {
    private final long leaseMs;
    
    public LeaseReadWriteLock(long leaseMs) {
        // Implementation here
    }
    
    public void acquireRead() {
        // Implementation here
    }
    
    public boolean renewRead() {
        // Implementation here
    }
    
    public void releaseRead() {
        // Implementation here
    }
    
    public void acquireWrite() {
        // Implementation here
    }
    
    public void releaseWrite() {
        // Implementation here
    }
}
```

### Python
```python
import threading
import time

class LeaseReadWriteLock:
    def __init__(self, lease_ms: int):
        """
        Readers-writers lock with lease-based read access.
        
        Args:
            lease_ms: Duration of each read lease in milliseconds
        """
        pass
    
    def acquire_read(self) -> None:
        """Acquire a read lease."""
        pass
    
    def renew_read(self) -> bool:
        """Attempt to renew lease. Returns False if writer waiting."""
        pass
    
    def release_read(self) -> None:
        """Release the read lease."""
        pass
    
    def acquire_write(self) -> None:
        """Acquire exclusive write access, waiting for readers."""
        pass
    
    def release_write(self) -> None:
        """Release write lock."""
        pass
```

### C++
```cpp
#include <mutex>
#include <condition_variable>
#include <chrono>

class LeaseReadWriteLock {
public:
    LeaseReadWriteLock(int leaseMs);
    
    void acquireRead();
    bool renewRead();  // Returns false if writer waiting
    void releaseRead();
    
    void acquireWrite();
    void releaseWrite();
};
```

## Input Format

The input will be provided as:
- First line: Lease duration L in milliseconds
- Following lines: Thread actions (READ_ACQUIRE, READ_RENEW, READ_RELEASE, WRITE_ACQUIRE, WRITE_RELEASE)

### Sample Input
```
50
READ_ACQUIRE thread1
WRITE_ACQUIRE thread2
READ_RENEW thread1
```

## Hints

Use a counter for active readers and a "writer waiting" flag. When a writer is waiting, deny new read acquisitions and renewals to prevent writer starvation.

## Quiz

### Question 1
Why use lease-based locks instead of simple read locks?

A) Better performance  
B) Limits how long a reader can hold the lock, ensuring bounded writer wait time  
C) Reduces memory usage  
D) Simplifies the API

**Correct Answer:** B

**Explanation:** Leases ensure that even if a reader stalls or forgets to release, the lock automatically expires, bounding writer wait time.

### Question 2
How do we prevent writer starvation?

A) Give writers higher priority  
B) Block new reader acquisitions/renewals when a writer is waiting  
C) Limit the number of readers  
D) Use timeouts on readers

**Correct Answer:** B

**Explanation:** When a writer signals intent, we stop allowing new readers or renewals, ensuring the writer will eventually get access.

### Question 3
What happens if a reader's lease expires without renewal?

A) The reader is killed  
B) The reader loses its lock automatically; access is no longer valid  
C) Nothing, the reader keeps the lock  
D) The system deadlocks

**Correct Answer:** B

**Explanation:** Expired leases are automatically released. The reader must check if renewal succeeded before continuing.

### Question 4
Can multiple writers hold the lock simultaneously?

A) Yes, that's the point of read-write locks  
B) No, writers need exclusive access  
C) Only if they agree to  
D) Depends on implementation

**Correct Answer:** B

**Explanation:** The "write" in readers-writers means exclusive access. Multiple readers are allowed, but only one writer.
