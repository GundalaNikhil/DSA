---
problem_id: LNK_LINKED_LIST_CHECKPOINTS__2112
display_id: NTB-LNK-2112
slug: linked-list-checkpoints
title: "Linked List with Checkpoints"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-checkpoints
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Checkpoints

## Problem Statement

Maintain a singly linked list that supports checkpoints and rollback.

Operations:

- `INS pos x`: insert value `x` at 1-based position `pos`
- `DEL pos`: delete node at position `pos`
- `CKPT id`: save a checkpoint with identifier `id`
- `ROLL id`: restore list to the state at checkpoint `id`
- `GET pos`: output the value at position `pos`, or `-1` if out of range

Checkpoints are persistent and can be reused multiple times.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total list size across all versions <= 300000

## Clarifying Notes

- Rollback restores the entire list to the checkpointed state.
- If a checkpoint id does not exist, ignore the `ROLL`.

## Example Input

```
3
1 2 3
5
CKPT 1
INS 2 9
GET 2
ROLL 1
GET 2
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
    public List<Integer> processCheckpoints(int n, int[] initialValues, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processCheckpoints(self, n: int, initial_values: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processCheckpoints(int n, vector<int>& initialValues, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} initialValues
   * @param {string[]} operations
   * @returns {number[]}
   */
  processCheckpoints(n, initialValues, operations) {
    // Your code here
    return [];
  }
}
```
