---
problem_id: LNK_LINKED_LIST_SELF_HEALING__8089
display_id: NTB-LNK-8089
slug: linked-list-self-healing
title: "Linked List with Self-Healing"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-self-healing
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Self-Healing

## Problem Statement

Each node stores `value` and a checksum `cs = value XOR prev_value XOR next_value` (where missing neighbors are treated as 0). Some checksums are corrupted.

Repair the list by recomputing any node whose checksum does not match, setting its `value` to the **majority** of its neighbors' values (tie -> smaller value). After one full pass, output the repaired list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: values
- Third line: `n` integers: checksums

## Output Format

- One line: repaired values

## Constraints

- `1 <= n <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- Use original neighbor values from the start of the pass.
- For endpoints, missing neighbor value is 0.

## Example Input

```
3
5 7 5
2 0 2
```

## Example Output

```
5 5 5
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> repairList(int n, int[] values, int[] checksums) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def repairList(self, n: int, values: list[int], checksums: list[int]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> repairList(int n, vector<int>& values, vector<int>& checksums) {
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
   * @param {number[]} checksums
   * @returns {number[]}
   */
  repairList(n, values, checksums) {
    // Your code here
    return [];
  }
}
```
