---
problem_id: LNK_LINKED_LIST_UNDO_REDO__9439
display_id: NTB-LNK-9439
slug: linked-list-undo-redo
title: "Linked List with Undo/Redo Stacks"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-undo-redo
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Undo/Redo Stacks

## Problem Statement

Maintain a list with undo/redo support for insertions and deletions.

Operations:

- `INS pos x`
- `DEL pos`
- `UNDO`
- `REDO`
- `GET pos`

Undo reverts the last successful `INS` or `DEL`. Redo reapplies the last undone operation. Any new `INS` or `DEL` clears the redo stack.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- `UNDO` or `REDO` with empty stack is ignored.
- Positions are 1-based at the time of operation.

## Example Input

```
3
1 2 3
5
INS 2 9
GET 2
UNDO
GET 2
REDO
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
    public List<Integer> processUndoRedo(int n, int[] initialList, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processUndoRedo(self, n: int, initial_list: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processUndoRedo(int n, vector<int>& initialList, vector<string>& operations) {
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
  processUndoRedo(n, initialList, operations) {
    // Your code here
    return [];
  }
}
```
