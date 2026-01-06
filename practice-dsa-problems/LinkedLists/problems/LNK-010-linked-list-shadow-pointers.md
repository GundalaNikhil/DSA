---
problem_id: LNK_LINKED_LIST_SHADOW_POINTERS__7157
display_id: NTB-LNK-7157
slug: linked-list-shadow-pointers
title: "Linked List with Shadow Pointers"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-shadow-pointers
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Shadow Pointers

## Problem Statement

Each node stores a **shadow pointer** to the node that was immediately before it **at the time it was inserted**. Shadow pointers never change, even if nodes are moved or deleted.

Process operations:

- `INS u x`: insert value `x` after node `u` (new node's shadow = `u`)
- `DEL u`: delete node `u`
- `SHADOW u`: output the id of node `u`'s shadow, or `-1` if none

Node ids are assigned incrementally starting from 1 for the initial list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `SHADOW`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total nodes created <= 300000

## Clarifying Notes

- If a shadow node is deleted, its id is still returned.
- The first node's shadow is `-1`.

## Example Input

```
2
5 6
4
INS 1 9
SHADOW 3
DEL 1
SHADOW 3
```

## Example Output

```
1
1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processShadowPointers(int n, int[] values, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processShadowPointers(self, n: int, values: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processShadowPointers(int n, vector<int>& values, vector<string>& operations) {
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
   * @param {string[]} operations
   * @returns {number[]}
   */
  processShadowPointers(n, values, operations) {
    // Your code here
    return [];
  }
}
```
