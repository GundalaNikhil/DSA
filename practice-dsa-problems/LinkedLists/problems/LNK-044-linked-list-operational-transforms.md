---
problem_id: LNK_LINKED_LIST_OPERATIONAL_TRANSFORMS__5120
display_id: NTB-LNK-5120
slug: linked-list-operational-transforms
title: "Linked List with Operational Transforms"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-operational-transforms
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Operational Transforms

## Problem Statement

Two users edit the same base list concurrently. Each user provides a sequence of operations on the base list:

- `INS pos x`
- `DEL pos`

To merge, transform operations from user B against user A using these rules:

- If both insert at the same position, A's insert happens first.
- If A inserts before B's position, B's position shifts right by 1.
- If A deletes before B's position, B's position shifts left by 1.
- If both delete the same position, B's delete is dropped.

Apply all A operations, transform B, then apply transformed B. Output the final list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: base list
- Third line: integers `qa` and `qb`
- Next `qa` lines: operations of A
- Next `qb` lines: operations of B

## Output Format

- One line: final list values

## Constraints

- `1 <= n <= 200000`
- `0 <= qa, qb <= 200000`

## Clarifying Notes

- Positions are 1-based in the base list for both users.

## Example Input

```
3
1 2 3
1 1
INS 2 9
DEL 2
```

## Example Output

```
1 9 3
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processOperationalTransforms(int n, int[] baseList, String[] opsA, String[] opsB) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processOperationalTransforms(self, n: int, base_list: list[int], ops_a: list[str], ops_b: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processOperationalTransforms(int n, vector<int>& baseList, vector<string>& opsA, vector<string>& opsB) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} baseList
   * @param {string[]} opsA
   * @param {string[]} opsB
   * @returns {number[]}
   */
  processOperationalTransforms(n, baseList, opsA, opsB) {
    // Your code here
    return [];
  }
}
```
