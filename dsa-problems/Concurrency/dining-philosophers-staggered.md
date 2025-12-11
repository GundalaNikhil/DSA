---
unique_problem_id: concurrency_007
display_id: CONCURRENCY-007
slug: dining-philosophers-staggered
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Dining Philosophers
  - Deadlock Prevention
  - Resource Ordering
  - Lock Hierarchies
---

# Dining Philosophers with Staggered Seating

## Problem Description

Five philosophers sit around a table, but forks are asymmetric: some forks require two hands (cannot hold another fork simultaneously). Design a protocol to avoid deadlock and starvation when some forks are two-handed and some are normal. Philosophers know the fork types.

## Examples

- Example 1:
  - Input: 5 philosophers, forks: [normal, two-hand, normal, two-hand, normal]
  - Output: Protocol using resource ordering: philosophers acquire lower-numbered fork first, but two-hand forks block acquiring any other fork simultaneously. Use hierarchical locking.

- Example 2:
  - Input: All forks are normal
  - Output: Classic solution: one philosopher picks right fork first (breaks circular wait)

- Example 3:
  - Input: All forks are two-handed
  - Output: Only one philosopher can eat at a time (essentially a global mutex on eating)

## Constraints

- Number of philosophers <= 10^4
- Mix of normal and two-handed forks

## Function Signatures

### Java
```java
import java.util.concurrent.locks.*;

class DiningPhilosophers {
    private final boolean[] isTwoHanded;  // Fork properties
    private final Lock[] forks;
    
    public DiningPhilosophers(int n, boolean[] twoHandedForks) {
        // Implementation here
    }
    
    public void eat(int philosopher) throws InterruptedException {
        // Implementation here
    }
    
    public void think(int philosopher) {
        // Implementation here
    }
}
```

### Python
```python
import threading
from typing import List

class DiningPhilosophers:
    def __init__(self, n: int, two_handed_forks: List[bool]):
        """
        Initialize dining philosophers problem.
        
        Args:
            n: Number of philosophers
            two_handed_forks: True if fork[i] requires two hands
        """
        pass
    
    def eat(self, philosopher: int) -> None:
        """Philosopher attempts to eat (acquire forks, eat, release)."""
        pass
    
    def think(self, philosopher: int) -> None:
        """Philosopher thinks (no resources needed)."""
        pass
```

### C++
```cpp
#include <vector>
#include <mutex>

class DiningPhilosophers {
public:
    DiningPhilosophers(int n, const std::vector<bool>& twoHandedForks);
    
    void eat(int philosopher);
    void think(int philosopher);
    
private:
    std::vector<std::mutex> forks;
    std::vector<bool> isTwoHanded;
};
```

## Input Format

The input will be provided as:
- First line: Integer n (number of philosophers)
- Second line: Fork types (0 = normal, 1 = two-handed) for n forks

### Sample Input
```
5
0 1 0 1 0
```

## Hints

Combine resource ordering (acquire lower-numbered fork first) with special handling for two-handed forks. A two-handed fork acquisition must release any held fork first.

## Quiz

### Question 1
What is the classic deadlock scenario in dining philosophers?

A) All philosophers grab their right fork first, then wait for left  
B) One philosopher hoards all forks  
C) Philosophers never attempt to eat  
D) Forks break

**Correct Answer:** A

**Explanation:** If all grab right, all wait for left, none can proceed. This circular wait causes deadlock.

### Question 2
How does resource ordering prevent deadlock?

A) It makes forks move faster  
B) It breaks the circular wait by ensuring a global acquisition order  
C) It prevents philosophers from eating  
D) It adds more forks

**Correct Answer:** B

**Explanation:** If everyone acquires the lower-numbered fork first, no cycle can form in the resource graph.

### Question 3
What is the constraint of a two-handed fork?

A) It can only be used by two philosophers  
B) When holding it, the philosopher cannot hold any other fork  
C) It requires both hands to pick up  
D) It's heavier than normal forks

**Correct Answer:** B

**Explanation:** A two-handed fork blocks the holder from acquiring any other fork simultaneously, as both hands are occupied.

### Question 4
How does the asymmetric fork problem change the classic solution?

A) It doesn't change anything  
B) Two-handed forks add constraints that require adapted protocols  
C) The problem becomes impossible  
D) Only even-numbered philosophers can eat

**Correct Answer:** B

**Explanation:** Two-handed forks mean some philosophers effectively need exclusive access to their section, requiring more careful coordination.
