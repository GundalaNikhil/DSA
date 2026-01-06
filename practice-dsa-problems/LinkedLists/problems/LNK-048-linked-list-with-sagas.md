---
problem_id: LNK_LINKED_LIST_WITH_SAGAS__7503
display_id: NTB-LNK-7503
slug: linked-list-with-sagas
title: "Linked List with Sagas"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-with-sagas
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Sagas

## Problem Statement

Operations are grouped into sagas. If any step in a saga fails, all previous steps in that saga must be compensated in reverse order.

Steps:

- `INS pos x` (compensation: delete that position)
- `DEL pos` (compensation: re-insert the deleted value at that position)

You are given a sequence of steps with saga ids. A step fails if its position is invalid.

Output the final list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: `saga_id type pos [x]`

## Output Format

- One line: final list values

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Compensation restores list state as if the failed saga never executed.

## Example Input

```
3
1 2 3
3
1 INS 2 9
1 DEL 5
1 INS 2 7
```

## Example Output

```
1 2 3
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processSagas(int n, int[] initialList, int q, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processSagas(self, n: int, initial_list: list[int], q: int, operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processSagas(int n, vector<int>& initialList, int q, vector<string>& operations) {
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
   * @param {number} q
   * @param {string[]} operations
   * @returns {number[]}
   */
  processSagas(n, initialList, q, operations) {
    // Your code here
    return [];
  }
}
```
