---
problem_id: LNK_LINKED_LIST_CIRCUIT_BREAKER__5514
display_id: NTB-LNK-5514
slug: linked-list-circuit-breaker
title: "Linked List with Circuit Breaker"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-circuit-breaker
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Circuit Breaker

## Problem Statement

Each modification can fail if a constraint is violated. If there are `F` consecutive failures, the circuit opens for `T` operations, during which all modifications are rejected.

Operations:

- `INS pos x`: insert if `x` is within [L, U]
- `DEL pos`: delete if `pos` exists
- `GET pos`: output value or `-1`

Inputs `L` and `U` define valid value range for insertions. Failures count only for `INS` and `DEL`.

## Input Format

- First line: integers `n`, `F`, `T`, `L`, `U`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `1 <= F <= 10`
- `0 <= T <= 200000`

## Clarifying Notes

- While circuit is open, all `INS` and `DEL` are rejected and do not count as failures.

## Example Input

```
2 2 2 1 5
3 4
5
INS 1 9
INS 1 9
INS 1 2
GET 1
DEL 5
```

## Example Output

```
3
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processCircuitBreaker(int n, int F, int T, int L, int U, int[] initialList, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processCircuitBreaker(self, n: int, F: int, T: int, L: int, U: int, initial_list: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processCircuitBreaker(int n, int F, int T, int L, int U, vector<int>& initialList, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} F
   * @param {number} T
   * @param {number} L
   * @param {number} U
   * @param {number[]} initialList
   * @param {string[]} operations
   * @returns {number[]}
   */
  processCircuitBreaker(n, F, T, L, U, initialList, operations) {
    // Your code here
    return [];
  }
}
```
