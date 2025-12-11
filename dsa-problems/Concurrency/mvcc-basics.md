---
unique_problem_id: concurrency_016
display_id: CONCURRENCY-016
slug: mvcc-basics
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - MVCC
  - Database Concurrency
  - Snapshot Isolation
  - Transaction Management
---

# Multiversion Concurrency Control Basics

## Problem Description

Describe MVCC (Multiversion Concurrency Control) read/write rules to avoid blocking readers. Explain how write-write conflicts are handled and how transactions see consistent snapshots.

## Examples

- Example 1:
  - Two concurrent transactions T1 (read X) and T2 (write X)
  - Without MVCC: T1 blocks waiting for T2's lock
  - With MVCC: T1 reads old version of X, T2 writes new version
  - Output: Readers never block; T1 sees pre-T2 snapshot

- Example 2:
  - T1 writes X, T2 writes X (write-write conflict)
  - Output: One aborts (first committer wins) or serialized based on isolation level

- Example 3:
  - Long-running read transaction sees consistent snapshot throughout
  - Even if other transactions commit changes
  - Output: Read-only transaction never sees partial updates

## Constraints

- Transaction isolation levels (READ COMMITTED, SNAPSHOT, SERIALIZABLE)
- Version storage and garbage collection considerations

## Function Signatures

### Java
```java
import java.util.concurrent.*;

// Conceptual MVCC store
class MVCCStore<K, V> {
    // Implementation here
    
    public V read(K key, long txnTimestamp) {
        // Implementation here
    }
    
    public void write(K key, V value, long txnTimestamp) {
        // Implementation here
    }
    
    public void commit(long txnTimestamp) {
        // Implementation here
    }
    
    public void abort(long txnTimestamp) {
        // Implementation here
    }
}
```

### Python
```python
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass
from threading import Lock

K = TypeVar('K')
V = TypeVar('V')

@dataclass
class Version:
    value: any
    write_ts: int
    commit_ts: Optional[int]

class MVCCStore(Generic[K, V]):
    """
    Multiversion concurrency control key-value store.
    """
    
    def read(self, key: K, txn_timestamp: int) -> Optional[V]:
        """Read latest committed version visible to this transaction."""
        pass
    
    def write(self, key: K, value: V, txn_timestamp: int) -> None:
        """Write a new version (uncommitted until commit)."""
        pass
    
    def commit(self, txn_timestamp: int) -> bool:
        """Commit transaction. Returns False on conflict."""
        pass
    
    def abort(self, txn_timestamp: int) -> None:
        """Abort and discard uncommitted versions."""
        pass
```

### C++
```cpp
#include <map>
#include <vector>
#include <optional>
#include <mutex>

template<typename K, typename V>
class MVCCStore {
public:
    std::optional<V> read(const K& key, long txnTimestamp);
    void write(const K& key, const V& value, long txnTimestamp);
    bool commit(long txnTimestamp);  // False on conflict
    void abort(long txnTimestamp);
    
private:
    // Implementation here
};
```

## Input Format

Transaction operations in sequence showing read/write patterns.

### Sample Input
```
BEGIN T1
BEGIN T2
READ T1 X
WRITE T2 X 100
COMMIT T2
READ T1 X
COMMIT T1
```

## Hints

Readers see a snapshot at their start timestamp. Writers create new versions. Write-write conflicts detected at commit (first-committer-wins or abort). Old versions garbage collected when no transaction can read them.

## Quiz

### Question 1
How does MVCC achieve non-blocking reads?

A) Readers acquire exclusive locks  
B) Readers access old versions while writers create new versions  
C) Writes are buffered until reads complete  
D) Readers and writers use separate databases

**Correct Answer:** B

**Explanation:** MVCC keeps multiple versions. Readers access the appropriate old version for their snapshot, while writers create new versions. No blocking needed.

### Question 2
What is snapshot isolation?

A) Taking periodic backups  
B) Each transaction sees a consistent snapshot as of its start time  
C) Isolating the database from the network  
D) Running only one transaction at a time

**Correct Answer:** B

**Explanation:** In snapshot isolation, a transaction sees all commits that happened before it started, and none that happened after, providing a consistent view.

### Question 3
How are write-write conflicts handled in MVCC?

A) Both writes succeed  
B) First-committer-wins; second transaction aborts and retries  
C) Writes are merged  
D) The database crashes

**Correct Answer:** B

**Explanation:** When two transactions write the same key, the first to commit succeeds. The second detects the conflict at commit time and aborts.

### Question 4
Why is garbage collection important in MVCC?

A) To free memory by removing old versions no longer needed by any transaction  
B) To improve write speed  
C) To encrypt old data  
D) It's not important

**Correct Answer:** A

**Explanation:** Without GC, versions accumulate indefinitely. Old versions can be deleted once no active transaction has a snapshot timestamp that could read them.
