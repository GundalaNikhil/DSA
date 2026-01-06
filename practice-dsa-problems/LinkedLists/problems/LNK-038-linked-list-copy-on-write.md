---
problem_id: LNK_LINKED_LIST_COPY_ON_WRITE__7880
display_id: NTB-LNK-7880
slug: linked-list-copy-on-write
title: "Linked List with Copy-on-Write"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-copy-on-write
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Copy-on-Write

## Problem Statement

Each list version shares nodes with its parent until a modification occurs (copy-on-write). Version `0` is the initial list.

Operations:

- `CLONE v`: create a new version identical to version `v`
- `SET v pos x`: create a new version by setting position `pos` in version `v`
- `GET v pos`: output value at position `pos` in version `v`

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total nodes across versions <= 400000

## Clarifying Notes

- Each `CLONE` and `SET` creates a new version id in order.

## Example Input

```
3
1 2 3
4
CLONE 0
SET 1 2 9
GET 1 2
GET 0 2
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
    public List<Integer> processCopyOnWrite(int n, int[] initialList, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processCopyOnWrite(self, n: int, initial_list: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processCopyOnWrite(int n, vector<int>& initialList, vector<string>& operations) {
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
  processCopyOnWrite(n, initialList, operations) {
    // Your code here
    return [];
  }
}
```
