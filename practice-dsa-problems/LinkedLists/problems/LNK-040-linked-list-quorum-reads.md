---
problem_id: LNK_LINKED_LIST_QUORUM_READS__2933
display_id: NTB-LNK-2933
slug: linked-list-quorum-reads
title: "Linked List with Quorum Reads"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-quorum-reads
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Quorum Reads

## Problem Statement

There are `R` replicas of a linked list. Updates can target any replica. A read returns a value only if at least `Q` replicas agree on that value at a position.

Operations:

- `SET r pos x`: set replica `r` at `pos` to `x`
- `READ pos Q`: output the agreed value if at least `Q` replicas match; otherwise output `CONFLICT`

## Input Format

- First line: integers `n`, `R`, `q`
- Second line: `n` integers: initial list values (all replicas start identical)
- Next `q` lines: operations

## Output Format

- For each `READ`, output the value or `CONFLICT`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= R <= 20`

## Clarifying Notes

- If multiple values each reach quorum, choose the smallest value.

## Example Input

```
3 3 4
1 2 3
SET 1 2 9
SET 2 2 9
READ 2 2
READ 2 3
```

## Example Output

```
9
CONFLICT
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<String> processQuorumReads(int n, int R, int[] initialValues, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processQuorumReads(self, n: int, R: int, initial_values: list[int], operations: list[str]) -> list[str]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> processQuorumReads(int n, int R, vector<int>& initialValues, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} R
   * @param {number[]} initialValues
   * @param {string[]} operations
   * @returns {string[]}
   */
  processQuorumReads(n, R, initialValues, operations) {
    // Your code here
    return [];
  }
}
```
