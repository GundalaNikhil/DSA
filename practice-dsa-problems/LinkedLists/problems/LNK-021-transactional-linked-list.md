---
problem_id: LNK_TRANSACTIONAL_LINKED_LIST__3107
display_id: NTB-LNK-3107
slug: transactional-linked-list
title: "Transactional Linked List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
  - transactional-linked-list
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Transactional Linked List

## Problem Statement

Maintain a linked list with transactional support. Operations inside an active transaction are staged until commit.

Operations:

- `BEGIN`: start a new transaction (can be nested)
- `COMMIT`: commit the most recent transaction
- `ROLLBACK`: discard the most recent transaction
- `INS pos x`: insert value `x` at position `pos`
- `DEL pos`: delete node at position `pos`
- `GET pos`: output value at position `pos` in the current visible state

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total nodes across all committed states <= 400000

## Clarifying Notes

- `COMMIT` with no active transaction is ignored.
- `ROLLBACK` with no active transaction is ignored.
- Nested transactions commit into their parent, not directly into the base list.

## Example Input

```
3
1 2 3
6
BEGIN
INS 2 9
GET 2
ROLLBACK
GET 2
COMMIT
```

## Example Output

```
9
2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processTransactionalList(int n, int[] initialList, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processTransactionalList(self, n: int, initial_list: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processTransactionalList(int n, vector<int>& initialList, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} initialList
   * @param {string[]} operations
   * @returns {number[]}
   */
  processTransactionalList(n, initialList, operations) {
    // Your code here
    return [];
  }
}
```
