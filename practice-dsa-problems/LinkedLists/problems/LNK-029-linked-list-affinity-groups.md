---
problem_id: LNK_LINKED_LIST_AFFINITY_GROUPS__9842
display_id: NTB-LNK-9842
slug: linked-list-affinity-groups
title: "Linked List with Affinity Groups"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-affinity-groups
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Affinity Groups

## Problem Statement

Each node belongs to an affinity group. Operations can only be applied within a single group.

Operations:

- `SWAP u v`: swap two nodes if they are in the same group
- `MOVE u v`: move node `u` after node `v` if same group
- `COUNT g`: output the number of nodes in group `g`

Invalid operations are ignored.

## Input Format

- First line: integer `n`
- Second line: `n` integers: values
- Third line: `n` integers: group ids
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Group ids are integers in `1..n`

## Clarifying Notes

- `SWAP` and `MOVE` require both nodes in the same group.

## Example Input

```
4
1 2 3 4
1 2 1 2
3
MOVE 3 1
COUNT 1
SWAP 2 4
```

## Example Output

```
2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processAffinityGroups(int n, int[] values, int[] groupIds, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processAffinityGroups(self, n: int, values: list[int], group_ids: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processAffinityGroups(int n, vector<int>& values, vector<int>& groupIds, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} values
   * @param {number[]} groupIds
   * @param {string[]} operations
   * @returns {number[]}
   */
  processAffinityGroups(n, values, groupIds, operations) {
    // Your code here
    return [];
  }
}
```
