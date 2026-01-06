---
problem_id: LNK_LINKED_LIST_FUZZY_MEMBERSHIP__3175
display_id: NTB-LNK-3175
slug: linked-list-fuzzy-membership
title: "Linked List with Fuzzy Membership"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-fuzzy-membership
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Fuzzy Membership

## Problem Statement

Each node belongs to the list with probability `p_i/1000`. The **confidence score** of a prefix of length `k` is the expected number of present nodes in that prefix.

For each query `k`, output the confidence score multiplied by 1000.

## Input Format

- First line: integer `n`
- Second line: `n` integers: `p_i` (0..1000)
- Third line: integer `q`
- Next `q` lines: `k`

## Output Format

- For each query, output the expected count \* 1000

## Constraints

- `1 <= n, q <= 200000`
- `0 <= p_i <= 1000`

## Clarifying Notes

- Expectation is deterministic and additive.

## Example Input

```
3
500 1000 0
2
1
3
```

## Example Output

```
500
1500
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Long> confidenceScores(int n, int[] probabilities, int[] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def confidenceScores(self, n: int, probabilities: list[int], queries: list[int]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> confidenceScores(int n, vector<int>& probabilities, vector<int>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} probabilities
   * @param {number[]} queries
   * @returns {number[]}
   */
  confidenceScores(n, probabilities, queries) {
    // Your code here
    return [];
  }
}
```
